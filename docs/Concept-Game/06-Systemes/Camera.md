# Camera

> **Statut :** Valide

## Objectif

La camera accompagne Imran sans devenir une difficulte supplementaire. Elle privilegie toujours la lisibilite des plateformes, des ennemis, des dangers et des attaques.

## Cadre general

- Vue laterale en 2D au format `16:9`.
- Resolution de reference `1920 x 1080`.
- Zoom constant pendant l'exploration.
- Aucune rotation.
- Respect permanent des limites du niveau.

## Suivi horizontal

- La camera suit Imran de maniere fluide.
- Vers la droite, Imran vise `45 %` de la largeur, soit `864 px`.
- Vers la gauche, Imran vise `55 %` de la largeur, soit `1056 px`.
- Le decalage maximal autour du centre est de `96 px`.
- Apres un demi-tour, le cadrage change progressivement en `0.60 s`.
- Cette duree modifie uniquement la camera et ne ralentit jamais Imran.

## Suivi vertical

- Le centre visuel d'Imran vise `80 %` de la hauteur, soit `864 px`.
- La zone de confort s'etend de `70 %` a `84 %`, soit de `756 px` a environ `907 px`.
- Le saut normal de `89 px` reste dans cette zone et ne deplace pas la camera.
- Une variation de hauteur plus importante declenche un suivi progressif.
- La camera montre le sol ou la prochaine plateforme importante pendant une chute.

## Lisibilite

Le cadrage doit permettre de voir :

- les bords des plateformes et les trous ;
- les ennemis au sol et les menaces aeriennes ;
- les projectiles venant de la direction de progression ;
- les zones utiles au Dash et au Double saut ;
- les pancartes, coffres, feux de camp et objets interactifs ;
- les limites des arenes et des zones dangereuses.

Aucun decor au premier plan ne doit cacher durablement Imran ou un danger important.

## Reapparition

- La camera est correctement placee avant que l'image jouable apparaisse.
- Apres une mort, elle se replace immediatement au debut du niveau ou au checkpoint.
- Aucun trajet entre le point de mort et le point de reapparition n'est montre.

## Boss

- Chaque arene tient entierement dans un cadrage fixe `16:9`.
- Une courte presentation peut deplacer la camera avant le combat.
- La camera se verrouille avant de rendre le controle.
- Aucun suivi, zoom ou recentrage ne se produit pendant le combat.
- Imran, le boss, ses attaques et les bords de l'arene restent visibles.
- Apres un golem, la camera cadre Imran et le coffre.
- Apres Tata Lisa, elle cadre Imran et la porte du donjon.

## Secousses

- Une attaque lourde de boss peut produire `6 px` pendant `0.12 s`.
- La defaite d'un boss peut produire `12 px` pendant `0.25 s`.
- Les attaques normales, les degats ordinaires et les ennemis communs ne secouent pas la camera.
- Les effets ne depassent jamais la valeur maximale active.
- Une option permettra de reduire les secousses.

## Regle de conception

La camera aide le joueur a comprendre l'espace, anticiper les dangers et profiter des animations. Elle ne doit jamais constituer une difficulte supplementaire.
