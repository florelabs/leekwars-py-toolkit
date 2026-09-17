# leekwars-python-ais

IA Leek Wars écrites en Python (GraalPy 3.12, API **objet** : `Fight.me`, `Weapon.pistol`, pas de fonctions ni
constantes plates, pas de global `me`). Objectif du dépôt : sparring technique sur les algos + autocomplétion IDE.

## Sources de vérité (dans cet ordre)
1. `vendor/generator/objects.py` (gitignoré, `tools/fetch_sources.sh` le télécharge) — runtime Python réel du moteur
   (`leek-wars/leek-wars-generator`). Pour toute
   question « que fait vraiment X », lire ici (pooling, nullabilité, ordre des arguments, lecture seule).
2. `data/leekwars_raw.pyi` — stub exact de l'éditeur du site, extrait du bundle JS déployé (le dépôt public
   `leek-wars/leek-wars` est en retard sur la prod ; ne pas s'y fier pour l'API).
3. `docs/runtime.md` — synthèse : cycle de vie, budgets ops/RAM/wall-clock, déterminisme, pièges LS→Python.
4. `data/function_doc.fr.json` — doc officielle par fonction LeekScript ; `data/member_to_leekscript.json` fait
   le lien membre objet → fonction plate.

## Fichiers générés (ne pas éditer à la main)
`__builtins__.pyi`, `docs/api_reference.md`, `data/*` : `tools/fetch_sources.sh && python3 tools/gen_stub.py`.
Les docstrings ajoutées viennent de `tools/gen_stub.py` (`EXTRA_DOC`, `NULLABLE`) : c'est là qu'on corrige un texte.

## Conventions
- Les IA perso vivent dans `ais/` (gitignoré) ; `examples/` contient l'IA de démo versionnée qui sert de test du stub.
  Un fichier = une IA ou un module (`import` natif, noms sans tirets, pas de cycles).
- `npx pyright` et `uvx ruff check .` doivent rester à 0 erreur. Ruff ne lit pas `__builtins__.pyi` : ses globales sont
  dans `ruff.toml` (`builtins`, régénéré par `gen_stub.py`). Style 3.12 : `X | None`, jamais `Optional`.
- Les méthodes typées `-> Entity` / `-> Cell` peuvent renvoyer `None` au runtime (stub volontairement optimiste) :
  toujours garder les `if x is None`.
- Budget : `cœurs × 1 000 000` ops/tour, wall-clock 5 s, 3 dépassements = IA neutralisée. Toute recherche doit se
  borner sur `System.operations`.
