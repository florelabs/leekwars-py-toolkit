#!/usr/bin/env python3
"""Génère __builtins__.pyi (stub Pyright/Pylance enrichi de docstrings FR) et docs/api_reference.md.

Entrées (produites par tools/fetch_sources.sh) :
  data/leekwars_raw.pyi            stub EXACT de l'éditeur Leek Wars (signatures = source de vérité)
  data/member_to_leekscript.json   membre objet -> fonction LeekScript plate (pour retrouver sa doc)
  data/function_doc.fr.json        doc riche par fonction (description / Paramètres / Retour / Exemples)
  data/doc_strings.fr.json         docs courtes : func_X, func_X_arg_N, func_X_return, const_X
  data/game_data.json              armes, puces, constantes (valeurs), fonctions plates
  data/locale.fr.json              noms FR des armes / puces

Les signatures ne sont PAS modifiées (même API que l'éditeur, mêmes faux positifs évités : pas de
`| None` sur getNearestEnemy etc., cf vendor/client/leekwars-pyi.ts). On ajoute uniquement :
  - une docstring sous chaque def / attribut (Pylance affiche les docstrings d'attributs),
  - la fiche de chaque arme / puce (coût, portée, effets) sous Weapon.pistol, Chip.bandage...,
  - la valeur et la doc de chaque constante (Effect.DAMAGE, Fight.Use.SUCCESS...).
Pourquoi __builtins__.pyi : c'est la convention Pyright (fichier à la racine du projet) pour déclarer
des symboles disponibles sans import ; c'est aussi ce que fait l'éditeur du site (pyright-client.ts).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / 'data'

raw = (DATA / 'leekwars_raw.pyi').read_text(encoding='utf-8').split('\n')
member_to_ls = json.loads((DATA / 'member_to_leekscript.json').read_text(encoding='utf-8'))
func_doc = json.loads((DATA / 'function_doc.fr.json').read_text(encoding='utf-8'))
short = json.loads((DATA / 'doc_strings.fr.json').read_text(encoding='utf-8'))
game = json.loads((DATA / 'game_data.json').read_text(encoding='utf-8'))
locale = json.loads((DATA / 'locale.fr.json').read_text(encoding='utf-8'))

CONST_BY_NAME = {c['name']: c for c in game['constants']}
FUNC_BY_NAME = {f['name']: f for f in game['functions']}
WEAPONS = {w['name']: w for w in game['weapons'].values()}
CHIPS = {c['name']: c for c in game['chips'].values()}
# id d'effet -> nom de constante EFFECT_X (les EFFECT_MODIFIER_/EFFECT_TARGET_ sont d'autres familles)
EFFECT_NAME = {int(c['value']): c['name'][7:] for c in game['constants']
               if c['name'].startswith('EFFECT_') and not c['name'].startswith(('EFFECT_MODIFIER_', 'EFFECT_TARGET_'))
               and not c['deprecated']}
AREA_NAME = {int(c['value']): c['name'][5:] for c in game['constants'] if c['name'].startswith('AREA_')}
LAUNCH_NAME = {int(c['value']): c['name'][12:] for c in game['constants'] if c['name'].startswith('LAUNCH_TYPE_')}
TARGET_BITS = [(int(c['value']), c['name'][14:]) for c in game['constants'] if c['name'].startswith('EFFECT_TARGET_')]

# Membres sans équivalent plat documenté : docs reprises des commentaires de vendor/generator/objects.py.
EXTRA_DOC = {
    'Effect.raw': 'Tableau brut [type, value, caster_id, turns, critical, item_id, target_id, modifiers].',
    'Effect.caster': "L'entité qui a lancé l'effet.",
    'Effect.critical': "L'effet vient d'un coup critique.",
    'Effect.item': "L'arme ou la puce qui a provoqué l'effet (`Weapon`/`Chip`, comparable par `is`).",
    'Effect.target': "L'entité qui subit l'effet.",
    'Feature.raw': 'Tableau brut [type, minValue, maxValue, turns, targets, modifiers].',
    'Message.raw': 'Message brut tel que renvoyé par getMessages().',
    'Cell.get': "Cellule d'id `id`, ou None s'il est invalide (chemin inverse : relire un id rangé dans un registre).",
    'Cell.hasEntity': 'Une entité (poireau, bulbe, tourelle...) occupe-t-elle la case.',
    'Item.name': "Nom de l'arme / de la puce.",
    'Item.inline': "L'item se lance en ligne (tir en ligne).",
    'Item.needsLos': "L'item exige une ligne de vue.",
    'Item.features': "Caractéristiques déclarées de l'item (list[Feature] : dégâts, poison, téléport...). Distinct de entity.effects (effets ACTIFS).",
    'Item.effectiveArea': "Zone d'effet réelle de l'item sur `cell`, lancé depuis `frm` (défaut : position courante). list[Cell].",
    'Item.get': "L'item (arme OU puce) d'id `id`, ou None. Weapon.get / Chip.get restreignent à leur type.",
    'Weapon.get': "L'arme d'id `id`, ou None si l'id n'est pas celui d'une arme.",
    'Chip.get': "La puce d'id `id`, ou None si l'id n'est pas celui d'une puce.",
    'Entity.get': "Entité d'id `id` (typée : Leek, Bulb, Mob...), ou None s'il est invalide.",
    'Entity.entityType': 'Genre d\'entité (Entity.Type.LEEK / BULB / TURRET / CHEST / MOB / PLANT). Ne pas confondre avec `.type` des sous-classes (Bulb.Type.*, Chest.Type.*...).',
    'Me.weaponCell': "Cellule d'où utiliser l'arme (équipée par défaut) sur `target` (entité ou case), ou None. Alias de Fight.weaponCell.",
    'Me.weaponCells': "Toutes les cellules d'où utiliser l'arme sur `target`. Alias de Fight.weaponCells.",
    'Me.chipCell': "Cellule d'où utiliser `chip` sur `target`, ou None. Alias de Fight.chipCell.",
    'Me.chipCells': "Toutes les cellules d'où utiliser `chip` sur `target`. Alias de Fight.chipCells.",
    'Me.weaponTargets': "Entités touchées si l'arme (équipée par défaut) est lancée sur `cell`. Alias de Fight.weaponTargets.",
    'Me.chipTargets': "Entités touchées si `chip` est lancée sur `cell`. Alias de Fight.chipTargets.",
    'Me.lama': "Fait dire « lama » à l'entité (trophée).",
    'Chip.bulbCharacteristics': "Pour une puce d'invocation : caractéristiques du bulbe invoqué (dict).",
    'Fight.me': "VOTRE entité (remplace l'ancien global `me`). Pendant le tour d'un bulbe invoqué, `Fight.me` EST le bulbe.",
}

NULLABLE = {  # méthodes qui renvoient None côté runtime (objects.py : _ent / _cell / _weap) : on le dit dans la doc
    'Fight.getNearestEnemy', 'Fight.getNearestAlly', 'Fight.getFarthestEnemy', 'Fight.getFarthestAlly',
    'Fight.getNearestEnemyTo', 'Fight.getNearestAllyTo', 'Fight.getNearestEnemyToCell', 'Fight.getNearestAllyToCell',
    'Fight.getAlliedTurret', 'Fight.getEnemyTurret', 'Fight.getNextPlayer', 'Fight.getPreviousPlayer',
    'Fight.weaponCell', 'Fight.chipCell', 'Me.weaponCell', 'Me.chipCell', 'Field.cellFromXY',
    'Cell.entity', 'Entity.weapon', 'Entity.summoner', 'Effect.caster', 'Effect.target', 'Effect.item',
}


def clean(md):
    """Nettoie le markdown de la doc : liens wiki, ancres #fn, exemples LeekScript/JS (on garde Python)."""
    md = re.sub(r'```(?:leekscript|js|javascript)\n.*?```\n?', '', md, flags=re.S)
    md = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', md)
    md = re.sub(r'\[\[([^\]]+)\]\]', r'`\1`', md)
    md = re.sub(r'(?<![\w`])#(\w+)', r'`\1`', md)
    md = re.sub(r'</?b>', '**', md)
    md = re.sub(r'<br\s*/?>', '\n', md)
    md = re.sub(r'<[^>]+>', '', md)
    md = md.replace('\\', '\\\\').replace('"""', "'''")
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def ls_doc(ls_name, with_sections=True):
    """Doc FR d'une fonction LeekScript plate : la version riche (API) sinon les chaînes courtes."""
    d = func_doc.get(ls_name)
    parts = []
    if d:
        parts.append(clean(d.get('description', '')))
        if with_sections:
            for sec in ('primary', 'secondary'):
                v = d.get(sec)
                if isinstance(v, dict):
                    for title, body in v.items():
                        if title in ('Voir aussi',):
                            continue
                        body = clean(body)
                        if body:
                            parts.append(f'**{title}**\n{body}')
    else:
        desc = short.get('func_' + ls_name)
        if desc:
            parts.append(clean(desc))
        fn = FUNC_BY_NAME.get(ls_name)
        if fn and with_sections:
            args = []
            for i, a in enumerate(fn['arguments_names']):
                t = short.get(f'func_{ls_name}_arg_{i + 1}')
                if t:
                    args.append(f'- **{a}** : {clean(t)}')
            if args:
                parts.append('**Paramètres**\n' + '\n'.join(args))
            r = short.get(f'func_{ls_name}_return')
            if r:
                parts.append(f'**Retour**\n- **{fn["return_name"]}** : {clean(r)}')
    return '\n\n'.join(p for p in parts if p)


