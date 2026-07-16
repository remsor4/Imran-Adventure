# Protection automatique du Bouclier

> **Statut :** Valide

## Objectif

Definir la protection passive du Bouclier de lumiere contre les projectiles ennemis venant de face.

## Absence de commande

- Le Bouclier ne possede aucune touche ni aucun bouton dedie.
- Il ne figure pas parmi les actions remappables.
- Le joueur utilise uniquement une direction pour orienter Imran face au projectile.
- La protection ne cree aucun etat d'action et ne force jamais Imran a s'arreter.

## Conditions de protection

Un impact est bloque automatiquement si :

1. la source est un projectile ennemi ;
2. le centre du projectile se trouve du cote gauche si Imran regarde a gauche, ou du cote droit s'il regarde a droite ;
3. Imran n'est pas en train de preparer ou charger le Smash Tranchant ;
4. Imran peut normalement recevoir des degats a cet instant.

La protection reste active pendant l'attente, le deplacement, le saut, la chute, le Double saut, le Dash et l'attaque normale. Elle est inactive uniquement pendant toute la preparation ou la charge du Smash Tranchant.

## Dimensions visuelles du Bouclier

- Le Bouclier de lumiere est affiche avec une largeur de `20 px` et une hauteur de `28 px` pendant le gameplay.
- Sa hauteur represente environ `40 %` a `45 %` de la hauteur visuelle d'Imran.
- Il reste place devant le torse, du cote vers lequel Imran regarde.
- Il est retourne horizontalement lorsque l'orientation d'Imran change.
- Ces proportions reprennent le bouclier visible dans la capture de reference de *Wonder Boy*.
- L'illustration source conserve sa haute definition ; les dimensions indiquees correspondent a son affichage dans le gameplay.
- La protection automatique depend de l'orientation d'Imran et non des limites exactes du visuel du Bouclier.

## Effet d'un impact bloque

- Aucun coeur n'est retire.
- Aucun etat `Degat` ne commence.
- Aucune invulnerabilite de degat ne commence.
- Le mouvement ou l'action en cours continue.
- Le projectile disparait immediatement au point d'impact.
- Le projectile n'est ni renvoye, ni transforme en attaque d'Imran.
- Une lumiere doree et un son court confirment la protection.

## Attaques non protegees

Le Bouclier ne protege pas contre :

- un projectile arrivant de dos ;
- un projectile frontal recu pendant la preparation ou la charge du Smash Tranchant ;
- un contact avec un ennemi ;
- une attaque de corps a corps ;
- un piege ou un danger du decor ;
- une chute hors du niveau ;

Ces sources suivent les regles normales de degats.

## Criteres de validation

La protection est valide si :

- aucune commande de blocage n'existe ;
- un projectile ennemi frontal ne retire aucun coeur, meme pendant un mouvement ;
- un projectile bloque disparait sans etre renvoye ;
- le meme projectile venant de dos inflige ses degats normaux ;
- le meme projectile frontal inflige ses degats normaux pendant la preparation ou la charge du Smash Tranchant ;
- la protection ne force pas l'arret du mouvement ou d'une action compatible ;
- le Bouclier reste lisible a `20 x 28 px` sans masquer le visage ou l'animation d'Imran ;
- un contact, une attaque de corps a corps ou un danger du decor reste dangereux ;
- le retour visuel et sonore permet de comprendre l'impact bloque.

## Sources

- [Bouclier de lumiere](../../Concept-Game/05-Gameplay/Bouclier-de-Lumiere.md)
- [Reactions aux degats](../Joueur/Reactions-aux-Degats.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Reference video du combat Wonder Boy](Reference-Video-Wonder-Boy-Combat.md)
