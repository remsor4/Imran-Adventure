# Boucle de jeu et experience du joueur

> **Statut :** Valide

## Objectif

Ce document definit les actions repetees par le joueur, le deroulement d'un niveau, la progression sur toute l'aventure et les conditions de victoire ou d'echec.

Les valeurs de mouvement, de combat et d'equilibrage seront definies dans les etapes suivantes du GDD.

## Objectif permanent du joueur

L'objectif global reste toujours le meme : traverser les six niveaux, recuperer les six cles, vaincre Tata Lisa et liberer Aliyah.

Dans un niveau, l'objectif immediat est de suivre le chemin principal jusqu'au golem, de le vaincre, d'ouvrir son coffre et de recuperer sa cle.

Le joueur ne doit jamais avoir besoin de chercher un objectif cache ou un chemin alternatif pour progresser.

## Boucle courte

La boucle courte correspond aux actions repetees pendant l'exploration d'un niveau :

1. observer les plateformes, les ennemis et les dangers visibles ;
2. avancer sur le chemin principal ;
3. sauter ou utiliser une capacite de deplacement lorsque le parcours l'exige ;
4. eviter un danger ou affronter un ennemi ;
5. recevoir un retour visuel et sonore apres chaque action importante ;
6. atteindre la prochaine zone sure et recommencer la boucle.

Cette boucle alterne plateforme et combat sans interrompre longtemps le controle du joueur.

## Choix face aux ennemis ordinaires

Les ennemis ordinaires creent une menace sur le chemin mais ne constituent pas une condition de victoire du niveau.

Le joueur peut :

- les combattre avec la Shadow Sword ;
- charger le Smash Tranchant ;
- bloquer une attaque avec le Bouclier de lumiere ;
- les eviter lorsque le parcours et leur position le permettent.

Un ennemi peut temporairement controler un passage par sa position ou ses attaques, mais le jeu ne demande jamais de vaincre tous les ennemis d'un niveau.

Les golems et Tata Lisa sont les seuls ennemis obligatoires.

## Boucle complete d'un niveau

Chaque niveau principal suit cet ordre :

1. Imran entre dans le niveau avec trois coeurs et trois vies.
2. Le joueur identifie le chemin principal et commence la progression.
3. Une premiere partie combine plateformes, dangers et ennemis.
4. Imran atteint la pancarte situee approximativement au milieu du niveau.
5. Le joueur active la pancarte pour etablir le checkpoint temporaire.
6. Une seconde partie reprend la boucle courte avec une pression progressivement plus forte.
7. Imran atteint l'arene du golem.
8. Une courte presentation annonce le boss sans ralentir durablement le rythme.
9. Le joueur observe les attaques du golem, evite ou bloque les dangers et attaque pendant les ouvertures.
10. Le golem est vaincu et le coffre devient accessible.
11. Le joueur ouvre lui-meme le coffre.
12. Imran recupere la cle du niveau et la capacite eventuelle.
13. La progression est sauvegardee automatiquement.
14. Les coeurs et les vies sont restaures.
15. Le niveau suivant devient accessible.

La victoire contre le golem ne termine pas seule le niveau. L'ouverture du coffre et la recuperation de la cle sont obligatoires.

## Fonction du checkpoint

La pancarte divise le niveau en deux parties et limite la repetition apres la perte d'une vie.

Avant son activation :

- la perte d'une vie replace Imran au debut du niveau.

Apres son activation :

- la perte d'une vie replace Imran a la pancarte ;
- Imran revient avec trois coeurs ;
- le checkpoint reste actif uniquement pendant le niveau en cours.

La pancarte ne cree aucune sauvegarde permanente. Quitter le jeu pendant un niveau impose de recommencer ce niveau depuis le debut lors de la prochaine partie.

## Boucle des combats de boss

Chaque combat de golem repose sur la sequence suivante :

1. identifier le comportement et les attaques du boss ;
2. eviter ou bloquer une attaque clairement annoncee ;
3. reperer une ouverture ;
4. attaquer sans rester inutilement expose ;
5. observer la reaction du boss ;
6. recommencer jusqu'a vider sa barre de vie.

Le combat doit recompenser l'observation et l'apprentissage. Il ne doit pas dependre d'une attaque invisible, d'un hasard impossible a anticiper ou d'une execution incompatible avec le public cible.

Les phases, attaques, valeurs et ouvertures propres a chaque boss seront definies pendant l'etape 9.

## Boucle globale de l'aventure

| Progression | Action principale | Recompense permanente |
|---:|---|---|
| Niveau 1 | Traverser la Foret enchantee et vaincre son golem | Cle 1 |
| Niveau 2 | Traverser la Grotte mysterieuse et vaincre son golem | Cle 2 et Dash |
| Niveau 3 | Traverser le Lac gele et vaincre son golem | Cle 3 |
| Niveau 4 | Traverser le Desert oublie et vaincre son golem | Cle 4 et Double saut |
| Niveau 5 | Traverser le Volcan et vaincre son golem | Cle 5 |
| Niveau 6 | Traverser le Chateau de Tata Lisa et vaincre son golem | Cle 6 |
| Finale | Vaincre Tata Lisa devant le donjon | Liberation d'Aliyah et fin de l'aventure |

Le Dash enrichit la boucle courte a partir du troisieme niveau. Le Double saut l'enrichit a partir du cinquieme niveau.

Les capacites obtenues et les cles recuperees restent disponibles apres la sauvegarde automatique.

## Boucle du combat final

Apres la recuperation de la sixieme cle :

