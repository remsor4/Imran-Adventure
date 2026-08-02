# Niveau 5 - Volcan

> **Statut :** Valide

## Objectif

Remplacer les Squelettes par les Zombies, montrer leur resistance de `3 PV`, puis utiliser les mouvements d'Imran pendant des rencontres longues sur des surfaces volcaniques lisibles.

## Identite

- Le parcours traverse des coulees refroidies, des falaises de basalte, de la cendre et des fissures de lave.
- Le sol principal reste a `y = 896 px`.
- Les plateformes sont des blocs de basalte statiques.
- Les fosses de lave sont declarees mortelles et restent visibles avant chaque saut.
- Les coulees placees en arriere-plan sont decoratives et ne touchent jamais la surface jouable.
- La cendre ne ralentit pas Imran et ne masque aucune preparation.

## Dimensions et structure

- Le niveau applique le [gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md).
- Sa largeur totale est de `29 664 px`.
- Imran apparait a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Le checkpoint est centre a `x = 14 304 px`.
- Le feu de camp est centre a `x = 27 360 px`.
- L'arene du Golem du Volcan commence a `x = 27 744 px`.

## Parcours detaille

| Seq. | Intervalle | Terrain et obstacle | Ennemis | Largeur utile | Fonction |
|---:|---:|---|---|---:|---|
| 1 | `1 632 a 3 936` | Sol de basalte plat | Zombie epeiste seul | `1 280 px` | Introduire les `3 PV` sans autre pression |
| 2 | `3 936 a 6 240` | Ligne de vue libre | Zombie archer seul | `1 280 px` | Introduire le tir resistant |
| 3 | `6 624 a 8 928` | Plateformes de basalte, reception sure | Serpent seul | `1 280 px` | Rappeler la menace rapide |
| 4 | `8 928 a 11 232` | Sol continu, deux zones d'atterrissage | Slime de lave + Zombie epeiste | `1 280 px` | Associer bond et lame |
| 5 | `11 616 a 13 920` | Zombie archer en soutien a droite | Zombie epeiste + Zombie archer | `1 280 px` | Reutiliser la paire de Squelettes |
| 6 | `14 688 a 16 992` | Fosse de `192 px`, reception de `384 px` | Slime seul apres reception | `960 px` | Double saut puis reprise simple |
| 7 | `16 992 a 19 296` | Sol continu de `1 440 px` | Zombie archer + Serpent | `1 440 px` | Fleche et projection rapide |
| 8 | `19 680 a 21 984` | Grande terrasse plate | Slime + Zombie epeiste + Zombie archer | `1 600 px` | Premier groupe volcanique |
| 9 | `21 984 a 24 288` | Deux receptions et sol continu | Slime + Zombie epeiste | `1 280 px` | Maintenir la pression d'endurance |
| 10 | `24 672 a 26 976` | Terrasse finale sans fosse | Slime + Zombie archer + Serpent | `1 600 px` | Groupe final avant le golem |

## Introduction des Zombies

- Le Zombie epeiste apparait seul avant le Zombie archer.
- Chaque premiere rencontre utilise un sol plat sans fosse ou autre ennemi.
- Une attaque normale produit une reaction non fatale et laisse clairement des PV restants.
- Le Smash Tranchant inflige `2 degats` mais ne bat pas un Zombie en un seul coup.
- Le comportement, les vitesses et les attaques restent ceux des Squelettes equivalents.
- Aucun Squelette n'apparait dans le niveau.

## Placement et limites des rencontres

- Les positions initiales utilisent le gabarit commun.
- Slime + Zombie epeiste et la paire de Zombies utilisent `320 px` de separation.
- Zombie archer + Serpent utilise `480 px` avec l'Archer a droite.
- Les groupes de trois utilisent `C - 480 px`, `C` et `C + 480 px`.
- Dans le premier groupe, l'ordre gauche vers droite est `Slime, Zombie epeiste, Zombie archer`.
- Dans le groupe final, le Zombie archer reste a droite du Slime et du Serpent.
- Chaque groupe de trois utilise une terrasse continue de `1 600 px`.
- Aucune Chauve-souris ou combinaison interdite n'apparait.

## Fosses de lave et mouvements

- Une fosse normale mesure au maximum `128 px`.
- La fosse de Double saut de la sequence 6 mesure `192 px`.
- Chaque bord, destination et reception est visible avant l'engagement.
- Une chute dans la lave retire une vie et provoque la reapparition normale.
- Aucun ennemi ne s'active avant les `384 px` de reception de la sequence 6.
- Une paroi de basalte coupe la ligne de vue du Slime jusqu'a cette reception.
- Les rencontres de paires et de groupes restent sur un sol continu sans lave jouable.
- Le Dash reste uniquement terrestre et ne permet jamais de traverser une fosse en quittant le sol.

## Checkpoint

- La pancarte est centree a `x = 14 304 px` sur une terrasse de basalte plate.
- Des parois refroidies bloquent les fleches des zones voisines.
- Aucune lave, fissure dangereuse ou cendre active n'entre dans la zone sure.
- L'activation reste automatique, temporaire et sans soin.

## Fin du parcours et feu de camp

- La derniere terrasse conduit a une zone sure en basalte refroidi.
- Le feu de camp est centre a `x = 27 360 px` et reste distinct des coulees de lave.
- L'interaction restaure les coeurs uniquement.
- L'ancienne coulee refroidie qui dissimule le golem devient visible avant l'arene.
- Franchir `x = 27 744 px` lance la presentation.

## Golem du Volcan

- Le combat utilise integralement la fiche [Golem du Volcan](../Boss/Golem-Volcan.md).
- Son cycle utilise l'Orbe de magma frontal, la Double vague de lave et l'Eruption volcanique ciblee.
- Le combat verifie le Bouclier, le saut, le Double saut et le Dash au sol.
- L'arene reste plate et les coulees d'arriere-plan ne produisent aucun danger supplementaire.

## Coffre, cle et transition

- Le coffre utilise du bois noirci, du basalte, de l'obsidienne, de la cendre et une serrure rouge-orange.
- Son centre global se trouve a `x = 29 568 px`.
- La cinquieme cle est ajoutee apres l'ouverture volontaire.
- La sauvegarde debloque le Chateau de Tata Lisa avant la transition.
- Imran commence le niveau 6 avec `3 coeurs` et `3 vies`.

## Reprise et retour en arriere

- Une vie perdue replace Imran a `x = 864 px` ou `x = 14 304 px` selon le checkpoint.
- Tous les Zombies, Slimes, Serpents, projectiles et dangers temporaires sont reinitialises.
- Le retour en arriere reste possible avant l'arene.
- Un Game Over recommence le niveau et oublie le checkpoint.

## Criteres de validation

- les deux Zombies apparaissent seuls avant leur premiere combinaison ;
- aucun Squelette ou Chauve-souris n'apparait ;
- les Zombies conservent `3 PV` et les comportements de leur variante d'origine ;
- les paires et groupes respectent `1 280`, `1 440` ou `1 600 px` ;
- aucune fosse de lave ne partage une nouvelle reception avec un ennemi actif ;
- les groupes de trois conservent plusieurs solutions d'esquive ;
- le checkpoint, le feu, l'arene et le coffre restent surs et mesurables ;
- le niveau vise `20 a 25 min`.

## Sources

- [Volcan](../../Concept-Game/03-Univers/Volcan.md)
- [Gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Zombies](../Ennemis/Zombies.md)
- [Golem du Volcan](../Boss/Golem-Volcan.md)
