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
2. Dash ;
3. attaque ;
4. saut ;
5. deplacement horizontal.

L'interaction n'est prioritaire que si un message d'interaction est visible. Sans cible valide, sa commande est ignoree et les autres actions restent disponibles.

La protection du Bouclier ne figure pas dans cette liste, car elle est automatique et ne correspond a aucune commande.

Le saut et l'attaque normale constituent une exception compatible. S'ils commencent exactement au meme instant au sol, le saut est applique en premier et l'attaque devient aerienne. L'attaque ne transforme donc pas cette combinaison en attaque immobile au sol.

Pendant une attaque aerienne, les commandes gauche et droite restent acceptees. L'animation du coup ne remplace ni la vitesse horizontale, ni la vitesse verticale, ni la gravite du saut.

## Protection automatique du Bouclier

Avant d'appliquer les degats d'un projectile ennemi, le jeu verifie l'orientation et l'absence de charge d'Imran. Un projectile venant de face est bloque automatiquement, meme pendant un mouvement, si Imran ne prepare pas le Smash Tranchant. Le Bouclier ne force jamais l'arret d'une action ou d'un mouvement.

## Etats prioritaires d'Imran

| Etat | Actions annulees ou bloquees |
|---|---|
| Mort | Toutes les actions sont annulees jusqu'a la reapparition |
| Degat recu | L'attaque, la charge, le Dash et l'interaction sont interrompus |
| Interaction en cours | Le deplacement, le saut, le Dash et l'attaque sont bloques |
| Dash en cours | Une nouvelle attaque et une interaction sont bloquees |
| Attaque normale au sol | Le deplacement, le saut, le Double saut, le Dash, une nouvelle attaque et l'interaction sont bloques |
| Preparation ou charge du Smash | Le deplacement, le saut, le Double saut, le Dash, une nouvelle attaque et l'interaction sont bloques |
| Lancement du Smash | Le deplacement, le saut, le Double saut, le Dash, une nouvelle attaque et l'interaction sont bloques pendant `0.35 s` |

Une attaque normale aerienne conserve le deplacement horizontal, la vitesse verticale et la gravite. Le Smash reste strictement terrestre.

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
- Imran n'est pas mort, touche, en Dash ou en attaque ;
- aucun menu ou contexte verrouille n'est actif.

Pendant l'ouverture d'un coffre, le controle d'Imran reste bloque jusqu'a la fin de la courte sequence d'ouverture et de recompense.

Pres d'un feu de camp, le soin commence uniquement apres une pression volontaire sur la commande `Interaction`. La simple entree dans sa zone ne produit aucun effet. Le controle d'Imran reste bloque pendant la courte animation de repos et les coeurs sont ensuite ramenes a `3`, sans modifier les vies restantes.

## Memoire courte des commandes

- Seule une commande de saut utilisee moins de `0.12 s` avant une reception peut etre conservee.
- Cette commande declenche un saut normal des que le contact avec le sol devient valide.
- Une commande de Dash recue dans les airs ou pendant un etat incompatible est ignoree.
- Une commande d'attaque recue pendant une attaque normale ou le lancement du Smash est ignoree.
- Une commande recue pendant un degat, une interaction, une mort, une cinematique ou un chargement est ignoree.
- Aucune commande ignoree ne declenche une action retardee au retour du controle.

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
- la protection automatique ne demande aucune commande et ne modifie pas la priorite des actions ;
- deux directions opposees produisent un resultat neutre ;
- une action deja engagee ne peut pas etre annulee sans regle explicite ;
- seule la commande de saut utilise une memoire de `0.12 s` avant la reception ;
- les commandes maintenues pendant une cinematique ne declenchent rien au retour du controle ;
- un changement de menu ne declenche aucune action de gameplay involontaire.

## Sources

- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Dash](../../Concept-Game/05-Gameplay/Dash.md)
- [Combat](../../Concept-Game/05-Gameplay/Combat.md)
- [Smash Tranchant](../../Concept-Game/05-Gameplay/Smash-Tranchant.md)
- [Bouclier de lumiere](../../Concept-Game/05-Gameplay/Bouclier-de-Lumiere.md)
- [Coffres](../../Concept-Game/05-Gameplay/Coffres.md)
- [Feux de camp](../../Concept-Game/05-Gameplay/Feux-de-Camp.md)
- [Pause](../../Concept-Game/11-Interface/Pause.md)
- [Options](../../Concept-Game/11-Interface/Options.md)
