# Style graphique @xcryptokeys

Référence : [reference-banner.png](reference-banner.png) (la bannière du compte).
Exemples : [threads/pactus-001/post_6.png](threads/pactus-001/post_6.png) (schéma sur mesure), [threads/pactus-001/post_1.png](threads/pactus-001/post_1.png) (carte simple).

Le but : qu'on reconnaisse un visuel @xcryptokeys au premier coup d'œil dans le fil X.
Ambiance « réseau la nuit » : fond bleu nuit profond, traits néon cyan → violet, effet verre, pistes de circuit et bribes de code en fond.

## Règles des illustrations (obligatoires)

1. **Coller au message.** L'image illustre ce que dit *ce* post : son mécanisme, son chiffre, sa chronologie, sa comparaison. On part du texte (`long`) et on se demande quel dessin l'explique le mieux (une courbe pour une formule de prix, une frise pour un incident, un arbre pour une dérivation de clés, un réseau pour un quorum…), pas quel gabarit est le plus rapide.
2. **Varier.** Pas toujours la même forme (fini les carrés et cubes à droite sur chaque post). Le modèle à suivre est [threads/pactus-001/post_6.png](threads/pactus-001/post_6.png) : un schéma fait pour ce post-là. Dans une campagne, éviter trois posts de suite avec le même type de schéma.
3. **Jamais deux fois la même illustration dans une campagne** (règle de sécurité). Chaque post a son propre schéma, avec ses propres textes et données. `design/diagram.py` le vérifie : il refuse de générer une campagne où deux schémas sont identiques, et signale ceux qui se ressemblent trop ou trois types identiques de suite.
4. **Rien d'inventé.** Pas de chiffre d'exemple ni de détail absent du post. Si un dessin a besoin d'un nombre que le post ne donne pas, on change de dessin (sans axe chiffré, ou un autre type).

## Palette

| Rôle | Couleur | Usage |
|---|---|---|
| Fond, bord | `#040823` | coins de l'image, fond le plus sombre |
| Fond, milieu | `#081039` | dégradé radial du fond |
| Fond, centre | `#10235b` | centre lumineux du fond |
| Panneau | `#0b2053` / `#172667` | cartes « verre » (opacité 70–85 %) |
| Bleu circuit | `#2169af` | bordures fines, grille, pistes |
| Bleu clair | `#488fdb` / `#46b6e9` | libellés secondaires, signature |
| **Cyan néon** | `#5cfcfa` | accent principal : flux, numéro, chiffre clé |
| Indigo | `#4a7ce1` / `#8565e4` | halos, accents secondaires |
| **Violet néon** | `#ad59e9` | accent secondaire : cas optionnel, alerte, rejet |
| Texte | `#eaf6ff` | titres et texte principal |
| Texte atténué | `#8fa8dd` | sous-titres, précisions |

D'autres couleurs sont permises si elles restent dans cette famille froide (bleu, cyan, indigo, violet, magenta).
Pas de rouge vif, d'orange ni de vert saturé : une alerte se fait en violet néon, un « OK » en cyan.
Un seul dégradé d'accent : cyan `#5cfcfa` → violet `#ad59e9`, de gauche à droite.

## Typographie

