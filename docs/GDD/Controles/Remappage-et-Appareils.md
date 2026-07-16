# Remappage et appareils

> **Statut :** Valide

## Objectif

Permettre au joueur de consulter et modifier les commandes sans rendre une action essentielle inutilisable.

## Groupes de commandes

Les commandes sont separees en trois groupes :

1. gameplay au clavier ;
2. gameplay a la manette ;
3. navigation dans les menus.

Les modifications du clavier et de la manette sont enregistrees separement.

## Actions essentielles

Les actions suivantes doivent toujours posseder au moins une commande valide sur l'appareil concerne :

- gauche ;
- droite ;
- saut ;
- Dash ;
- attaque ;
- blocage ;
- interaction ;
- Pause ;
- navigation dans les menus ;
- confirmation ;
- retour.

Le Dash reste assignable avant son deblocage. Le Double saut partage la commande du saut et le Smash Tranchant partage celle de l'attaque.

## Detection des conflits

Dans un meme contexte, une commande ne peut pas etre attribuee a deux actions essentielles differentes.

Lorsqu'un conflit est detecte :

1. le jeu nomme les deux actions concernees ;
2. la nouvelle commande n'est pas appliquee automatiquement ;
3. le joueur peut annuler ou choisir une autre commande ;
4. l'ancienne configuration reste active tant que le conflit n'est pas resolu.

Une meme commande peut etre reutilisee dans deux contextes incompatibles, par exemple `Echap` pour Pause en gameplay et Retour dans un menu.

## Procedure de remappage

1. Le joueur selectionne une action.
2. Le jeu attend une nouvelle entree du meme type d'appareil.
3. `Echap` ou le bouton Retour annule la saisie.
4. Le jeu controle les conflits.
5. La commande est appliquee uniquement si elle reste valide.
6. La nouvelle icone ou le nouveau nom apparait immediatement.

Une entree analogique accidentelle ou trop faible ne doit pas etre acceptee comme commande.

## Valeurs par defaut

Le bouton `Valeurs par defaut` :

- agit separement sur le clavier ou la manette ;
- affiche une confirmation ;
- restaure toutes les commandes du groupe ;
- ne modifie pas les options audio, video ou d'accessibilite.

## Changement d'appareil

- Le clavier, la souris et la manette peuvent etre utilises sans redemarrer le jeu.
- Le dernier appareil ayant produit une entree valide determine les icones affichees.
- Un mouvement minime du stick ne change pas les icones.
- La souris ne remplace jamais les commandes essentielles du gameplay.
- La deconnexion de la manette suspend le gameplay avant d'afficher le message de reconnexion.

## Persistance

Les commandes personnalisees sont conservees dans la configuration locale des Options.

- Elles sont independantes de la sauvegarde de progression.
- Une Nouvelle partie ne les efface pas.
- Une configuration invalide restaure les commandes par defaut de l'appareil concerne.

## Criteres de validation

Le remappage est valide si :

- aucune action essentielle ne peut rester sans commande ;
- aucun conflit dans un meme contexte ne peut etre confirme ;
- une annulation conserve la configuration precedente ;
- les valeurs par defaut peuvent etre restaurees ;
- les commandes persistent apres la fermeture du jeu ;
- le changement d'appareil met a jour les icones sans interrompre la partie.

## Sources

- [Options](../../Concept-Game/11-Interface/Options.md)
- [Menu principal](../../Concept-Game/11-Interface/Menu-Principal.md)
- [Pause](../../Concept-Game/11-Interface/Pause.md)
