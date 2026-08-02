# Niveau 6 - Chateau de Tata Lisa

> **Statut :** Valide

## Objectif

Verifier la maitrise complete des mouvements et des combinaisons finales autorisees sans introduire de nouvelle regle avant le dernier golem.

## Identite

- Le parcours traverse des salles de pierre noire, des galeries, des bannieres bordeaux et des traces de magie du Chaos.
- Le sol principal reste a `y = 896 px`.
- Les plateformes sont des dalles et balcons statiques en pierre anthracite.
- Les fosses donnent sur des profondeurs du Chateau et restent clairement delimitees.
- Les piliers et tentures restent dans le decor et ne cachent aucun ennemi ou projectile.
- Les effets violets du decor sont moins lumineux que les avertissements de gameplay.

## Dimensions et structure

- Le niveau applique le [gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md).
- Sa largeur totale est de `29 664 px`.
- Imran apparait a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Le checkpoint est centre a `x = 14 304 px`.
- Le feu de camp est centre a `x = 27 360 px`.
- L'arene du Golem du Chateau commence a `x = 27 744 px`.

## Rappel final des mouvements

- L'entree sure utilise une porte de pierre ouverte pendant `0.70 s` par une dalle situee `192 px` avant elle.
- Le Dash au sol permet de la franchir sans danger.
- Une plateforme a `128 px` de hauteur suit une reception stable de `256 px`.
- Le Double saut permet d'atteindre cette plateforme.
- Aucun ennemi ne peut s'activer avant une seconde reception de `384 px`.
- Un mur de pierre coupe les lignes de vue jusqu'a cette seconde reception.
- Ce rappel ne cree aucune nouvelle mecanique et permet un nombre illimite d'essais.

## Parcours detaille

| Seq. | Intervalle | Terrain et obstacle | Ennemis | Largeur utile | Fonction |
|---:|---:|---|---|---:|---|
| 1 | `1 632 a 3 936` | Grande salle de `480 px` de haut | Chauve-souris seule | `1 280 x 480 px` | Reprendre la lecture aerienne |
| 2 | `3 936 a 6 240` | Galerie plate | Zombie epeiste seul | `1 280 px` | Rappeler la lame et les `3 PV` |
| 3 | `6 624 a 8 928` | Archer a droite, voute ouverte | Chauve-souris + Zombie archer | `1 440 x 480 px` | Plongee et fleche |
| 4 | `8 928 a 11 232` | Sol continu | Zombie epeiste + Zombie archer | `1 280 px` | Pression terrestre resistante |
| 5 | `11 616 a 13 920` | Grande galerie de `1 440 px` | Zombie archer + Serpent | `1 440 px` | Tir et projection rapide |
| 6 | `14 688 a 16 992` | Voute sans colonne centrale | Chauve-souris + Zombie archer | `1 440 x 480 px` | Reprise apres checkpoint |
| 7 | `16 992 a 19 296` | Sol plat et deux sorties | Zombie epeiste + Zombie archer | `1 280 px` | Confirmer la paire de Zombies |
| 8 | `19 680 a 21 984` | Grande salle ouverte | Chauve-souris + Zombie epeiste + Zombie archer | `1 600 x 480 px` | Premier groupe final |
| 9 | `21 984 a 24 288` | Voute et sol continu | Chauve-souris + Zombie archer + Serpent | `1 600 x 480 px` | Groupe tres avance |
| 10 | `24 672 a 26 976` | Cour interieure plate | Zombie epeiste + Serpent + Zombie archer | `1 600 px` | Derniere rencontre ordinaire |

## Placement et limites des rencontres

- Les positions initiales utilisent le gabarit commun.
- Chauve-souris + Zombie archer utilise une separation horizontale de `480 px`.
- La paire de Zombies utilise `320 px`, avec l'Archer a droite.
- Zombie archer + Serpent utilise `480 px` et `1 440 px` de sol continu.
- Les groupes de trois utilisent `C - 480 px`, `C` et `C + 480 px`.
- Le groupe de la sequence 8 utilise l'ordre `Chauve-souris a gauche, Zombie epeiste au centre, Zombie archer a droite`.
- Le groupe de la sequence 9 place le Zombie archer en soutien a droite du Serpent.
- La sequence 10 utilise l'ordre gauche vers droite `Zombie epeiste, Serpent, Zombie archer`.
- Les salles avec Chauve-souris conservent `480 px` de hauteur libre.
- La combinaison interdite Chauve-souris + Zombie epeiste + Serpent n'apparait jamais.
- Aucun Slime ou Squelette n'apparait.

