# Courbe de difficulte

> **Statut :** Valide

## Objectif

Definir une montee en difficulte progressive, lisible et juste entre le niveau 0, les six niveaux principaux et le combat final.

## Forme generale validee

La difficulte suit des vagues douces.

Chaque niveau principal respecte la progression suivante :

1. une courte phase accessible rappelle les regles deja apprises ;
2. les dangers et les combinaisons augmentent progressivement ;
3. une respiration permet au joueur de se preparer avant le golem ;
4. le golem constitue le pic de difficulte du niveau ;
5. le niveau suivant recommence avec une pression legerement plus faible que ce pic ;
6. cette nouvelle introduction reste plus exigeante que le debut du niveau precedent.

Cette structure permet de faire progresser le joueur sans maintenir une pression maximale en permanence.

## Pression globale par sequence

| Sequence | Pression visee | Fonction |
|---|---|---|
| Niveau 0 - Village des Bles | Initiation | Apprendre et pratiquer sans forte punition |
| Niveau 1 - Foret enchantee | Faible | Confirmer les bases et decouvrir les premieres paires |
| Niveau 2 - Grotte mysterieuse | Faible a moderee | Ajouter l'Epeiste et demander plus de lecture |
| Niveau 3 - Lac gele | Moderee | Introduire le Serpent et une pression terrestre plus rapide |
| Niveau 4 - Desert oublie | Moderee a elevee | Utiliser les paires avancees et les premiers groupes de trois |
| Niveau 5 - Volcan | Elevee | Introduire les Zombies et augmenter la duree des rencontres |
| Niveau 6 - Chateau de Tata Lisa | Elevee a tres elevee | Utiliser les combinaisons finales autorisees |
| Combat final - Tata Lisa | Pic final | Verifier la maitrise de toutes les regles utiles |

La pression indique la complexite des situations et non une modification cachee des statistiques.

## Leviers de difficulte valides

La difficulte est geree par la conception des situations.

- `Valeurs stables` : un meme ennemi conserve ses PV, ses vitesses, ses preparations et ses comportements.
- `Complexite progressive` : ennemi seul, paire identique, paire mixte, puis groupe de trois dans les niveaux avances.
- `Terrain progressif` : sol simple, plateformes accessibles, puis zones d'atterrissage et dangers combines.
- `Maitrise des actions` : une action est pratiquee seule avant d'etre demandee pendant une rencontre.
- `Rythme en vagues` : une introduction, une montee, une respiration et un boss organisent chaque niveau principal.
- `Endurance` : les Zombies augmentent la duree des rencontres avec leurs `3 PV` sans changer les regles des Squelettes.
- `Lisibilite constante` : aucune attaque ne devient volontairement moins lisible pour creer une difficulte artificielle.

## Ordre de correction d'une situation trop difficile

Lorsqu'un test revele une situation trop exigeante, les corrections sont appliquees dans cet ordre :

1. augmenter l'espace praticable ;
2. augmenter la separation entre les ennemis ;
3. reduire le nombre de dangers simultanes ;
4. simplifier le terrain ;
5. modifier une valeur validee uniquement en dernier recours.

Une valeur validee ne peut etre modifiee qu'apres avoir verifie que les quatre premieres corrections sont insuffisantes.

## Progression des ennemis ordinaires

L'ordre d'introduction, les paires, les groupes de trois et les combinaisons interdites sont definis dans [Combinaisons et progression des ennemis](../Ennemis/Combinaisons-et-Progression.md).

Cette fiche reste la source de verite pour :

- la presentation de chaque famille seule ;
- l'ordre d'apparition des familles ;
- les combinaisons autorisees par niveau ;
- l'introduction des premiers groupes de trois au niveau 4 ;
- le remplacement des Squelettes par les Zombies aux niveaux 5 et 6.

L'equilibrage utilise cette progression sans la recopier ni modifier le comportement d'une famille.

## Progression du Dash et du Double saut

Le Dash et le Double saut restent disponibles des la premiere prise de controle. Ils ne sont jamais debloques plus tard.

Le tableau suivant concerne les phases de plateforme et les rencontres avec les ennemis ordinaires. Les utilisations demandees pendant un combat de boss sont definies uniquement dans la fiche du boss concerne.

