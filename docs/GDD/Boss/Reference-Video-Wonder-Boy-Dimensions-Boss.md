# Reference video Wonder Boy - Dimensions des boss

> **Statut :** Valide

## Sources

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.25-03.48.mp4` | `1920 x 1088` | Environ `60 images/s` | `57.03 s` |
| `Wonder Boy The Dragon's Trap_2026.07.25-03.46.mp4` | `1920 x 1088` | Environ `60 images/s` | `21.57 s` |

## Methode

- Des images ont ete extraites lorsque le personnage et le boss etaient entierement visibles.
- La hauteur du personnage sert d'unite commune afin d'ignorer la taille de la fenetre d'enregistrement.
- La largeur et la hauteur visibles des boss ont ete comparees a cette unite.
- Les animations deformant temporairement la silhouette ont ete comparees sur plusieurs images.
- Les rapports ont ensuite ete appliques a la hauteur visuelle de reference d'Imran, fixee a `64 px`.
- Les resultats ont ete arrondis a des multiples de `8 px` pour obtenir des dimensions de production simples.

## Mesures approximatives

| Element mesure | Personnage | Boss | Rapport |
|---|---:|---:|---:|
| Hauteur dans les images lisibles | Environ `160 px` | Environ `360 a 375 px` | Environ `2.25 a 2.35` |
| Largeur du boss comparee a la hauteur du personnage | `160 px` comme unite | Environ `360 px` | Environ `2.25` |

Les captures montrent donc des boss presque aussi larges que hauts, avec une hauteur legerement superieure a leur largeur.

## Valeur retenue pour Imran Adventure

| Element | Valeur |
|---|---:|
| Largeur visuelle commune d'un golem | `144 px` |
| Hauteur visuelle commune d'un golem | `152 px` |
| Enveloppe visuelle commune | `144 x 152 px` |
| Rapport de hauteur avec Imran | `2.375` |

Cette valeur reste proche de la description du Concept Game indiquant environ deux fois et demie la taille d'Imran, tout en suivant plus precisement les proportions mesurees dans les captures.

## Limites

- Les captures montrent des boss de Wonder Boy et non les golems definitifs d'Imran Adventure.
- Les poses, les ailes, les queues, les armes et les effets peuvent depasser temporairement l'enveloppe commune.
- L'enveloppe visuelle ne constitue pas une zone de collision.
- Les dimensions de collision, de contact dangereux et de vulnerabilite de la tete doivent etre fixees separement.

## Sources internes

- [Regles communes des boss](Regles-Communes.md)
- [Statistiques d'Imran](../Joueur/Statistiques-Imran.md)
- [Principes des golems](../../Concept-Game/08-Boss/Principes-des-Golems.md)
