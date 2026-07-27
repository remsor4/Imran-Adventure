# GDD - Boss et golems

> **Statut :** En cours

## Objectif

Definir les regles communes et les sept combats obligatoires afin que chaque boss possede un debut lisible, des attaques previsibles, une progression, des ouvertures de contre-attaque et une fin complete.

## Documents

| Ordre | Document | Statut |
|---:|---|---|
| 1 | [Regles communes](Regles-Communes.md) | Valide |
| 2 | [Golem de la Foret](Golem-Foret.md) | Valide |
| 3 | [Golem de la Grotte](Golem-Grotte.md) | Valide |
| 4 | [Golem du Lac gele](Golem-Lac.md) | Valide |
| 5 | [Golem du Desert](Golem-Desert.md) | A rediger |
| 6 | [Golem du Volcan](Golem-Volcan.md) | A rediger |
| 7 | [Golem du Chateau](Golem-Chateau.md) | A rediger |
| 8 | [Tata Lisa](Tata-Lisa.md) | A rediger |

## Ordre de validation

1. Fixer la structure commune des arenes et des combats.
2. Definir le Golem de la Foret comme premier apprentissage.
3. Definir le Golem de la Grotte.
4. Definir le Golem du Lac gele.
5. Definir le Golem du Desert.
6. Definir le Golem du Volcan.
7. Definir le Golem du Chateau.
8. Definir le combat final contre Tata Lisa.
9. Verifier la progression et la coherence des sept combats.

## Regles deja acquises

- Les six golems protegent chacun un coffre et une cle.
- Tata Lisa constitue le boss final apres la sixieme cle.
- Les sept combats sont obligatoires.
- Chaque attaque de boss retire `1 coeur` par defaut.
- L'attaque normale inflige `1 degat` au boss.
- Le Smash Tranchant inflige `2 degats` au premier boss touche puis disparait.
- Un projectile frontal peut etre bloque automatiquement par le Bouclier de lumiere.
- Un feu de camp permet de restaurer volontairement les coeurs avant chaque golem.
- Une perte de vie restaure le boss a sa vie maximale et a sa premiere phase.
- La barre de vie du boss est centree en haut de l'ecran pendant le combat.
- Toutes les zones de combat de boss mesurent `1280 px` de largeur utile.
- Le sol principal des sept arenes de boss se trouve a `y = 896 px`.
- Les zones de combat apparaissent entre `x = 320 px` et `x = 1600 px` dans le cadre de reference.
- Les barrieres des six golems utilisent une energie semi-transparente et des particules adaptees a leur theme.
- Les zones de recompense des six golems mesurent `640 px`.
- Le centre des six coffres se trouve a la position locale `x = 1824 px`.
- Le defilement vers les six coffres utilise le meme recentrage de `128 px` en `0.50 s`.
- La distance d'interaction commune des six coffres est de `56 px`.
- Les six golems utilisent le meme decoupage de defaite de `1.00 s`, adapte a leur theme.
- La victoire contre un golem rend son coffre accessible.
- La victoire contre Tata Lisa brise la Pierre du Chaos et lance la conclusion.

## Criteres de validation de l'etape

L'etape 9 est validee si :

- chaque combat possede une introduction, un declenchement et une fin ;
- chaque boss possede des points de vie, des phases et des attaques mesurables ;
- chaque attaque possede une preparation, une phase dangereuse et une recuperation ;
- chaque boss possede des fenetres de vulnerabilite lisibles ;
- les changements de phase sont clairement annonces ;
- chaque arene permet d'eviter les attaques sans degat inevitable ;
- les recompenses et les reprises respectent les systemes deja valides ;
- Tata Lisa possede une conclusion complete apres la destruction de la Pierre du Chaos ;
- aucune regle technique propre a Godot n'est imposee dans le GDD.

## Sources principales

- [Boss du Concept Game](../../Concept-Game/05-Gameplay/Boss.md)
- [Principes des golems](../../Concept-Game/08-Boss/Principes-des-Golems.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Degats](../Combat/Degats.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Checkpoints](../Systemes/Checkpoints.md)
- [Coffres et cles](../Systemes/Coffres-et-Cles.md)
- [Sauvegarde](../Systemes/Sauvegarde.md)
- [Reference video des degats des boss](Reference-Video-Wonder-Boy-Degats-Boss.md)
- [Reference video des dimensions des boss](Reference-Video-Wonder-Boy-Dimensions-Boss.md)
- [Reference video des collisions avec le corps des boss](Reference-Video-Wonder-Boy-Collisions-Boss.md)
- [Reference video du rythme des attaques de boss](Reference-Video-Wonder-Boy-Rythme-Boss.md)
- [Reference video de la defaite d'un boss](Reference-Video-Wonder-Boy-Defaite-Boss.md)