Leur utilisation progresse par couches :

| Sequence | Utilisation visee |
|---|---|
| Niveau 0 - Village des Bles | Apprentissage separe du Dash et du Double saut dans des zones simples |
| Niveau 1 - Foret enchantee | Utilisations obligatoires simples sans ennemi actif pendant l'action |
| Niveau 2 - Grotte mysterieuse | Utilisation avec un ennemi proche et une zone d'arrivee sure |
| Niveau 3 - Lac gele | Alternance du Dash et du Double saut dans une meme section avec un appui stable entre les actions |
| Niveau 4 - Desert oublie | Apprentissage de l'enchainement Dash au sol, saut et Double saut, puis utilisation pendant les paires et les premiers groupes de trois |
| Niveau 5 - Volcan | Utilisation pendant les rencontres avec des Zombies |
| Niveau 6 - Chateau de Tata Lisa | Maitrise complete avec les combinaisons finales autorisees |
| Combat final - Tata Lisa | Utilisation libre selon les attaques sans introduire de nouvelle regle |

Regles communes :

- chaque nouvelle utilisation est montree sans pression avant d'etre associee a un ennemi ;
- un Dash au sol ne peut jamais etre demande pendant une phase aerienne ;
- une zone d'arrivee ou d'atterrissage lisible reste disponible ;
- aucun passage obligatoire ne demande une precision au pixel pres ;
- l'echec d'une action ne doit pas provoquer un degat impossible a anticiper ;
- le niveau 6 et Tata Lisa verifient des actions deja apprises sans ajouter de nouvelle commande.

## Durees cibles

Les durees sont mesurees entre la prise de controle et la sauvegarde de fin de la sequence.

Elles ne comprennent pas :

- les cinematiques ;
- les menus et les pauses ;
- les echecs et les reprises ;
- le temps passe volontairement immobile.

| Sequence | Duree cible |
|---|---:|
| Niveau 0 - Village des Bles | `8 a 12 min` |
| Niveau 1 - Foret enchantee | `20 a 25 min` |
| Niveau 2 - Grotte mysterieuse | `20 a 25 min` |
| Niveau 3 - Lac gele | `20 a 25 min` |
| Niveau 4 - Desert oublie | `20 a 25 min` |
| Niveau 5 - Volcan | `20 a 25 min` |
| Niveau 6 - Chateau de Tata Lisa | `20 a 25 min` |
| Combat final et conclusion jouable | `10 a 15 min` |

La duree totale cible d'un parcours reussi sans echec se situe entre `2 h 18` et `2 h 57`.

Les derniers niveaux deviennent plus difficiles par leurs situations sans devenir plus longs. Cette regle evite d'associer la pression la plus elevee a la fatigue la plus forte.

## Densite simultanee des dangers

Les limites de cette section concernent uniquement les phases de plateforme et les rencontres avec les ennemis ordinaires. Les arenes de boss suivent les dangers et les attaques valides dans leurs propres fiches.

Une source de danger active est un element qui demande une reaction immediate du joueur :

- un ennemi ordinaire actuellement capable de blesser Imran compte comme `1 source`, meme si son corps et son attaque sont dangereux ;
- les projectiles et les composants d'attaque produits par ce meme ennemi restent rattaches a sa source ;
- un obstacle de plateforme actuellement dangereux compte comme `1 source` ;
- un groupe de trois ennemis ordinaires occupe donc au maximum `3 sources`.

La densite simultanee suit cette progression :

| Sequence | Densite habituelle | Maximum autorise |
|---|---:|---:|
| Niveau 0 - Village des Bles | `1` | `1` |
| Niveau 1 - Foret enchantee | `1` | `2` exceptionnellement |
| Niveau 2 - Grotte mysterieuse | `1 a 2` | `2` |
| Niveau 3 - Lac gele | `1 a 2` | `2` |
| Niveau 4 - Desert oublie | `2` | `3` |
| Niveau 5 - Volcan | `2` | `3` |
| Niveau 6 - Chateau de Tata Lisa | `2 a 3` | `3` |

Regles de repartition :

