# Sauvegarde

> **Statut :** Validé

## Objectif

Le système de sauvegarde permet au joueur de reprendre son aventure sans perdre les niveaux terminés, les clés récupérées ni les capacités débloquées.

Il reste volontairement simple afin d'être facile à comprendre pour les enfants à partir de 7 ans.

## Sauvegarde automatique

La partie est sauvegardée automatiquement après chaque victoire contre un boss, une fois la clé du niveau récupérée.

Un indicateur visuel doit informer le joueur lorsque la sauvegarde est en cours ou vient d'être terminée.

## Données conservées

La sauvegarde conserve :

- le dernier niveau terminé ;
- les niveaux débloqués ;
- les clés récupérées ;
- le Dash, après la victoire contre le deuxième golem ;
- le Double saut, après la victoire contre le quatrième golem ;
- la progression générale de l'aventure.

Les cœurs et les vies ne sont pas conservés entre deux niveaux, car ils sont automatiquement restaurés après chaque boss.

## Points de contrôle

Les pancartes laissées par Rémi et Amélie servent uniquement de points de réapparition temporaires dans le niveau en cours.

Elles ne créent pas de sauvegarde permanente.

Lorsqu'Imran perd une vie après avoir activé une pancarte, il réapparaît à cet endroit avec ses trois cœurs.

## Fermeture du jeu pendant un niveau

Si le joueur quitte le jeu avant d'avoir vaincu le boss du niveau, sa progression à l'intérieur de ce niveau n'est pas conservée.

Lors du prochain lancement, il recommence le niveau depuis le début avec :

- trois cœurs ;
- trois vies ;
- les capacités déjà débloquées lors des niveaux précédents.

## Game Over

Si Imran perd ses trois vies, un écran Game Over apparaît.

Le joueur recommence alors le niveau depuis le début. Les clés et les capacités obtenues dans les niveaux précédemment terminés restent sauvegardées.

## Emplacement de sauvegarde

Le jeu utilise un seul emplacement de sauvegarde.

Le menu principal propose :

- **Continuer**, pour reprendre depuis le dernier niveau débloqué ;
- **Nouvelle partie**, pour effacer la progression existante et recommencer l'aventure depuis le début.

Avant l'effacement d'une sauvegarde, le jeu demande une confirmation au joueur afin d'éviter toute suppression accidentelle.

## Résumé des règles

| Situation | Résultat |
|---|---|
| Boss vaincu et clé récupérée | Sauvegarde automatique |
| Pancarte activée | Point de réapparition temporaire |
| Vie perdue | Retour à la pancarte activée avec trois cœurs |
| Trois vies perdues | Game Over et reprise au début du niveau |
| Jeu fermé pendant un niveau | Reprise au début de ce niveau |
| Nouvelle partie choisie | Confirmation puis effacement de la progression |
