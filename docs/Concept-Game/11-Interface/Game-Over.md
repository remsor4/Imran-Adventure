# Ecran Game Over

> **Statut :** Valide

## Objectif

Informer le joueur apres la perte des trois vies et lui permettre de recommencer sans presentation punitive.

## Declenchement

Le Game Over apparait lorsque Imran perd sa derniere vie.

- L'action s'arrete avant l'ouverture de l'ecran.
- Le dernier impact est confirme visuellement et par le son.
- Le HUD disparait apres la mise a jour du compteur de vies.
- Aucune sauvegarde n'est declenchee.

## Presentation

- Le message principal reste court et encourageant.
- Une illustration ou une pose d'Imran montre sa determination plutot qu'une defaite violente.
- Le motif musical d'Imran est joue sous une forme lente et breve.
- Le fond rappelle le niveau perdu sans rendre le texte difficile a lire.
- Aucun compte a rebours ne force une decision.

## Actions

1. Recommencer le niveau ;
2. Retour au menu principal.

`Recommencer le niveau` recoit le focus initial.

## Recommencer le niveau

Le redemarrage est lance apres une seule validation, car le niveau est deja considere comme perdu.

- Imran revient au debut du niveau.
- Il retrouve trois coeurs et trois vies.
- La pancarte activee pendant la tentative est oubliee.
- Les cles et capacites des niveaux termines restent disponibles.
- La progression non sauvegardee du niveau est perdue.
- La musique du niveau recommence depuis son introduction.

## Retour au menu principal

- Revient au menu sans demander une seconde confirmation.
- Conserve la derniere sauvegarde valide.
- Ne cree pas de nouvelle sauvegarde.
- Replace le focus sur `Continuer` si une sauvegarde existe.

## Accessibilite

- Le message principal est lu facilement sans animation rapide.
- Les deux actions utilisent du texte et des icones distinctes.
- La selection ne repose pas uniquement sur la couleur.
- La musique peut etre coupee sans perdre l'information.
- L'ecran reste affiche jusqu'a une action du joueur.

## Validation du Game Over

L'ecran est coherent si :

- la cause de l'arret est comprise ;
- le redemarrage constitue l'action principale ;
- la progression conservee est claire ;
- aucune pression automatique ne relance le niveau ;
- le ton reste encourageant et adapte aux enfants.