def member_doc(cls, name):
    key = f'{cls}.{name}'
    ls = member_to_ls.get(key) or (member_to_ls.get('Weapon.' + name) if cls == 'Item' else None) \
        or (name if name in func_doc or 'func_' + name in short else None)
    text = ls_doc(ls) if ls else ''
    extra = EXTRA_DOC.get(key)
    if extra:
        text = (extra + '\n\n' + text) if text else extra
    if key in NULLABLE:
        text += '\n\n⚠️ Peut renvoyer **None** (le stub dit le contraire pour éviter les faux positifs Pyright : gardez un `if x:`).'
    if ls:
        ops = FUNC_BY_NAME.get(ls, {}).get('operations')
        cost = f' — {ops} opérations' if ops else ''
        text += f'\n\nLeekScript : `{ls}()`{cost} · https://leekwars.com/help/documentation/{ls}'
    return text.strip()


def fmt_effect(e, kind):
    name = EFFECT_NAME.get(e['id'], f"effet {e['id']}")
    v1, v2 = e.get('value1', 0), e.get('value2', 0)
    fmt = lambda x: f'{x:g}'
    val = fmt(v1) if not v2 else f'{fmt(v1)}–{fmt(v1 + v2)}'
    s = f'Effect.{name} {val}'
    if e.get('turns') and e['turns'] > 0:
        s += f" ({e['turns']} tours)"
    t = e.get('targets', 0)
    if t and t != 31:
        names = [n for bit, n in TARGET_BITS if t & bit]
        if names:
            s += f' [{"|".join(names)}]'
    return s


