# Revue de documentation - 2026-07-26

> **Statut :** A valider

## Objectif du document

Fournir une revue critique complete de l'etat de la documentation d'Imran Adventure (Concept Game, GDD, TDD) telle qu'elle existe au 2026-07-26, avant toute decision de demarrer une nouvelle phase de production. Cette revue ne modifie aucune regle de gameplay : chaque correction proposee doit etre reportee dans le document source concerne pour devenir effective.

## Etat au moment de la revue

Reference : [PLAN-GDD.md](../GDD/PLAN-GDD.md).

- Etapes 1 a 8 du GDD validees (Cadre, Fiche generale, Boucle de jeu, Controles, Joueur, Combat, Systemes, Ennemis).
- Etape 9 (Boss et golems) en cours : seul le Golem de la Foret est redige, les 5 autres golems et Tata Lisa sont des fiches vides (`_A rediger._`).
- Etapes 10 a 18 non commencees (Equilibrage, Niveaux, Narration, Interface, Direction artistique, Direction sonore, Production, Tests).
- TDD : les 41 fichiers de contenu sont un gabarit identique (`Statut : A completer`, 7 sections vides). Aucun autoload, aucune scene, aucun script, aucun signal, aucune ressource, aucun format de sauvegarde n'existe encore.

Cette revue tient compte de cet etat : la documentation est un document vivant en cours de redaction, pas un livrable final soumis a validation de bout en bout.

---

## 1. Vision globale

Le concept est clair et coherent : plateformer 2D d'action-aventure solo, inspire de *Wonder Boy: The Dragon's Trap*, public 7 ans et plus, Imran part seul delivrer sa soeur Aliyah a travers un niveau 0 tutoriel, six niveaux principaux et un combat final. Aucune derive vers du multijoueur, du monde ouvert ou du contenu commercial : le perimetre reste protege.

Le scope est realiste sur le papier mais ambitieux en pratique : sept environnements uniques, six boss uniques, systeme de combat, narration, sauvegarde, accessibilite, pour une equipe de deux personnes sans echeance commerciale.

**Contradiction relevee** : le [README.md](../Concept-Game/README.md) du Concept Game annonce travailler "sans entrer dans les valeurs chiffrees", mais [06-Systemes/Camera.md](../Concept-Game/06-Systemes/Camera.md) contient une resolution precise (1920x1080), des pourcentages de cadrage et des durees en secondes ; [09-Direction-Artistique/Palette.md](../Concept-Game/09-Direction-Artistique/Palette.md) liste des dizaines de codes hexadecimaux et un ratio 60/30/10 ; les ages d'Imran (10 ans) et Aliyah (8 ans) sont chiffres des le Concept Game. Les valeurs de secousse camera (6px/0.12s, 12px/0.25s) sont en outre dupliquees a l'identique entre `Camera.md` et `Effets-Visuels.md`, alors que la convention documentaire interdit la duplication sans lien vers une definition unique.

## 2. Gameplay

Les mecaniques validees (etapes 1 a 8) sont detaillees a un niveau rigoureux : vitesses, accelerations, hitboxes, fenetres actives en secondes, croisees avec des mesures sur des captures video reelles (dont des captures maison a 60fps) et verifiees arithmetiquement (exemple : fleche de squelette 600px/s x 1.6s = 960px de portee, coherent avec la valeur annoncee).

**Zones d'ombre malgre l'etape 7 validee :**

- La duree de l'invulnerabilite de reprise apres reapparition au checkpoint est annoncee dans [Etats-du-Joueur.md](../GDD/Joueur/Etats-du-Joueur.md) et [Invulnerabilite.md](../GDD/Combat/Invulnerabilite.md) comme devant etre fixee "a l'etape 7". L'etape 7 est validee et cette valeur n'existe toujours nulle part.
- La regle de mort instantanee ou de chute hors des limites d'un niveau est renvoyee au meme endroit et jamais definie.

**Cas limites non tranches :**

