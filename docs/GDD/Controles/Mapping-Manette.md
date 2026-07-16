# Mapping manette

> **Statut :** Valide

## Objectif

Definir des commandes par defaut identiques dans leur position generale sur les principales manettes PC.

Les noms Xbox et PlayStation servent uniquement d'exemples. Le jeu affiche l'icone correspondant au dernier appareil utilise.

## Gameplay

| Action | Position standard | Exemple Xbox | Exemple PlayStation | Type d'entree |
|---|---|---|---|---|
| Se deplacer | Stick gauche ou croix directionnelle | Stick gauche ou D-pad | Stick gauche ou croix | Maintenue |
| Sauter | Bouton bas | `A` | `Croix` | Pression |
| Double saut | Bouton bas | `A` | `Croix` | Seconde pression en l'air apres deblocage |
| Dash | Bouton droit | `B` | `Rond` | Pression apres deblocage |
| Attaque normale | Bouton gauche | `X` | `Carre` | Pression courte |
| Charger le Smash Tranchant | Bouton gauche | `X` | `Carre` | Maintien puis relachement |
| Bloquer | Gachette gauche | `LT` | `L2` | Maintenue |
| Interagir | Bouton haut | `Y` | `Triangle` | Pression pres d'un element interactif |
| Pause | Bouton Menu | `Menu` | `Options` | Pression |

Le stick gauche ne modifie pas la vitesse d'Imran. Une inclinaison suffisante vers la gauche ou la droite produit la meme vitesse constante que la croix directionnelle.

## Menus

| Action | Commande |
|---|---|
| Naviguer | Stick gauche ou croix directionnelle |
| Confirmer | Bouton bas : `A` ou `Croix` |
| Retour | Bouton droit : `B` ou `Rond` |
| Ouvrir ou fermer Pause | Bouton `Menu` ou `Options` |

Le bouton droit sert au Dash pendant le gameplay et au retour dans les menus. Les contextes ne sont jamais actifs simultanement.

## Capacites verrouillees

- Le Dash conserve son bouton avant et apres son deblocage.
- Le Double saut partage toujours le bouton du saut.
- Une commande verrouillee ne produit aucune action de gameplay.
- Un message de deblocage affiche l'icone adaptee a la manette active.

## Cas particuliers

- Des directions opposees sur le stick ou la croix produisent une direction horizontale neutre.
- Une entree maintenue pendant une cinematique doit etre relachee avant de pouvoir declencher une action.
- Si la manette est deconnectee, le jeu ouvre Pause et affiche un message clair.
- Le joueur peut reprendre avec le clavier ou reconnecter une manette.
- Une manette reconnectee peut etre utilisee sans redemarrer le jeu.

## Criteres de validation

Le mapping manette est valide si :

- toutes les actions essentielles sont accessibles ;
- toute l'aventure peut etre terminee sans clavier ni souris ;
- les boutons de saut, attaque, Dash, blocage et interaction sont distincts ;
- le stick et la croix directionnelle permettent les memes deplacements ;
- les icones correspondent au dernier appareil utilise ;
- la deconnexion ne laisse jamais Imran sans controle pendant une action en cours.

## Sources

- [Deplacements](../../Concept-Game/05-Gameplay/Deplacements.md)
- [Dash](../../Concept-Game/05-Gameplay/Dash.md)
- [Double saut](../../Concept-Game/05-Gameplay/Double-Saut.md)
- [Combat](../../Concept-Game/05-Gameplay/Combat.md)
- [Smash Tranchant](../../Concept-Game/05-Gameplay/Smash-Tranchant.md)
- [Bouclier de lumiere](../../Concept-Game/05-Gameplay/Bouclier-de-Lumiere.md)
- [Coffres](../../Concept-Game/05-Gameplay/Coffres.md)
- [Options](../../Concept-Game/11-Interface/Options.md)
