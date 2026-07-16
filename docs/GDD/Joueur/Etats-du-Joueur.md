# Etats du joueur

> **Statut :** Valide

## Objectif

Lister les etats visibles d'Imran et les transitions autorisees entre ses actions.

## Etats principaux

| Etat | Entree | Sortie normale |
|---|---|---|
| Attente | Imran est au sol sans direction ni action | Deplacement, Saut, Dash, Attaque, Charge ou Interaction |
| Deplacement | Une direction horizontale est maintenue au sol | Attente, Saut, Dash ou action de combat autorisee |
| Saut | Le saut est declenche | Chute, Double saut ou action aerienne autorisee |
| Chute | La vitesse verticale est dirigee vers le bas | Reception, Double saut ou action aerienne autorisee |
| Double saut | La capacite est disponible et sa commande est utilisee en l'air | Saut, Chute ou action aerienne autorisee |
| Dash | Imran touche le sol, la capacite est disponible et sa commande est acceptee | Attente, Deplacement ou Chute si le support est perdu |
| Attaque | Une attaque autorisee commence | Etat de mouvement compatible apres la fin de l'attaque |
| Charge du Smash | La commande d'attaque est maintenue assez longtemps | Smash Tranchant, Degat ou Mort |
| Smash Tranchant | La charge validee est relachee | Etat de mouvement compatible apres l'attaque |
| Interaction | Une cible valide accepte l'interaction | Attente apres la sequence |
| Degat | Imran recoit un degat non bloque | Saut, Chute, Attente ou Mort |
| Mort | Les trois coeurs sont perdus et une vie doit etre retiree | Reapparition ou Game Over |
| Verrouille | Une scene, un chargement ou une interface retire le controle | Etat impose par la reprise |

Les disponibilites exactes des attaques au sol et dans les airs seront definies pendant l'etape 6.

## Regles communes

- Un seul etat d'action principal est actif a la fois.
- Le deplacement horizontal et la vitesse verticale peuvent continuer lorsqu'un etat compatible l'autorise.
- Une action deja engagee suit les priorites validees dans le dossier Controles.
- Recevoir un degat non bloque interrompt l'action en cours.
- La mort interrompt tous les autres etats.
- Pause suspend les etats sans les remplacer.
- Une cinematique ou un chargement place Imran dans l'etat `Verrouille`.

## Orientation

- Imran regarde vers la derniere direction horizontale valide.
- Une direction neutre ne change pas son orientation.
- Le Dash sans direction utilise l'orientation actuelle.
- Une action verrouillant son orientation conserve la direction choisie au debut de l'action.
- Le Bouclier utilise l'orientation actuelle sans creer un etat de blocage. Sa protection automatique reste active pendant les etats de mouvement et devient inactive uniquement pendant la preparation ou la charge du Smash Tranchant.

## Reapparition

Lors d'une reapparition :

1. Imran entre dans l'etat `Verrouille` ;
2. sa position est replacee au debut du niveau ou au checkpoint actif ;
3. ses trois coeurs sont restaures ;
4. ses vitesses horizontale et verticale reviennent a zero ;
5. le delai du Dash est annule et son Double saut redevient disponible ;
6. une courte invulnerabilite de reprise empeche un degat immediat ;
7. le controle revient en etat `Attente` ou `Chute` selon le point de reapparition.

La duree exacte de l'invulnerabilite de reprise sera definie avec les systemes de vies et checkpoints pendant l'etape 7.

## Controles bloques

Les commandes de gameplay sont bloquees pendant :

- un chargement ;
- une cinematique non interactive ;
- l'ouverture et la recompense d'un coffre ;
- la reaction a un degat ;
- la mort ;
- le Game Over ;
- la sequence de victoire ;
- un menu actif.

La commande Pause reste disponible uniquement dans les contextes autorises par le document des priorites.

## Criteres de validation

Les etats sont valides si :

- chaque action visible possede un etat identifiable ;
- aucun etat ne permet deux actions incompatibles ;
- la mort et le verrouillage bloquent toutes les commandes de gameplay ;
- la reapparition remet les vitesses a zero ;
- Pause suspend sans perdre l'etat courant ;
- les regles de priorite correspondent aux Controles.

## Liens

- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Statistiques d'Imran](Statistiques-Imran.md)
- [Deplacement](Deplacement.md)
- [Saut](Saut.md)
- [Dash](Dash.md)
- [Double saut](Double-Saut.md)
- [Reactions aux degats](Reactions-aux-Degats.md)
