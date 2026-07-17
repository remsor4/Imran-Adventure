# Mapping clavier

> **Statut :** Valide

## Objectif

Definir les commandes clavier par defaut pour le gameplay et les menus sur un clavier AZERTY, avec les fleches comme alternative de deplacement.

## Gameplay

| Action | Commande principale | Commande secondaire | Type d'entree |
|---|---|---|---|
| Aller a gauche | `Q` | `Fleche gauche` | Maintenue |
| Aller a droite | `D` | `Fleche droite` | Maintenue |
| Sauter | `Espace` | Aucune | Pression |
| Double saut | `Espace` | Aucune | Seconde pression en l'air |
| Dash | `Maj gauche` | Aucune | Pression au sol |
| Attaque normale | `J` | Aucune | Pression courte |
| Charger le Smash Tranchant | `J` | Aucune | Maintien puis relachement |
| Interagir | `E` | Aucune | Pression pres d'un element interactif |
| Pause | `Echap` | Aucune | Pression |

Il n'existe aucune commande de course. Imran conserve la vitesse de deplacement definie par les regles du joueur.

Le Double saut partage la commande du saut. Le Smash Tranchant partage la commande de l'attaque normale.

La commande `Interaction` sert notamment a ouvrir un coffre, a utiliser volontairement un feu de camp et a ouvrir les six verrous du donjon apres Tata Lisa. La proximite d'un feu ne declenche jamais le soin automatiquement.

Le Bouclier de lumiere ne possede aucune commande. Il bloque automatiquement un projectile ennemi venant du cote vers lequel Imran regarde, meme pendant un mouvement.

## Menus

| Action | Commande principale | Commande secondaire |
|---|---|---|
| Monter | `Fleche haut` | `Z` |
| Descendre | `Fleche bas` | `S` |
| Aller a gauche | `Fleche gauche` | `Q` |
| Aller a droite | `Fleche droite` | `D` |
| Confirmer | `Entree` | `Espace` |
| Retour | `Echap` | `Retour arriere` |
| Ouvrir ou fermer Pause | `Echap` | Aucune |

Les memes touches peuvent remplir des fonctions differentes dans le contexte `Gameplay` et le contexte `Menu`. Les deux contextes ne sont jamais actifs simultanement.

## Souris

La souris peut :

- deplacer le focus sur un bouton ;
- confirmer avec le clic gauche ;
- modifier un curseur ou une option compatible.

Aucune action essentielle du gameplay ne depend de la souris.

## Capacites disponibles

- Le Dash est utilisable et remappable des le debut de l'aventure.
- La commande du Double saut reste celle du saut et ne possede pas une ligne de remappage separee.
- Les pancartes du niveau 0 affichent les commandes correspondant au dernier appareil utilise.

## Cas particuliers

- Maintenir gauche et droite en meme temps produit une direction horizontale neutre.
- Une touche maintenue avant la fin d'une cinematique ne declenche pas automatiquement une action au retour du controle.
- `Echap` ne ferme pas le jeu directement pendant le gameplay.
- Si un champ de remappage attend une touche, `Echap` annule la saisie au lieu d'ouvrir Pause.
- Les commandes de menu restent disponibles meme si une commande de gameplay est mal configuree.

## Criteres de validation

Le mapping clavier est valide si :

- toutes les actions essentielles possedent une touche ;
- toute l'aventure peut etre terminee sans souris ;
- les commandes principales sont utilisables sur un clavier AZERTY ;
- les fleches permettent un deplacement alternatif ;
- le saut et le Double saut utilisent la meme touche ;
- l'attaque normale et le Smash Tranchant utilisent la meme touche ;
- aucun conflit non signale ne peut etre valide dans un meme contexte.

## Sources

- [Deplacements](../../Concept-Game/05-Gameplay/Deplacements.md)
- [Dash](../../Concept-Game/05-Gameplay/Dash.md)
- [Double saut](../../Concept-Game/05-Gameplay/Double-Saut.md)
- [Combat](../../Concept-Game/05-Gameplay/Combat.md)
- [Smash Tranchant](../../Concept-Game/05-Gameplay/Smash-Tranchant.md)
- [Bouclier de lumiere](../../Concept-Game/05-Gameplay/Bouclier-de-Lumiere.md)
- [Coffres](../../Concept-Game/05-Gameplay/Coffres.md)
- [Feux de camp](../../Concept-Game/05-Gameplay/Feux-de-Camp.md)
- [Options](../../Concept-Game/11-Interface/Options.md)
