# GDD - Ennemis et intelligence artificielle

> **Statut :** En cours

## Objectif

Definir des ennemis simples a comprendre, previsibles et assez differents pour faire progresser la difficulte sans devenir injustes pour un public a partir de 7 ans.

## Documents

| Ordre | Document | Statut |
|---:|---|---|
| 1 | [Regles communes](Regles-Communes.md) | Valide |
| 2 | [Slimes](Slimes.md) | Valide |
| 3 | [Chauves-souris](Chauves-Souris.md) | A rediger |
| 4 | [Squelettes](Squelettes.md) | A rediger |
| 5 | [Serpents](Serpents.md) | A rediger |
| 6 | [Zombies](Zombies.md) | A rediger |

## Ordre de validation

1. Fixer les regles partagees par tous les ennemis ordinaires.
2. Definir le deplacement et l'attaque bondissante des Slimes.
3. Definir le vol et l'attaque en plongee des Chauves-souris.
4. Definir les variantes epeiste et archer des Squelettes.
5. Definir le deplacement rapide et l'attaque de proximite des Serpents.
6. Adapter les deux roles des Squelettes aux Zombies plus resistants.
7. Verifier les combinaisons autorisees et la progression entre les niveaux.

## Criteres de validation de l'etape

L'etape 8 est validee si :

- chaque ennemi possede des valeurs de vie, de degats et de vitesse ;
- chaque detection possede une distance et une condition d'activation ;
- chaque attaque possede une preparation, une phase dangereuse et une recuperation ;
- chaque projectile possede une vitesse, une portee et une condition de disparition ;
- chaque reaction aux degats et chaque defaite possedent un resultat unique ;
- chaque ennemi reste limite a sa zone de rencontre ;
- les combinaisons restent lisibles pour le public cible ;
- aucune regle technique propre a Godot n'est imposee dans le GDD.

## Sources principales

- [Principes d'IA du Concept Game](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Degats](../Combat/Degats.md)
- [Recul](../Combat/Recul.md)
- [Invulnerabilite](../Combat/Invulnerabilite.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Camera](../Systemes/Camera.md)
- [Reference video des collisions entre ennemis](Reference-Video-Wonder-Boy-Collisions-Ennemis.md)
- [Reference video du bond unique des Slimes](Reference-Video-Wonder-Boy-Bonds-Slimes.md)
- [Reference video de la detection horizontale des Slimes](Reference-Video-Wonder-Boy-Detection-Slimes.md)
