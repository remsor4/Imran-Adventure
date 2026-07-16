# Reference video du combat Wonder Boy

> **Statut :** Valide

## Source

- Jeu observe : *Wonder Boy: The Dragon's Trap*.
- Capture locale fournie par Rems le 17 juillet 2026.
- Fichier analyse : `Wonder Boy The Dragon's Trap_2026.07.17-00.57.mp4`.
- Flux analyse : `1920 x 1088`, `60 images/s`.
- Methode : lecture image par image des attaques sans contact, des impacts, de l'epee et du Bouclier.

La capture comprend les limites de la fenetre du jeu. Elle sert a mesurer des rapports visuels et temporels, pas a imposer sa resolution brute au projet.

## Mesures retenues

| Element observe | Rapport approximatif | Cible normalisee pour Imran |
|---|---:|---:|
| Hauteur visuelle du personnage | Reference de comparaison | `64 px` |
| Portee du centre a la pointe pendant le coup | Environ `75 %` de la hauteur | `48 px` |
| Longueur totale de l'epee au repos | Environ `85 %` a `90 %` de la hauteur | `56 px` |
| Hauteur du bouclier | Environ `40 %` a `45 %` de la hauteur | `28 px` |
| Largeur du bouclier | Environ `25 %` a `30 %` de la hauteur | `20 px` |
| Duree visuelle du coup sans impact | Environ `0.32 s` a `0.35 s` | `0.35 s` |
| Premier impact apres le debut offensif | Environ `0.067 s` a `0.083 s` | Fenetre active de `0.10 s` |

## Consequences pour le GDD

- La Shadow Sword mesure `56 px` de la pointe au pommeau et `16 px` au maximum au niveau de la garde.
- Le Bouclier de lumiere est affiche en `20 x 28 px`.
- La lame atteint `48 px` depuis le centre d'Imran.
- L'attaque normale dure `0.35 s` avec une collision offensive active pendant `0.10 s`.
- Une rotation ou une perspective peut raccourcir visuellement l'epee pendant certaines images sans modifier sa portee de gameplay.

## Limites

- La capture ne donne pas acces aux colliders ni au code du jeu de reference.
- Les mesures reposent sur les pixels visibles et restent donc approximatives.
- Les valeurs sont arrondies pour respecter la grille logique de `64 px` du projet.
- Leur confort final devra etre confirme dans le prototype Godot a `1920 x 1080`.

## Criteres de validation

La reference est correctement appliquee si :

- la lame visible et sa portee offensive restent synchronisees ;
- le Bouclier couvre le torse sans masquer la posture d'Imran ;
- l'attaque conserve un rythme proche de la capture ;
- les proportions restent lisibles dans les poses au sol et aeriennes.

## Sources

- [Attaque normale](Attaque-Normale.md)
- [Protection automatique du Bouclier](Blocage.md)
- [Statistiques d'Imran](../Joueur/Statistiques-Imran.md)
