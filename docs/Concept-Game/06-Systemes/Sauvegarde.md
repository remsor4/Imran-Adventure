# Sauvegarde

> **Statut :** Valide

## Objectif

Le systeme de sauvegarde permet au joueur de reprendre son aventure sans perdre les niveaux termines ni les cles recuperees.

Il reste volontairement simple afin d'etre facile a comprendre pour les enfants a partir de 7 ans.

## Sauvegarde automatique

La sauvegarde est entierement automatique. Aucun bouton de sauvegarde manuelle n'apparait dans le menu Pause ou ailleurs dans le jeu.

La fin du niveau 0 declenche une premiere sauvegarde automatique. Elle enregistre la fin du tutoriel et debloque la Foret enchantee sans ajouter de cle.

La partie est sauvegardee automatiquement apres chaque victoire contre un golem, une fois la cle du niveau recuperee.

Un indicateur visuel doit informer le joueur lorsque la sauvegarde est en cours ou vient d'etre terminee.

Apres la recuperation de la sixieme cle, la sauvegarde place le point de reprise devant la porte du donjon, avant le combat contre Tata Lisa.

Une sauvegarde finale est effectuee apres la liberation d'Aliyah et avant les credits. Elle marque l'aventure comme terminee.

## Donnees conservees

La sauvegarde conserve :

- la fin du niveau 0 et l'acces a la Foret enchantee ;
- le dernier niveau termine ;
- les niveaux debloques ;
- les cles recuperees ;
- l'acces au combat final, apres la recuperation de la sixieme cle ;
- l'etat `Aventure terminee`, apres la liberation d'Aliyah ;
- la progression generale de l'aventure.

Les coeurs et les vies ne sont pas conserves entre deux niveaux, car ils sont automatiquement restaures apres la recuperation de chaque cle.

## Points de controle

Les pancartes de controle laissees par Remi et Amelie servent uniquement de points de reapparition temporaires dans le niveau principal en cours.

Elles ne creent pas de sauvegarde permanente.

Lorsqu'Imran perd une vie apres avoir active une pancarte de controle, il reapparait a cet endroit avec ses trois coeurs.

Les pancartes de tutoriel du niveau 0 ne sont pas des points de controle.

## Fermeture du jeu pendant un niveau

Si le joueur quitte pendant le niveau 0 avant d'atteindre sa sortie, il reprend le tutoriel depuis son debut.

Si le joueur quitte le jeu avant d'avoir recupere et sauvegarde la cle du niveau, sa progression a l'interieur de ce niveau n'est pas conservee, meme si le golem a deja ete vaincu.

Lors du prochain lancement, il recommence le niveau depuis le debut avec :

- trois coeurs ;
- trois vies ;
- le Dash et le Double saut, toujours disponibles des le debut de l'aventure.

La sixieme cle constitue une exception : si elle a deja ete sauvegardee, `Continuer` replace Imran devant la porte du donjon avec trois coeurs et trois vies, juste avant le combat contre Tata Lisa.

## Game Over

Si Imran perd ses trois vies, un ecran Game Over apparait.

Le joueur recommence alors le niveau depuis le debut. Les cles obtenues dans les niveaux precedemment termines restent sauvegardees. Le Dash et le Double saut restent disponibles car ils ne dependent pas de la sauvegarde.

## Emplacement de sauvegarde

Le jeu utilise un seul emplacement de sauvegarde.

Le menu principal propose :

- **Continuer**, pour reprendre depuis le dernier niveau debloque ;
- **Nouvelle partie**, pour effacer la progression existante et recommencer au debut du niveau 0.

Lorsque la sauvegarde porte l'etat `Aventure terminee`, `Continuer` est remplace par `Revoir la fin`. Cette action rejoue la liberation d'Aliyah et les credits sans relancer le combat final.

Avant l'effacement d'une sauvegarde, le jeu demande une confirmation au joueur afin d'eviter toute suppression accidentelle.

## Resume des regles

| Situation | Resultat |
|---|---|
| Niveau 0 termine | Sauvegarde automatique et acces a la Foret enchantee |
| Golem vaincu et cle recuperee | Sauvegarde automatique |
| Sixieme cle recuperee | Sauvegarde et reprise devant la porte du donjon |
| Tata Lisa vaincue et Aliyah liberee | Sauvegarde finale `Aventure terminee` |
| Pancarte de controle activee | Point de reapparition temporaire |
| Vie perdue | Retour a la pancarte activee avec trois coeurs |
| Trois vies perdues | Game Over et reprise au debut du niveau |
| Jeu ferme pendant un niveau | Reprise au debut de ce niveau |
| Nouvelle partie choisie | Confirmation puis effacement de la progression |