- une nouvelle mecanique est toujours presentee avec un seul danger actif ;
- le maximum autorise reste reserve a une zone offrant toutes les trajectoires d'esquive necessaires ;
- une rencontre utilisant le maximum autorise est suivie d'une courte zone sans ennemi actif ;
- deux situations utilisant la pression maximale ne se suivent jamais directement ;
- les limites de `3 emplacements d'attaque` et de `3 ennemis ordinaires` restent applicables ;
- un danger de plateforme et des ennemis ne sont combines qu'apres avoir ete pratiques separement.

## Nombre de sequences dangereuses

Une sequence dangereuse est :

- une rencontre de combat ;
- une phase de plateforme dangereuse ;
- une combinaison des deux dans un niveau avance.

Les quantites suivantes constituent des plages de conception. Le placement exact sera defini pendant le detail des niveaux.

| Sequence | Nombre cible |
|---|---:|
| Niveau 0 - Village des Bles | `5 a 7` |
| Niveau 1 - Foret enchantee | `8 a 10` |
| Niveau 2 - Grotte mysterieuse | `8 a 10` |
| Niveau 3 - Lac gele | `8 a 10` |
| Niveau 4 - Desert oublie | `10 a 12` |
| Niveau 5 - Volcan | `10 a 12` |
| Niveau 6 - Chateau de Tata Lisa | `10 a 12` |

Regles communes :

- un maximum de `2 sequences dangereuses` peut se suivre sans respiration ;
- une respiration ne contient aucun ennemi actif et aucun danger immediat ;
- une pancarte de tutoriel n'est jamais comptee comme une sequence dangereuse ;
- le feu de camp et la presentation du boss ne sont pas comptes comme des sequences dangereuses ;
- le combat de boss reste un pic distinct et n'entre pas dans cette plage ;
- les quantites pourront varier dans leur plage sans modifier la pression globale visee.

## Repartition interne de la pression

Dans chaque niveau principal, les sequences dangereuses sont reparties ainsi :

| Partie du niveau | Part des sequences | Pression relative |
|---|---:|---|
| Debut | `30 %` | Simple |
| Milieu | `40 %` | Intermediaire |
| Fin avant le boss | `30 %` | Exigeante |

La pression est relative au niveau concerne. Une situation exigeante du niveau 1 reste donc plus accessible qu'une situation exigeante du niveau 6.

Le niveau 0 constitue une exception :

| Pression | Part des sequences |
|---|---:|
| Simple | Environ `60 %` |
| Intermediaire | Environ `40 %` |
| Elevee | `0 %` |

Regles de repartition :

- le debut rappelle les acquis avant toute nouvelle combinaison ;
- le milieu developpe les mecanismes deja presentes ;
- la fin verifie la maitrise sans introduire de nouvelle regle ;
- une respiration et le feu de camp separent la derniere sequence du combat de boss ;
- les pourcentages peuvent etre arrondis selon le nombre reel de sequences ;
- l'arrondi favorise toujours la categorie la plus accessible.

## Profil de joueur de reference

Le profil novice et les objectifs de tolerance aux echecs sont definis uniquement dans le document [Tests d'equilibrage](Tests.md).

La courbe de difficulte utilise ce profil sans recopier sa definition.

## Regles communes validees

- Le niveau 0 reste le point le plus accessible de l'aventure.
- Une nouvelle famille d'ennemis est presentee seule avant toute combinaison.
- Une nouvelle utilisation du Dash ou du Double saut est montree dans une situation sure avant d'etre associee a un ennemi.
- Un meme ennemi conserve les memes valeurs et le meme comportement dans tous les niveaux ou il apparait.
- Les degats recus restent fixes a `1 coeur` par impact valide.
- La difficulte augmente par la composition, le placement, le terrain et le rythme des situations.
- Aucun pic de difficulte ne repose sur un danger invisible ou une attaque sans preparation.
- Une situation obligatoire conserve toujours au moins une solution lisible.
- Le boss final constitue le pic de difficulte de toute l'aventure.

## Criteres de validation

La courbe sera validee si :

- chaque niveau possede une introduction, une montee, une respiration et un pic ;
- le debut d'un niveau reste plus accessible que le boss precedent ;
- la difficulte globale augmente du niveau 0 au combat final ;
- aucune nouvelle regle ne doit etre comprise pendant une situation de pression maximale ;
- le public cible peut progresser sans pic injuste.
