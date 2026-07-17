# Sauvegarde

> **Statut :** Valide

## Objectif

Permettre au joueur de reprendre l'aventure depuis le dernier niveau debloque sans conserver les progres temporaires d'un niveau incomplet.

## Emplacement unique

- Le jeu utilise un seul emplacement de sauvegarde.
- La sauvegarde est entierement automatique.
- Aucun bouton, raccourci ou menu de sauvegarde manuelle n'existe.
- `Continuer` charge toujours cet emplacement.
- Lorsqu'aucune sauvegarde n'existe, `Continuer` reste visible mais indisponible.
- `Nouvelle partie` efface une sauvegarde existante uniquement apres une confirmation explicite.
- Le jeu ne propose ni selection de niveau, ni Nouvelle Partie Plus.

## Declencheurs automatiques

| Declencheur | Progression enregistree | Point de reprise |
|---|---|---|
| Sortie du niveau 0 | Tutoriel termine et Foret accessible | Debut de la Foret enchantee |
| Cle 1 recuperee | Niveau 1 termine et Cle 1 conservee | Debut de la Grotte mysterieuse |
| Cle 2 recuperee | Niveau 2 termine et Cles 1 a 2 conservees | Debut du Lac gele |
| Cle 3 recuperee | Niveau 3 termine et Cles 1 a 3 conservees | Debut du Desert oublie |
| Cle 4 recuperee | Niveau 4 termine et Cles 1 a 4 conservees | Debut du Volcan |
| Cle 5 recuperee | Niveau 5 termine et Cles 1 a 5 conservees | Debut du Chateau de Tata Lisa |
| Cle 6 recuperee | Six niveaux termines et six cles conservees | Devant la porte du donjon avant Tata Lisa |
| Aliyah liberee | Etat `Aventure terminee` | Action `Revoir la fin` |

La victoire contre un golem ne sauvegarde rien avant l'ajout automatique de sa cle.

## Donnees conservees

La sauvegarde conserve uniquement les informations permanentes suivantes :

- fin du niveau 0 ;
- dernier niveau termine ;
- prochain niveau accessible ;
- liste des cles recuperees ;
- acces au combat final apres la sixieme cle ;
- etat `Aventure terminee` apres la liberation d'Aliyah.

## Donnees non conservees

La sauvegarde ne conserve jamais :

- les coeurs ou les vies d'une tentative ;
- la pancarte de controle activee ;
- les ennemis vaincus ;
- la position d'Imran dans un niveau ;
- l'etat des dangers, objets temporaires ou feux de camp ;
- la vie restante d'un golem ou de Tata Lisa ;
- une animation ou une cinematique interrompue.

Chaque reprise jouable commence avec `3 coeurs` et `3 vies`.

## Fermeture ou abandon pendant un niveau

- Fermer le jeu, retourner au menu principal ou abandonner un niveau ne cree aucune sauvegarde.
- Le niveau incomplet recommence depuis son debut lors de la prochaine reprise.
- Son checkpoint temporaire et tous ses progres locaux sont oublies.
- Les cles des niveaux deja termines restent conservees.
- Quitter le niveau 0 avant sa sortie oblige a recommencer le tutoriel depuis son debut.
- Apres la sixieme cle, la reprise reste devant la porte du donjon avant Tata Lisa.

## Game Over

- L'ouverture du Game Over ne cree aucune sauvegarde.
- `Recommencer le niveau` relance la sequence en cours avec `3 coeurs` et `3 vies`.
- `Retour au menu principal` conserve uniquement la derniere sauvegarde permanente.
- Aucun echec ne peut retirer une cle deja sauvegardee.

## Nouvelle partie

- Sans sauvegarde existante, `Nouvelle partie` commence directement le niveau 0.
- Si une sauvegarde existe, une fenetre propose `Annuler` et `Effacer et recommencer`.
- `Annuler` possede le focus initial.
- L'effacement commence uniquement apres la seconde validation.
- Une nouvelle partie ne conserve aucune cle ni aucun niveau termine.

## Aventure terminee

- La liberation d'Aliyah declenche la sauvegarde finale avant les credits.
- La sauvegarde recoit l'etat `Aventure terminee`.
- `Continuer` est remplace par `Revoir la fin` dans le menu principal.
- `Revoir la fin` rejoue la liberation d'Aliyah et les credits sans relancer Tata Lisa.

## Retour d'information

- Un indicateur distinct informe le joueur que la sauvegarde est en cours.
- Une confirmation visuelle courte indique que la sauvegarde est terminee.
- Une transition vers la sequence suivante attend la fin de l'enregistrement.
- Le joueur ne peut pas confondre cet indicateur avec une cle, un checkpoint ou un soin.
- Une erreur de sauvegarde ne doit jamais afficher une fausse confirmation de reussite.

## Criteres de validation

La sauvegarde sera validee si :

- chaque declencheur automatique possede un point de reprise unique ;
- aucune sauvegarde manuelle ne peut etre creee ;
- une cle est enregistree avant le passage au niveau suivant ;
- une tentative incomplete ne conserve aucun progres temporaire ;
- chaque reprise commence avec `3 coeurs` et `3 vies` ;
- une cle sauvegardee ne peut jamais etre perdue ;
- un checkpoint ne cree jamais de sauvegarde permanente ;
- une nouvelle partie ne peut pas effacer la progression sans confirmation ;
- la fin de l'aventure remplace `Continuer` par `Revoir la fin` ;
- le joueur recoit une confirmation visible de chaque sauvegarde reussie.

## Sources

- [Sauvegarde du Concept Game](../../Concept-Game/06-Systemes/Sauvegarde.md)
- [Menu principal](../../Concept-Game/11-Interface/Menu-Principal.md)
- [Menu Pause](../../Concept-Game/11-Interface/Pause.md)
- [Progression du Concept Game](../../Concept-Game/06-Systemes/Progression.md)
- [Game Over](Game-Over.md)
- [Checkpoints](Checkpoints.md)
- [Coffres et cles](Coffres-et-Cles.md)
