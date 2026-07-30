# Valeurs de reference

> **Statut :** Valide

## Objectif

Classer les valeurs utilisees pendant l'equilibrage afin de distinguer les ajustements de level design des modifications de regles deja validees.

Ce document ne remplace pas les fiches du joueur, du combat, des ennemis, des boss et des systemes. Chaque valeur detaillee conserve sa fiche d'origine comme source de verite.

## Niveau 1 - Ajustement libre

Ces elements peuvent etre ajustes pendant le prototype sans modifier une regle de gameplay :

- position des ennemis dans leur zone autorisee ;
- separation initiale entre les ennemis dans le respect des minimums valides ;
- largeur d'une zone de rencontre ;
- longueur d'une zone sure ;
- largeur et position des plateformes ;
- ordre des rencontres dans une meme categorie de pression ;
- nombre de sequences dangereuses dans les plages validees ;
- duree et emplacement des respirations ;
- repartition entre les pressions simple, intermediaire et exigeante selon les pourcentages valides.

Chaque ajustement doit continuer a respecter :

- les distances minimales des combinaisons d'ennemis ;
- les trajectoires d'esquive obligatoires ;
- le maximum de dangers simultanes ;
- la lisibilite des preparations ;
- les limites de camera et de terrain deja validees.

## Niveau 2 - Nouvelle validation obligatoire

Ces valeurs peuvent etre modifiees uniquement si les ajustements libres restent insuffisants :

- vitesse de deplacement d'Imran ;
- acceleration et freinage d'Imran ;
- hauteur et duree des sauts ;
- vitesse, distance et duree du Dash ;
- duree d'une attaque ;
- vitesse d'un projectile ;
- duree d'une preparation ou d'une recuperation ;
- dimensions d'une zone de collision, de degat ou de vulnerabilite ;
- points de vie d'un ennemi ou d'un boss ;
- degats infliges par une attaque ;
- duree d'invulnerabilite ou de recul.

Une modification de niveau 2 exige :

1. un resultat de test montrant que les ajustements de niveau 1 sont insuffisants ;
2. l'identification de la fiche source de la valeur ;
3. une nouvelle decision de Rems ;
4. la mise a jour de toutes les references concernees ;
5. un nouveau test de non-regression.

## Niveau 3 - Regles verrouillees

Les regles suivantes ne peuvent pas etre modifiees pendant un simple test d'equilibrage :

- Imran possede `3 coeurs` ;
- Imran commence une nouvelle sequence avec `3 vies` ;
- un impact valide retire `1 coeur` ;
- toutes les capacites principales sont disponibles des le niveau 0 ;
- le Dash reste utilisable uniquement au sol ;
- le Smash Tranchant reste impossible pendant un saut ou une chute ;
- le Bouclier de lumiere reste automatique face aux projectiles frontaux compatibles ;
- le jeu conserve une seule difficulte ;
- les niveaux restent lineaires et ne peuvent pas etre rejoues ;
- les ennemis ordinaires ne rendent aucun coeur ;
- le feu de camp restaure les coeurs sans restaurer les vies.

Toute modification d'une regle verrouillee constitue une nouvelle decision de conception et non un ajustement d'equilibrage.

## Ordre d'intervention

En cas de difficulte excessive :

1. modifier un element de niveau 1 ;
2. retester la situation ;
3. essayer les autres ajustements de niveau 1 pertinents ;
4. demander une nouvelle validation avant toute modification de niveau 2 ;
5. ne jamais modifier silencieusement une regle de niveau 3.

## Fiches sources par domaine

| Domaine | Fiches sources | Valeurs controlees |
|---|---|---|
| Mouvement d'Imran | [Statistiques](../Joueur/Statistiques-Imran.md), [Deplacement](../Joueur/Deplacement.md), [Saut](../Joueur/Saut.md), [Double saut](../Joueur/Double-Saut.md), [Dash](../Joueur/Dash.md) | Vitesses, accelerations, hauteurs, durees et distances |
| Combat d'Imran | [Attaque normale](../Combat/Attaque-Normale.md), [Smash Tranchant](../Combat/Smash-Tranchant.md), [Blocage](../Combat/Blocage.md), [Degats](../Combat/Degats.md), [Recul](../Combat/Recul.md), [Invulnerabilite](../Combat/Invulnerabilite.md) | Degats, portees, durees, charge, defense et reactions |
| Ressources du joueur | [Coeurs et vies](../Systemes/Coeurs-et-Vies.md), [Checkpoints](../Systemes/Checkpoints.md), [Game Over](../Systemes/Game-Over.md) | Coeurs, vies, reprises et conditions d'echec |
| Ennemis ordinaires | [Regles communes](../Ennemis/Regles-Communes.md), [Slimes](../Ennemis/Slimes.md), [Chauves-souris](../Ennemis/Chauves-Souris.md), [Squelettes](../Ennemis/Squelettes.md), [Serpents](../Ennemis/Serpents.md), [Zombies](../Ennemis/Zombies.md) | PV, detection, attaques, deplacements et reactions |
| Combinaisons d'ennemis | [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md) | Distances minimales, groupes autorises et progression par niveau |
| Boss | [Regles communes](../Boss/Regles-Communes.md), [Sommaire des boss](../Boss/README.md) | PV, collisions, vulnerabilite, rythme, attaques et recompenses |
| Progression globale | [Progression](../Systemes/Progression.md), [Courbe de difficulte](Courbe-de-Difficulte.md) | Ordre des niveaux, pression, durees, densites et apprentissages |
| Evaluation | [Tests d'equilibrage](Tests.md) | Tolerance aux echecs, mesures, protocole et validation |

## Regle de source de verite

- La fiche source conserve la definition complete de sa valeur.
- Ce document indique ou verifier la valeur sans la recopier.
- En cas de contradiction, la fiche source validee reste prioritaire.
- Une modification validee met a jour la fiche source avant ses documents dependants.
- Les valeurs propres a l'equilibrage sont definies dans la Courbe de difficulte et dans les Tests d'equilibrage.

## Criteres de validation

Le document est valide si :

- chaque domaine possede une fiche source identifiable ;
- les trois niveaux de modification sont distincts ;
- une modification de niveau 2 exige une nouvelle validation ;
- les regles verrouillees ne peuvent pas changer silencieusement ;
- les liens vers les fiches sources fonctionnent ;
- aucune valeur detaillee n'est dupliquee sans necessite.
