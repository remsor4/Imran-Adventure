# Progression

> **Statut :** Valide

## Objectif

Definir une progression entierement lineaire dans laquelle chaque niveau termine rapproche Imran de la liberation d'Aliyah sans ajouter de statistiques, de monnaie ou de capacites a debloquer.

## Ordre de l'aventure

| Ordre | Sequence | Condition de fin | Progression permanente |
|---:|---|---|---|
| 0 | Village des Bles | Atteindre la sortie du tutoriel | Acces a la Foret enchantee |
| 1 | Foret enchantee | Vaincre le golem et recuperer la Cle 1 | Acces a la Grotte mysterieuse |
| 2 | Grotte mysterieuse | Vaincre le golem et recuperer la Cle 2 | Acces au Lac gele |
| 3 | Lac gele | Vaincre le golem et recuperer la Cle 3 | Acces au Desert oublie |
| 4 | Desert oublie | Vaincre le golem et recuperer la Cle 4 | Acces au Volcan |
| 5 | Volcan | Vaincre le golem et recuperer la Cle 5 | Acces au Chateau de Tata Lisa |
| 6 | Chateau de Tata Lisa | Vaincre le golem et recuperer la Cle 6 | Acces au combat contre Tata Lisa |
| Finale | Porte du donjon | Vaincre Tata Lisa et ouvrir les six verrous | Liberation d'Aliyah et aventure terminee |

Le niveau 0 ne compte pas parmi les six niveaux principaux. Le donjon sert uniquement de decor a la liberation d'Aliyah et ne devient jamais un niveau jouable.

## Capacites disponibles des le debut

Imran possede toutes ses actions principales des la premiere prise de controle :

- deplacement horizontal ;
- saut ;
- Double saut ;
- Dash uniquement au sol ;
- attaque normale ;
- charge et lancement du Smash Tranchant ;
- protection automatique du Bouclier de lumiere ;
- interaction avec les objets compatibles.

Les pancartes du niveau 0 enseignent ces actions mais ne les debloquent pas.

## Absence d'ameliorations

L'aventure ne contient aucun :

- arbre de competences ;
- niveau d'experience ;
- point de statistique ;
- amelioration de degats ;
- augmentation du maximum de coeurs ou de vies ;
- achat de capacite ;
- equipement alternatif ;
- monnaie ;
- score ;
- objet optionnel a collectionner.

La difficulte augmente par la conception des plateformes, les combinaisons d'ennemis et les comportements des boss, jamais en retirant une capacite deja apprise.

## Role des cles

- Les six cles constituent les seules recompenses permanentes des niveaux principaux.
- Une cle confirme que son niveau est termine.
- Chaque cle sauvegardee debloque la prochaine sequence de l'aventure.
- Les cles ne modifient aucune valeur d'Imran.
- Les six cles sont obligatoires pour ouvrir les six verrous apres Tata Lisa.
- Une cle sauvegardee ne peut jamais etre perdue.

## Progression lineaire

- Les sequences sont parcourues dans un ordre fixe.
- Aucun embranchement narratif ou choix de niveau ne modifie cet ordre.
- Aucun monde central, carte de selection ou chemin alternatif n'est necessaire.
- Un niveau termine ne peut pas etre rejoue depuis la sauvegarde en cours.
- `Continuer` charge toujours la prochaine sequence non terminee.
- La recuperation d'une cle declenche la sauvegarde avant la transition vers la sequence suivante.
- Chaque nouvelle sequence jouable commence avec `3 coeurs` et `3 vies`.

## Echec et reprise

- La perte d'une vie ne modifie aucune progression permanente.
- Un Game Over recommence uniquement la sequence en cours.
- Une fermeture du jeu pendant un niveau incomplet reprend au debut de ce niveau.
- Les niveaux termines et les cles sauvegardees restent conserves.
- Une nouvelle partie efface toute la progression uniquement apres confirmation.

## Fin de l'aventure

- Apres la sixieme cle, `Continuer` replace Imran devant la porte du donjon avant Tata Lisa.
- La victoire contre Tata Lisa rend la porte interactive.
- Une interaction utilise automatiquement les six cles et ouvre les six verrous.
- La liberation d'Aliyah marque la sauvegarde comme `Aventure terminee`.
- Le menu principal propose ensuite `Revoir la fin` sans ajouter de Nouvelle Partie Plus.

## Criteres de validation

La progression sera validee si :

- l'aventure respecte toujours l'ordre du niveau 0 a la liberation d'Aliyah ;
- aucun niveau termine ne peut etre rejoue depuis la sauvegarde en cours ;
- les six niveaux principaux accordent exactement six cles ;
- toutes les capacites d'Imran restent disponibles des le niveau 0 ;
- aucune cle ne modifie les capacites ou les statistiques ;
- aucun systeme d'experience, monnaie, score ou collection optionnelle n'est ajoute ;
- un echec ne retire jamais une progression sauvegardee ;
- le donjon ne devient jamais un niveau jouable ;
- la liberation d'Aliyah constitue l'unique fin de l'aventure.

## Sources

- [Progression du Concept Game](../../Concept-Game/06-Systemes/Progression.md)
- [Fiche generale](../Fiche-Generale.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Dash](../../Concept-Game/05-Gameplay/Dash.md)
- [Double saut](../../Concept-Game/05-Gameplay/Double-Saut.md)
- [Coffres et cles](Coffres-et-Cles.md)
- [Sauvegarde](Sauvegarde.md)
