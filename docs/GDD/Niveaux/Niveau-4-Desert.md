# Niveau 4 - Desert oublie

> **Statut :** Valide

## Objectif

Faire utiliser l'enchainement Dash, saut et Double saut, introduire Serpent + Serpent, puis presenter les premiers groupes de trois dans de grandes zones terrestres lisibles.

## Identite

- Le parcours traverse des dunes, des arches de gres et des ruines anciennes.
- Le sol principal reste a `y = 896 px`.
- Les plateformes sont des blocs de gres statiques et des marches larges.
- Le sable visible ne ralentit pas Imran et ne modifie pas ses sauts.
- Les fosses correspondent a des parties effondrees des ruines et restent visibles avant l'engagement.
- La chaleur, la poussiere et les grains de sable restent purement visuels.

## Dimensions et structure

- Le niveau applique le [gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md).
- Sa largeur totale est de `29 664 px`.
- Imran apparait a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Le checkpoint est centre a `x = 14 304 px`.
- Le feu de camp est centre a `x = 27 360 px`.
- L'arene du Golem du Desert commence a `x = 27 744 px`.

## Enchainement de mouvements recommande

- La sequence 1 commence par une demonstration sans ennemi actif.
- Une dalle ouvre une porte de gres pendant `0.70 s` a `192 px`, ce qui demande un Dash au sol.
- Une surface stable de `256 px` suit la porte.
- Une fosse de `128 px` demande ensuite un saut normal.
- Une seconde surface stable de `256 px` separe le saut du Double saut.
- Une corniche a `128 px` de hauteur demande enfin le Double saut.
- La reception finale mesure `384 px` et precede l'activation du Slime.
- Un mur de ruine coupe la ligne de vue du Slime jusqu'a cette reception.
- Aucune commande de Dash recue dans les airs n'est necessaire.

## Parcours detaille

| Seq. | Intervalle | Terrain et obstacle | Ennemis | Largeur utile | Fonction |
|---:|---:|---|---|---:|---|
| 1 | `1 632 a 3 936` | Enchainement Dash, saut, Double saut, puis reception | Slime de sable seul | `960 px` | Apprendre la chaine sans pression active |
| 2 | `3 936 a 6 240` | Galerie de ruine plate | Squelette epeiste seul | `1 280 px` | Rappeler la lame permanente |
| 3 | `6 624 a 8 928` | Sol continu et deux zones d'atterrissage | Serpent + Serpent | `1 280 px` | Introduire la paire rapide |
| 4 | `8 928 a 11 232` | Sol de `1 440 px`, Archer a droite | Archer + Serpent | `1 440 px` | Pression distante et terrestre |
| 5 | `11 616 a 13 920` | Sol de `1 280 px`, reception libre | Slime + Epeiste | `1 280 px` | Eviter bond et lame |
| 6 | `14 688 a 16 992` | Grande allee de ruines | Epeiste + Serpent | `1 440 px` | Reprendre apres le checkpoint |
| 7 | `16 992 a 19 296` | Archer en soutien, sol continu | Archer + Serpent | `1 440 px` | Confirmer la paire avancee |
| 8 | `19 680 a 21 984` | Grande cour sans fosse | Slime + Epeiste + Archer | `1 600 px` | Introduire le premier groupe de trois |
| 9 | `21 984 a 24 288` | Deux zones d'atterrissage visibles | Epeiste + Serpent | `1 440 px` | Consolider la pression terrestre |
| 10 | `24 672 a 26 976` | Cour finale plate et ouverte | Epeiste + Serpent + Archer | `1 600 px` | Derniere combinaison avant le golem |

## Placement et limites des rencontres

