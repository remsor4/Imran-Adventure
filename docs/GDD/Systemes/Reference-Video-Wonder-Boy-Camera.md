# Reference video Wonder Boy - Camera

> **Statut :** Valide

## Source

- Fichier analyse : `Wonder Boy The Dragon's Trap_2026.07.17-03.57.mp4`
- Resolution de la capture : `1920 x 1088`
- Frequence : environ `60 images/s`
- Duree : `25.47 s`
- Nombre total d'images : `1528`

La capture inclut les bordures de la fenetre et la barre des taches. Ces elements ne modifient pas la mesure temporelle du changement de camera.

## Methode

- Les premieres secondes contenant l'overlay d'enregistrement ont ete exclues.
- Le deplacement horizontal des batiments a ete mesure image par image.
- Trois demi-tours directs ont ete retenus.
- Le debut correspond au premier ralentissement visible du decor.
- La fin correspond au retour a une vitesse de defilement stable dans la direction opposee.

## Mesures

| Demi-tour | Plage approximative | Duree | Images |
|---:|---|---:|---:|
| 1 | `8.25 s` a `8.90 s` | `0.65 s` | Environ `39` |
| 2 | `13.75 s` a `14.30 s` | `0.55 s` | Environ `33` |
| 3 | `19.32 s` a `19.90 s` | `0.58 s` | Environ `35` |
| Moyenne | - | `0.59 s` | Environ `36` |

## Valeur retenue

La duree cible est arrondie a `0.60 s` pour Imran Adventure.

Pendant ce changement, la camera ralentit, passe par une courte phase presque immobile, puis repart progressivement dans la direction opposee. Cette duree concerne uniquement le cadrage et ne ralentit jamais Imran.

La valeur devra etre confirmee dans le prototype Godot a la resolution de reference `1920 x 1080`.

## Cadrage vertical retenu

Dans les passages plats de la capture, le centre visuel du personnage se situe approximativement a `80 %` de la hauteur jouable.

Imran Adventure conserve cette position cible et ajoute une zone de confort de `70 %` a `84 %`. Cette adaptation absorbe le saut normal de `89 px` et commence a suivre une chute apres environ `43 px` sous la position cible.

## Limites

- La capture ne donne pas acces au code interne de Wonder Boy.
- La mesure porte sur le resultat visuel et non sur une valeur de programmation originale.
- Le decor utilise plusieurs plans, mais les batiments du plan jouable donnent une mesure stable.
- Une petite marge d'environ une image peut subsister au debut ou a la fin de chaque transition.
