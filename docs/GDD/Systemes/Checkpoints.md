# Checkpoints

> **Statut :** Valide

## Objectif

Definir le fonctionnement des pancartes de controle temporaires et garantir un point de reapparition previsible apres la perte d'une vie.

## Nombre et placement

| Sequence | Nombre de checkpoints | Placement general |
|---|---:|---|
| Niveau 0 - Village des Bles | `0` | Aucun checkpoint |
| Chacun des six niveaux principaux | `1` | Approximativement au milieu du parcours |
| Combat final contre Tata Lisa | `0` | Reprise permanente devant la porte du donjon |

Chaque pancarte de controle des niveaux principaux a ete laissee par Remi et Amelie pendant leurs anciennes expeditions afin de securiser les routes des voyageurs.

## Activation automatique

- La pancarte s'active automatiquement lorsque Imran entre dans sa zone de declenchement.
- Aucune pression sur la commande `Interaction` n'est demandee.
- L'activation ne bloque pas le deplacement et ne lance aucune sequence obligatoire.
- Le symbole de la pancarte produit une courte impulsion lumineuse doree accompagnee de quelques particules.
- Un son bref, doux et clairement reconnaissable confirme immediatement l'activation.
- Le symbole conserve ensuite une faible lueur doree pendant toute la tentative en cours.
- Retraverser la zone d'une pancarte deja activee ne rejoue pas le retour d'activation.

## Duree de validite

- Une pancarte activee devient le point de reapparition temporaire du niveau en cours.
- Elle reste active apres la perte d'une vie tant qu'il reste au moins une vie.
- Elle reste active pendant toute la tentative en cours dans ce niveau.
- Elle est oubliee apres un Game Over, un retour au menu principal, une fermeture du jeu, un abandon du niveau ou la fin du niveau.
- Elle ne cree jamais de sauvegarde permanente.

## Reapparition apres la perte d'une vie

| Situation | Point de reapparition | Coeurs | Vies |
|---|---|---:|---:|
| Niveau 0 | Debut du tutoriel | `3` | Une vie en moins |
| Niveau principal avant activation | Debut du niveau | `3` | Une vie en moins |
| Niveau principal apres activation | Pancarte de controle | `3` | Une vie en moins |

La reapparition doit placer Imran sur une position stable et lisible. Aucun danger ne doit pouvoir lui infliger un degat avant qu'il puisse de nouveau agir.

## Reinitialisation apres la perte d'une vie

Lorsqu'il reste au moins une vie, la sequence jouable est rechargee avec les regles suivantes :

- la pancarte de controle activee reste le point de reapparition ;
- tous les ennemis vaincus ou encore presents reviennent a leur etat initial ;
- tous les projectiles actifs disparaissent ;
- les dangers mobiles et les objets temporaires reviennent a leur position et leur etat initial ;
- les objets cassables eventuels reviennent a leur etat initial ;
- le golem revient avec sa vie maximale et sa premiere phase ;
- le feu de camp revient a son etat disponible et peut etre utilise de nouveau ;
- aucun autre progres temporaire du niveau n'est conserve.

Cette reinitialisation ne rend pas la vie perdue. Imran reapparait avec `3 coeurs` et le nombre de vies restant apres la perte.

## Effets exclus

L'activation d'une pancarte de controle :

- ne restaure aucun coeur ;
- ne restaure aucune vie ;
- ne sauvegarde pas la partie ;
- ne remplace pas un feu de camp ;
- ne termine pas le niveau ;
- ne debloque aucune capacite.

## Pancartes du niveau 0

- Les pancartes du Village des Bles servent uniquement au tutoriel.
- Elles affichent les commandes et les regles de gameplay.
- Elles ne modifient jamais le point de reapparition.
- Une vie perdue dans le niveau 0 replace toujours Imran au debut du tutoriel.

## Criteres de validation

Les checkpoints seront valides si :

- chacun des six niveaux principaux contient exactement une pancarte de controle ;
- le niveau 0 ne contient aucun checkpoint ;
- une pancarte de controle s'active automatiquement sans interrompre le joueur ;
- un retour visuel et sonore confirme l'activation une seule fois ;
- le point de reapparition depend uniquement de l'activation dans la tentative en cours ;
- une reapparition rend `3 coeurs` sans restaurer la vie perdue ;
- tous les elements temporaires du niveau sont reinitialises apres la perte d'une vie ;
- seule la pancarte activee reste conservee pendant les vies restantes ;
- un Game Over et une reprise permanente oublient toujours le checkpoint ;
- aucune pancarte de controle ne cree de sauvegarde ;
- les pancartes du tutoriel ne peuvent jamais etre confondues avec un checkpoint.

## Sources

- [Points de controle du Concept Game](../../Concept-Game/05-Gameplay/Points-de-Controle.md)
- [Checkpoints du Concept Game](../../Concept-Game/06-Systemes/Checkpoints.md)
- [Tutoriel du niveau 0](../../Concept-Game/05-Gameplay/Tutoriel-Niveau-0.md)
- [Coeurs et vies](Coeurs-et-Vies.md)
- [Game Over](Game-Over.md)
- [Sauvegarde du Concept Game](../../Concept-Game/06-Systemes/Sauvegarde.md)
- [Effets visuels](../../Concept-Game/09-Direction-Artistique/Effets-Visuels.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
