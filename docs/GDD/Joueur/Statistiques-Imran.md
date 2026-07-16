# Statistiques d'Imran

> **Statut :** Valide

## Objectif

Regrouper les valeurs de reference utilisees par les autres documents du joueur.

## Echelle de gameplay

| Element | Valeur |
|---|---:|
| Resolution de reference | `1920 x 1080` |
| Format d'image | `16:9` |
| Grille logique de reference | `64 px` |
| Largeur du collider principal | `36 px` |
| Hauteur du collider principal | `60 px` |
| Largeur de la zone de degat d'Imran | `32 px` |
| Hauteur de la zone de degat d'Imran | `56 px` |
| Distance maximale d'interaction | `56 px` |
| Pente maximale praticable | `45 degres` |

La resolution de reference definit le cadre de composition visible. La grille logique sert a comparer les distances. Elle n'impose pas un style pixel art ni une taille de tuile visible.

Une mise a l'echelle de l'image conserve le format `16:9` et ne modifie ni les distances, ni les vitesses, ni les collisions de gameplay. Les modes d'affichage et leur comportement exact seront finalises pendant l'etape 14.

Le visuel d'Imran peut depasser legerement du collider principal. Sa zone vulnerable reste centree et ne depasse jamais ce collider.

## Sante et tentatives

| Element | Valeur |
|---|---:|
| Coeurs au debut d'un niveau | `3` |
| Vies au debut d'un niveau | `3` |
| Invulnerabilite apres un degat | `1.00 s` |
| Duree de reaction a un degat | `0.20 s` |

Les degats exacts des ennemis, boss et dangers seront definis pendant les etapes Combat, Ennemis et Boss.

## Deplacement horizontal

| Element | Valeur |
|---|---:|
| Vitesse maximale au sol | `240 px/s` |
| Acceleration au sol | `1800 px/s2` |
| Freinage au sol | `2200 px/s2` |
| Acceleration en l'air | `1200 px/s2` |
| Freinage en l'air | `600 px/s2` |

Il n'existe aucune vitesse de course distincte.

## Saut

| Element | Valeur |
|---|---:|
| Impulsion du saut | `480 px/s` vers le haut |
| Gravite pendant la montee | `1300 px/s2` |
| Gravite pendant la chute | `1500 px/s2` |
| Vitesse maximale de chute | `800 px/s` |
| Hauteur maximale visee | Environ `89 px` |
| Duree totale visee | Environ `0.71 s` |
| Tolerance apres avoir quitte un bord | `0.12 s` |
| Memoire de la commande de saut | `0.12 s` |

## Double saut

| Element | Valeur |
|---|---:|
| Impulsion du Double saut | `450 px/s` vers le haut |
| Hauteur maximale visee | Environ `78 px` |
| Duree totale visee | Environ `0.67 s` |
| Utilisations par periode aerienne | `1` |

## Dash

| Element | Valeur |
|---|---:|
| Vitesse | `620 px/s` |
| Duree | `0.20 s` |
| Distance theorique | Environ `124 px` |
| Intervalle entre deux Dashs | `1.00 s` mesure depuis le debut du Dash |
| Delai restant apres la fin du Dash | `0.80 s` |
| Disponibilite | Au sol uniquement |
| Perte du contact avec le sol | Interruption immediate du Dash |

## Recul apres un degat

| Element | Valeur |
|---|---:|
| Vitesse horizontale initiale | `220 px/s` loin de la source |
| Vitesse verticale initiale | `280 px/s` vers le haut |
| Duree sans controle | `0.20 s` |

## Valeurs a tester dans le prototype

Les valeurs suivantes doivent etre observees ensemble :

- temps necessaire pour atteindre la vitesse maximale ;
- distance de freinage ;
- lisibilite de la hauteur du saut ;
- facilite des receptions sur une plateforme de `64 px` ;
- distance du Dash par rapport a un trou ;
- controle apres un saut et apres la fin d'un Dash ;
- confort du recul et de l'invulnerabilite.

Un ajustement conserve les rapports generaux : le Dash reste plus rapide que la marche, le Double saut reste legerement moins haut que le premier saut et la chute reste plus rapide que la montee.

## Criteres de validation

Les statistiques sont valides si :

- chaque valeur possede une unite ;
- les valeurs permettent un prototype sans decision manquante ;
- Imran peut atteindre sa vitesse maximale rapidement sans changement instantane brutal ;
- un saut franchit confortablement une hauteur proche d'une grille logique ;
- le Dash couvre environ deux grilles logiques ;
- le Dash ne peut jamais etre declenche dans les airs ;
- les coeurs et les vies correspondent au Concept Game.

## Sources

- [Coeurs](../../Concept-Game/05-Gameplay/Coeurs.md)
- [Vies](../../Concept-Game/05-Gameplay/Vies.md)
- [Deplacements](../../Concept-Game/05-Gameplay/Deplacements.md)
- [Dash](../../Concept-Game/05-Gameplay/Dash.md)
- [Double saut](../../Concept-Game/05-Gameplay/Double-Saut.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
- [Reference video du Dash Godot](Reference-Video-Dash-Godot.md)
