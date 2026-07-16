# Saut

> **Statut :** Valide

## Objectif

Definir un saut precis, modulable et tolerant pour le public cible.

## Declenchement

Le saut commence si :

- Imran touche le sol ;
- ou il a quitte le bord d'une plateforme depuis moins de `0.12 s` ;
- ou une commande de saut conservee depuis moins de `0.12 s` devient valide au contact du sol.

Une seule impulsion est appliquee par pression. Maintenir la commande ne declenche pas plusieurs sauts.

## Valeurs

| Element | Valeur |
|---|---:|
| Impulsion initiale | `480 px/s` vers le haut |
| Gravite pendant la montee | `1300 px/s2` |
| Gravite pendant la chute | `1500 px/s2` |
| Vitesse maximale de chute | `800 px/s` |
| Hauteur maximale visee | Environ `89 px` |
| Temps jusqu'au sommet | Environ `0.37 s` |
| Duree totale visee | Environ `0.71 s` |
| Tolerance apres un bord | `0.12 s` |
| Memoire de saut avant reception | `0.12 s` |

## Hauteur modulable

- Maintenir la commande produit le saut complet.
- Relacher la commande pendant la montee limite la vitesse restante vers le haut a `240 px/s`.
- Une pression courte produit ainsi un saut plus bas sans annuler instantanement la montee.
- Relacher la commande apres le sommet ne modifie pas la chute.

## Sommet et chute

- La gravite plus forte pendant la chute rend les receptions plus lisibles.
- La vitesse de chute ne depasse jamais `800 px/s` hors evenement special valide.
- Le passage de la montee a la chute ne bloque pas le controle horizontal.
- Une animation distincte rend le sommet et la chute faciles a identifier.

## Reception

- Le contact avec une surface praticable termine la periode aerienne.
- La vitesse verticale revient a zero.
- Le Double saut redevient disponible.
- La commande de saut conservee peut declencher immediatement un nouveau saut.
- Une reception normale ne bloque pas le controle.

## Cas particuliers

- Une plateforme traversable est ignoree pendant la montee et devient solide pendant la chute.
- Un plafond annule la vitesse vers le haut et provoque la chute.
- Un degat peut interrompre la montee et appliquer le recul.
- Le saut ne peut pas commencer pendant un etat verrouille ou une interaction.
- La disponibilite du saut pendant une attaque ou un blocage sera definie pendant l'etape 6.

## Criteres de validation

Le saut est valide si :

- une pression effectuee juste avant la reception n'est pas perdue ;
- une pression effectuee juste apres avoir quitte un bord reste acceptee ;
- une pression courte et un maintien produisent deux hauteurs clairement differentes ;
- le sommet et la chute restent faciles a lire ;
- une reception normale rend immediatement le controle ;
- le saut reste identique au clavier et a la manette.

## Sources

- [Statistiques d'Imran](Statistiques-Imran.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Deplacement](Deplacement.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
- [Deplacements du Concept Game](../../Concept-Game/05-Gameplay/Deplacements.md)
