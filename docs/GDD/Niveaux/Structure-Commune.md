# Structure commune des niveaux

> **Statut :** Valide

## Objectif

Definir les regles structurelles partagees par les six niveaux principaux et les exceptions du niveau 0 avant la redaction detaillee de chaque parcours.

## Entree des niveaux principaux

- Chaque niveau principal commence dans une zone sure.
- Imran commence avec `3 coeurs`, `3 vies` et une vitesse nulle.
- Imran recoit le controle immediatement.
- Aucun ennemi, projectile, obstacle dangereux ou autre source de degat n'est actif dans cette zone.
- Le decor permet d'identifier rapidement le theme du niveau.
- La premiere sequence dangereuse commence seulement apres une courte progression controlee par le joueur.
- La premiere source de danger se trouve a au moins `768 px` du point d'apparition.
- Cette distance correspond a `12 grilles logiques` et a environ `3.2 s` de marche a `240 px/s`.
- Le joueur peut traverser cette zone plus rapidement avec le Dash sans declencher de delai obligatoire.

## Rythme commun des niveaux principaux

Le parcours precedant le golem est divise en quatre grandes sections :

| Section | Fonction |
|---:|---|
| 1 | Rappeler les acquis dans des situations accessibles |
| 2 | Faire progresser la pression jusqu'au checkpoint |
| Checkpoint | Diviser le parcours approximativement en deux moities |
| 3 | Reprendre avec une pression intermediaire |
| 4 | Proposer la partie la plus exigeante sans nouvelle regle |
| Fin du parcours | Offrir une respiration, le feu de camp, puis l'acces a l'arene |

- Les sections 1 et 2 se trouvent avant le checkpoint.
- Les sections 3 et 4 se trouvent apres le checkpoint.
- Le checkpoint est place a la frontiere entre les sections 2 et 3.
- Les sequences dangereuses sont reparties dans ces quatre sections selon les plages validees dans la courbe de difficulte.
- La section 1 porte la pression simple du debut, les sections 2 et 3 portent la pression intermediaire du milieu et la section 4 porte la pression exigeante de fin.
- Cette repartition conserve les proportions communes de `30 %`, `40 %` et `30 %` sans imposer le meme parcours a tous les niveaux.
- Le golem reste le pic de difficulte du niveau.

## Zones de respiration

- Une zone de respiration mesure au minimum `384 px`.
- Cette longueur correspond a `6 grilles logiques` et a environ `1.6 s` de marche a `240 px/s`.
- Elle ne contient aucun ennemi actif, projectile, obstacle dangereux ou autre danger immediat.
- Une zone de respiration separe les sections 1 et 2.
- Le checkpoint et sa zone sure remplacent la respiration entre les sections 2 et 3.
- Une zone de respiration separe les sections 3 et 4.
- Le feu de camp et sa zone sure remplacent la derniere respiration avant l'arene.
- Une respiration supplementaire est ajoutee dans une section si elle est necessaire pour ne jamais enchainer plus de deux sequences dangereuses.

## Zone du checkpoint

- Le checkpoint se trouve au centre d'une zone sure de `768 px`.
- Cette zone conserve au minimum `384 px` libres de chaque cote de la pancarte.
- Le sol est plat, stable et entierement praticable.
- La zone ne contient ni pente, ni fosse, ni plateforme mobile, ni obstacle dangereux.
- Aucun ennemi ne peut apparaitre, entrer ou attaquer dans cette zone.
- Aucun projectile provenant d'une section voisine ne peut atteindre la zone.
- La camera est deja stabilisee sur Imran apres une reapparition.
- Le joueur peut repartir vers la section 3 sans subir de degat avant de pouvoir agir.

## Zones de reception

- Un saut, un Dash ou un Double saut obligatoire se termine toujours sur une zone de reception sure.
- Cette zone offre au minimum `256 px` praticables apres le point de reception attendu.
- Cette longueur correspond a `4 grilles logiques` et a environ `1.1 s` de marche a `240 px/s`.
- Aucun ennemi ne se trouve dans cette distance au moment de la premiere reception.
- Aucun projectile, piege ou obstacle dangereux ne couvre le point de reception.
- Le joueur peut observer la situation suivante avant de s'y engager.

## Placement des ennemis ordinaires

- Chaque ennemi appartient a une zone de rencontre predeterminee.
- Un ennemi ne peut jamais quitter cette zone pour poursuivre Imran dans une autre section.
- Une zone de rencontre ne chevauche jamais une entree, une respiration, un checkpoint, un feu de camp ou une zone de reception sure.
- Les projectiles ennemis ne peuvent pas traverser la limite d'une zone sure.
- Quitter une rencontre ne transporte aucun ennemi dans la rencontre suivante.
- Plusieurs groupes ne peuvent donc pas se cumuler par poursuite.
- Les ennemis ordinaires ne ferment pas automatiquement le passage et ne deviennent pas une condition generale de fin du niveau.
- Les limites de patrouille, de detection et d'attaque propres a chaque famille restent definies dans les fiches des ennemis.
- Un ennemi doit etre entierement visible a l'ecran avant d'activer sa detection ou de preparer une attaque.
- Aucun ennemi ne peut commencer une attaque depuis une position hors de l'ecran.
- Aucun projectile ennemi ne peut etre lance depuis une position hors de l'ecran.
- Le placement doit conserver cette visibilite avec le suivi de camera normal dans les deux directions.

