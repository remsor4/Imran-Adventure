# Game Over

> **Statut :** Valide

## Objectif

Definir le resultat previsible de la perte de la derniere vie et permettre au joueur de reprendre sans sanction permanente supplementaire.

## Declenchement

- Le Game Over se declenche lorsque Imran perd son dernier coeur alors que son compteur ne contient plus qu'une vie.
- Le dernier coeur et la derniere vie passent a `0`.
- L'etat `Mort` interrompt le gameplay et toutes les commandes en cours.
- La reaction de defaite se termine avant l'ouverture de l'ecran Game Over.
- Le HUD disparait et aucune sauvegarde automatique n'est creee.
- Aucune entree maintenue avant l'ouverture de l'ecran ne peut choisir une action automatiquement.

## Actions disponibles

L'ecran propose exactement deux actions :

1. `Recommencer le niveau` ;
2. `Retour au menu principal`.

`Recommencer le niveau` possede le focus initial. L'ecran reste affiche sans compte a rebours jusqu'a une action volontaire du joueur.

## Recommencer le niveau

Apres validation de cette action :

- la sequence jouable en cours est rechargee depuis son debut ;
- Imran recommence avec `3 coeurs` et `3 vies` ;
- le checkpoint temporaire de la tentative perdue est desactive ;
- les ennemis, dangers, objets et combats de boss de la sequence reviennent a leur etat initial ;
- les activations de pancartes, de feux de camp et les autres progres temporaires de la tentative sont oublies ;
- la progression non sauvegardee dans le niveau est perdue ;
- les niveaux termines et les cles deja sauvegardees restent conserves ;
- le Dash et le Double saut restent disponibles, car ils le sont depuis le debut de l'aventure ;
- la musique de la sequence recommence depuis son introduction.

Le debut de la sequence depend du contexte :

| Contexte du Game Over | Point de reprise |
|---|---|
| Niveau 0 | Debut du tutoriel au Village des Bles |
| Niveau principal | Debut du niveau principal en cours |
| Combat final | Devant la porte du donjon, avant Tata Lisa |

## Retour au menu principal

Apres validation de cette action :

- le menu principal est affiche sans creer de sauvegarde ;
- la derniere sauvegarde permanente valide reste intacte ;
- `Continuer` recoit le focus si une sauvegarde existe ;
- une reprise ulterieure charge le point permanent enregistre, jamais le checkpoint temporaire perdu.

## Cas particuliers

- Un Game Over dans le niveau 0 recommence toujours le tutoriel depuis son debut.
- Un Game Over dans un niveau principal oublie toujours sa pancarte de controle temporaire.
- Un Game Over pendant un combat de golem recommence le niveau principal, pas seulement le combat.
- Un Game Over contre Tata Lisa conserve les six cles sauvegardees et replace Imran devant la porte du donjon.
- Le feu de camp utilise avant le Game Over ne cree aucun point de reprise et ne restaure aucune vie.
- Fermer le jeu depuis l'ecran Game Over produit le meme point de reprise que la derniere sauvegarde permanente.

## Criteres de validation

Le Game Over est valide si :

- il apparait uniquement apres la perte de la derniere vie ;
- aucune sauvegarde automatique ne se declenche lors de son ouverture ;
- aucune entree maintenue ne choisit une action sans validation volontaire ;
- recommencer rend exactement `3 coeurs` et `3 vies` ;
- le checkpoint et tous les progres temporaires de la tentative sont oublies ;
- les cles et les niveaux deja sauvegardes restent conserves ;
- chaque contexte possede un point de reprise unique ;
- le joueur peut toujours revenir au menu principal.

## Sources

- [Game Over du Concept Game](../../Concept-Game/05-Gameplay/Game-Over.md)
- [Ecran Game Over](../../Concept-Game/11-Interface/Game-Over.md)
- [Vies](../../Concept-Game/05-Gameplay/Vies.md)
- [Checkpoints du Concept Game](../../Concept-Game/06-Systemes/Checkpoints.md)
- [Sauvegarde du Concept Game](../../Concept-Game/06-Systemes/Sauvegarde.md)
- [Coeurs et vies](Coeurs-et-Vies.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