1. la progression est sauvegardee ;
2. Imran est place devant la porte du donjon avec trois coeurs et trois vies ;
3. Tata Lisa engage le combat final ;
4. le joueur applique les apprentissages de deplacement, d'attaque, de blocage et d'observation ;
5. Tata Lisa est vaincue ;
6. la Pierre du Chaos se brise et Tata Lisa prend la fuite ;
7. Imran ouvre les six verrous avec les six cles ;
8. Aliyah est liberee pendant la scene finale ;
9. la sauvegarde passe a l'etat `Aventure terminee`.

Le donjon ne contient aucune nouvelle boucle jouable apres Tata Lisa.

## Rythme recherche

Le rythme d'un niveau alterne :

- lecture rapide de la zone ;
- deplacement et plateforme ;
- danger ou combat court ;
- respiration visuelle ;
- nouvelle combinaison de dangers ;
- checkpoint ;
- seconde partie plus exigeante ;
- presentation et combat du golem ;
- ouverture du coffre et recompense.

Les respirations servent a laisser le joueur observer le decor, comprendre la prochaine difficulte et recuperer apres une sequence intense.

Les sequences narratives restent courtes pendant la progression. Les cinematiques principales se concentrent au debut et a la fin de l'aventure. Leur contenu detaille sera defini pendant l'etape 13.

Le rituel de Tata Lisa cree une urgence dans l'histoire, mais aucun chronometre ne limite le temps de jeu.

## Experience recherchee

La boucle doit produire les sensations suivantes :

- comprendre rapidement le prochain objectif ;
- anticiper un danger avant de le subir ;
- apprendre une regle, puis la reutiliser ;
- progresser sans se perdre ;
- ressentir une difficulte croissante mais juste ;
- obtenir une recompense claire apres chaque boss ;
- rester motive par le sauvetage d'Aliyah.

Le jeu ne repose pas sur un score, une monnaie, des objets optionnels a collectionner ou une limite de temps. Ces systemes ne peuvent etre ajoutes sans une nouvelle validation du Concept Game.

## Conditions de victoire

### Victoire d'un combat ordinaire

Un ennemi est vaincu lorsque sa condition de defaite est remplie. La destruction de tous les ennemis d'une zone n'est pas requise pour continuer, sauf si une future fiche de niveau valide explicitement une arene fermee.

### Victoire d'un combat de golem

Le golem est vaincu lorsque sa barre de vie est vide. Le coffre devient alors accessible.

### Victoire d'un niveau

Un niveau est termine lorsque :

1. son golem est vaincu ;
2. son coffre est ouvert ;
3. sa cle est recuperee.

La recuperation de la cle declenche immediatement la sauvegarde automatique et le deblocage du niveau suivant.

### Victoire finale

L'aventure est terminee lorsque Tata Lisa est vaincue, que les six verrous sont ouverts et qu'Aliyah est liberee.

## Conditions d'echec et reprise

| Echec | Consequence |
|---|---|
| Imran perd ses trois coeurs | Une vie est perdue |
| Une vie est perdue avant le checkpoint | Reapparition au debut du niveau avec trois coeurs |
| Une vie est perdue apres le checkpoint | Reapparition a la pancarte avec trois coeurs |
| Les trois vies sont perdues | Game Over et reprise du niveau depuis le debut |
| Le jeu est ferme pendant un niveau | Reprise du niveau depuis le debut lors du prochain lancement |
| Le jeu est ferme apres une cle sauvegardee | Reprise au niveau suivant avec les capacites deja obtenues |
| Le jeu est ferme apres la sixieme cle | Reprise devant le donjon avant Tata Lisa |

Un echec ne retire jamais une cle ou une capacite deja sauvegardee.

## Sources

- [Fiche generale du GDD](Fiche-Generale.md)
- [Boucle de jeu du Concept Game](../Concept-Game/05-Gameplay/Boucle-de-Jeu.md)
- [Deplacements](../Concept-Game/05-Gameplay/Deplacements.md)
- [Combat](../Concept-Game/05-Gameplay/Combat.md)
- [Points de controle](../Concept-Game/05-Gameplay/Points-de-Controle.md)
- [Boss](../Concept-Game/05-Gameplay/Boss.md)
- [Coffres](../Concept-Game/05-Gameplay/Coffres.md)
- [Cles](../Concept-Game/05-Gameplay/Cles.md)
- [Coeurs](../Concept-Game/05-Gameplay/Coeurs.md)
- [Vies](../Concept-Game/05-Gameplay/Vies.md)
- [Game Over](../Concept-Game/05-Gameplay/Game-Over.md)
- [Progression](../Concept-Game/06-Systemes/Progression.md)
- [Sauvegarde](../Concept-Game/06-Systemes/Sauvegarde.md)
- [Structure narrative](../Concept-Game/02-Histoire/Structure-Narrative.md)

## Criteres de validation

Le document est valide si :

- la boucle courte decrit clairement les actions repetees ;
- la boucle d'un niveau couvre le debut, le checkpoint, le golem, le coffre et la sauvegarde ;
- la boucle globale couvre les six niveaux et le combat final ;
- les conditions de victoire et d'echec sont explicites ;
- les ennemis ordinaires peuvent etre evites lorsque le parcours le permet ;
- seuls les boss sont toujours obligatoires ;
- aucun systeme de score, monnaie, collection optionnelle ou chronometre n'est introduit ;
- aucune valeur reservee aux prochaines etapes n'est inventee ;
- le contenu respecte le public cible et le Concept Game.
