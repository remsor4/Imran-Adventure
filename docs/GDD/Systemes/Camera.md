# Camera

> **Statut :** Valide

## Objectif

Accompagner Imran sans devenir une difficulte supplementaire et conserver les plateformes, les ennemis, les projectiles et les dangers importants dans une zone lisible.

## Cadre de reference

| Element | Valeur ou regle |
|---|---|
| Resolution de reference | `1920 x 1080` |
| Format | `16:9` |
| Perspective | Vue laterale en 2D |
| Zoom d'exploration | Constant |
| Rotation | Aucune |
| Sortie des limites du niveau | Interdite |
| Position horizontale vers la droite | `45 %`, soit `864 px` |
| Position horizontale vers la gauche | `55 %`, soit `1056 px` |
| Decalage maximal depuis le centre | `96 px` |
| Duree du changement apres un demi-tour | `0.60 s` |
| Position verticale cible | `80 %`, soit `864 px` |
| Limite haute de confort | `70 %`, soit `756 px` |
| Limite basse de confort | `84 %`, soit environ `907 px` |
| Camera pendant un combat de boss | Fixe |
| Secousse d'une attaque lourde | `6 px` pendant `0.12 s` |
| Secousse d'une defaite de boss | `12 px` pendant `0.25 s` |

Les rapports sont definis pour la resolution de reference. Leur mise a l'echelle vers les autres resolutions et modes d'affichage sera detaillee pendant l'etape Interface et dans le TDD.

## Suivi horizontal

- La camera suit Imran de maniere fluide pendant les deplacements normaux.
- Lorsque Imran regarde vers la droite, sa position cible correspond a `45 %` de la largeur de l'ecran.
- Lorsqu'Imran regarde vers la gauche, sa position cible correspond a `55 %` de la largeur de l'ecran.
- A `1920 px` de largeur, ces positions correspondent a `864 px` et `1056 px`, soit un decalage maximal de `96 px` autour du centre.
- Un changement de direction deplace progressivement ce cadrage en `0.60 s`, sans saut instantane.
- Cette duree provient de la moyenne de trois demi-tours mesures dans une capture Wonder Boy a `60 images/s`.
- Les petits ajustements de position ne doivent pas produire de tremblement permanent.
- La camera ne depasse jamais la limite gauche ou droite du niveau.

## Suivi vertical

- Le suivi vertical reste plus stable que le suivi horizontal.
- Le centre visuel d'Imran vise `80 %` de la hauteur, soit `864 px` en `1080p`.
- La zone de confort s'etend de `70 %` a `84 %` de la hauteur, soit de `756 px` a environ `907 px`.
- Le saut normal de `89 px` reste entierement dans cette zone et ne provoque aucun suivi vertical.
- Une chute depassant environ `43 px` sous la position cible commence a entrainer la camera vers le bas.
- La camera se repositionne progressivement uniquement lorsqu'Imran quitte une zone verticale de confort.
- Les changements importants de hauteur conservent Imran et la prochaine plateforme utile a l'ecran.
- Une chute ne doit pas masquer le sol ou le danger vers lequel Imran se dirige.

## Lisibilite du gameplay

Le cadrage doit permettre de voir suffisamment tot :

- le bord des plateformes et les trous ;
- les ennemis au sol et les menaces aeriennes ;
- les projectiles venant de la direction de progression ;
- les zones necessaires au Dash ou au Double saut ;
- les pancartes, coffres, feux de camp et autres objets utiles ;
- la limite d'une arene ou d'une zone dangereuse.

Aucun decor au premier plan ne doit cacher durablement Imran, une plateforme ou un danger important.

## Debut et reapparition

- Au chargement d'une sequence, la camera est placee correctement avant que l'image jouable apparaisse.
- Apres la perte d'une vie, elle se replace immediatement sur Imran au debut du niveau ou au checkpoint actif.
- Le suivi fluide reprend uniquement apres ce placement initial.
- Aucun trajet de camera depuis le point de mort vers le point de reapparition n'est montre.

## Arenes de boss