## Lisibilite des obstacles obligatoires

- Le point de depart, le danger et la zone de reception sont visibles simultanement avant toute action de deplacement obligatoire.
- Cette regle concerne le saut, le Dash au sol, le Double saut et leurs enchainements valides.
- La camera montre la destination avant que le joueur atteigne le point ou il doit s'engager.
- Aucun saut obligatoire ne vise une plateforme entierement hors de l'ecran.
- Aucun obstacle ne demande un essai aveugle ou la memorisation d'une destination cachee.
- La difficulte peut venir de l'execution, du rythme ou d'une combinaison deja apprise, mais jamais d'une information absente.
- Une nouvelle utilisation d'un obstacle est presentee sans ennemi actif avant d'etre combinee a une rencontre.
- Un danger de plateforme et des ennemis sont combines uniquement apres avoir ete pratiques separement.
- Le decor au premier plan ne peut jamais masquer Imran, un bord, une reception ou un danger utile a la decision.
- Aucun passage obligatoire ne demande une precision au pixel pres.

## Zone du feu de camp

- Le feu de camp precedant le golem se trouve au centre d'une zone sure de `768 px`.
- Cette zone conserve au minimum `384 px` libres avant et apres le feu de camp.
- Elle ne contient aucun ennemi, projectile, piege ou obstacle dangereux.
- Aucun ennemi de la section 4 ne peut entrer ou attaquer dans cette zone.
- Le joueur conserve le controle et choisit volontairement d'utiliser le feu de camp avec la commande `Interaction`.
- Le feu de camp restaure uniquement les coeurs selon les regles deja validees.
- L'entree de l'arene se trouve apres cette zone sure.
- Le passage dans l'arene declenche ensuite la fermeture des barrieres et la presentation du golem selon les regles communes des boss.

## Sortie et transition d'un niveau principal

- La victoire contre le golem seule ne termine jamais le niveau.
- Imran rejoint la zone de recompense et ouvre volontairement le coffre.
- La cle est ajoutee a la progression avant le changement de scene.
- La sauvegarde automatique doit etre terminee avant le debut de la transition.
- L'ecran effectue un fondu noir de `0.50 s`.
- Le niveau suivant est charge pendant l'ecran noir.
- Imran commence le niveau suivant avec `3 coeurs` et `3 vies` dans sa zone d'entree sure.
- L'image reapparait avec un fondu de `0.50 s`.
- Une courte sequence narrative pourra etre inseree entre les deux niveaux pendant l'etape 13 sans modifier la sauvegarde ni le point de reprise.
- Apres la sixieme cle, la meme transition conduit au point de reprise situe devant le donjon avant Tata Lisa.
- La conclusion suivant Tata Lisa reste une exception definie dans sa fiche et pendant l'etape 13.

## Circulation et retour en arriere

- Le chemin principal progresse horizontalement de la gauche vers la droite.
- Imran peut se deplacer dans les deux directions et revenir dans les sections deja traversees.
- Aucun changement de section, checkpoint ou feu de camp ne ferme automatiquement le passage derriere lui.
- Les limites des rencontres empechent les ennemis de suivre Imran pendant ce retour.
- Le franchissement de l'entree de l'arene constitue le seul point de non-retour de la tentative en cours.
- La barriere gauche empeche alors de revenir dans le niveau pendant le combat et l'acces a la recompense.
- Apres une perte de vie, Imran reapparait selon le checkpoint actif et l'entree de l'arene redevient accessible.
- Apres la recuperation de la cle, le niveau termine ne peut plus etre rejoue.

## Continuite de la camera

- La camera suit Imran sans coupure entre l'entree, les quatre sections, le checkpoint et le feu de camp.
- Aucun fondu, chargement ou changement instantane de cadre ne separe les sections d'un meme niveau.
- Le suivi horizontal et vertical utilise les valeurs definies dans la fiche Camera.
- La camera ne depasse jamais la limite gauche ou droite du niveau.
- Elle commence deja stabilisee sur Imran au debut du niveau et apres chaque reapparition.
- Elle devient fixe uniquement apres l'entree dans l'arene du golem.
- Le defilement particulier vers la zone de recompense commence uniquement apres la defaite du golem.

## Limites du niveau

