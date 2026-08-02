# Niveau 2 - Grotte mysterieuse

> **Statut :** Valide

## Objectif

Introduire le Squelette epeiste dans un espace lisible, puis combiner les deux variantes de Squelettes avec les Chauves-souris sans supprimer les zones d'esquive.

## Identite

- Le parcours traverse des galeries de roche sombre, des minerais et des cristaux violets.
- Le sol principal reste a `y = 896 px`.
- Les plateformes sont des corniches de pierre statiques alignees sur la grille de `64 px`.
- Les cristaux decoratifs ne possedent aucune collision dangereuse.
- Les salles de Chauves-souris offrent une hauteur libre minimale de `480 px`.
- Les plafonds bas sont reserves aux respirations et ne couvrent jamais une plongee.

## Dimensions et structure

- Le niveau applique le [gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md).
- Sa largeur totale est de `29 664 px`.
- Imran apparait a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Le checkpoint est centre a `x = 14 304 px`.
- Le feu de camp est centre a `x = 27 360 px`.
- L'arene du Golem de la Grotte commence a `x = 27 744 px`.

## Entree sure

- L'entree montre la transition de la Foret vers une galerie minerale stable.
- Une corniche de `128 px` de haut est visible dans le premier ecran sans ennemi actif.
- Imran peut pratiquer le Double saut avant la premiere rencontre.
- La reception mesure `384 px` et reste hors de toute detection.
- Une paroi rocheuse coupe les lignes de vue ennemies jusqu'a la fin de cette reception.
- Aucun danger ne commence avant `x = 1 632 px`.

## Parcours detaille

| Seq. | Intervalle | Terrain et obstacle | Ennemis | Largeur utile | Fonction |
|---:|---:|---|---|---:|---|
| 1 | `1 632 a 3 936` | Salle ouverte de `480 px` | Chauve-souris seule | `1 280 x 480 px` | Rappeler la plongee |
| 2 | `3 936 a 6 240` | Galerie plate et ligne de vue libre | Squelette archer seul | `1 280 px` | Rappeler le tir frontal |
| 3 | `6 624 a 8 928` | Couloir large, sol continu | Squelette epeiste seul | `1 280 px` | Introduire la lame permanente |
| 4 | `8 928 a 11 232` | Corniche a `128 px`, reception sure avant activation | Chauve-souris seule | `1 280 x 480 px` | Utiliser le Double saut pres d'un ennemi connu |
| 5 | `11 616 a 13 920` | Grande salle sans pilier central | Chauve-souris + Chauve-souris | `1 280 x 480 px` | Lire deux plongees |
| 6 | `14 688 a 16 992` | Porte de cristal a franchir au Dash, puis `256 px` surs | Archer seul | `1 280 px` | Associer Dash et menace distante |
| 7 | `16 992 a 19 296` | Sol plat et large | Epeiste seul | `1 280 px` | Confirmer le franchissement de la lame |
| 8 | `19 680 a 21 984` | Archer a droite derriere l'Epeiste | Epeiste + Archer | `1 280 px` | Combiner corps a corps et fleche |
| 9 | `21 984 a 24 288` | Salle ouverte avec reception visible | Chauve-souris + Epeiste | `1 280 x 480 px` | Proteger la zone d'atterrissage |
| 10 | `24 672 a 26 976` | Grande voute sans plafond bas | Chauve-souris + Chauve-souris | `1 280 x 480 px` | Derniere lecture aerienne |

## Porte de cristal de la sequence 6

- Une dalle au sol ouvre la porte pendant `0.70 s`.
- La distance entre la dalle et le passage mesure `192 px`.
- La porte ne blesse pas Imran et se rouvre apres un echec.
- L'Archer ne peut detecter Imran qu'apres la reception sure de `256 px` situee a droite.
- Une paroi bloque toute fleche vers la dalle et le checkpoint.
- Cette meme paroi coupe la ligne de vue avant la reception.
- La porte reste ouverte pendant un retour depuis la droite.

## Placement et limites des rencontres

- Les positions initiales utilisent le gabarit commun.
- Les deux Chauves-souris sont separees de `480 px` horizontalement.
- Dans Epeiste + Archer, les centres sont separes de `320 px` et l'Archer reste a droite.
- Dans Chauve-souris + Epeiste, les centres horizontaux sont separes de `320 px`.
- Chaque salle aerienne conserve `480 px` de hauteur libre et aucune colonne ne coupe une trajectoire.
- Les Squelettes utilisent leur patrouille complete de `800 px` uniquement dans leur rencontre.
- Aucun Slime, Serpent ou Zombie n'apparait.
- Aucun groupe de trois n'est utilise.

## Checkpoint

- La pancarte de controle est centree a `x = 14 304 px` dans une galerie minerale plate.
- Deux parois de roche ferment les lignes de tir voisines sans bloquer le passage d'Imran.
- L'activation automatique conserve le fonctionnement commun et ne restaure aucune ressource.

## Fin du parcours et feu de camp

- La derniere voute conduit a une zone calme sans stalactite active.
- Le feu de camp est centre a `x = 27 360 px` sur un sol rocheux plat.
- L'interaction restaure uniquement les coeurs.
- La paroi integree au Golem de la Grotte devient visible avant l'entree de l'arene.
- Franchir `x = 27 744 px` lance la fermeture et la presentation.

## Golem de la Grotte

- Le combat utilise integralement la fiche [Golem de la Grotte](../Boss/Golem-Grotte.md).
- Son cycle utilise l'Eclat de cristal frontal, les Piliers de cristal et la Chute de stalactites.
- L'arene reste plate et ne contient aucun danger independant du golem.
- Les stalactites decoratives du niveau ne partagent jamais les zones dangereuses du boss.

## Coffre, cle et transition

- Le coffre utilise de la roche, du minerai et des formes de cristaux.
- Son centre global se trouve a `x = 29 568 px`.
- La deuxieme cle est ajoutee apres l'ouverture volontaire du coffre.
- La sauvegarde debloque le Lac gele avant la transition.
- Imran commence le niveau 3 avec `3 coeurs` et `3 vies`.

## Reprise et retour en arriere

- Avant activation, une vie perdue replace Imran a `x = 864 px`.
- Apres activation, elle le replace a `x = 14 304 px`.
- Toutes les Chauves-souris, tous les Squelettes, projectiles et portes reviennent a leur etat initial.
- Le retour vers les galeries precedentes reste possible avant l'arene.
- Un Game Over oublie le checkpoint et recommence le niveau.

## Criteres de validation

- l'Epeiste apparait seul avant sa premiere paire ;
- les Chauves-souris disposent toujours de `480 px` de hauteur libre ;
- Chauve-souris + Chauve-souris, Epeiste + Archer et Chauve-souris + Epeiste respectent leurs distances ;
- le Dash et le Double saut sont utilises pres d'un ennemi seulement apres une demonstration sure ;
- aucune reception ne conduit sur la lame de l'Epeiste ;
- aucun Slime, Serpent, Zombie ou groupe de trois n'apparait ;
- le checkpoint, le feu et l'arene respectent le gabarit ;
- la duree visee reste `20 a 25 min`.

## Sources

- [Grotte mysterieuse](../../Concept-Game/03-Univers/Grotte-Mysterieuse.md)
- [Gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Chauves-souris](../Ennemis/Chauves-Souris.md)
- [Squelettes](../Ennemis/Squelettes.md)
- [Golem de la Grotte](../Boss/Golem-Grotte.md)
