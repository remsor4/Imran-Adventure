# Tests d'equilibrage

> **Statut :** Valide

## Objectif

Verifier que la difficulte reste progressive, lisible et compatible avec un joueur novice a partir de 7 ans.

## Profil de reference

Le test principal utilise un joueur novice qui :

- a termine le niveau 0 ;
- connait toutes les commandes ;
- ne maitrise pas encore parfaitement le Dash et le Double saut ;
- ne connait pas les rencontres ni les attaques des boss ;
- apprend par l'observation, l'essai et la repetition.

## Objectifs de tolerance aux echecs

| Situation | Objectif |
|---|---|
| Niveau 0 | Terminer sans perdre de vie |
| Niveau principal | Atteindre le feu de camp avec au moins `2 vies` |
| Golem | Obtenir la victoire en `1 a 3 essais` |
| Tata Lisa | Obtenir la victoire en `2 a 4 essais` |
| Nouvelle situation | Comprendre la solution apres au maximum `2 echecs` |
| Meme section | Plusieurs Game Over indiquent une difficulte excessive |

Ces objectifs servent a evaluer l'equilibrage global. Ils ne garantissent pas le meme resultat pour chaque joueur.

## Interpretation d'un echec

Un echec est acceptable si :

- sa cause est visible ou comprise immediatement apres l'impact ;
- le joueur peut identifier une autre action a essayer ;
- la reprise permet de retenter sans confusion ;
- l'echec ne vient pas d'un danger invisible ou d'une collision incoherente.

Un echec indique un probleme d'equilibrage si :

- le joueur ne comprend pas ce qui lui a inflige un degat ;
- plusieurs dangers suppriment toutes les solutions autorisees ;
- la meme situation provoque plusieurs Game Over ;
- le joueur connait la solution mais la precision demandee reste excessive ;
- un nouvel apprentissage est impose pendant la pression maximale.

## Protocole de test valide

Chaque section importante est verifiee par trois passages complementaires.

### Passage 1 - Controle technique par Codex

Codex utilise le projet Godot pour verifier :

- les valeurs chargees par la scene ;
- les dimensions et les positions des collisions ;
- les distances minimales entre les ennemis ;
- les limites des zones de rencontre ;
- les trajectoires d'esquive disponibles ;
- le nombre de dangers et d'attaques simultanes ;
- l'absence de collision ou de danger invisible ;
- l'absence d'erreur dans les journaux du moteur.

Ce passage verifie le fonctionnement mesurable. Il ne remplace pas le ressenti du joueur.

### Passage 2 - Decouverte par Rems

Rems joue normalement sans utiliser d'outil de developpement ni consulter les valeurs techniques pendant le passage.

Ce passage sert a observer :

- la comprehension des nouvelles situations ;
- le temps de reaction ;
- les degats recus ;
- les echecs et leur cause ;
- la fatigue ou la confusion ;
- le nombre d'essais necessaires ;
- le rythme entre pression et respiration.

Une capture video peut etre utilisee pour examiner un probleme image par image.

### Passage 3 - Confirmation par Rems

Apres une correction, Rems rejoue la section concernee.

La correction est conservee si :

- le probleme initial ne se reproduit plus ;
- la solution reste lisible ;
- la section conserve la pression visee ;
- aucune nouvelle erreur ou facilite excessive n'apparait.

Si la correction modifie une valeur de niveau 2, les sections utilisant cette valeur sont egalement retestees.

## Mesures a relever

Une fiche de test contient :

| Mesure | Moment ou detail |
|---|---|
| Duree | Section testee et niveau complet |
| Coeurs restants | Checkpoint, feu de camp et fin de sequence |
| Vies restantes | Checkpoint, feu de camp et fin de sequence |
| Degats recus | Nombre total et source de chaque impact |
| Pertes de vie | Nombre et situation concernee |
| Game Over | Nombre et section concernee |
| Essais contre le boss | Du declenchement du premier combat a la victoire |
| Echecs repetes | Toute situation echouee au moins `2 fois` |
| Dash | Utilisation reussie, oubliee ou mal comprise |
| Double saut | Utilisation reussie, oubliee ou mal comprise |
| Comprehension | Cause comprise ou non apres chaque echec important |
| Evaluation finale | Trop facile, juste, trop difficile ou confus |

## Regles de mesure

- Le chronometre de gameplay exclut les menus, les pauses et les cinematiques.
- Un degat est associe a l'ennemi, au projectile, au boss ou au danger de plateforme qui l'a provoque.
- Un echec repete est note meme s'il ne retire aucun coeur.
- Une action oubliee est distinguee d'une action comprise mais mal executee.
- Le commentaire final de Rems complete les valeurs mesurees sans les remplacer.
- Une capture video est conservee uniquement lorsqu'une cause reste incertaine ou demande une analyse image par image.

## Double validation d'une section

Une section est equilibree uniquement lorsque Rems et Codex la valident.

### Validation technique par Codex

Codex confirme :

- l'absence d'erreur bloquante dans Godot ;
- l'absence de collision incoherente ;
- l'absence de danger invisible ;
- la presence d'au moins une solution autorisee ;
- le respect des distances, densites et valeurs de reference ;
- le respect de la plage de pression prevue.

### Validation de gameplay par Rems

Rems confirme :

- la comprehension des echecs importants ;
- le respect de la duree cible ;
- le respect des objectifs de coeurs et de vies ;
- le respect du nombre d'essais vise contre le boss ;
- l'absence de Game Over repetes anormalement sur la meme section ;
- un ressenti final `juste` ;
- la reussite du passage de confirmation apres une correction.

### Regle de decision

- Une erreur technique bloquante empeche toujours la validation.
- Un ressenti `confus` ou `trop difficile` empeche la validation meme si les valeurs techniques sont correctes.
- Un ressenti `trop facile` demande une verification de la pression visee avant validation.
- En cas de desaccord entre les mesures et le ressenti, la section reste `En cours`.
- Une correction est validee uniquement apres un passage de confirmation.

## Criteres de validation du document

Le protocole de test est pret si :

- le profil de reference est defini ;
- les objectifs de tolerance aux echecs sont mesurables ;
- les causes d'echec acceptables et injustes sont distinguees ;
- les trois passages de test sont decrits ;
- les mesures a relever sont listees ;
- la double validation de Rems et Codex est obligatoire ;
- chaque correction exige un passage de confirmation.