- Les positions initiales utilisent le gabarit commun.
- Serpent + Serpent utilise une separation de `480 px`.
- Archer + Serpent et Epeiste + Serpent utilisent `480 px`.
- Slime + Epeiste utilise `320 px` et conserve une reception sure.
- Les groupes de trois utilisent les positions `C - 480 px`, `C` et `C + 480 px`.
- Dans Slime + Epeiste + Archer, l'Archer reste a droite et le Slime ne couvre pas l'unique reception.
- Dans Epeiste + Serpent + Archer, l'ordre gauche vers droite est `Epeiste, Serpent, Archer`.
- Les groupes de trois apparaissent uniquement sur un sol plat de `1 600 px`.
- Aucune Chauve-souris ou Zombie n'apparait.
- Aucune combinaison interdite n'est utilisee.

## Obstacles et fosses

- Les fosses de saut normal mesurent au maximum `128 px`.
- Les fosses de Double saut mesurent au maximum `192 px`.
- Les groupes de deux ou trois ennemis ne partagent jamais leur zone avec une nouvelle fosse.
- Les premieres utilisations de chaque obstacle sont terminees avant l'activation d'une rencontre.
- Une chute hors des ruines retire une vie et declenche la reapparition normale.
- Les tempetes de sable ne produisent aucun degat et ne modifient pas la visibilite du gameplay.

## Checkpoint

- La pancarte est centree a `x = 14 304 px` sur une dalle de gres plate.
- Deux murs de ruine bloquent les projectiles voisins sans fermer le passage.
- Aucun sable mobile, ennemi ou fosse n'entre dans les `768 px` de la zone.
- L'activation ne restaure aucune ressource et reste temporaire.

## Fin du parcours et feu de camp

- La derniere cour conduit a une zone de ruines calme.
- Le feu de camp est centre a `x = 27 360 px`.
- L'interaction volontaire restaure les coeurs uniquement.
- La facade ancienne qui dissimule le golem devient visible depuis cette zone.
- Franchir `x = 27 744 px` lance la presentation du boss.

## Golem du Desert

- Le combat utilise integralement la fiche [Golem du Desert](../Boss/Golem-Desert.md).
- Son cycle utilise le Javelot de gres, le Mur de sable et le Piege des ruines.
- Il verifie le Bouclier, le Double saut et l'enchainement des mouvements pratique dans le niveau.
- L'arene reste plate, sans plateforme, pente, fosse ou obstacle.

## Coffre, cle et transition

- Le coffre utilise du bois brun sombre, du gres ocre, du bronze, des symboles graves et une serrure ambre.
- Son centre global se trouve a `x = 29 568 px`.
- La quatrieme cle est ajoutee apres l'ouverture volontaire.
- La sauvegarde debloque le Volcan avant la transition.
- Imran commence le niveau 5 avec `3 coeurs` et `3 vies`.

## Reprise et retour en arriere

- Une vie perdue replace Imran a `x = 864 px` ou `x = 14 304 px` selon le checkpoint.
- Tous les ennemis, projectiles, portes et dangers temporaires sont reinitialises.
- Le retour vers la gauche reste possible avant la fermeture de l'arene.
- Un Game Over recommence le niveau et oublie le checkpoint.

## Criteres de validation

- l'enchainement Dash, saut et Double saut est montre sans ennemi actif ;
- Serpent + Serpent apparait avant les groupes de trois ;
- chaque paire avancee respecte `1 280` ou `1 440 px` selon sa fiche ;
- les groupes de trois utilisent `1 600 px` et trois positions separees ;
- aucune combinaison interdite, Chauve-souris ou Zombie n'apparait ;
- les fosses ne suppriment jamais l'unique esquive ou reception ;
- le checkpoint, le feu, le boss et le coffre restent conformes au gabarit ;
- la duree visee reste `20 a 25 min`.

## Sources

- [Desert oublie](../../Concept-Game/03-Univers/Desert-Oublie.md)
- [Gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Golem du Desert](../Boss/Golem-Desert.md)
- [Courbe de difficulte](../Equilibrage/Courbe-de-Difficulte.md)