- Chaque arene est concue pour tenir entierement dans le cadrage fixe `16:9`.
- Les zones de combat des sept boss mesurent `1280 px` de largeur utile.
- Dans la resolution de reference `1920 x 1080`, cette largeur est centree horizontalement.
- La limite gauche utile apparait a `x = 320 px` et la limite droite utile a `x = 1600 px`.
- Le sol principal des sept arenes apparait a `y = 896 px`.
- Une courte presentation peut deplacer la camera avant le debut du combat.
- La camera rejoint ensuite son cadrage final et se verrouille avant de rendre le controle.
- Elle ne suit plus Imran pendant le combat.
- Imran, le boss, ses attaques importantes et tous les bords de la zone restent visibles.
- La barre de vie du boss reste centree en haut de l'ecran.
- Aucun zoom ni recentrage ne se produit pendant le combat.
- Le coffre du golem reste hors du cadre pendant le combat.
- Apres la defaite, Imran avance lui-meme par le passage situe a droite.
- La zone de recompense des six golems commence apres les `1280 px` de combat et mesure `640 px`.
- La longueur totale accessible de chaque arene de golem atteint donc `1920 px`.
- Le centre du coffre se trouve a la position locale `x = 1824 px`.
- Au decalage maximal de `640 px`, le coffre apparait a `x = 1504 px` dans l'ecran.
- La camera reste fixe tant que le centre d'Imran ne depasse pas la position locale `x = 1280 px`.
- Elle commence son defilement uniquement lorsqu'il franchit cette limite.
- Elle effectue alors un recentrage horizontal de `128 px` pendant `0.50 s`.
- Imran passe progressivement de `x = 1600 px` a `x = 1472 px` dans l'ecran.
- Le joueur conserve le controle pendant ce recentrage.
- La camera suit ensuite Imran vers la droite avec un decalage maximal de `640 px`.
- Elle ne revient jamais vers la zone de combat deja depassee.
- Le decalage maximal deja atteint ne diminue jamais.
- Le bord gauche de l'ecran empeche Imran de quitter le cadre visible.
- Le coffre apparait progressivement pendant ce deplacement.
- Ces valeurs de defilement sont identiques pour les six golems.
- Apres Tata Lisa, la camera cadre Imran et la porte du donjon.

## Effets de camera

- Une attaque lourde de boss peut produire une secousse maximale de `6 px` pendant `0.12 s`.
- La defaite d'un golem ou de Tata Lisa peut produire une secousse maximale de `12 px` pendant `0.25 s`.
- Une attaque normale, un degat ordinaire et la disparition d'un ennemi commun ne produisent aucune secousse.
- Deux secousses ne peuvent pas additionner leurs amplitudes au-dela de la valeur maximale active.
- Une secousse ne doit jamais cacher une attaque, un projectile ou une plateforme.
- Les flashs plein ecran et les mouvements violents sont exclus.
- Une option permettra de reduire les secousses pendant l'etape Interface et accessibilite.

## Criteres de validation

La camera sera validee si :

- Imran et les dangers importants restent lisibles en `1920 x 1080` ;
- le suivi horizontal anticipe legerement la direction de progression ;
- un saut normal ne provoque aucun mouvement vertical inutile ;
- la camera respecte toujours les limites du niveau ;
- une reapparition commence avec un cadrage deja stabilise ;
- les combats de boss conservent Imran, le boss et les attaques importantes a l'ecran ;
- la camera reste fixe pendant chaque combat de boss ;
- une attaque lourde ne depasse jamais `6 px` pendant `0.12 s` ;
- une defaite de boss ne depasse jamais `12 px` pendant `0.25 s` ;
- les secousses restent courtes, limitees et reductibles.

## Sources

- [Camera du Concept Game](../../Concept-Game/06-Systemes/Camera.md)
- [Fiche generale](../Fiche-Generale.md)
- [Reference video Wonder Boy](../Joueur/Reference-Video-Wonder-Boy.md)
- [Reference camera Wonder Boy](Reference-Video-Wonder-Boy-Camera.md)
- [Interface visuelle](../../Concept-Game/09-Direction-Artistique/UI.md)
- [Effets visuels](../../Concept-Game/09-Direction-Artistique/Effets-Visuels.md)
