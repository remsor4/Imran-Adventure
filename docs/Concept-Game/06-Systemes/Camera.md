# Caméra

> **Statut :** À valider

## Objectif du document

Décrire le comportement visuel attendu de la caméra dans ce jeu de plateforme 2D.

La caméra doit accompagner le joueur sans attirer inutilement son attention. Elle doit toujours privilégier la lisibilité des plateformes, des ennemis, des pièges et des attaques.

## Principes généraux

La caméra adopte une vue latérale en 2D.

Elle doit :

- suivre Imran de manière fluide ;
- éviter les mouvements brusques ;
- conserver Imran et les dangers proches dans une zone clairement visible ;
- anticiper légèrement la direction dans laquelle le joueur avance ;
- rester stable pendant les petits sauts et les déplacements courts ;
- respecter les limites de chaque niveau ;
- ne jamais révéler des zones situées en dehors du décor jouable.

Le niveau de zoom doit rester cohérent pendant l'exploration afin que le joueur puisse facilement évaluer les distances.

## Suivi du joueur

Pendant les déplacements normaux, la caméra suit Imran horizontalement avec un léger décalage vers l'avant.

Ce décalage permet au joueur de voir :

- les plateformes qui arrivent ;
- les ennemis placés devant lui ;
- les pièges du chemin principal ;
- les projectiles provenant de la direction de progression.

Le suivi vertical doit être plus stable que le suivi horizontal. La caméra ne doit pas monter et descendre à chaque petit saut.

Lors des passages comportant une forte variation de hauteur, elle peut se repositionner progressivement afin de conserver Imran et la prochaine plateforme importante à l'écran.

Après une réapparition au début du niveau ou à une pancarte de contrôle, la caméra se replace immédiatement autour d'Imran avant de reprendre son suivi normal.

## Lisibilité des obstacles

La caméra doit offrir suffisamment d'espace devant Imran pour que le joueur puisse identifier les obstacles avant de les atteindre.

Elle doit notamment permettre de voir clairement :

- les bords des plateformes ;
- les trous ;
- les pièges ;
- les ennemis au sol ;
- les chauves-souris et autres menaces aériennes ;
- les flèches tirées par les archers ;
- les éléments nécessaires au Dash ou au Double saut.

Aucun élément de décor situé au premier plan ne doit cacher durablement Imran ou un danger important.

Dans les passages plus étroits ou verticaux, le cadrage peut être adapté, mais les changements doivent rester progressifs et faciles à comprendre.

## Arènes de boss

Lorsqu'Imran entre dans une arène de boss, la caméra se verrouille dans les limites de l'arène.

Le cadrage doit permettre de voir :

- Imran ;
- le boss ;
- les attaques importantes ;
- les limites de la zone de combat ;
- les éléments dangereux du décor.

Au début du combat, une courte mise en scène peut présenter le golem ou Tata Lisa. Cette présentation doit rester brève afin de ne pas interrompre inutilement le rythme du jeu.

Pendant le combat, la caméra ne doit pas effectuer de zoom ou de déplacement soudain pouvant gêner le joueur.

Après la victoire, elle se recentre sur Imran et le coffre du niveau.

## Effets de caméra

Les effets de caméra doivent rester limités afin de préserver le confort des jeunes joueurs.

Un léger tremblement peut accompagner :

- une attaque lourde d'un boss ;
- la destruction d'un golem ;
- un impact important ;
- la défaite de Tata Lisa.

Ces effets doivent être courts, lisibles et ne jamais empêcher le joueur de voir une attaque ou un obstacle.

## Règle de conception

La caméra ne doit jamais devenir une difficulté supplémentaire.

Son rôle est d'aider le joueur à comprendre l'espace, à anticiper les dangers et à profiter des animations et des environnements.