- Le caractere obligatoire ou facultatif du Double saut pendant un combat de boss n'est tranche que pour le Golem de la Foret ; rien ne garantit que les cinq autres golems trancheront ce point de la meme facon.
- Aucune regle d'invulnerabilite (ou son absence explicite) pendant l'ouverture d'un coffre, moment ou Imran est immobile et sans defense.
- Le comportement d'Echap pendant les 3.00s verrouillees du reveil d'un boss n'entre dans aucun des quatre niveaux de priorite listes dans [Priorites-des-Actions.md](../GDD/Controles/Priorites-des-Actions.md).
- Aucune exception de degats "boss different de 1 coeur" n'est encore posee, alors que [Degats.md](../GDD/Combat/Degats.md) previenait qu'une exception devrait etre annoncee et validee a l'etape 9.

## 3. Architecture technique (Godot 4)

Le TDD ne permet aujourd'hui de concevoir aucune scene, aucun noeud, aucune ressource technique. Les 41 fichiers de [docs/TDD/](../TDD/README.md) sont sans exception un gabarit identique de 35 lignes, sans autoload, sans arborescence de scene, sans nom de classe, sans signal, sans champ de ressource, sans format de sauvegarde. Ce n'est pas anormal vu l'avancement du GDD, mais cela signifie qu'un developpeur Godot ne peut rien construire a partir du TDD seul a ce stade.

Ce que le GDD permet deja de preparer : les valeurs du joueur ([Statistiques-Imran.md](../GDD/Joueur/Statistiques-Imran.md)), les hitboxes de combat, les regles communes d'ennemis et de boss sont assez precises pour deriver directement des scripts et des noeuds Godot.

**Manques structurels a corriger avant de figer le TDD :**

- Aucun emplacement pour un controleur de camera technique dans [TDD/Scripts](../TDD/Scripts/README.md), alors que `Camera.md` est l'un des documents les plus chiffres de tout le projet.
- Aucun emplacement pour un systeme de cinematique ou de dialogue, alors que l'etape 13 du GDD (Narration) est planifiee.
- Aucune decision sur l'architecture de la machine a etats (enum interne ou noeuds d'etat separes), malgre trois familles d'entites (Joueur, Ennemis, Boss) qui en dependent toutes.

## 4. Architecture logicielle

Systemes recommandes, en s'appuyant sur ce qui est deja specifie :

- **GameManager** (autoload) : etat de progression, flux de scenes.
- **Machine a etats generique** reutilisable Joueur/Ennemi/Boss, pour eviter trois implementations divergentes.
- **InputManager** : la doc [Controles/](../GDD/Controles/README.md) est deja tres detaillee (priorites, memoire de commande, remappage par groupes) et quasi prete a coder.
- **SaveManager** : slot unique, declencheurs deja listes dans [Sauvegarde.md](../GDD/Systemes/Sauvegarde.md).
- **AudioManager** : la hierarchie sonore a six niveaux ([10-Direction-Sonore/README.md](../Concept-Game/10-Direction-Sonore/README.md)) donne une bonne base de bus.
- **CameraController** dedie (absent du TDD, voir section 3).
- **EnemyAI / BossAI** : classe de base par famille.
- **CombinationSpawner** : systeme dedie pour appliquer la matrice de 15 paires et 10 triples de [Combinaisons-et-Progression.md](../GDD/Ennemis/Combinaisons-et-Progression.md). Ce systeme n'apparait nulle part dans l'architecture prevue alors que c'est l'un des systemes de gameplay les plus subtils du jeu.
- **ChestKeySystem**, **CheckpointManager**, **DamageSystem** partage.
- **DialogueSystem / CutsceneManager** : absent du plan (voir section 3).

## 5. Donnees

Modeles deja bien cadres par le GDD : PlayerStats, EnemyData par famille, BossData (Golem de la Foret comme gabarit).

**Modeles manquants :**

- **SaveData** est defini a minima (niveau atteint, six cles, indicateur "Aventure terminee") mais rien n'existe pour les reglages d'options (volumes, remappage, accessibilite) : pas clair si c'est un fichier separe du save de progression, ni son format.
- **LevelData** ne peut pas exister tant que [GDD/Niveaux](../GDD/Niveaux/README.md) reste un ensemble de fiches vides.
- **Format de sauvegarde concret** (JSON, Resource Godot, ConfigFile) : aucune decision prise.
- **Schema de spawn des ennemis et des combinaisons** : la regle de gameplay est riche mais rien n'indique si elle sera codee en dur scene par scene ou pilotee par des donnees, decision a prendre avant de rediger les fiches de niveaux (etapes 11 et 12).

