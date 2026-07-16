# Fiche generale du jeu

> **Statut :** Valide

## Objectif

Cette fiche transforme la vision du Concept Game en contraintes generales pour tout le GDD. Les regles detaillees, les valeurs et l'implementation seront definies dans les etapes suivantes.

## Identite du jeu

| Element | Decision |
|---|---|
| Titre | **Imran Adventure** |
| Genre principal | Jeu de plateforme 2D |
| Sous-genre | Action-aventure lineaire avec combats et boss de fin de niveau |
| Mode de jeu | Solo |
| Nombre de joueurs | Un joueur controle Imran |
| Plateforme cible | PC |
| Moteur | Godot Engine |
| Perspective | Vue laterale en 2D |
| Resolution de reference | `1920 x 1080`, format `16:9` |
| Camera | Suivi lateral fluide donnant de la visibilite devant Imran |
| Public principal | Enfants a partir de 7 ans |
| Public secondaire | Joueurs recherchant une aventure familiale simple et lisible |
| Structure | Progression lineaire avec un seul chemin principal par niveau |
| Difficulte | Une difficulte unique avec une progression graduelle |
| Contenu principal | Six niveaux, six golems et un combat final contre Tata Lisa |
| Modele du projet | Projet personnel non commercial et sans vente |

## Principe general

Le joueur controle Imran, un garcon de 10 ans qui traverse le royaume de Vitrolles pour sauver sa soeur Aliyah. Il utilise la Shadow Sword et le Bouclier de lumiere, affronte les ennemis de chaque region, bat six golems et recupere les six cles du donjon.

Apres le sixieme niveau, Imran affronte Tata Lisa devant la porte du donjon. Sa victoire permet d'ouvrir les six verrous et de liberer Aliyah.

## Debut de l'aventure

1. Une cinematique montre Remi et Amelie confiant les equipements a Imran.
2. Les parents partent en exploration.
3. Tata Lisa enleve Aliyah.
4. Imran quitte le Village des Bles pour sauver sa soeur.
5. Le joueur prend le controle d'Imran au debut de la Foret enchantee.

Le Village des Bles apparait uniquement dans la cinematique d'introduction et ne constitue pas une zone jouable.

## Structure de l'aventure

| Ordre | Zone | Conclusion |
|---:|---|---|
| 1 | Foret enchantee | Golem, coffre et premiere cle |
| 2 | Grotte mysterieuse | Golem, coffre, deuxieme cle et Dash |
| 3 | Lac gele | Golem, coffre et troisieme cle |
| 4 | Desert oublie | Golem, coffre, quatrieme cle et Double saut |
| 5 | Volcan | Golem, coffre et cinquieme cle |
| 6 | Chateau de Tata Lisa | Golem, coffre et sixieme cle |
| Finale | Porte du donjon | Combat contre Tata Lisa et liberation d'Aliyah |

Le donjon sert uniquement de decor a la scene finale. Il ne constitue pas un septieme niveau.

## Fin de l'aventure

1. Imran bat Tata Lisa.
2. La Pierre du Chaos se brise.
3. Tata Lisa perd ses pouvoirs et prend la fuite.
4. La protection magique des verrous disparait.
5. Imran utilise les six cles et libere Aliyah.
6. Remi et Amelie reviennent de leur exploration.
7. La famille est reunie et l'aventure est marquee comme terminee.

## Experience recherchee

Le jeu doit proposer :

- des objectifs immediatement comprehensibles ;
- des commandes simples et precises ;
- une progression entierement lineaire ;
- une alternance lisible entre plateforme, combat et courtes sequences narratives ;
- des ennemis faciles a identifier ;
- des boss fondes sur l'observation et l'apprentissage ;
- une difficulte progressive sans pic injuste ;
- des retours visuels et sonores clairs ;
- une direction artistique de dessin anime ;
- une aventure epique, positive et centree sur la famille ;
- aucune violence graphique.

## Limites du projet

Le GDD ne doit pas ajouter :

- de mode multijoueur ;
- de monde ouvert ;
- de chemins narratifs alternatifs ;
- de choix de difficulte ;
- de septieme niveau dans le donjon ;
- de contenu commercial, de boutique ou de vente ;
- de violence graphique incompatible avec le public cible.

Toute proposition qui depasse ces limites exige une modification validee du Concept Game avant son ajout au GDD.

## Decisions reservees aux etapes suivantes

| Decision | Etape du plan |
|---|---|
| Boucles de jeu detaillees | Etape 3 |
| Commandes clavier et manette | Etape 4 |
| Valeurs de deplacement et de saut | Etape 5 |
| Valeurs de combat | Etape 6 |
| Duree cible et courbe de difficulte | Etape 10 |
| Mise a l'echelle, modes d'affichage et options | Etape 14 |
| Specifications des ressources visuelles | Etape 15 |
| Specifications audio | Etape 16 |
| Version de Godot, outils et retroplanning | Etape 17 |

## Sources

- [Presentation du Concept Game](../Concept-Game/01-Projet/Presentation.md)
- [Vision](../Concept-Game/01-Projet/Vision.md)
- [Objectifs](../Concept-Game/01-Projet/Objectifs.md)
- [Plateforme](../Concept-Game/01-Projet/Plateforme.md)
- [Public cible](../Concept-Game/01-Projet/Public-Cible.md)
- [Deroulement](../Concept-Game/02-Histoire/Deroulement.md)
- [Introduction](../Concept-Game/02-Histoire/Introduction.md)
- [Fin](../Concept-Game/02-Histoire/Fin.md)
- [Camera](../Concept-Game/06-Systemes/Camera.md)
- [Sauvegarde](../Concept-Game/06-Systemes/Sauvegarde.md)

## Criteres de validation

La fiche est valide si :

- toutes les decisions correspondent au Concept Game ;
- le mode solo est confirme ;
- le jeu conserve exactement six niveaux principaux et un combat final ;
- le Village des Bles et le donjon restent non jouables ;
- la fiche ne contient aucune valeur reservee a une etape ulterieure ;
- aucune fonction commerciale n'est introduite ;
- toutes les futures sections du GDD respectent ce perimetre.
