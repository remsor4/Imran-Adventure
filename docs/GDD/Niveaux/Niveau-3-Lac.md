# Niveau 3 - Lac gele

> **Statut :** Valide

## Objectif

Introduire le Serpent seul, apprendre a anticiper l'inertie du sol glace et alterner Dash et Double saut avec un appui stable entre les actions.

## Identite

- Le parcours traverse la rive d'un lac gele, des arches de glace, de la neige et des cristaux froids.
- Le sol principal reste a `y = 896 px`.
- Les surfaces bleues lisses utilisent le comportement de glace valide dans la fiche du Golem du Lac.
- Les zones blanches de neige compacte utilisent le deplacement normal et servent d'appuis stables.
- Les ouvertures dans le lac sont des chutes hors niveau clairement visibles.
- La brume et les flocons restent en arriere-plan et ne masquent aucun signal.

## Dimensions et structure

- Le niveau applique le [gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md).
- Sa largeur totale est de `29 664 px`.
- Imran apparait a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Le checkpoint est centre a `x = 14 304 px` sur de la neige compacte.
- Le feu de camp est centre a `x = 27 360 px` sur une dalle rocheuse non glissante.
- L'arene du Golem du Lac commence a `x = 27 744 px`.

## Introduction sure de la glace

- Une surface glacee de `768 px` commence apres `x = 1 024 px`.
- Elle ne contient aucun ennemi, fosse ou obstacle.
- Une bande de neige compacte de `256 px` termine cette pratique avant le premier danger.
- Le joueur peut observer l'acceleration et le freinage sans perdre de coeur ou de vie.
- Aucun danger ne commence avant `x = 1 632 px`.

## Parcours detaille

| Seq. | Intervalle | Terrain et obstacle | Ennemis | Largeur utile | Fonction |
|---:|---:|---|---|---:|---|
| 1 | `1 632 a 3 936` | Glace plate puis appui de neige | Slime de glace seul | `960 px` | Adapter le bond au freinage |
| 2 | `3 936 a 6 240` | Sol glace et ligne de vue libre | Squelette archer seul | `1 280 px` | Bloquer en mouvement sur glace |
| 3 | `6 624 a 8 928` | Longue surface de neige continue | Serpent seul | `1 280 px` | Introduire sa vitesse et sa projection |
| 4 | `8 928 a 11 232` | Glace, fosse de `128 px`, appui stable | Slime seul | `960 px` | Alterner saut et repositionnement |
| 5 | `11 616 a 13 920` | Sol de `1 440 px`, deux receptions | Slime + Serpent | `1 440 px` | Gerer deux menaces terrestres |
| 6 | `14 688 a 16 992` | Appui stable, Dash, appui, Double saut | Archer seul | `1 280 px` | Alterner les deux capacites |
| 7 | `16 992 a 19 296` | Longue dalle de neige | Serpent seul | `1 280 px` | Reprendre la lecture de proximite |
| 8 | `19 680 a 21 984` | Glace plate et meme hauteur de tir | Slime + Archer | `1 280 px` | Reutiliser une paire connue sur glace |
| 9 | `21 984 a 24 288` | Sol continu de `1 440 px` | Slime + Serpent | `1 440 px` | Confirmer les zones d'atterrissage |
| 10 | `24 672 a 26 976` | Neige compacte, Archer a droite | Archer + Serpent | `1 440 px` | Derniere pression terrestre rapide |

## Enchainement de la sequence 6

- Une dalle de neige stable precede chaque action.
- Une porte de glace non dangereuse utilise une dalle et une ouverture de `0.70 s` pour demander le Dash sur `192 px`.
- Une reception stable de `320 px` suit la porte.
- Une plateforme a `128 px` de hauteur demande ensuite le Double saut.
- Sa reception mesure `384 px` et reste separee de l'Archer par un mur de glace.
- L'Archer devient visible et peut tirer seulement apres cette derniere reception.
- Aucun mouvement ne demande un Dash aerien.

## Placement et limites des rencontres

- Les positions initiales utilisent le gabarit commun.
- Slime + Serpent et Archer + Serpent utilisent une separation de `480 px`.
- Slime + Archer utilise une separation de `320 px` sur le meme niveau de sol.
- L'Archer reste a droite dans les paires.
- Les Serpents utilisent un sol continu et ne peuvent jamais projeter Imran vers une unique reception dangereuse.
- Les Slimes et Serpents restent dans leur zone malgre l'inertie d'Imran.
- Aucun Epeiste, Zombie ou Chauve-souris n'apparait.
- Serpent + Serpent et les groupes de trois restent exclus de ce niveau.

## Checkpoint

- La pancarte est centree a `x = 14 304 px` sur `768 px` de neige compacte.
- Cette surface utilise le deplacement normal et arrete naturellement la glissade.
- Des blocs de glace solides interceptent les projectiles des sequences voisines.
- La zone ne contient aucune ouverture dans le lac.

## Fin du parcours et feu de camp

- La sequence 10 se termine sur une dalle rocheuse stable.
- Le feu de camp est centre a `x = 27 360 px` et ne repose pas directement sur la glace.
- L'interaction restaure les coeurs sans modifier les vies.
- La paroi de glace contenant le golem devient visible a droite.
- L'arene commence a `x = 27 744 px` et utilise ensuite son sol glace integral.

## Golem du Lac gele

- Le combat utilise integralement la fiche [Golem du Lac gele](../Boss/Golem-Lac.md).
- Son cycle utilise le Disque de glace frontal, la Vague gelee au sol et la Tempete de givre ciblee.
- Le sol de l'arene utilise le meme comportement de glace que les surfaces bleues du niveau.
- La camera reste fixe et le sol reste unique, plat et sans fosse.

## Coffre, cle et transition

- Le coffre utilise du bois bleu sombre, du metal gris bleute, du givre et des cristaux de glace.
- Son centre global se trouve a `x = 29 568 px`.
- La troisieme cle est ajoutee apres l'ouverture volontaire.
- La sauvegarde debloque le Desert oublie avant la transition.
- Imran commence le niveau 4 avec `3 coeurs` et `3 vies`.

## Reprise et retour en arriere

- Une vie perdue replace Imran au debut ou a `x = 14 304 px` selon le checkpoint.
- La vitesse est nulle et Imran reapparait sur une surface non glissante.
- Tous les ennemis, projectiles, portes et dangers temporaires sont reinitialises.
- Le retour vers la gauche reste possible avant l'arene.
- Un Game Over recommence le niveau et oublie la pancarte.

## Criteres de validation

- la glace est pratiquee sans danger avant sa premiere rencontre ;
- le Serpent apparait seul avant ses paires ;
- Dash et Double saut sont alternes avec un appui stable entre eux ;
- Slime + Serpent, Slime + Archer et Archer + Serpent respectent leurs largeurs ;
- aucune reception obligatoire ne reste sur une surface glissante trop courte ;
- Serpent + Serpent et tous les groupes de trois sont absents ;
- le checkpoint et le feu utilisent un sol stable ;
- le niveau vise `20 a 25 min` sans changer les statistiques ennemies.

## Sources

- [Lac gele](../../Concept-Game/03-Univers/Lac-Gele.md)
- [Gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Slimes](../Ennemis/Slimes.md)
- [Serpents](../Ennemis/Serpents.md)
- [Squelettes](../Ennemis/Squelettes.md)
- [Golem du Lac gele](../Boss/Golem-Lac.md)
