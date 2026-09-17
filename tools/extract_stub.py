#!/usr/bin/env python3
r"""Extrait du bundle minifié de l'éditeur Leek Wars les morceaux JS qui génèrent le stub Pyright.

Usage : extract_stub.py <ai-view-monaco.js> <directives.js> <out.js>

Repères (stables tant que le code source amont garde la même forme, cf vendor/client/*.ts) :
  - directives.js : `const <Za>=new Set([...mots réservés JS...])`, `<za>=/^[A-Za-z_$]...$/`,
    `function <Ve>` (pySafe), `function <ja>` (camel), `const <ui>=[{prefix:"WEAPON_"...` (CONST_CONTAINERS),
    `<hn>={OPERATIONS_LIMIT:"System"...}` (EXACT), `<ao>=...`, `function <Ua>`, `function <Co>` (routeConstant),
    puis `function Ba(` marque la fin. Le template .d.ts `const <_o>=\`...\`` et la table `<qa>={"Entity.entityType":...}`.
  - ai-view-monaco.js : de `const on=new Set([...mots réservés Python...])` jusqu'à `function un(` :
    contient ot (pySafe py), ln (CLASSES), an, rn, cn (buildLeekwarsPyi).
Les identifiants minifiés changent à chaque build : on les retrouve par les littéraux, pas par leur nom.
"""
import re
import sys


def seg(s, start_re, end_re):
    m = re.search(start_re, s)
    if not m:
        raise SystemExit(f'repère introuvable : {start_re}')
    i = m.start()
    e = re.search(end_re, s[i + 1:])
    if not e:
        raise SystemExit(f'fin introuvable : {end_re}')
    return s[i:i + 1 + e.start()], m


def main(aiview_path, directives_path, out_path):
    d = open(directives_path, encoding='utf-8').read()
    a = open(aiview_path, encoding='utf-8').read()
    parts = []

    # 1. bloc constantes/routeConstant : commence au Set des mots réservés JS, finit à la fonction suivant Co.
    block, _ = seg(d, r'const \w+=new Set\(\["break","case","catch"', r'function \w+\(e\)\{const \w+=\w+\(e\);if\(!\w+\)return null;const \w+=\w+\(\w+\);')
    parts.append(block)
    route_fn = re.search(r'function (\w+)\(e\)\{if\(\w+\[e\]\)return\{container:', block).group(1)

    # 2. template .d.ts (gabarit à backticks, contient des \` échappés).
    m = re.search(r'const (\w+)=`// --- API de combat orientée objet', d)
    i = m.start()
    j = m.end()  # juste après le backtick ouvrant
    while True:
        j = d.find('`', j)
        if d[j - 1] != '\\':
            break
        j += 1
    parts.append(d[i:j + 1] + ';')
    dts_name = m.group(1)

    # 3. table membre objet -> fonction LeekScript.
    m = re.search(r'const (\w+)=\{"Entity\.entityType":"getType"', d)
    i = m.start()
    j = d.find('};', i)
    parts.append(d[i:j + 2])
    qa_name = m.group(1)

    # 4. générateur Python : du Set des mots réservés Python jusqu'à la fonction d'échappement suivante.
    block, _ = seg(a, r'const \w+=new Set\(\["False","None","True","and"', r'function \w+\(e\)\{return e\.replace\(/\\\\/g')
    parts.append(block)
    cn = re.search(r'function (\w+)\(e\)\{const \w+=\w+\(e\),\w+=\["# Auto-généré', block).group(1)
    # an() appelle routeConstant sous son nom d'import (Dt) : on l'aliase.
    an_call = re.search(r'const \w+=(\w+)\(s\);if\(!\w+\|\|!\w+\(\w+\.member\)\)', block).group(1)
    parts.append(f'const {an_call}={route_fn};' if an_call != route_fn else '')

    parts.append(f'module.exports={{buildPyi:{cn},dtsTemplate:{dts_name},memberToLs:{qa_name}}};')
    open(out_path, 'w', encoding='utf-8').write('\n'.join(parts) + '\n')
    print(f'  générateur extrait : buildPyi={cn} route={route_fn} dts={dts_name} map={qa_name}')


if __name__ == '__main__':
    main(*sys.argv[1:4])