## 6. UX

Les ecrans (menu principal, options, pause, HUD, game over, victoire) sont bien penses au niveau vision dans [11-Interface/](../Concept-Game/11-Interface/README.md), avec de bons reflexes d'accessibilite : jamais d'information basee uniquement sur la couleur, sous-titres systematiques, confirmations en deux temps pour les actions destructrices.

**Manques :**

- Aucune transition entre niveaux n'est decrite (fondu, ecran de chargement, duree).
- Aucun retour "sante faible" (dernier coeur restant) : pour un public de 7 ans, un signal clair avant la mort serait pertinent et n'est mentionne nulle part.
- Les resolutions et valeurs par defaut des options sont renvoyees "au GDD et au TDD" et restent absentes des deux.
- [GDD/Interface](../GDD/Interface/README.md) est entierement a rediger malgre une bonne base de vision en amont.

## 7. Cas limites

**Deja bien couverts** : perte de ligne de vue avec memoire de position, aucune attaque ennemie declenchee hors ecran, deconnexion manette entrainant une pause automatique, conflits de remappage bloquant tant que non resolus, plafond de trois ennemis attaquant simultanement avec regle de priorite, contact ennemi-ennemi jamais solide, checkpoint qui reinitialise integralement l'etat de la zone.

**Non couverts :**

- Sauvegarde interrompue par un plantage ou une coupure : un seul emplacement, aucune sauvegarde de secours, [Gestion-des-Erreurs.md](../TDD/Sauvegarde/Gestion-des-Erreurs.md) est vide.
- Perte de focus de la fenetre (alt-tab) en dehors du cas "manette deconnectee".
- Joueur bloque dans le decor, sans mecanisme de recuperation generique.
- Pause pendant une cinematique (le systeme de cinematique n'existe pas encore).
- Redemarrage apres un plantage en plein combat de boss, sans sauvegarde intermediaire : perte de progression potentiellement frustrante.

## 8. Risques

**Techniques** : TDD a 0% de contenu reel en pleine etape 9 du GDD ; aucune machine a etats generique documentee ; systeme de combinaisons d'ennemis riche mais sans traduction technique prevue, avec risque d'implementation ad hoc et fragile.

**Game design** : progression strictement lineaire sans soupape de difficulte (pas de mode facile, pas de selection de niveau) pour un jeu destine explicitement a un enfant, le seul recours en cas de blocage etant de recommencer le niveau entier ; les six golems n'ont qu'une seule phase chacun avec seulement deux points de vie de plus et un habillage different entre eux, ce qui cree un risque reel de repetitivite si les cinq golems restants ne se differencient pas davantage que par leurs attaques.

**Maintenance** : 236 fichiers pour un projet a deux personnes ; le temps de coherence documentaire (statuts, liens, non-duplication) montre deja de premieres fissures (voir section 11).

**Dette technique** : sans TDD stabilise, le code risque de demarrer avant que les decisions d'architecture (autoloads, machine a etats, format de sauvegarde) soient prises, avec un risque accru si du code est ecrit au fil de l'eau sans TDD de reference.

## 9. Decoupage du developpement propose

**Phase 0 - Fondations documentaires et amorce technique (en parallele, pas en sequence stricte)**
Combler les deux trous ouverts depuis l'etape 7 ; demarrer des maintenant le TDD Architecture (Autoloads, convention de machine a etats) et Scripts (Player-Controller, Enemy-Base), sans attendre l'etape 18. Priorite critique.

**Phase 1 - Prototype technique (tranche jouable)**
GameManager, machine a etats generique, Player-Controller complet (deplacement, saut, dash, double saut), CameraController. Priorite critique.

**Phase 2 - Combat et un premier ennemi**
DamageSystem, Enemy-Base generique, Slimes (le plus simple, 1 PV) en tranche verticale. Priorite critique.

**Phase 3 - Reste des ennemis et systeme de combinaisons**
Chauves-Souris, Squelettes, Serpents, Zombies, plus un vrai composant de spawn et de validation des combinaisons (a concevoir). Priorite haute.

**Phase 4 - Premier boss et premier niveau jouable**
BossBase, Golem de la Foret, systeme coffre/cle, Niveau 0 ou Niveau 1. Ecrire en parallele au moins un squelette des cinq autres golems pour eviter que BossBase soit surajuste au seul cas Golem-Foret. Bloque tant que [GDD/Niveaux](../GDD/Niveaux/README.md) reste vide : c'est le vrai goulot d'etranglement actuel.

**Phase 5 - Sauvegarde et HUD de base**
Systeme simple, deja bien specifie cote GDD.

**Phase 6 - Niveaux et golems restants**
Une fois le gabarit valide en phase 4, derouler les cinq niveaux et golems restants. Depend des etapes 10 a 12 du GDD, aujourd'hui le plus gros trou documentaire.

**Phase 7 - Narration et cinematiques**
Necessite d'abord un emplacement technique dedie (absent aujourd'hui du TDD).

