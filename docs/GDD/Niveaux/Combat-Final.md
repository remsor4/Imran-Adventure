# Combat final devant le donjon

> **Statut :** Valide

## Objectif

Relier la sixieme cle au combat contre Tata Lisa, puis conduire directement a l'ouverture des six verrous et a la liberation d'Aliyah sans creer un niveau jouable dans le donjon.

## Condition d'acces

- La sequence est accessible uniquement lorsque les six cles ont ete sauvegardees.
- Elle est chargee apres la fin du niveau 6 ou par `Continuer` si le combat final reste incomplet.
- Imran commence avec `3 coeurs`, `3 vies`, les six cles et une vitesse nulle.
- Aucun checkpoint, feu de camp, coffre ou cle supplementaire n'apparait.

## Dimensions de la scene

- La scene mesure `2 048 px` de large dans la resolution de reference `1920 x 1080`.
- L'approche sure occupe `x = 0 a 768 px`.
- L'arene commence a la coordonnee globale `x = 768 px`.
- Sa largeur utile locale est de `1 280 px` et sa limite globale droite se trouve a `x = 2 048 px`.
- Le sol unique reste plat a `y = 896 px`.
- Les positions de Tata Lisa et de la porte restent exprimees dans le repere local de l'arene.

## Point de reprise et declenchement

- Imran apparait dans l'approche sure avec son centre global a `x = 640 px`.
- Il regarde vers la droite et recoit immediatement le controle.
- Il avance lui-meme jusqu'au declencheur global `x = 896 px`, correspondant a la position locale `x = 128 px`.
- Le declencheur bloque les commandes et place la camera dans le cadrage fixe de l'arene.
- Aucun danger ne peut toucher Imran avant le debut officiel du combat.
- La presentation de `5.00 s` commence alors integralement selon la fiche de Tata Lisa.

## Arene

- La zone utile locale s'etend de `x = 0 a 1 280 px`.
- Dans l'ecran fixe, elle apparait entre `x = 320 et 1 600 px`.
- Imran commence la presentation a la position locale `x = 128 px`.
- Tata Lisa termine son apparition a la position locale `x = 1 024 px`.
- La porte du donjon est centree a la position locale `x = 1 184 px`.
- Le sol ne contient aucune plateforme, pente, fosse ou obstacle.
- La barriere gauche et la protection magique de la porte ferment les deux limites pendant le combat.
- La camera reste fixe pendant la presentation, les deux phases, la transition et la defaite.

## Combat contre Tata Lisa

- Toutes les valeurs et attaques utilisent la fiche [Tata Lisa](../Boss/Tata-Lisa.md) comme source de verite.
- Tata Lisa commence avec `24 PV` et utilise exactement deux phases.
- La phase 1 couvre `24 a 13 PV` et utilise trois attaques.
- La transition commence a `12 PV` et dure `2.50 s`.
- La phase 2 couvre `12 a 0 PV` et ajoute le Rituel de la Pierre du Chaos.
- Les attaques restent dans leurs cycles fixes et une teleportation suit chaque attaque terminee.
- La tete reste la zone vulnerable normale pendant le combat actif.
- A `0 PV`, Tata Lisa devient etourdie sans limite de temps.
- Un Smash Tranchant touchant n'importe quelle partie visible termine alors le combat.

## Perte de vie et Game Over

- Perdre une vie annule tous les dangers et retire une vie.
- S'il reste une vie, Imran reapparait a la coordonnee globale `x = 640 px` avec `3 coeurs`.
- Tata Lisa revient a `24 PV`, en phase 1, et la presentation complete est rejouee.
- Un Game Over propose de recommencer la sequence devant le donjon avec `3 coeurs` et `3 vies`.
- Les six cles sauvegardees ne sont jamais perdues.
- Fermer le jeu avant la liberation d'Aliyah reprend aussi a `x = 640 px`.

## Defaite et porte du donjon

- Le Smash final lance la destruction de la Pierre du Chaos et la fuite de Tata Lisa.
- La barriere gauche et la protection de la porte disparaissent pendant cette sequence.
- Le controle revient lorsque la defaite est terminee et qu'aucun danger ne reste.
- Imran avance lui-meme jusqu'a la porte.
- L'interaction devient disponible a `64 px` ou moins de la position locale `x = 1 184 px`.
- Une seule pression sur `Interaction` utilise automatiquement les six cles.
- Les six verrous s'ouvrent successivement pendant la sequence de `6.00 s`.
- Le donjon ne devient jamais une zone jouable.
- Le fondu final conduit directement a la scene de liberation d'Aliyah definie a l'etape 13.

## Progression et sauvegarde finale

- La victoire contre Tata Lisa seule ne marque pas encore l'aventure comme terminee.
- L'ouverture complete des six verrous lance la sequence finale.
- La liberation d'Aliyah marque ensuite la sauvegarde comme `Aventure terminee`.
- Le menu principal remplace `Continuer` par `Revoir la fin`.
- Revoir la fin ne relance ni le Chateau ni le combat contre Tata Lisa.

## Direction visuelle et sonore

- L'antichambre utilise la pierre noire, le gris anthracite, le bordeaux, le violet sombre et de petites touches dorees.
- La porte, ses six verrous et la faible lumiere derriere elle restent visibles.
- Les effets de magie du Chaos conservent un contour plus clair que le decor.
- La musique finale utilise la maquette et la structure dynamique validees dans la fiche de Tata Lisa.
- Le violon reste l'instrument principal et la seconde phase augmente l'intensite sans masquer les signaux d'attaque.

## Criteres de validation

- la sequence charge uniquement avec les six cles sauvegardees ;
- Imran dispose d'une approche sure avant le declencheur ;
- toutes les positions locales de Tata Lisa restent compatibles avec l'arene de `1 280 px` ;
- aucun checkpoint, feu, coffre ou nouvelle cle n'apparait ;
- une perte de vie et un Game Over conservent les six cles ;
- la defaite exige le Smash final sur Tata Lisa etourdie ;
- une seule interaction ouvre automatiquement les six verrous ;
- le donjon ne devient jamais jouable ;
- la sequence conduit sans embranchement a la liberation d'Aliyah.

## Sources

- [Tata Lisa](../Boss/Tata-Lisa.md)
- [Progression](../Systemes/Progression.md)
- [Coffres et cles](../Systemes/Coffres-et-Cles.md)
- [Sauvegarde](../Systemes/Sauvegarde.md)
- [Game Over](../Systemes/Game-Over.md)
- [Camera](../Systemes/Camera.md)
