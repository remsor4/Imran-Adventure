# Recul

> **Statut :** Valide

## Objectif

Definir le mouvement impose a Imran apres un degat non bloque et les limites de ce mouvement.

## Valeurs validees

| Element | Valeur |
|---|---:|
| Vitesse horizontale initiale | `220 px/s` loin de la source |
| Vitesse verticale initiale | `280 px/s` vers le haut |
| Duree sans controle | `0.20 s` |

## Declenchement

- Le recul commence sur la meme image que la perte du coeur.
- L'action en cours est interrompue avant l'application des vitesses de recul.
- La direction horizontale eloigne Imran du centre de la source du degat.
- Si la source ne possede aucune position exploitable, le recul utilise la direction opposee a l'orientation d'Imran.
- Un projectile bloque par le Bouclier ne declenche aucun recul.

## Controle pendant le recul

- Les commandes gauche, droite, saut, Double saut, Dash, attaque et interaction sont ignorees pendant `0.20 s`.
- L'orientation d'Imran ne change pas automatiquement pendant la reaction.
- Le controle revient a la fin des `0.20 s` si Imran n'est ni mort, ni verrouille.
- L'invulnerabilite continue pendant `0.80 s` apres ce retour du controle.

## Collisions et gravite

- Un mur solide annule la partie horizontale du recul sans etre traverse.
- Un plafond annule la vitesse verticale vers le haut et declenche la chute.
- Le sol arrete la chute normalement.
- La gravite s'applique apres l'impulsion verticale selon les valeurs habituelles du joueur.
- Un recul commence au sol peut soulever Imran.
- Un recul commence dans les airs remplace les vitesses actuelles par les valeurs validees.
- Le recul ne traverse jamais le decor, un ennemi solide ou une limite de niveau.

## Interruptions

- Un degat non bloque interrompt une attaque normale, une charge, un lancement de Smash, un Dash ou une interaction interruptible.
- Le projectile d'un Smash deja cree continue son trajet meme si Imran subit ensuite un degat.
- La mort remplace immediatement le recul par l'etat `Mort`.
- Pause suspend le mouvement et la duree restante.

## Retour visuel et sonore

- Une pose distincte montre clairement la direction du choc.
- Un flash court et un son d'impact accompagnent la perte du coeur.
- Aucun effet ne doit masquer la position de reception d'Imran.

## Criteres de validation

Le recul est valide si :

- Imran est pousse loin de la source ;
- le joueur perd le controle pendant exactement `0.20 s` ;
- un mur ou un plafond arrete la composante correspondante ;
- le decor n'est jamais traverse ;
- un projectile bloque ne produit aucun recul ;
- le controle revient avant la fin de l'invulnerabilite.

## Sources

- [Degats](Degats.md)
- [Invulnerabilite](Invulnerabilite.md)
- [Reactions aux degats](../Joueur/Reactions-aux-Degats.md)
- [Statistiques d'Imran](../Joueur/Statistiques-Imran.md)