- Une limite solide empeche Imran de quitter le niveau par la gauche de la zone d'entree.
- La camera reste bloquee sur sa limite gauche tant que son suivi normal ne peut pas commencer.
- Aucune source de danger n'est placee hors du cadre initial pour attaquer la zone d'entree.
- La limite droite du parcours principal correspond a l'entree de l'arene et a ses barrieres pendant la tentative.
- La limite droite finale se trouve apres la zone de recompense.
- Imran ne peut jamais sortir du cadre jouable ni franchir une limite de camera.
- Les zones sures sont entierement comprises dans les limites du niveau et restent visibles avec le cadrage normal.

## Arene du golem et recompense

- L'arene commence apres la zone sure du feu de camp.
- Le franchissement de son entree declenche les barrieres, le cadrage fixe et la presentation commune de `3.00 s`.
- La zone de combat mesure `1280 px` de largeur utile et utilise un sol plat place a `y = 896 px` en `1920 x 1080`.
- Elle ne contient aucune plateforme, pente, fosse ou obstacle de deplacement.
- Les attaques, dimensions, positions et exceptions restent definies dans la fiche du golem concerne.
- Le coffre reste hors du cadre pendant le combat.
- Apres la defaite, la barriere droite ouvre une zone de recompense sure de `640 px`.
- La camera accompagne alors uniquement la progression vers la droite selon les valeurs deja validees.
- Le centre du coffre se trouve a la position locale `x = 1824 px`.
- Imran doit rejoindre le coffre et utiliser la commande `Interaction` a `56 px` ou moins.
- La recuperation de la cle declenche la sauvegarde et la transition de fin du niveau.
- L'ensemble combat et recompense mesure `1920 px` accessibles.
- Les regles detaillees restent centralisees dans la fiche des regles communes des boss afin d'eviter deux sources de verite.

## Exception du niveau 0

- Le Village des Bles reste un tutoriel lineaire et n'utilise pas les quatre grandes sections des niveaux principaux.
- Son entree respecte la meme distance sure minimale de `768 px` avant la premiere source de danger.
- Chaque action est enseignee par une boucle `pancarte, pratique, respiration`.
- Les zones de respiration mesurent au minimum `384 px` lorsqu'elles separent deux sequences dangereuses.
- Les actions de deplacement obligatoires conservent une reception sure minimale de `256 px`.
- Le point de depart, le danger et la reception restent visibles simultanement.
- Le niveau ne contient aucun checkpoint, golem, coffre de fin ou cle.
- Les quelques ennemis ordinaires restent limites a leur zone de rencontre et ne peuvent pas entrer dans les zones de tutoriel sures.
- Un feu de camp est place dans une zone sure a la fin du parcours.
- Son utilisation reste volontaire et restaure uniquement les coeurs.
- Atteindre la sortie apres ce feu de camp sauvegarde la fin du tutoriel et debloque la Foret enchantee.
- La transition utilise le meme fondu noir de `0.50 s`, puis le meme fondu d'ouverture de `0.50 s`.
- La Foret enchantee commence ensuite avec `3 coeurs` et `3 vies` comme tout niveau principal.
- Le niveau 0 ne peut plus etre rejoue apres cette sauvegarde.

## Sources

- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Checkpoints](../Systemes/Checkpoints.md)
- [Camera](../Systemes/Camera.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Coffres et cles](../Systemes/Coffres-et-Cles.md)
- [Sauvegarde](../Systemes/Sauvegarde.md)
- [Courbe de difficulte](../Equilibrage/Courbe-de-Difficulte.md)
- [Regles communes des ennemis](../Ennemis/Regles-Communes.md)
- [Combinaisons et progression des ennemis](../Ennemis/Combinaisons-et-Progression.md)
- [Regles communes des boss](../Boss/Regles-Communes.md)

## Criteres de validation

- les six niveaux principaux utilisent une entree sure puis quatre grandes sections ;
- le checkpoint se trouve entre les sections 2 et 3 dans une zone sure mesurable ;
- aucune zone sure ne peut etre atteinte par un ennemi, un projectile ou un danger voisin ;
- deux sequences dangereuses au maximum se suivent sans respiration ;
- chaque mouvement obligatoire montre son depart, son danger et sa reception ;
- chaque reception obligatoire conserve `256 px` sans danger immediat ;
- aucun ennemi ne detecte ou n'attaque Imran avant d'etre entierement visible ;
- les rencontres restent separees et ne peuvent pas se cumuler par poursuite ;
- Imran peut revenir dans les sections precedentes avant l'entree dans l'arene ;
- la camera defile sans coupure et respecte les limites du niveau ;
- le feu de camp precede toujours l'arene dans une zone sure ;
- l'arene, la recompense, le coffre et la cle respectent les valeurs deja validees ;
- la sauvegarde precede toujours le fondu vers le niveau suivant ;
- le niveau 0 conserve sa boucle de tutoriel sans checkpoint, golem, coffre ou cle ;
- les distances, durees et regles restent compatibles avec le public cible et les etapes 7 a 10.