def item_doc(kind, data):
    fr = locale[kind].get(data['name'], data['name'])
    lines = [f'**{fr}** (`{kind}_{data["name"]}`, id {data["id"]}, niveau {data["level"]})']
    rng = f'{data["min_range"]}–{data["max_range"]}' if data['min_range'] != data['max_range'] else str(data['min_range'])
    info = [f'{data["cost"]} PT', f'portée {rng}', f'zone {AREA_NAME.get(data.get("area"), "?")}',
            f'lancer {LAUNCH_NAME.get(data.get("launch_type"), "?")}']
    if not data.get('los', True):
        info.append('sans ligne de vue')
    mu = data.get('max_uses', -1)
    info.append('utilisations illimitées' if mu in (-1, 0, None) else f'{mu} util./tour')
    if kind == 'chip':
        cd = data.get('cooldown', 0)
        info.append('sans cooldown' if not cd else ('cooldown infini' if cd == -1 else f'cooldown {cd}'))
        if data.get('team_cooldown'):
            info.append("cooldown d'équipe")
    lines.append(', '.join(info) + '.')
    effs = [fmt_effect(e, kind) for e in data.get('effects', [])]
    if effs:
        lines.append('Effets : ' + ' ; '.join(effs) + '.')
    peffs = [fmt_effect(e, kind) for e in data.get('passive_effects', [])]
    if peffs:
        lines.append('Passifs : ' + ' ; '.join(peffs) + '.')
    return '\n'.join(lines)


