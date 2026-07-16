# Dash

> **Statut :** Valide

## Objectif

Definir un deplacement horizontal court et rapide au sol, obtenu apres le deuxieme golem.

## Deblocage

- Le Dash devient disponible apres la recuperation de la deuxieme cle.
- Sa commande peut etre consultee et remappee avant son deblocage.
- Avant le deblocage, utiliser la commande ne produit aucune action.
- Le message de deblocage rappelle la commande de l'appareil actif.

## Declenchement

Le Dash peut commencer :

- uniquement lorsque Imran touche une surface praticable ;
- si le delai du Dash precedent est termine ;
- si Imran n'est pas dans un etat incompatible.

Le Dash se dirige vers la direction horizontale maintenue. Sans direction, il utilise l'orientation actuelle d'Imran.

Une commande utilisee dans les airs est ignoree. Elle n'est pas memorisee pour declencher un Dash lors de la reception.

## Valeurs

| Element | Valeur |
|---|---:|
| Vitesse | `620 px/s` |
| Duree | `0.20 s` |
| Distance theorique sans obstacle | Environ `124 px` |
| Intervalle entre deux declenchements | `1.00 s` mesure depuis le debut du Dash |
| Delai restant apres la fin du Dash | `0.80 s` |
| Disponibilite | Au sol uniquement |

## Comportement horizontal

- La vitesse horizontale normale est remplacee par la vitesse du Dash.
- La direction ne peut pas changer pendant les `0.20 s`.
- Relacher la commande de direction ne raccourcit pas le Dash.
- A la fin, Imran conserve au maximum sa vitesse horizontale normale dans la direction du Dash.

## Contact avec le sol

- Le Dash ne peut pas commencer pendant un saut ou une chute.
- Le contact avec une pente praticable reste considere comme un contact au sol.
- Si Imran quitte sa surface d'appui pendant le Dash, le Dash est interrompu immediatement.
- Apres cette interruption, la gravite et les regles normales de chute s'appliquent.

## Limites et collisions

- Le Dash ne rend pas Imran invulnerable.
- Un mur solide interrompt immediatement le Dash.
- Imran ne traverse ni un ennemi solide, ni un danger, ni une limite de niveau.
- Un contact dangereux pendant le Dash peut infliger un degat et declencher un recul.
- Le Dash ne peut pas commencer pendant une attaque, une charge, un blocage, une interaction, un degat, une mort ou un etat verrouille.
- Une commande de Dash recue dans les airs ne produit aucun mouvement, effet ou son complet.

## Reutilisation

- Au sol, un nouveau Dash demande que `1.00 s` se soit ecoulee depuis le debut du Dash precedent.
- Une reapparition restaure le Dash et termine tout delai actif.

## Retours au joueur

- Une pose claire indique le debut et la direction du Dash.
- Une trainee courte suit Imran sans masquer les dangers.
- Un son bref confirme le declenchement.
- Une commande refusee ne joue pas l'effet complet du Dash.

## Criteres de validation

Le Dash est valide si :

- il parcourt environ deux grilles logiques sans obstacle ;
- sa direction est comprise avant la fin du mouvement ;
- il fonctionne uniquement lorsque Imran touche une surface praticable ;
- une commande recue pendant un saut ou une chute ne declenche rien ;
- quitter une plateforme interrompt immediatement le Dash et declenche la chute normale ;
- un mur l'arrete sans vibration ni traverser le decor ;
- il ne procure aucune invulnerabilite ;
- une commande aerienne n'est pas memorisee jusqu'a la reception.

## Sources

- [Statistiques d'Imran](Statistiques-Imran.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Deplacement](Deplacement.md)
- [Saut](Saut.md)
- [Double saut](Double-Saut.md)
- [Reference video du Dash Godot](Reference-Video-Dash-Godot.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Dash du Concept Game](../../Concept-Game/05-Gameplay/Dash.md)
