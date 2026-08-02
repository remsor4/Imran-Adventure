# Niveau 1 - Foret enchantee

> **Statut :** Valide

## Objectif

Confirmer les bases apprises dans le Village, introduire la Chauve-souris seule, puis presenter les premieres paires d'ennemis avant le Golem de la Foret.

## Identite

- Le parcours traverse une foret coloree composee d'arbres massifs, de racines, de feuillages et de magie naturelle.
- Le sol principal utilise de la terre et des racines avec une surface de reference a `y = 896 px`.
- Les plateformes sont des racines larges et des branches statiques.
- Les ravins restent visibles avant le saut et utilisent des parois vegetales claires.
- Aucun feuillage au premier plan ne masque Imran, une reception ou un ennemi.

## Dimensions et structure

- Le niveau applique le [gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md).
- Sa largeur totale est de `29 664 px`.
- Imran apparait a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Le checkpoint est centre a `x = 14 304 px`.
- Le feu de camp est centre a `x = 27 360 px`.
- L'arene du Golem de la Foret commence a `x = 27 744 px`.

## Entree sure et rappel des mouvements

- L'entree montre immediatement les couleurs et les grandes racines de la Foret.
- Une porte de racines non dangereuse sert de premier rappel du Dash.
- Une dalle naturelle a `x = 1 024 px` ouvre cette porte pendant `0.70 s`.
- La porte se trouve a `x = 1 216 px`, soit `192 px` apres la dalle.
- La marche normale parcourt seulement `168 px` pendant cette duree.
- Un Dash suivi du mouvement normal permet de parcourir environ `244 px` et de franchir les `192 px` avec une marge de `52 px`.
- Un echec ferme simplement la porte et permet un nouvel essai sans degat.
- La porte reste ouverte lors d'un retour depuis la droite.
- Aucun danger ne commence avant `x = 1 632 px`.

## Parcours detaille

| Seq. | Intervalle | Terrain et obstacle | Ennemis | Largeur utile | Fonction |
|---:|---:|---|---|---:|---|
| 1 | `1 632 a 3 936` | Ledge de racine a `128 px`, reception sure | Slime vegetal seul | `960 px` | Rappeler le Double saut et l'attaque |
| 2 | `3 936 a 6 240` | Sol plat et ligne de vue libre | Squelette archer seul | `1 280 px` | Rappeler le Bouclier frontal |
| 3 | `6 624 a 8 928` | Clairiere de `480 px` de hauteur libre | Chauve-souris seule | `1 280 x 480 px` | Introduire la plongee aerienne |
| 4 | `8 928 a 11 232` | Sol continu sans ravin | Slime + Slime | `960 px` | Lire deux bonds simultanes |
| 5 | `11 616 a 13 920` | Sol plat, Archer en soutien a droite | Slime + Archer | `1 280 px` | Bloquer une fleche pendant un bond |
| 6 | `14 688 a 16 992` | Branche statique basse, reception de `256 px` | Chauve-souris seule | `1 280 x 480 px` | Reprendre apres le checkpoint |
| 7 | `16 992 a 19 296` | Sol continu et deux zones d'atterrissage | Slime + Slime | `960 px` | Confirmer le rythme des bonds |
| 8 | `19 680 a 21 984` | Sol plat, aucune fermeture du passage | Slime + Archer | `1 280 px` | Augmenter la pression terrestre |
| 9 | `21 984 a 24 288` | Clairiere ouverte sans plafond bas | Slime + Chauve-souris | `1 280 x 480 px` | Combiner danger terrestre et aerien |
| 10 | `24 672 a 26 976` | Deux receptions visibles et sol continu | Slime + Chauve-souris | `1 280 x 480 px` | Derniere verification avant le golem |

## Placement et limites des rencontres

- Les positions initiales utilisent le gabarit commun par rapport au centre de chaque sequence.
- Les deux Slimes sont separes de `256 px`.
- Le Slime et l'Archer sont separes de `320 px`, avec l'Archer a droite.
- Le Slime et la Chauve-souris sont separes de `320 px` horizontalement.
- La Chauve-souris dispose toujours de `480 px` de hauteur libre.
- Une barriere de collision de decor arrete les fleches avant chaque respiration, le checkpoint et le feu de camp.
- Aucun ennemi ne quitte sa rencontre et aucun groupe de trois n'apparait.
- Aucun Epeiste, Serpent ou Zombie n'est utilise.

