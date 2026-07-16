# Plan de redaction du GDD - Imran Adventure

> **Statut :** En cours
>
> **Derniere validation :** Etape 5
>
> **Etape actuelle :** Etape 6 - En cours

## Reference

Ce plan adapte le processus presente par [Gaming Campus](https://gamingcampus.fr/boite-a-outils/le-processus-de-creation-dun-jeu-video.html) au projet **Imran Adventure**.

Le projet est realise uniquement par Rems et Codex. Le jeu ne sera pas vendu. Les etudes de marche, la rentabilite, le financement, le budget commercial, le marketing et les ventes sont donc exclus.

## Suivi des etapes

| Numero | Etape | Statut |
|---:|---|---|
| 1 | Cadre du GDD | Valide |
| 2 | Fiche generale du jeu | Valide |
| 3 | Boucle de jeu et experience du joueur | Valide |
| 4 | Controles et priorites des actions | Valide |
| 5 | Regles du joueur | Valide |
| 6 | Combat et equipements | En cours |
| 7 | Systemes de jeu | A rediger |
| 8 | Ennemis et intelligence artificielle | A rediger |
| 9 | Boss et golems | A rediger |
| 10 | Progression et equilibrage | A rediger |
| 11 | Structure commune des niveaux | A rediger |
| 12 | Detail des six niveaux et du combat final | A rediger |
| 13 | Narration, dialogues et cinematiques | A rediger |
| 14 | Interface et accessibilite | A rediger |
| 15 | Specifications artistiques et storyboards | A rediger |
| 16 | Specifications sonores | A rediger |
| 17 | Outils, organisation et retroplanning | A rediger |
| 18 | Plan de tests et validation finale du GDD | A rediger |

## Methode de travail

Pour chaque etape :

1. relire les informations validees dans le Concept Game ;
2. reperer les valeurs ou comportements encore indefinis ;
3. prendre les decisions manquantes ensemble ;
4. rediger les documents concernes sans lettres accentuees ;
5. verifier la coherence, les liens et les criteres de validation ;
6. obtenir la validation de Rems avant de passer a l'etape suivante.

Apres chaque etape paire validee, un audit croise des deux dernieres etapes est obligatoire avant de commencer l'etape suivante.

## Correspondance avec le processus Gaming Campus

| Etape Gaming Campus | Application a Imran Adventure | Decision |
|---|---|---|
| 1. Trouver le concept | Concept Game, vision, public, histoire et directions | Termine |
| 2. Rediger le cahier des charges ou GDD | Redaction detaillee selon le plan ci-dessous | Prochaine phase |
| 3. Realiser les esquisses | Storyboards, poses, decors, interface et cinematiques | Apres le GDD |
| 4. Creer les niveaux | Plans, parcours, obstacles, ennemis et progression des six niveaux | Prepare dans le GDD, realise apres sa validation |
| 5. Realiser la programmation | Prototype Godot, tranche jouable puis jeu complet | Apres les esquisses et les plans de niveaux |
| 6. Effectuer les tests et deployer le jeu | Tests personnels, corrections et export gratuit du jeu | Apres la programmation |
| 7. Marketing et ventes | Aucune application | Exclu |
| 8. Continuer a faire evoluer le jeu | Corrections de bugs et ameliorations utiles | Apres la premiere version jouable |

## Plan detaille du GDD

### Etape 1 - Cadre du GDD

Definir la fonction du document, sa source de verite, son perimetre et ses regles de mise a jour.

Livrables :

- presentation du GDD ;
- liens vers le Concept Game et le TDD ;
- conventions de nommage ;
- statuts utilises pour suivre les documents ;
- frontiere entre GDD et TDD.

Validation : chaque information de gameplay possede un emplacement unique.

### Etape 2 - Fiche generale du jeu

Transformer la vision validee en contraintes concretes de conception.

Livrables :

- genre et sous-genre ;
- mode solo ;
- public a partir de 7 ans ;
- plateforme cible ;
- camera 2D de profil ;
- nombre de niveaux ;
- conditions de debut et de fin ;
- experience recherchee.

Validation : la fiche generale correspond au Concept Game sans ajouter de nouvelle promesse.

### Etape 3 - Boucle de jeu et experience du joueur

Decrire ce que le joueur fait de minute en minute, dans un niveau et sur toute l'aventure.

Livrables :

- boucle courte : avancer, eviter, combattre et explorer ;
- boucle de niveau : checkpoint, progression, golem, coffre et cle ;
- boucle globale : six niveaux, six cles, Tata Lisa et liberation d'Aliyah ;
- rythme entre plateforme, combat et narration ;
- regles de victoire et d'echec.

Validation : chaque action du joueur sert une boucle clairement definie.

### Etape 4 - Controles et priorites des actions

Finaliser les commandes clavier et manette ainsi que les conflits entre actions.

Livrables :

- deplacement ;
- saut et Double saut ;
- Dash ;
- attaque normale ;
- Smash Tranchant ;
- blocage avec le Bouclier de lumiere ;
- interaction avec les coffres et les menus ;
- priorites, annulations et actions impossibles simultanement.

Validation : toutes les actions possedent une commande et une reponse attendue.

### Etape 5 - Regles du joueur

Definir les valeurs et les comportements precis d'Imran.

Livrables :

- vitesse de deplacement ;
- acceleration et freinage ;
- hauteur et duree du saut ;
- valeurs du Dash et du Double saut ;
- etats du joueur ;
- collisions ;
- recul ;
- invulnerabilite apres un degat ;
- conditions de controle bloque.

Validation : les valeurs peuvent etre directement testees dans un prototype Godot.

### Etape 6 - Combat et equipements

Finaliser toutes les regles de la Shadow Sword et du Bouclier de lumiere.

Livrables :

- portee, duree et degats de l'attaque normale ;
- charge, projectile et degats du Smash Tranchant ;
- blocage, orientation et limites du bouclier ;
- reactions aux impacts ;
- degats recus ;
- recul et invulnerabilite ;
- priorites entre mouvement, attaque et defense.

Validation : chaque attaque et chaque defense possedent des valeurs, des limites et un retour visuel ou sonore.

### Etape 7 - Systemes de jeu

Finaliser les regles communes qui encadrent toute l'aventure.

Livrables :

- trois coeurs et trois vies ;
- perte et recuperation des coeurs ;
- checkpoints et pancartes ;
- Game Over ;
- coffres, cles et verrous ;
- sauvegarde automatique ;
- reprise de partie ;
- camera ;
- progression des capacites.

Validation : chaque echec, reprise et sauvegarde donne toujours un resultat previsible.

### Etape 8 - Ennemis et intelligence artificielle

Decrire le comportement complet de chaque famille d'ennemis.

Livrables :

- regles communes ;
- Slimes ;
- Chauves-souris ;
- Squelettes ;
- Serpents ;
- Zombies ;
- detection, poursuite, attaque, degats et mort ;
- variantes et combinaisons par niveau.

Validation : chaque ennemi peut etre implemente sans inventer une regle manquante.

### Etape 9 - Boss et golems

Finaliser les regles communes et les fiches des sept combats de boss.

Livrables :

- structure commune des combats ;
- barre de vie centree en haut de l'ecran ;
- phases et attaques de chaque golem ;
- fenetres de vulnerabilite ;
- transitions entre phases ;
- recompenses ;
- combat final contre Tata Lisa ;
- sequence suivant la destruction de la Pierre du Chaos.

Validation : chaque combat possede un debut, des regles lisibles, une progression et une fin.

### Etape 10 - Progression et equilibrage

Organiser la montee en difficulte pour un public a partir de 7 ans.

Livrables :

- courbe de difficulte ;
- introduction progressive des ennemis ;
- obtention du Dash et du Double saut ;
- valeurs de reference ;
- temps vise par niveau ;
- nombre et repartition des dangers ;
- criteres de test de l'equilibrage.

Validation : la difficulte augmente sans pic injuste et sans bloquer le public cible.

### Etape 11 - Structure commune des niveaux

Definir les regles appliquees aux six niveaux avant de detailler leur contenu.

Livrables :

- entree et sortie d'un niveau ;
- rythme commun ;
- position approximative du checkpoint ;
- placement des ennemis et obstacles ;
- arene du golem ;
- coffre et cle ;
- transitions entre niveaux ;
- limites de camera et zones de securite.

Validation : les six niveaux partagent une structure coherente sans devenir identiques.

### Etape 12 - Detail des six niveaux et du combat final

Rediger les parcours dans l'ordre de l'aventure.

Livrables :

1. Foret enchantee ;
2. Grotte mysterieuse ;
3. Lac gele ;
4. Desert oublie ;
5. Volcan ;
6. Chateau de Tata Lisa ;
7. combat final devant le donjon.

Chaque fiche precisera le parcours, les obstacles, les ennemis, le checkpoint, les apprentissages, le golem, le coffre, la cle et les criteres de validation.

Validation : chaque niveau peut etre transforme en plan puis en prototype sans decision structurelle manquante.

### Etape 13 - Narration, dialogues et cinematiques

Transformer l'histoire validee en sequences utilisables dans le jeu.

Livrables :

- cinematique d'introduction au Village des Bles ;
- enlevement d'Aliyah ;
- depart d'Imran ;
- courts evenements entre les niveaux ;
- apparition de Tata Lisa ;
- destruction de la Pierre du Chaos et fuite de Tata Lisa ;
- liberation d'Aliyah ;
- retour de Remi et Amelie ;
- dialogues, durees, commandes et passage des cinematiques.

Validation : chaque scene indique qui apparait, ce qui se passe, ce qui est affiche et quand le joueur reprend le controle.

### Etape 14 - Interface et accessibilite

Finaliser tous les ecrans et tous les retours donnes au joueur.

Livrables :

- menu principal ;
- options ;
- pause ;
- HUD ;
- barre de vie des boss ;
- messages contextuels ;
- Game Over ;
- ecran de victoire ;
- lisibilite, taille du texte, contrastes et informations non fondees uniquement sur la couleur.

Validation : chaque information utile est visible, comprehensible et compatible avec le public cible.

### Etape 15 - Specifications artistiques et storyboards

Transformer la direction artistique du Concept Game en besoins de production.

Livrables :

- liste des personnages, ennemis, boss, decors, objets et effets ;
- dimensions et formats des ressources ;
- besoins en animations ;
- plans des cinematiques ;
- storyboards a produire apres le GDD ;
- maquettes d'interface ;
- regles de reutilisation des ressources.

Validation : chaque element visuel necessaire au jeu figure dans une liste de production.

### Etape 16 - Specifications sonores

Transformer la direction sonore en besoins concrets.

Livrables :

- liste des musiques ;
- ambiances par niveau ;
- effets sonores du joueur, des ennemis, des boss et de l'interface ;
- vocalises et dialogues affiches ;
- priorites de mixage ;
- formats et boucles ;
- declencheurs associes aux evenements du jeu.

Validation : chaque evenement important possede le retour sonore prevu ou une decision explicite de rester silencieux.

### Etape 17 - Outils, organisation et retroplanning

Noter les moyens necessaires sans creer une section commerciale.

Livrables :

- moteur Godot et version retenue ;
- outils pour les images, animations, sons et documents ;
- roles de Rems et Codex ;
- ordre de production ;
- prototype minimal ;
- tranche jouable de reference ;
- jalons des six niveaux ;
- phase de finition ;
- retroplanning realiste pour un projet a deux ;
- risques et solutions de repli.

Validation : chaque jalon possede un resultat observable et une condition de fin.

### Etape 18 - Plan de tests et validation finale du GDD

Verifier que le document peut guider les esquisses, le level design et la programmation.

Livrables :

- tests fonctionnels ;
- tests de controles ;
- tests de difficulte ;
- tests de sauvegarde ;
- tests des cinematiques ;
- tests d'interface et d'accessibilite ;
- criteres de version jouable ;
- audit des contradictions, liens, valeurs et documents incomplets.

Validation : aucun document ne conserve un statut incomplet, aucun lien n'est casse et aucune regle essentielle ne depend d'une interpretation.

## Apres la validation du GDD

L'ordre de production restera conforme au processus Gaming Campus :

1. realiser les esquisses, storyboards et maquettes ;
2. creer les plans detailles puis les prototypes des niveaux ;
3. programmer un prototype Godot ;
4. produire une tranche jouable de reference ;
5. construire les six niveaux et le combat final ;
6. integrer les cinematiques, l'interface, l'art et le son ;
7. effectuer les tests et les corrections ;
8. exporter une version gratuite du jeu ;
9. corriger les bugs decouverts apres cette version.

Les etapes de marketing et de vente restent exclues de tout le projet.
