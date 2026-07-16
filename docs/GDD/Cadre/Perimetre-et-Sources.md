# Perimetre et sources

> **Statut :** Valide

## Hierarchie documentaire

| Document | Question principale | Contenu |
|---|---|---|
| [Concept Game](../../Concept-Game/README.md) | Quel jeu voulons-nous creer ? | Vision, identite, public, univers, histoire, principes de gameplay, art, son et interface |
| [GDD](../README.md) | Comment le jeu doit-il fonctionner ? | Regles, comportements, valeurs, niveaux, equilibrage, retours au joueur et criteres de validation |
| [TDD](../../TDD/README.md) | Comment le jeu sera-t-il construit dans Godot ? | Architecture, scenes, noeuds, scripts, signaux, ressources, donnees et tests techniques |

## Source de verite

- Le Concept Game est la source de verite pour la vision creative.
- Le GDD est la source de verite pour le fonctionnement du jeu.
- Le TDD est la source de verite pour l'implementation dans Godot.
- Le dossier `assets` contient les ressources visuelles et sonores validees.
- Le projet Godot contient les scenes, ressources et scripts executables.

Si deux documents se contredisent, la modification est suspendue jusqu'a ce que la source de verite concernee soit corrigee et validee.

## Frontiere entre les documents

| Sujet | Concept Game | GDD | TDD |
|---|---|---|---|
| Coeurs | Imran possede trois coeurs | Perte, recuperation, degats, invulnerabilite et affichage | Variables, signaux, noeuds et sauvegarde de la valeur |
| Dash | Capacite de deplacement rapide | Vitesse, duree, distance, recharge et restrictions | Script, machine a etats, collisions et effets appeles |
| Boss | Barre de vie en haut au centre | Conditions d'affichage, valeurs, phases et transitions | Scene UI, ancrages, signaux et mise a jour de la barre |
| Cinematique | Evenements racontes | Plans, dialogues, durees, passage et reprise du controle | Scenes Godot, AnimationPlayer, Camera2D et scripts |
| Niveau | Theme et ordre des regions | Parcours, obstacles, ennemis, checkpoint, boss et recompense | Scenes, TileMap, collisions, chargement et ressources |

## Perimetre du GDD

Le GDD contient :

- les controles et les priorites des actions ;
- les regles du joueur ;
- le combat et les equipements ;
- les ennemis et les boss ;
- les niveaux et leur progression ;
- les coeurs, vies, checkpoints, sauvegardes et autres systemes ;
- l'interface et l'accessibilite ;
- l'equilibrage et les criteres de test ;
- la narration interactive et les cinematiques ;
- les besoins artistiques et sonores utiles a la production ;
- les outils, jalons et risques du projet.

Le GDD ne contient pas :

- le code source ;
- l'architecture detaillee de Godot ;
- les chemins de noeuds ou les noms de classes techniques ;
- les etudes de marche ;
- le financement ou la rentabilite ;
- le marketing, la communication commerciale ou les ventes.

## Emplacement principal dans le GDD

| Type d'information | Emplacement principal |
|---|---|
| Cadre et conventions | `Cadre` |
| Fiche generale du jeu | `Fiche-Generale.md` |
| Commandes | `Controles` |
| Deplacement et capacites d'Imran | `Joueur` |
| Attaques, defense et degats | `Combat` |
| Comportement des ennemis | `Ennemis` |
| Comportement des golems et de Tata Lisa | `Boss` |
| Parcours et contenu des niveaux | `Niveaux` |
| Regles transversales | `Systemes` |
| HUD, menus et accessibilite | `Interface` |
| Valeurs globales et courbe de difficulte | `Equilibrage` |
| Histoire interactive et cinematiques | `Narration` |
| Besoins visuels | `Direction-Artistique` |
| Besoins musicaux et sonores | `Direction-Sonore` |
| Outils, jalons et retroplanning | `Production` |

Les dossiers absents seront crees uniquement lorsque leur etape de redaction commencera.
