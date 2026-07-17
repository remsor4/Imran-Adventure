# Reference video Wonder Boy

> **Statut :** Valide

## Source

- Video : [Wonderboy: The Dragon's Trap - Walkthrough Part 1 - Meka Dragon](https://www.youtube.com/watch?v=LAlqe2fANSQ)
- Plage demandee : de `0:00` a `6:00`
- Flux utilise pour les mesures : `640 x 360`, `30 images/s`, format `16:9`
- Resolution finale d'Imran Adventure : `1920 x 1080`, format `16:9`

Le flux analyse sert uniquement a mesurer les rapports de taille, de distance et de temps. Il ne devient pas la resolution interne obligatoire du projet Godot.

## Parties utiles de la plage

| Plage approximative | Contenu | Utilisation |
|---|---|---|
| `0:00 - 1:08` | Menus et introduction | Reference de presentation uniquement |
| `1:09 - 4:02` | Deplacement, sauts, collisions et combats ordinaires | Mesures principales du joueur |
| `4:03 - 4:14` | Introduction du boss | Rythme de transition |
| `4:15 - 5:55` | Combat contre Meka Dragon | Lisibilite en combat et occupation de l'ecran |
| `5:56 - 6:00` | Fin immediate du combat | Retour visuel de victoire |

## Mesures retenues

| Element observe | Mesure dans le flux | Cible normalisee pour Imran |
|---|---:|---:|
| Hauteur visuelle du personnage | Environ `60 a 68 px` | Une grille logique de `64 px` |
| Vitesse horizontale maximale | Environ `230 a 245 px/s` apres correction du suivi de camera | `240 px/s` |
| Temps pour atteindre la vitesse normale | Inferieur a `0.20 s` | Environ `0.13 s` |
| Hauteur du saut normal | Environ `80 px` | Environ `89 px` |
| Duree du saut normal | Environ `0.70 a 0.75 s` | Environ `0.71 s` |
| Temps jusqu'au sommet | Environ `0.35 a 0.40 s` | Environ `0.37 s` |
| Position horizontale suivie par la camera | Proche du centre avant le defilement | `45 %` vers la droite et `55 %` vers la gauche |

Les valeurs cibles conservent les rapports de la video tout en utilisant les equations de mouvement du GDD.

## Consequences pour l'etape 5

- La vitesse maximale de `240 px/s` est conservee.
- L'acceleration rapide est conservee.
- Le collider principal devient `36 x 60 px` afin de rester legerement plus petit que le visuel.
- La zone vulnerable devient `32 x 56 px`.
- Le saut est abaisse par rapport a la premiere proposition : impulsion `480 px/s`, hauteur proche de `89 px` et duree proche de `0.71 s`.
- La chute reste legerement plus rapide que la montee pour faciliter la lecture des receptions.

## Adaptations propres a Imran Adventure

Les elements suivants ne peuvent pas etre mesures dans cette plage de la video :

- Dash ;
- Double saut ;
- tolerance apres avoir quitte un bord ;
- memoire de la commande de saut ;
- hauteur variable selon le relachement ;
- vitesse maximale de chute ;
- duree exacte d'invulnerabilite apres un degat ;
- recul exact apres un degat.

Ils restent des propositions propres a Imran Adventure et devront etre verifies dans le prototype Godot. Le Double saut est ajuste a `450 px/s` pour rester legerement plus bas que le saut normal. Le Dash possede maintenant une [reference video dediee](Reference-Video-Dash-Godot.md).

## Limites de l'analyse

- Les mesures sont visuelles et ne donnent pas acces au code du jeu de reference.
- La camera se deplace pendant certaines courses ; sa vitesse a ete prise en compte dans l'estimation horizontale.
- Une [reference camera dediee](../Systemes/Reference-Video-Wonder-Boy-Camera.md) fixe le changement de cadrage apres un demi-tour a `0.60 s`.
- Les animations modifient legerement la taille visible du personnage selon la pose.
- Les valeurs finales devront etre confirmees par un prototype a `1920 x 1080`.

## Criteres de validation

La reference est correctement appliquee si :

- le saut dure environ `0.71 s` sans obstacle ;
- le sommet se situe environ `89 px` au-dessus de la position de depart ;
- la vitesse maximale est atteinte en moins de `0.20 s` ;
- le personnage reste lisible pendant une course, un saut et un combat ;
- les valeurs non visibles dans la video restent identifiees comme des adaptations du projet.
