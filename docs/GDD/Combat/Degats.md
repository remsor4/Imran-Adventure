# Degats

> **Statut :** Valide

## Objectif

Definir les degats infliges par Imran et la regle generale des degats qu'il recoit.

## Valeurs validees

| Source | Cible | Valeur |
|---|---|---:|
| Attaque normale | Ennemi ou boss | `1 degat` |
| Projectile du Smash Tranchant | Ennemi ou boss | `2 degats` |
| Attaque ennemie ordinaire non bloquee | Imran | `1 coeur` |
| Contact dangereux ordinaire | Imran | `1 coeur` |
| Projectile frontal bloque | Imran | `0 coeur` |

Une attaque future d'ennemi ou de boss utilise `1 coeur` par defaut. Une exception demandant davantage de degats devra etre annoncee et validee explicitement dans la fiche de cette attaque pendant les etapes Ennemis ou Boss.

## Degats infliges par Imran

- Une attaque normale inflige ses degats une seule fois a une meme cible pendant sa fenetre active.
- Le Smash Tranchant inflige ses degats au premier ennemi ou boss touche puis disparait.
- La vitesse, la distance et le moment du contact ne modifient pas les degats.
- Une cible deja vaincue ne peut plus recevoir de degats.
- Les points de vie des ennemis et des boss seront fixes dans leurs etapes respectives.

## Degats recus par Imran

1. Une source dangereuse touche la zone vulnerable d'Imran.
2. Un projectile ennemi frontal verifie d'abord la protection automatique du Bouclier.
3. L'invulnerabilite en cours est ensuite verifiee.
4. Si le contact reste valide, `1 coeur` est retire.
5. L'action en cours est interrompue et la reaction aux degats commence.
6. Le recul et l'invulnerabilite sont appliques.
7. La perte du dernier coeur declenche l'etat `Mort`.

## Sources ordinaires

La regle de `1 coeur` s'applique par defaut :

- aux projectiles non bloques ;
- aux attaques de corps a corps ;
- aux contacts avec un ennemi dangereux ;
- aux pieges et dangers non mortels ;
- aux contacts dangereux pendant un Dash, un saut, une chute ou une attaque.

## Reactions aux impacts

- Une attaque normale reussie produit un impact visuel court et un son d'epee.
- Le Smash Tranchant utilise un impact plus large et un son magique plus marque.
- Un projectile bloque utilise uniquement la lumiere et le son du Bouclier.
- Un degat recu produit le flash, le recul et le son deja valides pour Imran.
- Les effets visuels peuvent continuer apres la fin d'une collision offensive sans appliquer un second degat.

## Cas particuliers

- Plusieurs sources touchant Imran pendant la meme image ne retirent jamais plus de `1 coeur` avant le debut de l'invulnerabilite.
- Un danger continu attend la fin de l'invulnerabilite avant de pouvoir retirer un nouveau coeur.
- Un projectile bloque ne declenche ni degat, ni recul, ni invulnerabilite.
- Une chute hors du niveau ou un danger declare mortel utilise les regles de vies et de reapparition de l'etape 7.
- Pause suspend la resolution temporelle des reactions deja commencees.

## Criteres de validation

Les degats sont valides si :

- l'attaque normale retire `1 point de vie` a sa cible ;
- le Smash Tranchant retire `2 points de vie` a sa cible ;
- une attaque ennemie ordinaire non bloquee retire `1 coeur` a Imran ;
- une meme attaque ne touche jamais deux fois la meme cible pendant une seule fenetre active ;
- un projectile frontal bloque ne retire aucun coeur ;
- les effets d'impact ne produisent aucun degat supplementaire.

## Sources

- [Attaque normale](Attaque-Normale.md)
- [Smash Tranchant](Smash-Tranchant.md)
- [Protection automatique du Bouclier](Blocage.md)
- [Invulnerabilite](Invulnerabilite.md)
- [Recul](Recul.md)
- [Reactions aux degats](../Joueur/Reactions-aux-Degats.md)
