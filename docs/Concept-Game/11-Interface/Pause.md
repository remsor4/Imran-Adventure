# Menu Pause

> **Statut :** Valide

## Objectif

Suspendre l'action et donner acces aux fonctions utiles sans modifier automatiquement la progression.

## Presentation

- Le gameplay, les ennemis et le temps du niveau sont suspendus.
- Le HUD reste visible mais fige sous un fond assombri.
- Le titre `Pause` apparait clairement.
- Les boutons sont affiches dans une seule colonne.
- La musique diminue legerement sans redemarrer.
- La reprise restaure la musique au meme point.

## Ordre des actions

1. Reprendre ;
2. Options ;
3. Recommencer le niveau ;
4. Quitter vers le menu principal.

`Reprendre` recoit le focus initial a chaque ouverture normale.

Le menu ne contient aucune commande de sauvegarde manuelle. La progression permanente est enregistree uniquement par les declencheurs automatiques du jeu.

## Reprendre

- Ferme immediatement le menu.
- Replace le focus dans le jeu.
- Rend le controle apres une transition tres courte.
- Peut aussi etre active avec la commande Pause.

## Options

- Ouvre les memes reglages que le menu principal.
- Applique les changements sans quitter la partie.
- Le retour replace le focus sur `Options`.
- Le jeu reste suspendu pendant toute la navigation.

## Recommencer le niveau

Cette action ouvre une confirmation indiquant que la progression du niveau en cours et le point de controle temporaire seront perdus.

Apres validation :

- le niveau recommence depuis le debut ;
- Imran retrouve trois coeurs et trois vies ;
- les cles et capacites des niveaux deja termines sont conservees ;
- aucune nouvelle sauvegarde n'est creee ;
- le focus revient au jeu apres le chargement.

Le choix sans risque `Annuler` recoit le focus initial dans la confirmation.

## Quitter vers le menu principal

Cette action ouvre une confirmation indiquant que la progression interne au niveau ne sera pas conservee.

Apres validation :

- le niveau en cours est abandonne ;
- le dernier niveau debloque reste sauvegarde ;
- les options deja appliquees sont conservees ;
- le menu principal est affiche sans fermer le jeu.

## Sauvegarde en cours

Pendant une sauvegarde automatique :

- le menu Pause peut etre ouvert ;
- `Recommencer le niveau` et `Quitter vers le menu principal` sont temporairement indisponibles ;
- un texte court explique que la sauvegarde doit se terminer ;
- les actions redeviennent disponibles apres confirmation de la sauvegarde.

## Disponibilite

Le menu Pause est disponible pendant l'exploration et les combats. Il reste ferme pendant :

- un chargement ;
- une transition narrative non interactive ;
- le Game Over ;
- l'ecran de victoire.

## Navigation

- Le clavier, la manette et la souris peuvent ouvrir et parcourir le menu.
- La commande de retour agit comme `Reprendre` depuis la liste principale.
- Une fenetre de confirmation doit etre fermee avant de reprendre le jeu.
- Le focus revient sur le bouton qui a ouvert une confirmation annulee.

## Validation du menu

Le menu Pause est coherent si :

- l'action est totalement suspendue ;
- la reprise demande une seule action ;
- un redemarrage ne peut pas etre lance par erreur ;
- la perte de progression est expliquee avant de quitter ;
- une sauvegarde en cours reste protegee ;
- la musique et les sons reprennent sans decalage.
