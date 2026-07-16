# Sauvegarde

> **Statut :** Valide

## Objectif

Le système de sauvegarde permet au joueur de reprendre son aventure sans perdre les niveaux terminés, les clés récupérées ni les capacités débloquées.

Il reste volontairement simple afin d'être facile à comprendre pour les enfants à partir de 7 ans.

## Sauvegarde automatique

La fin du niveau 0 declenche une premiere sauvegarde automatique. Elle enregistre la fin du tutoriel et debloque la Foret enchantee sans ajouter de cle.

La partie est sauvegardee automatiquement apres chaque victoire contre un golem, une fois la cle du niveau recuperee.

Un indicateur visuel doit informer le joueur lorsque la sauvegarde est en cours ou vient d'être terminée.

Apres la recuperation de la sixieme cle, la sauvegarde place le point de reprise devant la porte du donjon, avant le combat contre Tata Lisa.

Une sauvegarde finale est effectuee apres la liberation d'Aliyah et avant les credits. Elle marque l'aventure comme terminee.

## Données conservées

La sauvegarde conserve :

- la fin du niveau 0 et l'acces a la Foret enchantee ;
- le dernier niveau terminé ;
- les niveaux débloqués ;
- les clés récupérées ;
- le Dash, après la victoire contre le deuxième golem ;
- le Double saut, après la victoire contre le quatrième golem ;
- l'acces au combat final, apres la recuperation de la sixieme cle ;
- l'etat `Aventure terminee`, apres la liberation d'Aliyah ;
- la progression générale de l'aventure.

Les cœurs et les vies ne sont pas conservés entre deux niveaux, car ils sont automatiquement restaurés après chaque boss.

## Points de contrôle

Les pancartes de controle laissees par Remi et Amelie servent uniquement de points de reapparition temporaires dans le niveau principal en cours.

Elles ne creent pas de sauvegarde permanente.

Lorsqu'Imran perd une vie apres avoir active une pancarte de controle, il reapparait a cet endroit avec ses trois coeurs.

Les pancartes de tutoriel du niveau 0 ne sont pas des points de controle.

## Fermeture du jeu pendant un niveau

Si le joueur quitte pendant le niveau 0 avant d'atteindre sa sortie, il reprend le tutoriel depuis son debut.

Si le joueur quitte le jeu avant d'avoir vaincu le boss du niveau, sa progression à l'intérieur de ce niveau n'est pas conservée.

Lors du prochain lancement, il recommence le niveau depuis le début avec :

- trois cœurs ;
- trois vies ;
- les capacités déjà débloquées lors des niveaux précédents.

La sixieme cle constitue une exception : si elle a deja ete sauvegardee, `Continuer` replace Imran devant la porte du donjon avec trois coeurs et trois vies, juste avant le combat contre Tata Lisa.

## Game Over

Si Imran perd ses trois vies, un écran Game Over apparaît.

Le joueur recommence alors le niveau depuis le début. Les clés et les capacités obtenues dans les niveaux précédemment terminés restent sauvegardées.

## Emplacement de sauvegarde

Le jeu utilise un seul emplacement de sauvegarde.

Le menu principal propose :

- **Continuer**, pour reprendre depuis le dernier niveau débloqué ;
- **Nouvelle partie**, pour effacer la progression existante et recommencer au debut du niveau 0.

Lorsque la sauvegarde porte l'etat `Aventure terminee`, `Continuer` est remplace par `Revoir la fin`. Cette action rejoue la liberation d'Aliyah et les credits sans relancer le combat final.

Avant l'effacement d'une sauvegarde, le jeu demande une confirmation au joueur afin d'éviter toute suppression accidentelle.

## Résumé des règles

| Situation | Résultat |
|---|---|
| Niveau 0 termine | Sauvegarde automatique et acces a la Foret enchantee |
| Golem vaincu et cle recuperee | Sauvegarde automatique |
| Sixieme cle recuperee | Sauvegarde et reprise devant la porte du donjon |
| Tata Lisa vaincue et Aliyah liberee | Sauvegarde finale `Aventure terminee` |
| Pancarte de controle activee | Point de reapparition temporaire |
| Vie perdue | Retour à la pancarte activée avec trois cœurs |
| Trois vies perdues | Game Over et reprise au début du niveau |
| Jeu fermé pendant un niveau | Reprise au début de ce niveau |
| Nouvelle partie choisie | Confirmation puis effacement de la progression |