**Phase 8 - Integration art et son, options et accessibilite, polish, tests avec l'enfant destinataire**
A faire tot et souvent, pas seulement en fin de projet : c'est le vrai testeur cible.

## 10. Documentation manquante

- Format de sauvegarde concret (schema JSON ou equivalent).
- Diagrammes d'etat visuels pour Joueur, Ennemi et Boss (actuellement seulement des tableaux texte).
- Diagramme d'architecture ou de classes pour le TDD (0% de contenu actuellement).
- Convention de style GDScript (fiche vide, utile des la premiere ligne de code).
- Plan de production des assets avec estimation d'effort, prevu aux etapes 15 et 16 mais absent.
- Journal des audits croises : le processus impose un audit croise obligatoire apres chaque etape paire validee ; aucune trace ecrite de ces audits n'a ete trouvee.
- Journal de decisions ("pourquoi une seule phase par golem", "pourquoi pas de mode facile") pour eviter de re-debattre des choix deja tranches.

## 11. Questions ouvertes

1. Duree exacte de l'invulnerabilite de reprise apres reapparition (promise a l'etape 7, jamais chiffree).
2. Regle de mort instantanee ou de chute hors des limites du niveau (idem).
3. Contenu reel des cinq golems restants et de Tata Lisa, et statut obligatoire ou facultatif du Double saut pour chacun.
4. La regle "une seule phase par golem" est-elle definitive malgre le risque de repetitivite sur six combats ?
5. Quelles exceptions de degats (different de 1 coeur) seront introduites pour des ennemis ou des boss specifiques ?
6. Niveaux encodes a la main scene par scene, ou pilotes par des donnees ? Decision non prise, impacte directement la redaction des etapes 11 et 12.
7. Format de sauvegarde technique et politique en cas de corruption ou d'erreur d'ecriture.
8. Architecture de la machine a etats (enum interne ou noeuds separes) ?
9. Le jeu se met-il en pause automatiquement en cas de perte de focus de la fenetre ?
10. Existe-t-il un filet de securite en cas de blocage du joueur dans le decor ?
11. Valeurs par defaut et plage de reglage des options d'accessibilite (secousses, flashs) ?
12. Specification technique minimale visee (systeme, resolution, machine) ?
13. A partir de quelle etape l'enfant destinataire testera-t-il reellement le jeu ?
14. Qui execute concretement les audits croises obligatoires, et ou sont-ils consignes ?

## 12. Note finale

| Critere | Note sur 10 | Justification |
|---|---:|---|
| Clarte | 8 | Langage precis, valeurs chiffrees, structure coherente ; penalise par les entorses au principe "Concept Game sans chiffres" et la derive orthographique Valide/Valide-accentue. |
| Completude | 3 | 8 etapes sur 18 validees, etape 9 realisee a 1 golem sur 6, TDD a 0% de contenu reel. Ce qui est ecrit est solide, mais c'est encore une minorite du document final. |
| Faisabilite | 6 | Scope ambitieux (sept zones, six boss uniques, narration complete) pour deux personnes sans echeance ; appuye sur une reference solide qui reduit le risque de conception, mais le rythme documentation/code doit etre surveille. |
| Maintenabilite | 7 | Excellente hierarchie source de verite et conventions strictes sur le papier ; premiers signes de derive deja visibles (statuts incoherents, phrases obsoletes non nettoyees, valeurs dupliquees). |
| Qualite technique | 8 | Valeurs precises au niveau de l'image, croisees avec des captures video reelles et verifiees arithmetiquement ; comportements d'ennemis et de boss anticipant de vrais cas limites. Penalise car le TDD n'existe pas encore. |