def const_doc(cls, sub, name):
    """Retrouve la constante LeekScript plate d'un membre Class[.Sub].NAME et rend '(= valeur) doc'."""
    prefixes = {
        ('Effect', None): ['EFFECT_'], ('Effect', 'Modifier'): ['EFFECT_MODIFIER_'], ('Effect', 'Target'): ['EFFECT_TARGET_'],
        ('Message', 'Type'): ['MESSAGE_'], ('Cell', 'Type'): ['CELL_'], ('Item', 'Area'): ['AREA_'],
        ('Item', 'LaunchType'): ['LAUNCH_TYPE_'], ('Entity', 'Type'): ['ENTITY_'], ('Entity', 'Stat'): ['STAT_'],
        ('Bulb', 'Type'): ['BULB_'], ('Chest', 'Type'): ['CHEST_'], ('Mob', 'Type'): ['MOB_'], ('Plant', 'Type'): ['PLANT_'],
        ('State', None): ['STATE_'], ('Fight', None): [''], ('Fight', 'Use'): ['USE_'], ('Fight', 'Erosion'): ['EROSION_'],
        ('Fight', 'Boss'): ['BOSS_'], ('Fight', 'Context'): ['FIGHT_CONTEXT_'], ('Fight', 'Type'): ['FIGHT_TYPE_'],
        ('Field', None): ['MAP_'], ('System', None): [''], ('Color', None): ['COLOR_'],
    }
    for p in prefixes.get((cls, sub), []):
        c = CONST_BY_NAME.get(p + name)
        if c:
            doc = short.get('const_' + c['name'], '')
            return f"(= {c['value']}) {clean(doc)}".strip() + f"\n\nLeekScript : `{c['name']}`"
    return ''


def emit(out, indent, text):
    if not text:
        return
    if '\n' not in text and len(text) < 100:
        out.append(f'{indent}"""{text}"""')
    else:
        out.append(f'{indent}"""')
        out.extend(f'{indent}{l}'.rstrip() for l in text.split('\n'))
        out.append(f'{indent}"""')


def build():
    out = ['# Stub Pyright/Pylance de l\'API de combat Leek Wars (Python 3.12 / GraalPy), enrichi de docstrings FR.',
           '# Généré par tools/gen_stub.py depuis data/leekwars_raw.pyi (le stub exact de l\'éditeur du site) + game data.',
           f'# Game data version {game["master_version"]}. NE PAS ÉDITER À LA MAIN : relancer tools/fetch_sources.sh && tools/gen_stub.py.',
           '# Convention Pyright : un __builtins__.pyi à la racine du projet déclare des globales disponibles sans import.']
    reference = {}  # cls -> [(signature, doc)] pour docs/api_reference.md
    cls = sub = None
    pending_decorator = False
    for line in raw:
        if line.startswith('# Auto-généré'):
            continue
        out.append(line)
        m = re.match(r'^class (\w+)', line)
        if m:
            cls, sub = m.group(1).lstrip('_'), None
            reference.setdefault(cls, [])
            continue
        m = re.match(r'^    class (\w+)', line)
        if m:
            sub = m.group(1)
            continue
        if line.strip() == '@staticmethod':
            pending_decorator = True
            continue
        m = re.match(r'^(\s+)(?:def (\w+)\(.*: \.\.\.|(\w+): (.+))$', line)
        if not m or cls is None:
            pending_decorator = False
            continue
        indent, name, attr, typ = m.group(1), m.group(2), m.group(3), m.group(4)
        name = name or attr
        doc = ''
        if len(indent) == 8 and sub:               # constante de sous-conteneur : Effect.Modifier.STACKABLE
            doc = const_doc(cls, sub, name)
        elif attr and typ == 'Weapon' and name in WEAPONS_BY_CAMEL:
            doc = item_doc('weapon', WEAPONS_BY_CAMEL[name])
        elif attr and typ == 'Chip' and name in CHIPS_BY_CAMEL:
            doc = item_doc('chip', CHIPS_BY_CAMEL[name])
        elif attr and typ == 'int' and name.isupper():   # constante directe : Effect.DAMAGE, Fight.MAX_TURNS
            doc = const_doc(cls, None, name)
        else:
            doc = member_doc(cls, name)
        if name and not attr and doc:
            out[-1] = line[:-len(' ...')]      # `def f(...) -> T:` puis docstring puis `...`
            emit(out, indent + '    ', doc)
            out.append(indent + '    ...')
        else:
            emit(out, indent, doc)
        if len(indent) == 4 and not (attr and typ in ('Weapon', 'Chip') and not name.isupper()):
            reference[cls].append((line.strip(), doc))
        pending_decorator = False
    return '\n'.join(out) + '\n', reference


