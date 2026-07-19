# Reference video Wonder Boy - Detection horizontale des Slimes

> **Statut :** Valide

## Source

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.19-20.25.mp4` | `1920 x 1088` | Environ `60 images/s` | `31.27 s` |

La capture montre plusieurs approches horizontales sur un terrain plat. Les bordures de la fenetre et la barre des taches ne modifient pas la mesure horizontale.

## Methode

- La capture complete a d'abord ete examinee a `1 image/s` pour localiser les approches du joueur.
- La premiere activation exploitable a ensuite ete examinee a `10 images/s`, puis image par image a `60 images/s`.
- La derniere pose d'attente du Slime et la premiere compression active ont ete comparees.
- La distance horizontale a ete mesuree entre le centre du joueur et le centre du Slime.

## Observations

- Le Slime est encore au repos vers `3.38 s`.
- Sa premiere compression active apparait vers `3.40 s`.
- La camera reste pratiquement immobile pendant ce passage.
- Imran et le Slime se trouvent sur le meme sol et disposent d'une ligne de vue libre.
- La distance entre leurs centres au seuil d'activation est comprise entre environ `790 px` et `800 px`.

## Regle retenue pour Imran Adventure

- La distance maximale de detection horizontale du Slime est arrondie a `800 px`.
- Imran doit aussi se trouver a `240 px` ou moins verticalement du Slime.
- Le Slime doit etre visible a l'ecran et posseder une ligne de vue libre.
- Toutes les conditions doivent etre reunies avant le debut de la compression active.

## Limites

- La capture ne montre aucune activation entre deux plateformes.
- La valeur verticale de `240 px` est donc une valeur de conception validee pour Imran Adventure et non une mesure de Wonder Boy.
- Les valeurs devront etre confirmees par un test de lisibilite dans le prototype en `1920 x 1080`.

## Sources internes

- [Slimes](Slimes.md)
- [Regles communes des ennemis](Regles-Communes.md)
- [Reference video du bond unique](Reference-Video-Wonder-Boy-Bonds-Slimes.md)
