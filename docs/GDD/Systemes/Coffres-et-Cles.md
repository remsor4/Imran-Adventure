# Coffres et cles

> **Statut :** Valide

## Objectif

Definir la recompense obligatoire de chaque niveau principal, la recuperation des six cles et l'ouverture des six verrous du donjon.

## Repartition

| Sequence | Coffres de progression | Cles |
|---|---:|---:|
| Niveau 0 - Village des Bles | `0` | `0` |
| Chacun des six niveaux principaux | `1` | `1` |
| Combat final contre Tata Lisa | `0` | `0` |
| Total de l'aventure | `6` | `6` |

Chaque coffre et chaque cle sont obligatoires. Le jeu ne contient aucun coffre optionnel, aucune cle cachee et aucun objet secondaire a collectionner.

## Etat du coffre

Un coffre de progression possede les etats suivants :

1. `Protege` pendant le combat contre le golem ;
2. `Disponible` apres la victoire contre le golem ;
3. `Ouvert` apres une interaction valide ;
4. `Cle recuperee` lorsque la recompense du niveau est accordee.

Le coffre ne peut pas etre ouvert avant la victoire contre le golem. La victoire seule ne termine pas le niveau.

## Ouverture volontaire

- Le joueur doit placer Imran a portee du coffre.
- Un message affiche la commande `Interaction`.
- Une pression valide lance une courte sequence d'ouverture.
- Le deplacement, le saut, le Dash et les attaques sont bloques pendant cette sequence.
- Une seconde pression ne peut pas ouvrir le coffre une nouvelle fois.
- Aucun ennemi ni danger ne peut atteindre Imran dans la zone de recompense.

## Variantes visuelles

Chaque coffre reprend le theme visuel et les principaux materiaux du golem qui le protege.

| Niveau | Golem | Identite du coffre |
|---:|---|---|
| 1 | Golem de la Foret | Bois, racines, feuilles et motifs naturels |
| 2 | Golem de la Grotte | Roche, minerai et formes de cristaux |
| 3 | Golem du Lac | Glace, givre et formes gelees |
| 4 | Golem du Desert | Gres, sable et motifs de ruines anciennes |
| 5 | Golem du Volcan | Basalte, roche volcanique et fissures de magma |
| 6 | Golem du Chateau | Pierre sombre, metal et motifs du Chateau |

Les six variantes utilisent le meme fonctionnement, les memes etats et la meme structure d'animation. Seuls leur habillage, leurs materiaux visibles et leurs sons de matiere changent.

## Retour visuel et sonore

- Le mecanisme du coffre et son couvercle s'animent pendant l'ouverture.
- Aucun rayon, aucune lumiere doree et aucun effet lumineux ne sont ajoutes.
- La cle sort du coffre et reste clairement visible pendant la courte sequence.
- Le coffre utilise un son d'ouverture adapte a ses materiaux, accompagne du mecanisme en bois ou en metal.
- La sortie de la cle utilise un tintement bref et clair.
- La cle est ajoutee automatiquement a la progression a la fin de ce retour.

## Recuperation de la cle

- Chaque coffre contient exactement la cle du niveau termine.
- La cle apparait pendant la sequence d'ouverture du coffre.
- Elle est automatiquement ajoutee a la progression a la fin de cette sequence.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- Imran ne peut pas quitter la courte sequence avant l'enregistrement de la cle.
- La cle n'augmente ni les degats, ni les coeurs, ni les vies et ne debloque aucune capacite.
- La cle sert uniquement a la progression vers le donjon.
- La sauvegarde automatique se declenche immediatement apres l'ajout effectif de la cle.
- Une cle sauvegardee ne peut jamais etre perdue.

## Fin d'un niveau principal

Un niveau principal est termine lorsque les trois conditions suivantes sont remplies dans cet ordre :

1. le golem est vaincu ;
2. le coffre est ouvert ;
3. la cle est recuperee.

La recuperation de la cle declenche la sauvegarde automatique, restaure les coeurs et les vies a `3`, puis rend le niveau suivant accessible.

Quitter le jeu avant la recuperation et la sauvegarde de la cle oblige a recommencer le niveau depuis son debut.

## Six verrous du donjon

- Chaque cle correspond a un verrou de la porte du donjon.
- La porte ne peut etre ouverte que lorsque les six cles ont ete sauvegardees.
- Tata Lisa doit etre vaincue avant que la porte devienne interactive.
- Un message d'interaction apparait lorsque Imran se place devant la porte apres cette victoire.
- Le joueur utilise une seule fois la commande `Interaction`.
- Cette interaction lance une sequence qui utilise automatiquement les six cles.
- Les six verrous s'ouvrent l'un apres l'autre sans demander six nouvelles commandes.
- Le controle d'Imran reste bloque jusqu'a la fin de l'ouverture.
- La fin de l'ouverture conduit directement a la liberation d'Aliyah.
- Les cles restent inscrites dans la sauvegarde apres l'ouverture de la porte.

## Criteres de validation

Les coffres et les cles seront valides si :

- chacun des six niveaux principaux contient exactement un coffre et une cle ;
- le niveau 0 et le combat final ne contiennent aucun coffre de progression ;
- un coffre reste inaccessible avant la victoire contre son golem ;
- le joueur ouvre lui-meme le coffre avec la commande `Interaction` ;
- la cle est ajoutee automatiquement sans seconde interaction ;
- chaque coffre correspond visuellement au golem qui le protege ;
- l'ouverture ne produit aucun effet lumineux ;
- la victoire contre le golem ne termine pas seule le niveau ;
- la sauvegarde se declenche uniquement apres la recuperation de la cle ;
- une cle sauvegardee ne peut jamais etre perdue ;
- les six cles ouvrent exactement les six verrous du donjon ;
- une seule interaction avec la porte lance l'ouverture automatique des six verrous ;
- aucune cle ne debloque une capacite d'Imran.

## Sources

- [Coffres du Concept Game](../../Concept-Game/05-Gameplay/Coffres.md)
- [Cles du Concept Game](../../Concept-Game/05-Gameplay/Cles.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Sauvegarde du Concept Game](../../Concept-Game/06-Systemes/Sauvegarde.md)
- [Structure narrative](../../Concept-Game/02-Histoire/Structure-Narrative.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Effets visuels](../../Concept-Game/09-Direction-Artistique/Effets-Visuels.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