def camel(s):
    parts = s.lower().split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])


WEAPONS_BY_CAMEL = {camel(n): w for n, w in WEAPONS.items()}
CHIPS_BY_CAMEL = {camel(n): c for n, c in CHIPS.items()}


def write_reference(reference):
    md = ['# Référence de l\'API objet Python Leek Wars',
          '',
          f'Générée par `tools/gen_stub.py` (game data `{game["master_version"]}`). Signatures = stub exact de l\'éditeur ; '
          'docs = documentation FR officielle de la fonction LeekScript équivalente. Voir aussi `docs/runtime.md`.',
          '']
    order = ['Fight', 'Me', 'Entity', 'Leek', 'Turret', 'Bulb', 'Chest', 'Mob', 'Plant', 'Cell', 'Field', 'Item', 'Weapon', 'Chip',
             'Effect', 'Feature', 'State', 'Registers', 'Network', 'Message', 'Debug', 'System', 'Color', 'Math']
    for c in order + [k for k in reference if k not in order]:
        members = reference.get(c)
        if not members:
            continue
        md.append(f'## {c}\n')
        for sig, doc in members:
            md.append(f'### `{c}.{sig.replace("def ", "").replace("(self, ", "(").replace("(self)", "()").replace(": ...", "")}`\n')
            if doc:
                md.append(doc.replace('\\\\', '\\') + '\n')
    md.append('## Armes\n')
    for name, w in sorted(WEAPONS.items(), key=lambda kv: kv[1]['level']):
        md.append(f'- `Weapon.{camel(name)}` — ' + item_doc('weapon', w).replace('\n', ' '))
    md.append('\n## Puces\n')
    for name, c in sorted(CHIPS.items(), key=lambda kv: kv[1]['level']):
        md.append(f'- `Chip.{camel(name)}` — ' + item_doc('chip', c).replace('\n', ' '))
    (ROOT / 'docs' / 'api_reference.md').write_text('\n'.join(md) + '\n', encoding='utf-8')


def write_ruff_builtins(stub):
    """Synchronise la liste `builtins` de ruff.toml (Ruff ignore __builtins__.pyi) avec le __all__ du stub."""
    names = re.search(r"^__all__ = \[(.*)\]$", stub, re.M).group(1).replace("'", '"')
    p = ROOT / 'ruff.toml'
    s = p.read_text(encoding='utf-8')
    s = re.sub(r'# <builtins>\n.*?\n# </builtins>', f'# <builtins>\nbuiltins = [{names}]\n# </builtins>', s, flags=re.S)
    p.write_text(s, encoding='utf-8')


if __name__ == '__main__':
    stub, reference = build()
    (ROOT / '__builtins__.pyi').write_text(stub, encoding='utf-8')
    write_reference(reference)
    write_ruff_builtins(stub)
    n_doc = stub.count('"""') // 2
    print(f'__builtins__.pyi : {len(stub.splitlines())} lignes, {n_doc} docstrings ; docs/api_reference.md écrit')
