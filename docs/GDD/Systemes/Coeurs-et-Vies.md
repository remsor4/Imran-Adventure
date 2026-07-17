# Coeurs et vies

> **Statut :** Valide

## Objectif

Definir la perte des coeurs, la perte des vies et les seules situations qui restaurent ces valeurs.

## Valeurs validees

| Element | Valeur |
|---|---:|
| Coeurs au debut d'une vie | `3` |
| Vies au debut d'un niveau | `3` |
| Degat ordinaire recu | `1 coeur` |
| Soin pendant l'exploration ordinaire | Aucun |
| Restauration avant un golem | Jusqu'a `3 coeurs` |
| Activation du feu de camp | Commande `Interaction` |
| Maximum de coeurs | `3` |
| Maximum de vies | `3` |

## Perte d'un coeur

- Une attaque ordinaire non bloquee retire `1 coeur` selon les regles du dossier Combat.
- Le HUD est mis a jour immediatement.
- Tant qu'il reste au moins un coeur, Imran conserve sa vie actuelle.
- L'invulnerabilite de `1.00 s` empeche plusieurs pertes consecutives immediates.
- Un projectile bloque par le Bouclier ne retire aucun coeur.

## Absence de soin pendant l'exploration

- Aucun coeur ne peut etre ramasse dans un niveau.
- Les ennemis ne donnent aucun coeur.
- Les coffres, objets cassables et elements du decor ne donnent aucun coeur.
- Une pancarte de controle ne restaure aucun coeur lors de son activation.
- Aucun menu ni aucune commande ne permet de restaurer un coeur pendant l'exploration ordinaire.
- Imran conserve donc ses coeurs restants jusqu'a un nouveau degat, la perte de sa vie ou la zone de preparation placee avant un golem.

## Restauration avant un golem

- Un feu de camp est place dans une zone sure juste avant chaque arene de golem.
- Ce feu a ete laisse par Remi et Amelie pendant leurs anciennes expeditions.
- Un message d'interaction apparait lorsque Imran est a portee du feu.
- Imran doit utiliser volontairement la commande `Interaction` pour recevoir le soin.
- Entrer dans la zone ne declenche aucun soin automatique.
- Une interaction valide remet les coeurs d'Imran a `3` avant le combat.
- Il ne restaure aucune vie : le nombre de vies restantes ne change pas.
- Il ne permet jamais de depasser le maximum de `3 coeurs`.
- Il reste separe du checkpoint temporaire situe approximativement au milieu du niveau.
- Aucun ennemi ni danger ne doit pouvoir infliger un degat pendant cette restauration.
- L'interaction suit les regles communes definies dans le dossier Controles.

## Perte d'une vie

1. Lorsque le dernier coeur est perdu, Imran entre dans l'etat `Mort`.
2. Une vie est retiree.
3. S'il reste au moins une vie, Imran reapparait au debut du niveau ou au checkpoint temporaire actif.
4. Cette nouvelle vie commence avec `3 coeurs`.
5. Le checkpoint reste actif jusqu'a la fin ou a l'abandon du niveau.
6. Si aucune vie ne reste, le Game Over apparait.

Le retour a `3 coeurs` apres une mort correspond au depart d'une nouvelle vie. Il ne constitue pas une recuperation pendant la vie precedente.

## Restauration apres un golem

- Vaincre le golem rend son coffre accessible.
- La recuperation de la cle confirme la fin du niveau.
- Avant le niveau suivant, les coeurs et les vies sont restaures a `3`.
- Aucun surplus ne peut depasser ces maximums.
- Cette restauration ne cree aucun objet de soin dans le niveau termine.

## Niveau 0 et reprises

- Le niveau 0 commence avec `3 coeurs` et `3 vies`.
- Une vie perdue dans le niveau 0 recommence au debut du tutoriel avec `3 coeurs`.
- Un Game Over recommence le niveau 0 avec `3 coeurs` et `3 vies`.
- Un feu de camp laisse par Remi et Amelie est place a la fin du niveau 0.
- Imran doit interagir avec ce feu pour restaurer ses coeurs a `3` avant le passage vers la Foret enchantee.
- Une reprise permanente au debut d'un niveau charge les valeurs initiales de `3 coeurs` et `3 vies`.

Ces valeurs de depart sont des reinitialisations de tentative et non des soins disponibles pendant le parcours.

## Criteres de validation

Les coeurs et les vies sont valides si :

- Imran ne possede jamais plus de `3 coeurs` ou `3 vies` ;
- aucun coeur ne peut etre recupere pendant l'exploration ordinaire ;
- un feu de camp restaure les coeurs juste avant chaque golem ;
- le soin du feu de camp ne se declenche jamais sans une interaction volontaire ;
- un feu de camp ne modifie jamais le nombre de vies restantes ;
- le feu de camp du niveau 0 permet de commencer la Foret enchantee avec `3 coeurs` ;
- un degat ordinaire retire `1 coeur` ;
- perdre le dernier coeur retire exactement une vie ;
- une nouvelle vie commence avec `3 coeurs` au bon point de reapparition ;
- perdre la derniere vie ouvre le Game Over ;
- la fin d'un niveau principal restaure les coeurs et les vies avant le niveau suivant.

## Sources

- [Degats](../Combat/Degats.md)
- [Invulnerabilite](../Combat/Invulnerabilite.md)
- [Reactions aux degats](../Joueur/Reactions-aux-Degats.md)
- [Coeurs du Concept Game](../../Concept-Game/05-Gameplay/Coeurs.md)
- [Vies du Concept Game](../../Concept-Game/05-Gameplay/Vies.md)
- [Checkpoints du Concept Game](../../Concept-Game/06-Systemes/Checkpoints.md)
- [Sauvegarde du Concept Game](../../Concept-Game/06-Systemes/Sauvegarde.md)
- [Feux de camp](../../Concept-Game/05-Gameplay/Feux-de-Camp.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
