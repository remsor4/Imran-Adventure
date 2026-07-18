# Reference video Wonder Boy - Degats recus par Imran

> **Statut :** Valide

## Sources

| Capture | Situation observee | Resolution | Frequence | Duree |
|---|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.18-04.23_clip_1.mp4` | Degats de contact a l'arret et en mouvement | `1920 x 1088` | Environ `60 images/s` | `26.98 s` |
| `Wonder Boy The Dragon's Trap_2026.07.18-04.26.mp4` | Degats provoques par un projectile | `1920 x 1088` | Environ `60 images/s` | `9.08 s` |
| `Wonder Boy The Dragon's Trap_2026.07.18-04.27.mp4` | Degats recus pendant un saut | `1920 x 1088` | Environ `60 images/s` | `11.10 s` |

Les bordures de la fenetre et la barre des taches visibles dans les captures ne modifient pas les mesures temporelles.

## Methode

- Les impacts ont ete examines image par image a partir des captures a `60 images/s`.
- Le debut de la reaction correspond au premier flash et a l'entree dans la pose de degat.
- La fin de la reaction correspond au retour a une pose controlable.
- La fin de l'invulnerabilite correspond au retour stable de la silhouette apres le dernier clignotement de la reference.
- Le deplacement avant et apres un impact aerien a ete compare pour identifier le remplacement de la trajectoire.

## Mesures observees

| Situation | Reaction visible | Invulnerabilite visible | Comportement principal |
|---|---:|---:|---|
| Contact a l'arret ou en mouvement | Environ `0.30 s` | Environ `1.27 a 1.30 s` | Interruption des commandes et recul loin de la source |
| Projectile non bloque | Environ `0.33 s` | Environ `1.25 a 1.30 s` | Meme reaction qu'un contact, puis disparition du projectile |
| Impact pendant un saut | Environ `0.33 s` | Environ `1.30 s` | Trajectoire interrompue, recul horizontal puis retombee |

La marge entre `0.30 s` et `0.33 s` correspond a environ deux images a `60 images/s` et au changement de pose pendant le flash d'impact.

## Valeurs retenues pour Imran Adventure

| Element | Valeur validee |
|---|---:|
| Duree de la reaction sans controle | `0.33 s` |
| Duree totale d'invulnerabilite | `1.30 s` |
| Temps d'invulnerabilite restant avec controle | `0.97 s` |
| Vitesse horizontale initiale | `220 px/s` loin de la source |
| Vitesse verticale initiale au sol | `280 px/s` vers le haut |
| Vitesse verticale initiale dans les airs | `0 px/s`, puis reprise de la gravite |

La duree de `0.33 s` conserve le resultat commun aux impacts de contact, de projectile et aux impacts aeriens. La protection de `1.30 s` retient la valeur haute observee afin d'eviter deux pertes de coeur trop rapprochees.

Les vitesses en `px/s` ne peuvent pas etre copiees directement depuis la video, car l'echelle du personnage et le cadrage different. La valeur horizontale de `220 px/s` et l'impulsion terrestre de `280 px/s` restent donc des valeurs de prototype validees. Leur confort devra etre confirme dans Godot sans modifier les durees retenues sans nouvelle validation.

## Regle du projectile non bloque

- Un projectile non bloque retire son degat normal.
- Il declenche la meme reaction de `0.33 s` et la meme invulnerabilite de `1.30 s` qu'une autre source ordinaire.
- Le recul horizontal eloigne Imran de la source du projectile.
- Le projectile disparait au point d'impact apres avoir applique son unique degat.
- Un projectile bloque par le Bouclier conserve les regles distinctes du document Blocage.

## Regle du degat aerien

- Un impact pendant un saut ou une chute interrompt la trajectoire verticale en cours.
- Le recul horizontal de `220 px/s` eloigne Imran de la source.
- La vitesse verticale actuelle est annulee.
- Aucune nouvelle impulsion vers le haut n'est ajoutee.
- La gravite reprend immediatement et Imran retombe.
- Les commandes restent ignorees pendant les `0.33 s` de reaction.

## Adaptation visuelle

Wonder Boy utilise un clignotement rapide pendant l'invulnerabilite. Imran Adventure conserve le choix deja valide de trois pulsations lentes au maximum afin de rendre la protection lisible sans effet visuel agressif.

## Limites

- Les mesures de temps possedent une marge d'environ une ou deux images.
- Les captures montrent le resultat visible et ne donnent pas acces au code de Wonder Boy.
- Les vitesses de recul devront etre testees avec les collisions, la gravite et les animations propres a Imran Adventure.
- Une modification future de ces valeurs demandera un test dans le prototype puis une nouvelle validation.

## Sources internes

- [Reactions aux degats](Reactions-aux-Degats.md)
- [Saut](Saut.md)
- [Statistiques d'Imran](Statistiques-Imran.md)
- [Degats](../Combat/Degats.md)
- [Recul](../Combat/Recul.md)
- [Invulnerabilite](../Combat/Invulnerabilite.md)
- [Protection automatique du Bouclier](../Combat/Blocage.md)
