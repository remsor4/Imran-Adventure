# HUD

> **Statut :** Valide

## Objectif

Afficher uniquement les informations utiles pendant l'exploration et les combats, sans masquer Imran, les plateformes ou les dangers.

## Organisation

| Zone | Contenu | Visibilite |
|---|---|---|
| Coin superieur gauche | Coeurs et vies | Toujours pendant le gameplay |
| Coin superieur droit | Cles et capacites de deplacement | Pendant l'exploration et les combats |
| Haut au centre | Barre de vie du boss | Uniquement pendant un combat de boss |
| Bas au centre | Message contextuel | Uniquement pres d'une interaction |
| Coin inferieur droit | Sauvegarde automatique | Pendant la sauvegarde et sa confirmation |

Le centre de l'ecran reste libre en dehors de la barre de vie du boss et des messages temporaires.

## Coeurs

Imran possede trois coeurs.

- Les trois emplacements restent visibles.
- Un coeur plein et un coeur perdu utilisent une forme differente en plus de leur couleur.
- La perte d'un coeur produit une courte animation et un son distinct.
- La recuperation restaure visuellement les coeurs de gauche a droite.
- Les coeurs clignotent une seule fois apres un degat, sans effet rapide ou prolonge.

## Vies

Les vies sont affichees avec un portrait simplifie d'Imran et un compteur.

- Le compteur commence a trois.
- La perte d'une vie est confirmee avant la reapparition.
- Lorsqu'une vie est perdue, les trois coeurs sont restaures.
- Le compteur ne descend jamais sous zero.
- La perte de la derniere vie ouvre l'ecran Game Over.

## Cles

Le compteur de cles utilise une icone de cle doree suivie du nombre obtenu sur six.

- Le compteur reste discret pendant un niveau.
- Une cle ajoutee produit un reflet, un son et une mise a jour claire du nombre.
- Le compteur ne change qu'apres l'ouverture du coffre et la recuperation de la cle.
- La sauvegarde automatique commence apres cette mise a jour.

## Capacites

Le Dash et le Double saut sont affiches des le debut du niveau 0.

- La pancarte du Dash presente son icone, son nom et sa commande.
- La pancarte du Double saut presente son icone, son nom et sa commande.
- Les icones servent de rappel et ne doivent pas suggerer une jauge ou un temps de recharge inexistant.

## Boss

Chaque combat de boss affiche une barre de vie horizontale centree en haut de l'ecran, sur le principe de la reference fournie pour *Wonder Boy: The Dragon's Trap*.

- La barre apparait lorsque le boss termine son reveil et que le combat commence.
- Elle est utilisee pour les six golems et pour Tata Lisa.
- Le remplissage principal est rouge, entoure d'un contour sombre et lisible.
- La valeur de vie actuelle est affichee au centre de la barre.
- La reduction de la longueur et la valeur numerique transmettent la meme information afin de ne pas dependre uniquement de la couleur.
- La barre reagit immediatement lorsque le boss subit un degat.
- Elle atteint clairement zero avant l'animation de defaite.
- Elle disparait apres la fin du combat.
- Elle ne doit pas masquer le boss, une plateforme ou une attaque aerienne.

Le nombre maximal de points de vie, les degats et les dimensions exactes de la barre seront definis dans le GDD.

## Messages contextuels

Les messages utilisent un verbe court et l'icone de la touche actuelle.

Exemples d'actions :

- lire une pancarte de tutoriel ;
- ouvrir un coffre ;
- activer une pancarte ;
- confirmer une action ;
- utiliser une capacite pour la premiere fois.

Le message apparait uniquement lorsque l'action est possible. Il disparait si Imran s'eloigne, si un combat commence ou si l'action est terminee.

Dans le niveau 0, le message d'une pancarte de commande affiche automatiquement l'entree adaptee au dernier appareil utilise et au remappage actuel. La pancarte du Bouclier affiche une direction et precise que la protection automatique fonctionne meme en mouvement.

## Sauvegarde automatique

- Une icone de livre et le texte `Sauvegarde...` apparaissent dans le coin inferieur droit.
- Une confirmation courte remplace le message lorsque l'ecriture est terminee.
- L'indicateur ne bloque pas le gameplay.
- Les actions de fermeture restent indisponibles tant que la sauvegarde n'est pas terminee.

## Retours temporaires

Le HUD confirme clairement :

- la perte ou la recuperation d'un coeur ;
- la perte d'une vie ;
- l'activation d'une pancarte ;
- la recuperation d'une cle ;
- l'apprentissage d'une capacite sur une pancarte de tutoriel ;
- la sauvegarde ;
- la victoire contre un boss.

Ces retours restent courts et ne s'empilent pas au centre de l'ecran. Une information plus importante remplace une information secondaire.

## Visibilite

- Le HUD est masque pendant les cinematiques et l'ecran de victoire.
- Il reste visible pendant les combats de boss.
- Il est fige sous le menu Pause.
- Il reapparait avant que le joueur retrouve le controle.
- Son contraste reste suffisant dans le niveau 0 et les six environnements principaux.

## Validation du HUD

Le HUD est coherent si :

- les coeurs, vies et cles sont compris sans explication ;
- les informations restent lisibles sur le plus petit ecran cible ;
- aucun element ne cache un danger ;
- les changements sont visibles et audibles ;
- les icones restent identifiables sans couleur ;
- aucune information inutile ne reste affichee.
