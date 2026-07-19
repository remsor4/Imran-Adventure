# Reference video Wonder Boy - Collisions entre ennemis

> **Statut :** Valide

## Source

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.19-18.51.mp4` | `1920 x 1088` | Environ `60 images/s` | `21.72 s` |

Les bordures de la fenetre et la barre des taches visibles dans la capture ne modifient pas l'observation des collisions.

## Methode

- La capture complete a ete examinee a basse frequence pour localiser les rencontres entre ennemis.
- Deux passages representatifs ont ensuite ete examines image par image a `60 images/s`.
- Le mouvement, la trajectoire et la reaction de chaque ennemi ont ete compares avant, pendant et apres la superposition.

## Passages observes

### Deux Slimes

- Vers `3.82 s`, deux Slimes se rapprochent dans des directions opposees.
- Leurs silhouettes commencent a se superposer sans ralentissement visible.
- Pendant plusieurs images, leurs corps occupent presque exactement le meme espace.
- Vers `4.43 s`, ils se separent en conservant leur mouvement.
- Aucun arret, recul, changement de direction ou degat n'est observe.

### Ennemis de familles differentes

- Vers `16.02 s`, un ennemi bleu et un Slime vert occupent la meme zone pendant leurs mouvements.
- Les silhouettes se chevauchent pendant leur trajectoire et leur saut.
- Vers `16.38 s`, ils se separent sans collision physique visible.
- Aucun ennemi ne pousse, ne bloque, ne blesse ou n'interrompt l'autre.

## Regle retenue pour Imran Adventure

- Les ennemis ordinaires ne sont pas solides entre eux.
- Ils peuvent se traverser et se superposer, quelle que soit leur famille.
- Leur vitesse, leur direction et leur action en cours ne sont pas modifiees par cette superposition.
- Un simple contact entre ennemis ne produit aucun degat ni aucune reaction.
- Le placement des rencontres doit eviter les superpositions prolongees qui rendraient les silhouettes illisibles.

## Limites

- La capture valide uniquement les collisions physiques et les contacts entre ennemis.
- Elle ne montre pas clairement un projectile ennemi touchant un autre ennemi.
- Elle ne permet donc pas encore de fixer les regles de degats entre attaques ennemies.
- Les collisions avec les murs, les sols, les plateformes et les limites de rencontre doivent etre definies separement.

## Sources internes

- [Regles communes des ennemis](Regles-Communes.md)
- [Reference video des reactions ennemies](Reference-Video-Wonder-Boy-Reactions-Ennemies.md)
- [Degats](../Combat/Degats.md)
