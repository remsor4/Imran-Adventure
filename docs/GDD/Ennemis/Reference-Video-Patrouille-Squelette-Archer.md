# Reference video - Patrouille et tir du Squelette archer

> **Statut :** Reference analysee

## Source

- Fichier : `C:/Users/REMS/Desktop/capture ia/unknown/unknown_2026.07.24-01.08.mp4`
- Resolution : `1920 x 1088`
- Frequence : environ `60 images par seconde`
- Duree : environ `11.62 s`
- Usage : reference de comportement pour le Squelette archer.

## Situation observee

- Le joueur reste principalement en hauteur, sur la droite de l'ecran.
- L'ennemi archer reste au sol dans une zone horizontale.
- L'ennemi parcourt cette zone dans les deux sens.
- Il fait demi-tour lorsqu'il atteint une limite de patrouille.
- Il ne poursuit pas directement le joueur.

## Tir observe

- L'Archer tire une seule fleche a la fois.
- La fleche suit une trajectoire droite et horizontale.
- La fleche part dans la direction regardee par l'Archer.
- L'Archer ne corrige pas la trajectoire de la fleche apres le tir.
- L'Archer ne vise ni vers le haut ni vers le bas.
- Il peut donc tirer sous Imran lorsque celui-ci se trouve en hauteur.
- L'Archer conserve son deplacement de patrouille pendant l'animation de tir.
- Il ne fait pas demi-tour instantanement uniquement pour tirer sur Imran.

## Methode retenue pour Imran Adventure

Le Squelette archer utilise la meme logique generale :

1. Il patrouille continuellement dans une zone horizontale predeterminee.
2. Il fait demi-tour uniquement a une limite de sa patrouille ou devant un obstacle infranchissable.
3. Il ne quitte jamais sa zone pour poursuivre Imran.
4. Lorsque les conditions de detection sont reunies et qu'il regarde dans la direction d'Imran, il peut tirer sans interrompre sa marche.
5. Sa fleche se deplace horizontalement dans sa direction actuelle.
6. Si Imran se trouve plus haut ou plus bas, la fleche conserve sa trajectoire horizontale.
7. Si l'Archer regarde dans la mauvaise direction, il poursuit sa patrouille sans se retourner immediatement pour tirer.

## Informations non deduites de la capture

La capture ne suffit pas a fixer avec precision :

- les dimensions du Squelette archer ;
- ses points de vie ;
- les dimensions de sa zone de detection ;
- sa vitesse de patrouille ;
- la duree exacte de preparation du tir ;
- la cadence entre deux tirs ;
- les dimensions et la vitesse de la fleche ;
- la portee maximale de la fleche ;
- le comportement exact si Imran passe derriere lui pendant un tir.

Ces valeurs doivent etre validees separement dans le GDD.

## Limite de la reference

Le personnage visible dans la capture n'est pas un Squelette. Seule sa logique de patrouille et de tir est reprise. L'apparence, les animations et les sons restent ceux du Squelette archer definis dans le Concept Game.
