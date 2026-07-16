# Priorites des actions

> **Statut :** Valide

## Objectif

Definir quelle action est acceptee lorsque plusieurs commandes sont utilisees en meme temps, ainsi que les actions qui ne peuvent pas etre executees simultanement.

Ce document ne fixe pas les durees, vitesses ou fenetres d'animation. Ces valeurs appartiennent aux etapes Joueur et Combat.

## Contextes d'entree

Un seul contexte principal est actif a la fois :

| Priorite | Contexte | Effet |
|---:|---|---|
| 1 | Etat verrouille | Les commandes de gameplay sont ignorees pendant un chargement, une transition non interactive, le Game Over ou la victoire |
| 2 | Pause ou menu | Seules les commandes de navigation sont acceptees |
| 3 | Interaction narrative | Seules les commandes demandees par la sequence sont acceptees |
| 4 | Gameplay | Les commandes d'Imran sont acceptees selon son etat actuel |

La commande Pause peut suspendre le gameplay pendant l'exploration ou un combat. Elle ne peut pas interrompre un chargement, le Game Over ou l'ecran de victoire.

## Priorite dans le gameplay

Lorsque plusieurs actions valides commencent exactement au meme instant, l'ordre suivant est utilise :

1. interaction disponible ;
2. blocage ;
3. Dash ;
4. attaque ;
5. saut ;
6. deplacement horizontal.

L'interaction n'est prioritaire que si un message d'interaction est visible. Sans cible valide, sa commande est ignoree et les autres actions restent disponibles.

Le blocage est place avant l'attaque afin de favoriser une reaction defensive claire pour le public cible.

## Etats prioritaires d'Imran

| Etat | Actions annulees ou bloquees |
|---|---|
| Mort | Toutes les actions sont annulees jusqu'a la reapparition |
| Degat recu | L'attaque, la charge, le Dash, le blocage et l'interaction sont interrompus |
| Interaction en cours | Le deplacement, le saut, le Dash, l'attaque et le blocage sont bloques |
| Dash en cours | Une nouvelle attaque, un blocage et une interaction sont bloques |
| Attaque en cours | Un nouveau Dash, un blocage et une interaction sont bloques |
| Charge du Smash | Un Dash, un blocage et une interaction sont bloques |
| Blocage maintenu | Une attaque, un Dash et une interaction sont bloques |

La disponibilite du saut, du deplacement ou de l'attaque dans les airs sera precisee dans les etapes 5 et 6. Le present document s'applique uniquement lorsqu'une action est autorisee par l'etat du joueur.

## Regle d'engagement

Une action de gameplay deja commencee ne peut pas etre annulee par une autre commande, sauf dans les cas suivants :

- Imran recoit un degat ;
- Imran meurt ;
- le jeu passe dans un contexte verrouille ;
- une future regle validee du Joueur ou du Combat autorise explicitement cette annulation.

Cette regle evite les changements d'etat difficiles a lire et les combinaisons involontaires.

## Directions opposees

- Gauche et droite maintenues ensemble produisent une direction neutre.
- Relacher une direction alors que l'autre reste maintenue applique immediatement la direction restante.
- Une direction donnee par le clavier et une direction opposee donnee par la manette produisent aussi une direction neutre.

## Interaction

Une interaction commence uniquement si :

- un element interactif valide est a portee ;
- son message est visible ;
- Imran n'est pas mort, touche, en Dash, en attaque ou en blocage ;
- aucun menu ou contexte verrouille n'est actif.

Pendant l'ouverture d'un coffre, le controle d'Imran reste bloque jusqu'a la fin de la courte sequence d'ouverture et de recompense.

## Memoire courte des commandes

Une commande de saut, d'attaque ou de Dash utilisee tres peu de temps avant la fin d'un etat incompatible peut etre conservee pendant une courte duree.

- Une seule commande peut etre conservee.
- La commande la plus recente remplace la precedente.
- La commande expire si son action reste impossible.
- Aucune commande maintenue pendant une cinematique ou un chargement n'est conservee.
- La duree exacte sera definie et testee dans les etapes Joueur et Combat.

Cette memoire limite les commandes perdues sans executer une action longtemps apres la pression du joueur.

## Menus

- Une seule direction de navigation est traitee a la fois.
- La confirmation est prioritaire sur une direction recue exactement au meme instant.
- Retour ferme d'abord une fenetre de confirmation avant de fermer le menu parent.
- Une action destructive demande toujours une confirmation distincte.
- Les commandes de gameplay ne traversent jamais la fermeture d'un menu.

## Criteres de validation

Les priorites sont valides si :

- un seul contexte principal recoit les commandes ;
- une interaction ne commence jamais sans cible valide ;
- le blocage gagne contre une attaque simultanee ;
- deux directions opposees produisent un resultat neutre ;
- une action deja engagee ne peut pas etre annulee sans regle explicite ;
- les commandes maintenues pendant une cinematique ne declenchent rien au retour du controle ;
- un changement de menu ne declenche aucune action de gameplay involontaire.

## Sources

- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Dash](../../Concept-Game/05-Gameplay/Dash.md)
- [Combat](../../Concept-Game/05-Gameplay/Combat.md)
- [Smash Tranchant](../../Concept-Game/05-Gameplay/Smash-Tranchant.md)
- [Bouclier de lumiere](../../Concept-Game/05-Gameplay/Bouclier-de-Lumiere.md)
- [Coffres](../../Concept-Game/05-Gameplay/Coffres.md)
- [Pause](../../Concept-Game/11-Interface/Pause.md)
- [Options](../../Concept-Game/11-Interface/Options.md)