## Plateformes et receptions

- La premiere elevation de `128 px` apparait sans ennemi actif dans la trajectoire du Double saut.
- Le Slime de la sequence 1 ne peut s'activer qu'apres une reception sure de `256 px`.
- Une racine solide coupe sa ligne de vue jusqu'a cette reception.
- Les ravins de la Foret mesurent au maximum `128 px` pour un saut normal et `192 px` pour un Double saut.
- Chaque plateforme au-dessus d'un ravin mesure au moins `256 px`.
- Une chute dans un ravin hors niveau retire une vie et applique la reprise normale.
- Les sequences avec deux ennemis utilisent un sol continu et ne sont jamais combinees a un ravin.

## Checkpoint

- La pancarte de controle est centree a `x = 14 304 px` dans une clairiere plate.
- Elle s'active automatiquement sans interrompre Imran.
- Des racines solides ferment les lignes de tir des sequences 5 et 6 vers la zone sure.
- Elle ne restaure ni coeur ni vie et ne sauvegarde pas la partie.

## Fin du parcours et feu de camp

- La sequence 10 conduit a une clairiere calme de `768 px`.
- Le feu de camp laisse par Remi et Amelie est centre a `x = 27 360 px`.
- L'interaction volontaire restaure les coeurs a `3` sans modifier les vies.
- La mousse, les racines et les arbres forment visuellement l'entree de l'arene.
- Franchir `x = 27 744 px` ferme les barrieres et declenche la presentation du golem.

## Golem de la Foret

- Le combat utilise integralement la fiche [Golem de la Foret](../Boss/Golem-Foret.md).
- Il constitue le premier apprentissage des regles communes des golems.
- Son cycle utilise le Projectile vegetal frontal, l'Onde de racines au sol et le Coup de poing direct.
- La zone de combat reste plate, sans fosse, plateforme, pente ou obstacle.
- Le coffre reste hors du cadre jusqu'a la defaite du golem.

## Coffre, cle et transition

- La zone de recompense utilise du bois, des racines, des feuilles et des motifs naturels.
- Le coffre se trouve a la coordonnee globale `x = 29 568 px`.
- Il s'ouvre avec `Interaction` a `56 px` ou moins.
- La premiere cle est ajoutee automatiquement a la fin de l'ouverture.
- La sauvegarde debloque la Grotte mysterieuse avant le fondu de transition.
- Imran commence le niveau 2 avec `3 coeurs` et `3 vies`.

## Reprise et retour en arriere

- Avant le checkpoint, une vie perdue replace Imran a `x = 864 px`.
- Apres son activation, une vie perdue replace Imran a `x = 14 304 px`.
- Tous les ennemis, projectiles, portes et dangers temporaires reviennent a leur etat initial.
- Imran peut revenir vers la gauche jusqu'a l'entree tant que l'arene n'est pas fermee.
- Un Game Over recommence le niveau depuis le debut et oublie le checkpoint.

## Criteres de validation

- le niveau contient exactement dix sequences reparties `3 simples, 4 intermediaires, 3 exigeantes` ;
- le Dash et le Double saut sont rappeles sans ennemi actif pendant leur premiere utilisation ;
- la Chauve-souris apparait seule avant toute combinaison ;
- Slime + Slime, Slime + Archer et Slime + Chauve-souris respectent leurs espaces ;
- aucun groupe de trois ou ennemi non prevu n'apparait ;
- le checkpoint et le feu de camp restent totalement surs ;
- le Golem de la Foret reste le pic de difficulte ;
- un joueur novice peut viser `20 a 25 min` et atteindre le feu avec au moins `2 vies`.

## Sources

- [Foret enchantee](../../Concept-Game/03-Univers/Foret-Enchantee.md)
- [Gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Courbe de difficulte](../Equilibrage/Courbe-de-Difficulte.md)
- [Golem de la Foret](../Boss/Golem-Foret.md)
- [Coffres et cles](../Systemes/Coffres-et-Cles.md)