## Plateformes et fosses

- Les rappels du Dash et du Double saut sont termines avant la sequence 1.
- Une fosse normale mesure au maximum `128 px` et une fosse de Double saut `192 px`.
- Les paires et groupes de trois utilisent un sol continu sans fosse dans leur zone utile.
- Les balcons decoratifs ne creent aucune seconde ligne de tir cachee.
- Une chute hors du Chateau retire une vie et provoque la reprise normale.
- Aucun obstacle ne demande une precision au pixel pres.

## Checkpoint

- La pancarte est centree a `x = 14 304 px` dans une salle plate et vide.
- Deux portes ouvertes forment des cadres solides qui arretent les projectiles voisins.
- La zone de `768 px` ne contient ni fosse, plateforme, ennemi ou magie dangereuse.
- L'activation automatique reste temporaire et ne restaure aucune ressource.

## Fin du parcours et feu de camp

- La derniere cour conduit a une salle calme precedant le dernier golem.
- Le feu de camp est centre a `x = 27 360 px`.
- L'interaction volontaire restaure uniquement les coeurs.
- La grande statue de chevalier du Golem du Chateau est visible au-dela de l'entree.
- Franchir `x = 27 744 px` ferme l'arene et lance la presentation.

## Golem du Chateau

- Le combat utilise integralement la fiche [Golem du Chateau](../Boss/Golem-Chateau.md).
- Son cycle utilise le Croissant violet, la Double entaille au sol et le Sceau de la lame.
- Il constitue la derniere verification avant Tata Lisa.
- L'arene reste plate, fixe et sans plateforme, fosse, pente ou obstacle.

## Coffre, sixieme cle et transition

- Le coffre utilise du bois noir, de la pierre anthracite, du metal sombre, de l'obsidienne et une serrure violette.
- Son centre global se trouve a `x = 29 568 px`.
- La sixieme cle est ajoutee apres l'ouverture volontaire.
- La sauvegarde conserve les six cles et fixe le point de reprise devant le donjon.
- La transition conduit a la scene du combat final, pas a un nouveau niveau d'exploration.
- Imran commence cette sequence avec `3 coeurs` et `3 vies`.

## Reprise et retour en arriere

- Une vie perdue replace Imran a `x = 864 px` ou `x = 14 304 px` selon le checkpoint.
- Tous les ennemis, projectiles, portes et dangers temporaires reviennent a leur etat initial.
- Le retour vers la gauche reste possible avant l'arene.
- Un Game Over recommence le Chateau et oublie son checkpoint.
- Apres la sauvegarde de la sixieme cle, `Continuer` charge le point devant le donjon.

## Criteres de validation

- aucune nouvelle famille ou regle de comportement n'est introduite ;
- les trois groupes finaux autorises apparaissent dans l'ordre defini ;
- la combinaison interdite reste absente ;
- les Chauves-souris conservent `480 px` de hauteur libre ;
- tous les groupes de trois disposent de `1 600 px` et de plusieurs sorties ;
- aucun Slime ou Squelette n'apparait ;
- le dernier golem, le coffre et la sixieme cle conduisent correctement au combat final ;
- le niveau vise `20 a 25 min` et reste juste avec `1 coeur` restant.

## Sources

- [Chateau de Tata Lisa](../../Concept-Game/03-Univers/Chateau-de-Tata-Lisa.md)
- [Gabarit des niveaux principaux](Gabarit-Niveaux-Principaux.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Zombies](../Ennemis/Zombies.md)
- [Chauves-souris](../Ennemis/Chauves-Souris.md)
- [Serpents](../Ennemis/Serpents.md)
- [Golem du Chateau](../Boss/Golem-Chateau.md)
