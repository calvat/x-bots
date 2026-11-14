# Règles de rédaction

## Choisir un sujet de thread

Un sujet n'est retenu que s'il :
- se découpe en **petites thématiques**, chacune tenant dans un post de 500 caractères maximum ;
- tient **au moins 30 posts et au plus 100**, sans remplissage (chaque post ayant au moins 2 versions, cela fait 60 à 200 textes) ;
- est **assez technique pour être intéressant**, mais reste compréhensible par quelqu'un qui n'est pas développeur.

## Écrire un post

- En **anglais**, **500 caractères maximum** comptés façon X (Johan a X Premium), préfixe et hashtag de campagne compris. Viser environ 300 à 450 : 500 est une limite, pas un objectif.
- **Structure du post** : l'accroche (préfixe compris) tient dans les **~250 premiers caractères**, ceux que X affiche avant « Show more ». Elle doit se suffire à elle-même. Puis une **ligne vide**, puis un peu plus de détail sur la même info (le mécanisme, le chiffre exact, la conséquence), tiré de `long`.
- Pas d'ouverture du type `Unlocking it 🔑` dans les posts de campagne : elle est réservée aux réponses ponctuelles (voir plus bas).
- **Une seule info technique par post**, compréhensible seule (un post peut être partagé hors du thread).
- **Ordre de rédaction, pour chaque post.** L'idée est d'utiliser le fonctionnement des LLM : un modèle écrit dans l'ordre, et ce qu'il a déjà écrit guide la suite. On le force donc à réfléchir d'abord, puis à reformuler. Les champs de `posts.json` sont dans cet ordre, et un générateur doit les remplir dans cet ordre, jamais `simple` avant `long` :
  1. `long` : on résume d'abord, en 500 caractères maximum, tout ce qu'on cherche à dire (le fait, le chiffre, le contexte, pourquoi c'est intéressant). C'est la référence du post : les autres versions en sont tirées.
  2. `tech` : ensuite seulement, la version technique, tirée de `long`.
  3. `simple` : en dernier, la version simple, tirée de `long` et de `tech`.
- Chaque post est proposé en **au moins 2 versions** (`simple` et `tech` dans `posts.json`), parfois 3 :
  - `simple` : pour tout le monde, sans jargon ou avec le jargon expliqué ;
  - `tech` : plus précis, avec les chiffres et les termes exacts ;
  - `variant` (optionnel) : une variante, par exemple plus accrocheuse ou avec un autre angle.
- Johan choisit une version par post au moment de publier.
- **Affirmations vérifiées** : chaque chiffre, date ou nom a une source notée dans le champ `source` du post (lien, BIP, EIP, rapport post-mortem). Toutes les versions d'un post doivent être vraies, la version simple aussi.
- Un chiffre approximatif s'écrit avec "about" ou "≈".
- Pas de conseil financier, pas de prédiction de prix.
- Le post 1 accroche, le dernier résume et invite à suivre.
- **Publication : 1 post de chaque thread par jour.** Chaque post doit donc se lire seul, sans le post de la veille.

## Préfixe

- Chaque post commence par un **préfixe identique dans tout le thread**, suivi du numéro : par exemple `Inside #Pactus #12:`.
- Le préfixe est **court et percutant**, **propre au sujet** (pas générique comme "Your Keys") et **différent pour chaque thread**.
- Règle simple : **en lisant le préfixe, on doit comprendre que ça touche l'univers crypto** (crypto, web3, blockchain, DeFi...). S'il est trop général ou ambigu, ajouter un mot (par exemple `Crypto #Anonymity Myths #N:`) ou le changer.
- Au moins un mot du préfixe est un **hashtag très utilisé** (comme `#Pactus`, `#Bitcoin`, `#DeFi`, `#Wallet`).
- Il compte dans les 500 caractères et dans l'accroche visible avant « Show more » : viser 30 caractères au plus.
- La liste des préfixes validés est dans `SUJETS.md`.

## Hashtags : 2 maximum par post

- **2 hashtags maximum par post**, tels que publiés : celui du **préfixe** et le **hashtag de campagne** (`#XCKbtc1`…), que le programme ajoute à la fin. Au-delà, X et les lecteurs y voient du spam.
- Le texte écrit (`simple`, `tech`, `variant`) ne contient donc **aucun autre hashtag** : ni hashtags fixes en fin de post, ni hashtag dans les phrases (écrire le mot sans `#`). Une mention comme `@PactusChain` reste possible.
- La numérotation (`#12:`) n'est pas un hashtag.
- Le hashtag de campagne compte dans les 500 caractères.

## Accroches : au moins 5 par campagne

Chaque dossier de campagne contient un dossier `hooks/` (« hooks » = accroches en anglais) dont le fichier `hooks.json` contient **au moins 5 accroches**, chacune avec **sa propre illustration**. Une accroche est une réponse que Johan colle à la main sous un post populaire qui parle du même sujet, pour faire connaître le thread.

**Le texte**
- Il dit **ce que raconte la campagne** et **donne envie d'aller voir** : le sujet du thread, 2 ou 3 de ses épisodes les plus marquants (un chiffre, une affaire, une question intrigante), et une invitation à suivre. Pas une simple info isolée.
- Dans la **langue du thread** (en anglais pour XCryptoKeys), **moins de 280 caractères** comptés façon X (une réponse doit se lire en entier sans « Show more »).
- Uniquement des faits déjà vérifiés dans `posts.json` de la campagne.
- Se termine par le **hashtag de campagne** (`#XCKbtc1`…), ajouté à la génération. **Aucun lien** (X pousse moins les réponses avec un lien), 2 hashtags maximum.
- Les 5 accroches prennent **des angles différents** (aperçu du sommaire, question, parcours, idée reçue contre réalité, chiffre fort) pour répondre à 5 posts sans se répéter.
- Pas de conseil financier, pas de prédiction de prix, pas de ton commercial.
- **Pas d'automatisation** : le bot ne publie jamais les accroches. Johan choisit à la main sous quels posts répondre.

**L'illustration**
- **Un dessin sur mesure par accroche**, sur le modèle de `threads/pactus-001/src/post_6.html` : un vrai schéma qui montre le mécanisme ou l'affaire dont parle le texte (courbe, jauge, frise, arbre, flux, comparaison d'adresses…), pas une carte de texte. Il s'écrit à la main dans `hooks/src/hook_N.html` ; `card.py` ne l'écrase jamais.
- **Jamais deux fois la même illustration dans une campagne** : ni entre deux accroches, ni avec l'image d'un post de la campagne. Chaque accroche a son propre type de dessin (pas 5 fois une liste de cartes).
- **Coller au message** : l'image reprend ce que dit le texte (même thème, même question, même chiffre), sans rien affirmer de plus que `posts.json`.
- Les 5 mises en page automatiques (`layout` : `hero`, `list`, `question`, `chain`, `versus`, dans `design/card.py`, fonction `accroche_body`) ne servent que de brouillon, avant le dessin sur mesure.
- Style de `STYLE-GRAPHIQUE.md`.

