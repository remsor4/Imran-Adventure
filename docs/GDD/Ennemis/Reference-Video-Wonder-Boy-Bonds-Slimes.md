# Reference video Wonder Boy - Bond unique des Slimes

> **Statut :** Valide

## Source

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.19-19.18.mp4` | `1920 x 1088` | Environ `60 images/s` | `13.70 s` |

Les bordures de la fenetre et la barre des taches visibles dans la capture ne modifient pas l'observation du mouvement.

## Methode

- La capture complete a ete examinee a `10 images/s` pour suivre les deux ennemis identiques.
- Des cycles representatifs ont ensuite ete examines image par image a `60 images/s`.
- Les poses, les trajectoires et les contacts avec le joueur ont ete compares entre un bond de deplacement et un bond provoquant un degat.

## Observations

- Les ennemis alternent une compression au sol, un etirement vertical, une trajectoire aerienne et une nouvelle compression a l'atterrissage.
- Ce cycle se repete pour avancer meme lorsque le joueur ne se trouve pas au point d'impact.
- Le meme cycle continue lorsque l'ennemi se rapproche du joueur.
- Aucun arret special, aucune charge distincte et aucun bond plus grand ne precedent le contact offensif.
- Lorsqu'un ennemi en retombee touche le joueur, le joueur subit sa reaction de degat normale.
- L'ennemi conserve le meme aspect et la meme logique de trajectoire avant ce contact.
- Les deux ennemis peuvent executer ce cycle simultanement.

## Regle retenue pour Imran Adventure

- Le Slime utilise un seul type de bond pour le deplacement et l'attaque.
- La compression au sol et le son du rebond annoncent chaque depart.
- Le bond ne devient pas plus haut ou plus long uniquement parce qu'Imran est vise.
- Le Slime utilise ce meme cycle dans le sens courant de sa patrouille sans recalculer sa direction vers Imran.
- Une zone predeterminee limite son deplacement et provoque son changement de sens a son extremite.
- Le contact avec le corps du Slime pendant ce mouvement inflige le degat ordinaire de `1 coeur`.
- Aucun etat de grand bond offensif distinct n'est ajoute.
- La phase au sol est limitee a une compression de `0.10 s`, sans pause supplementaire.
- La phase aerienne dure `0.72 s`, pour un cycle complet de `0.82 s`.
- Le bond normalise atteint `144 px` de haut et parcourt `112 px` horizontalement.

## Limites

- La capture valide la structure commune du bond, mais ne donne pas acces aux valeurs internes de Wonder Boy.
- Les valeurs retenues sont des mesures visuelles normalisees pour les dimensions propres a Imran Adventure et non les valeurs internes de Wonder Boy.
- Cette capture ne mesure pas la distance de detection ni les points de vie du Slime ; ces elements sont definis separement dans la fiche du Slime.
- Le comportement contre un mur ou un plafond devra etre defini separement.

## Sources internes

- [Slimes](Slimes.md)
- [Regles communes des ennemis](Regles-Communes.md)
- [Reference video des collisions entre ennemis](Reference-Video-Wonder-Boy-Collisions-Ennemis.md)
- [Degats](../Combat/Degats.md)
