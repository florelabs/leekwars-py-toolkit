#!/usr/bin/env bash
# Récupère depuis leekwars.com + GitHub tout ce qui sert à générer __builtins__.pyi et la doc.
# Rejouable : à relancer quand Leek Wars change (nouvelle arme, nouvelle méthode de l'API objet...).
#
#   tools/fetch_sources.sh            # télécharge dans data/ et vendor/
#   tools/gen_stub.py                 # puis régénère __builtins__.pyi + docs/api_reference.md
#
# Sources :
#   - https://leekwars.com/encyclopedia/fr/Python : la page embarque window.__DATA__ (functions,
#     constants, weapons, chips...) = les game data que l'éditeur utilise pour générer son stub.
#   - le bundle JS de l'éditeur (chunk ai-view-monaco + directives) : contient le GÉNÉRATEUR du stub
#     Pyright (`cn(constants)`) que l'éditeur pose en /__builtins__.pyi. On l'exécute dans Node pour
#     obtenir exactement le même stub que l'éditeur (data/leekwars_raw.pyi).
#     NB : le dépôt public github.com/leek-wars/leek-wars est EN RETARD sur le bundle déployé
#     (pas de Message, Item, Fight.weaponCell... en septembre 2026) -> le bundle fait foi.
#   - /api/encyclopedia/get/fr/Python : l'article (markdown).
#   - /api/function/doc/fr : doc riche par fonction LeekScript (avec exemples Python pour 62 d'entre
#     elles) ; le chunk doc.fr : docs courtes (func_X, func_X_arg_N, func_X_return, const_X).
#   - github leek-wars/leek-wars-generator : objects.py = le runtime Python RÉEL côté serveur
#     (source de vérité sur le comportement), + guide de portage.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=$(pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
BASE=https://leekwars.com

echo "# page encyclopédie + game data"
curl -sSL "$BASE/encyclopedia/fr/Python" -o "$TMP/page.html"
curl -sSL "$BASE/api/encyclopedia/get/fr/Python" | python3 -c "import json,sys; print(json.load(sys.stdin)['content'])" > docs/python_encyclopedia.md
python3 - "$TMP/page.html" data/game_data.json <<'EOF'
import re, json, sys
s = open(sys.argv[1]).read()
m = re.search(r'__DATA__\s*=\s*(.*?)</script>', s, re.S)
j = json.loads(m.group(1).strip().rstrip(';'))
d = j['data']
out = {'master_version': j['master_version'], 'hashes': j['hashes'],
       'functions': d['functions'], 'constants': d['constants'], 'weapons': d['weapons'], 'chips': d['chips'],
       'summon_templates': d.get('summon_templates'), 'alterations': d.get('alterations')}
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
print('game data', j['master_version'], len(d['functions']), 'functions', len(d['constants']), 'constants')
EOF

echo "# bundles de l'éditeur (noms hashés : découverts par grep)"
MAIN=$(grep -oE 'assets/main-[A-Za-z0-9_-]+\.js' "$TMP/page.html" | head -1)
curl -sSL "$BASE/$MAIN" -o "$TMP/main.js"
AIVIEW=$(grep -oE 'assets/ai-view-monaco-[A-Za-z0-9_-]+\.js' "$TMP/main.js" | head -1)
curl -sSL "$BASE/$AIVIEW" -o "$TMP/ai-view.js"
DIRECTIVES=$(grep -oE 'directives-[A-Za-z0-9_-]+\.js' "$TMP/ai-view.js" | head -1)
curl -sSL "$BASE/assets/$DIRECTIVES" -o "$TMP/directives.js"
DOCCHUNK=$(grep -oE 'documentation-[A-Za-z0-9_-]+\.js' "$TMP/main.js" | grep -v function | head -1)
curl -sSL "$BASE/assets/$DOCCHUNK" -o "$TMP/documentation.js"
DOCFR=$(grep -oE 'doc\.fr-[A-Za-z0-9_-]+\.js' "$TMP/documentation.js" | head -1)
curl -sSL "$BASE/assets/$DOCFR" -o "$TMP/doc.fr.js"
LOCFR=$(grep -oE 'locale-fr-[A-Za-z0-9_-]+\.js' "$TMP/directives.js" | head -1)
curl -sSL "$BASE/assets/$LOCFR" -o "$TMP/locale-fr.js"
echo "  $MAIN / $AIVIEW / $DIRECTIVES / $DOCFR / $LOCFR"

echo "# stub brut (exécution du générateur de l'éditeur dans Node)"
python3 tools/extract_stub.py "$TMP/ai-view.js" "$TMP/directives.js" "$TMP/stubgen_parts.js"
node tools/run_stubgen.js "$TMP/stubgen_parts.js" data/game_data.json data/leekwars_raw.pyi data/leekwars_base.d.ts data/member_to_leekscript.json

echo "# docs FR"
curl -sSL "$BASE/api/function/doc/fr" -o data/function_doc.fr.json
node tools/parse_i18n.js doc "$TMP/doc.fr.js" data/doc_strings.fr.json
node tools/parse_i18n.js locale "$TMP/locale-fr.js" data/locale.fr.json

echo "# sources upstream (référence, lecture seule)"
gh_get() { curl -sSL "https://raw.githubusercontent.com/$1/master/$2" -o "$3"; }
gh_get leek-wars/leek-wars-generator src/main/resources/polyglot/objects.py vendor/generator/objects.py
gh_get leek-wars/leek-wars-generator POLYGLOT_PORTING_GUIDE.md vendor/generator/POLYGLOT_PORTING_GUIDE.md
gh_get leek-wars/leek-wars-generator POLYGLOT_TODO.md vendor/generator/POLYGLOT_TODO.md
gh_get leek-wars/leek-wars src/component/editor/leekwars-pyi.ts vendor/client/leekwars-pyi.ts
gh_get leek-wars/leek-wars src/component/editor/leekwars-dts.ts vendor/client/leekwars-dts.ts
gh_get leek-wars/leek-wars src/component/editor/pyright-client.ts vendor/client/pyright-client.ts

echo "OK -> lancer tools/gen_stub.py"
