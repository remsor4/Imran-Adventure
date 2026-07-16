# Double saut

> **Statut :** Valide

## Objectif

Definir un second saut aerien disponible des le debut de l'aventure.

## Disponibilite initiale

- Le Double saut est disponible des la premiere prise de controle dans le niveau 0.
- Une pancarte du tutoriel explique la seconde pression en l'air avant la premiere situation qui la demande.
- Il partage toujours la commande du saut normal.
- Il ne depend d'aucune cle, d'aucun golem et d'aucune donnee de sauvegarde.

## Disponibilite

Le Double saut peut etre utilise une fois pendant une periode aerienne :

- apres un saut normal ;
- apres avoir quitte une plateforme sans sauter ;
- pendant une chute.

Il ne peut pas etre utilise pendant une interaction, un degat, une mort ou un etat verrouille.

## Valeurs

| Element | Valeur |
|---|---:|
| Impulsion | `450 px/s` vers le haut |
| Gravite pendant la montee | `1300 px/s2` |
| Gravite pendant la chute | `1500 px/s2` |
| Hauteur maximale visee | Environ `78 px` |
| Duree totale visee | Environ `0.67 s` |
| Utilisations | `1` par periode aerienne |

## Comportement

- L'impulsion remplace la vitesse verticale actuelle, meme pendant une chute.
- Le controle horizontal est conserve.
- Relacher la commande pendant la montee limite la vitesse vers le haut a `225 px/s`, soit la moitie de son impulsion initiale.
- Toucher une surface praticable restaure le Double saut.
- Une reapparition restaure le Double saut.

## Lisibilite

Le Double saut doit se distinguer du premier saut par :

- une pose aerienne specifique ;
- une impulsion visuelle courte ;
- un son plus aerien ;
- un effet qui ne ressemble pas a la magie du Chaos.

## Cas particuliers

- Une commande de saut conservee avant une reception declenche un saut normal, pas un Double saut.
- Un plafond interrompt la montee sans restaurer la capacite.
- Recevoir un degat ne restaure pas la capacite.
- Le Double saut reste disponible pendant une attaque normale aerienne si son utilisation n'a pas deja ete consommee.
- Son impulsion remplace alors la vitesse verticale sans interrompre l'animation du coup.

## Criteres de validation

Le Double saut est valide si :

- une seule utilisation est possible avant une reception ;
- il fonctionne apres un saut ou pendant une chute ;
- il reprend le controle vertical pendant une chute ;
- il reste utilisable pendant une attaque normale aerienne ;
- il reste legerement moins haut que le saut normal ;
- son effet est immediatement distinct du saut normal et de la magie du Chaos.

## Sources

- [Statistiques d'Imran](Statistiques-Imran.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Saut](Saut.md)
- [Dash](Dash.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Double saut du Concept Game](../../Concept-Game/05-Gameplay/Double-Saut.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