**Recommandation** : ne pas demarrer la production complete maintenant, mais demarrer le prototypage technique immediatement, en parallele de la redaction des etapes 10 a 18. Tout ce qui est valide (Joueur, Combat, Ennemis, Systemes, Golem de la Foret) est suffisamment precis pour coder une tranche verticale complete des aujourd'hui. Attendre la fin du GDD avant d'ouvrir Godot ferait perdre l'occasion de tester en moteur des valeurs qui n'ont encore ete validees que sur le papier.

## Checklist priorisee

### Critique

1. Combler les deux trous ouverts depuis l'etape 7 validee (invulnerabilite de reprise, mort ou chute hors niveau).
2. Decider du format de sauvegarde et de la gestion des erreurs avant tout code du SaveManager (slot unique = risque de perte totale).
3. Ecrire au moins un squelette (attaques et phases minimales) des cinq golems et de Tata Lisa restants avant de figer BossBase.
4. Ajouter des emplacements TDD pour CameraController et pour le systeme narration/cinematique.
5. Trancher l'architecture data-driven ou non des niveaux et des combinaisons avant de rediger les etapes 11 et 12.

### Important

6. Nettoyer les deux phrases "reste a definir" obsoletes dans [Golem-Foret.md](../GDD/Boss/Golem-Foret.md).
7. Uniformiser l'orthographe du statut "Valide" et regulariser le statut hors convention "Reference analysee" trouve dans [Ennemis](../GDD/Ennemis/README.md).
8. Clarifier si Echap fonctionne pendant les 3.00s verrouillees de reveil d'un boss.
9. Definir explicitement l'invulnerabilite, ou son absence, pendant l'ouverture d'un coffre.
10. Ajouter un retour "sante faible" clair et adapte a 7 ans.
11. Fixer la resolution et la plateforme minimale ciblees, renvoyees mais jamais definies.
12. Documenter le comportement en cas de perte de focus de la fenetre.

### Amelioration

13. Retirer ou centraliser les valeurs chiffrees dupliquees du Concept Game (Camera, Palette, secousses).
14. Journaliser les audits croises obligatoires, dont aucune trace n'existe actuellement.
15. Ajouter un journal de decisions de design.
16. Demarrer le prototypage technique en parallele des etapes 10 a 18 plutot qu'apres.

## Documents references

- [PLAN-GDD.md](../GDD/PLAN-GDD.md)
- [Cadre/Conventions-Documentaires.md](../GDD/Cadre/Conventions-Documentaires.md)
- [Cadre/Perimetre-et-Sources.md](../GDD/Cadre/Perimetre-et-Sources.md)
- [Boss/Regles-Communes.md](../GDD/Boss/Regles-Communes.md)
- [Boss/Golem-Foret.md](../GDD/Boss/Golem-Foret.md)
- [Ennemis/Regles-Communes.md](../GDD/Ennemis/Regles-Communes.md)
- [Ennemis/Combinaisons-et-Progression.md](../GDD/Ennemis/Combinaisons-et-Progression.md)
- [Joueur/Etats-du-Joueur.md](../GDD/Joueur/Etats-du-Joueur.md)
- [Combat/Invulnerabilite.md](../GDD/Combat/Invulnerabilite.md)
- [Combat/Degats.md](../GDD/Combat/Degats.md)
- [Controles/Priorites-des-Actions.md](../GDD/Controles/Priorites-des-Actions.md)
- [Systemes/Sauvegarde.md](../GDD/Systemes/Sauvegarde.md)
- [TDD/README.md](../TDD/README.md)
- [TDD/Sauvegarde/Gestion-des-Erreurs.md](../TDD/Sauvegarde/Gestion-des-Erreurs.md)