Format de `hooks/hooks.json` :

```json
[
  {
    "index": 1,
    "text": "texte de la réponse, sans le hashtag de campagne",
    "card": { "layout": "list", "title": "Titre", "items": ["Thème 1", "Thème 2", "Thème 3", "Thème 4"], "sub": "Une phrase" },
    "used": null
  }
]
```

Champs de `card` selon `layout` : `hero` (`title`, `big`, `sub`, `items` ×3, `foot`), `list` (`title`, `items` ×4, `sub`), `question` (`q`, `sub`), `chain` (`title`, `items` ×4, `sub`), `versus` (`left` et `right` = `{"label", "items"}`, `sub`).
`used` : `null`, ou le lien du post sous lequel l'accroche a été postée (pour ne pas la réutiliser).

Générer les images et la liste à copier (`hooks/HOOKS.md`, à ne pas modifier à la main), depuis la racine du dépôt :
`python3 design/card.py accounts/XCryptoKeys/threads/<campagne> --hooks --png`

Contenu de `threads/<campagne>/hooks/` : `hooks.json` (la source des textes), `HOOKS.md` (textes à copier avec leur image), `hook_N.png` (les images), `src/hook_N.html` (les dessins sur mesure, sources des images).

## Réponses ponctuelles (sous un post X collé par Johan)

- Johan colle un post X ; on propose **1 ou 2 réponses en anglais**, prêtes à copier-coller, **moins de 280 caractères**, qui commencent par une **ouverture variée** finissant par 🔑, jamais la même deux fois de suite (ni deux fois dans une même proposition). Liste de départ : `Unlocking it 🔑`, `Key detail 🔑`, `Here's the key 🔑`, `Under the hood 🔑`, `The key part 🔑`, `Quick unlock 🔑`, `Worth knowing 🔑`, `Key fact 🔑`, `One key nuance 🔑`, `Let's unlock this 🔑`. On peut en inventer d'autres dans le même esprit (court, lié à la clé ou au déverrouillage). Cette ouverture ne concerne que les réponses, pas les posts de campagne.
- Ton pédagogique et technique, une seule info par réponse, sans conseil financier, sans prédiction de prix, sans shilling, sans lien ni hashtag.
- Un fait non vérifié s'écrit prudemment (« often », « likely », « ≈ ») et est signalé à Johan.
- Puis **une ligne de recommandation en français** qui dit quelle réponse choisir et pourquoi.
- **Toujours générer une image pour la réponse recommandée** : schéma sur mesure 1200 × 675 dans le style de `STYLE-GRAPHIQUE.md`, qui montre ce que dit la réponse sans rien affirmer de plus. Source dans `reponses/<sujet>/src/reply.html`, image dans `reponses/<sujet>/reply_N.png`, rendue avec Playwright.
- Rien n'est publié automatiquement : Johan poste lui-même.
