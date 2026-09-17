# leekwars-py-toolkit

IA Leek Wars en Python (GraalPy 3.12, API objet), avec autocomplétion et vérification de types dans l'IDE.

## Autocomplétion

`__builtins__.pyi` à la racine déclare l'API de combat (`Fight`, `Field`, `Entity`, `Cell`, `Weapon`, `Chip`, ...)
comme globales, exactement comme le fait l'éditeur du site (convention Pyright, reprise par Pylance dans VS Code).
Ouvre le dossier dans VS Code avec Pylance : survol, complétion et erreurs (`reportUndefinedVariable` attrape
les `me` / `getNearestEnemy()` / `WEAPON_PISTOL` hérités du LeekScript). En ligne de commande : `npx pyright`.

Ruff (lint/format dans VS Code) ne lit pas `__builtins__.pyi` : `ruff.toml` déclare les mêmes globales
(`builtins = [...]`, ligne régénérée par `tools/gen_stub.py`) et cible Python 3.12 (`X | None`, pas `Optional`).

Les docstrings (FR) reprennent la doc officielle de la fonction LeekScript équivalente, le coût en opérations,
et une fiche par arme / puce (`Weapon.pistol`, `Chip.bandage` : coût, portée, effets).

## Contenu

- `ais/` — tes IA (ignoré par git).
- `examples/` — IA d'exemple (`example.py` + `helpers.py`), aussi test du stub.
- `docs/runtime.md` — modèle d'exécution, budgets, pièges (à lire avant d'écrire un algo).
- `docs/api_reference.md` — référence de l'API objet, générée.
- `docs/python_encyclopedia.md` — l'article officiel « Python ».
- `data/` — game data, stub brut de l'éditeur, docs FR (JSON).
- `vendor/generator/objects.py` — le runtime Python réel côté serveur (source de vérité) + guide de portage
  (non versionné : `tools/fetch_sources.sh` le récupère).
- `tools/fetch_sources.sh` puis `tools/gen_stub.py` — régénèrent tout depuis leekwars.com et GitHub.

## Mise à jour

```sh
tools/fetch_sources.sh && python3 tools/gen_stub.py && npx pyright && uvx ruff check .
```

## Licence

MIT pour l'outillage de ce dépôt. `vendor/client/` reprend des fichiers du client Leek Wars (GPL-3.0) ; les données
et docs dans `data/` proviennent de leekwars.com et restent la propriété de Leek Wars.