- **Titres** : Exo 2, 800 (Google Fonts). Une ligne, 40–46 px, couleur `#eaf6ff`.
- **Préfixe de série** (« INSIDE #PACTUS #6 ») : JetBrains Mono, gras, majuscules, espacement 2, cyan néon avec halo.
- **Code, champs, adresses, petits libellés** : JetBrains Mono.
- **Texte courant** : Inter.

## Composition (1200 × 675)

1. En haut à gauche : préfixe de série, puis titre (marge 60 px).
2. Au centre : un seul schéma, lisible sur mobile. 3 à 6 boîtes maximum, texte ≥ 15 px.
3. En bas à droite : la signature `@xcryptokeys`, seule (pas de hashtag ni d'autre mention), en mono bleu clair.
4. Fond : dégradé radial + grille 40 px très discrète + 1 ou 2 halos flous (bleu, violet) + quelques pistes de circuit et bribes `0x…`/binaire à 20 % d'opacité, jamais derrière du texte.

## Éléments

- **Cartes** : coins arrondis 12–16 px, fond verre, bordure 1,5 px `#2169af`.
- **Carte mise en avant** (l'idée clé du post) : bordure 2,5 px en dégradé cyan → violet, avec halo.
- **Flèches et flux** : courbes de Bézier, 2,5 px, cyan avec halo. En pointillé violet pour un cas optionnel.
- **Chiffre ou formule clé** : dans une carte mise en avant, en Exo 2 800.
- Pas de logo de marque, de photo ni d'image IA dans les schémas. Les logos de chaînes restent pour la bannière.

## Exactitude

L'image ne doit rien affirmer de plus que le post (`long`, `tech`, `simple`). Un schéma se vérifie comme un post, contre la même source.

## Fichiers

- Chaque post a une image : `threads/<campagne>/post_N.png` (dans `accounts/XCryptoKeys/`) (numéro sans zéro devant : post_1, post_12, post_105).
- Sa source : `threads/<campagne>/src/post_N.html`.
- **Schéma sur mesure (par défaut)** : décrit dans `threads/<campagne>/visuals.json` (une entrée par numéro de post), puis
  `python3 design/diagram.py accounts/XCryptoKeys/threads/<campagne> [index ...] --png` (depuis la racine du dépôt).
  Le script écrit `src/post_N.html` (marque `auto-diagram`), rend les PNG, signale tout texte qui déborde (« ATTENTION ») et applique la règle anti-doublon (« ERREUR » = rien n'est généré, « AVERTISSEMENT » = à revoir).
  Il n'écrase jamais un fichier écrit à la main, et card.py n'écrase jamais ses fichiers.
- **Schéma écrit à la main** (quand aucun type ne convient) : écrire `src/post_N.html` en partant de `threads/pactus-001/src/post_6.html`, puis
  `node design/render.js accounts/XCryptoKeys/threads/<campagne>/src/post_N.html`.
- **Carte simple** (`design/card.py`, depuis le champ `card` du post) : seulement pour un post sans schéma possible ; elle ne respecte pas à elle seule la règle « coller au message ».
- **Accroches** : un **dessin sur mesure** par accroche, écrit à la main dans `threads/<campagne>/hooks/src/hook_N.html` en partant de `threads/pactus-001/src/post_6.html`. Il montre ce que dit le texte de l'accroche (son mécanisme, son affaire, son chiffre). **Jamais deux fois la même illustration dans une campagne**, ni entre accroches ni avec les images des posts. Les 5 mises en page automatiques (`hero`, `list`, `question`, `chain`, `versus`, champ `card` de `hooks/hooks.json`) ne sont qu'un brouillon ; card.py n'écrase jamais un dessin sur mesure. Rendu des images et de `HOOKS.md` :
  `python3 design/card.py accounts/XCryptoKeys/threads/<campagne> --hooks --png` → `threads/<campagne>/hooks/hook_N.png`.
- Rendu : Playwright + Chromium (`npm i playwright`).

## Types de schéma (visuals.json)

Champs communs : `title` (sinon `card.title` du post), `note` `{k, v}` (carte « idée clé » en bas). Une boîte = `{k, label, big, lines, sub}` + drapeaux `hl` (mise en avant cyan), `alt` (pointillé violet), `bad` (alerte violet), `dim`. Dans les textes, `**x**` = gras cyan, `` `x` `` = mono.

| Type | Pour | Champs principaux |
|---|---|---|
| `flow` | une suite d'étapes A → B → C | `steps` [boîtes], `loop` |
| `split` | une source qui mène à 2–4 issues | `src`, `to` [boîtes], `reverse` |
| `compare` | deux options face à face | `left`/`right` `{head, big, items, hl}` |
| `stack` | des couches empilées | `head`, `layers` [`{label, r}`], `side` |
| `segments` | une barre découpée en parts | `items` [`{label, value, display}`], `total`, `cards`, `legend` |
| `timeline` | une chronologie, une fenêtre de temps | `events` [`{t, label, sub, at}`], `span` `[a, b, libellé]`, `alternate`, `w` |
| `bars` | des grandeurs comparées | `items` [`{label, value, display}`], `log` |
| `formula` | une formule et ses termes | `k`, `expr`, `terms` [`{k, v}`], `foot` |
| `fields` | une structure de données, champ par champ | `struct` `{name, lines}`, `side` (avec `from` = ligne pointée) |
| `cycle` | une boucle | `nodes`, `center` |
| `tree` | un arbre (Merkle, dérivation de clés) | `leaves`, `root`, `inner`, `hl`, `side` |
| `network` | un réseau, un quorum, des nœuds | `nodes`, `hl`, `bad`, `cluster`, `*_label`, `side` |
| `gauge` | une proportion sur un cercle | `pct`, `mark`, `big`, `label`, `side` |
| `checklist` | ce qui passe / ne passe pas | `checks` [`{text, ok, sub}`], `side` |
| `hash` | des entrées → une fonction → une sortie | `fn`, `fn_k`, `inputs`, `out` |
| `chain` | des blocs chaînés, une fourche | `blocks`, `branch` `{at, blocks}` |
| `steps` | une procédure numérotée | `steps` [`{label, sub}`], `side` |
| `table` | un petit tableau | `head`, `rows`, `cols`, `hl_col` (✓ / ✗ deviennent des icônes) |
| `curve` | une courbe y = f(x) (AMM, perte, taux) | `curves` [`{expr, label, hl}`], `xr`, `yr`, `points`, `vlines`, `xl`, `yl` |
| `big` | un chiffre clé | `k`, `big`, `label`, `side` |
