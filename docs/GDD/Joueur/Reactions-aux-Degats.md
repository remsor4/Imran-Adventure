# Reactions aux degats

> **Statut :** Valide

## Objectif

Definir la reaction generale d'Imran apres un degat non bloque. Les degats infliges par chaque source seront definis dans les documents Combat, Ennemis et Boss.

## Sequence d'un degat

1. Une source valide touche la zone vulnerable d'Imran.
2. Si la source est un projectile, la protection automatique du Bouclier est verifiee avant d'appliquer le degat.
3. Si le projectile n'est pas bloque ou si la source est d'un autre type, l'action en cours est interrompue.
4. Le nombre de coeurs correspondant est retire.
5. Imran entre dans l'etat `Degat` pendant `0.20 s`.
6. Le recul horizontal et vertical est applique.
7. Une invulnerabilite de `1.00 s` commence.
8. Si aucun coeur ne reste, Imran passe dans l'etat `Mort`.
9. Sinon, le controle revient apres la reaction de `0.20 s`.

## Recul

| Element | Valeur |
|---|---:|
| Vitesse horizontale initiale | `220 px/s` loin de la source |
| Vitesse verticale initiale | `280 px/s` vers le haut |
| Duree sans controle | `0.20 s` |

- La direction horizontale eloigne Imran de la source du degat.
- Sans source positionnee, le recul utilise la direction opposee a son orientation.
- Un mur peut arreter le recul horizontal.
- Un plafond peut arreter le recul vertical.
- Le recul ne traverse jamais le decor.
- La gravite reprend normalement apres l'impulsion verticale.

## Invulnerabilite

- La duree commence au moment ou le degat est applique.
- Pendant `1.00 s`, une nouvelle source de degat ne retire aucun coeur.
- Une attaque ignoree ne relance pas la duree.
- Imran peut se deplacer et agir apres les `0.20 s` de reaction, pendant le reste de l'invulnerabilite.
- L'invulnerabilite ne permet pas de traverser un mur ou une limite de niveau.
- La mort annule l'invulnerabilite en cours.

## Retours visuels et sonores

- Un flash court confirme le degat initial.
- La silhouette utilise au maximum trois pulsations lentes pendant l'invulnerabilite.
- Aucun clignotement rapide n'est utilise.
- Un son d'impact court accompagne le degat.
- Aucun son en boucle ne joue pendant l'invulnerabilite.
- La perte du dernier coeur utilise un retour distinct avant la perte de vie.

## Projectile bloque automatiquement

Un projectile frontal correctement bloque, meme pendant un mouvement :

- ne retire aucun coeur ;
- ne declenche pas l'invulnerabilite de degat ;
- utilise la reaction propre au bouclier ;
- ne declenche aucun recul de degat ;
- ne coupe pas l'action en cours ;
- fait disparaitre le projectile au point d'impact sans le renvoyer.

## Cas particuliers

- Un danger continu ne peut infliger un nouveau degat qu'apres la fin de l'invulnerabilite.
- Un contact dangereux pendant le Dash applique les memes regles.
- Une chute hors du niveau ou un danger mortel utilise les regles de vies qui seront definies pendant l'etape 7.
- Pause suspend la duree de reaction et l'invulnerabilite.

## Criteres de validation

La reaction est valide si :

- un seul degat est applique pendant la fenetre d'invulnerabilite ;
- le recul eloigne Imran de la source sans traverser le decor ;
- le controle revient avant la fin de l'invulnerabilite ;
- les retours restent lisibles sans clignotement rapide ;
- une protection automatique reussie contre un projectile frontal ne retire aucun coeur, meme pendant un mouvement ;
- Pause ne consomme aucune duree de reaction ou d'invulnerabilite.

## Sources

- [Statistiques d'Imran](Statistiques-Imran.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Coeurs](../../Concept-Game/05-Gameplay/Coeurs.md)
- [Vies](../../Concept-Game/05-Gameplay/Vies.md)
- [Effets visuels](../../Concept-Game/09-Direction-Artistique/Effets-Visuels.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
