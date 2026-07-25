# Combinaisons et progression des ennemis

> **Statut :** Valide

## Objectif

Verifier que les ennemis valides peuvent etre combines sans produire de situation confuse ou impossible a eviter, puis definir une progression reutilisable pendant la conception detaillee des niveaux.

## Portee du document

Ce document distingue :

- la coexistence de plusieurs ennemis dans une meme rencontre ;
- la possibilite pour plusieurs ennemis d'attaquer simultanement ;
- les conditions de terrain necessaires a une combinaison ;
- l'ordre d'introduction des familles ;
- le remplacement des Squelettes par les Zombies dans les deux derniers niveaux.

Il ne fixe pas encore le placement exact de chaque ennemi dans chaque salle. Ces placements seront definis pendant l'etape consacree aux niveaux a partir des regles validees ici.

## Cadre spatial 2D

- Imran Adventure est un jeu de plateforme en vue laterale 2D.
- Imran se deplace horizontalement de gauche a droite ou de droite a gauche.
- Le saut et le Double saut produisent un deplacement vertical dans ce meme plan.
- Il n'existe aucun deplacement vers l'avant ou l'arriere du decor.
- Toutes les largeurs sont mesurees sur l'axe horizontal.
- Toutes les hauteurs sont mesurees sur l'axe vertical.
- Une trajectoire d'esquive doit donc rester possible par un mouvement horizontal, un saut, un Double saut, un Dash au sol ou un blocage frontal.
- Aucun placement ne peut considerer le premier plan ou l'arriere-plan comme une voie de contournement.
- Les rencontres sont verifiees dans le cadre visible de reference `1920 x 1080`.

## Regles communes deja validees

- Les ennemis ordinaires ne sont jamais solides entre eux.
- Ils peuvent se traverser et se superposer sans se pousser.
- Ils ne peuvent ni se blesser, ni s'interrompre entre eux.
- Les projectiles ennemis traversent les autres ennemis.
- Un maximum de `3 ennemis ordinaires` peut occuper simultanement les emplacements d'attaque.
- Chaque attaque conserve sa preparation visuelle et sonore complete.
- Un ennemi ne commence aucune attaque avant d'etre visible a l'ecran.
- Une ligne de vue libre reste obligatoire pour chaque attaque active.
- Les ennemis restent dans leur zone de rencontre.
- Les ennemis ordinaires peuvent etre evites et ne sont pas une condition generale de fin du niveau.
- Aucun ennemi ordinaire ne rend de coeur a Imran.

## Familles utilisees dans la matrice

| Famille | Pression principale |
|---|---|
| Slime | Bond terrestre cyclique |
| Chauve-souris | Plongee aerienne |
| Epeiste | Danger corporel et lame frontale permanents |
| Archer | Fleche horizontale blocable de face |
| Serpent | Projection terrestre rapide a proximite |

Dans les niveaux 5 et 6, le Zombie epeiste remplace l'Epeiste et le Zombie archer remplace l'Archer. Les combinaisons restent identiques ; seuls leurs `3 PV` augmentent la duree de la rencontre.

## Statuts possibles

- `Autorisee` : la combinaison peut etre utilisee sur un terrain compatible sans regle supplementaire.
- `Conditionnelle` : la combinaison exige des conditions de placement precises.
- `Interdite` : la combinaison produit une pression trop confuse ou trop difficile pour le public cible.

## Matrice des paires

| Combinaison | Statut | Condition principale |
|---|---|---|
| Slime + Slime | Conditionnelle | Sol praticable de `960 px` et separation initiale de `256 px` |
| Chauve-souris + Chauve-souris | Conditionnelle | Zone de `1280 x 480 px` et points aeriens separes de `480 px` |
| Epeiste + Epeiste | Conditionnelle | Sol de `1280 px`, separation de `320 px` et aucun encerclement ferme |
| Archer + Archer | Conditionnelle | Meme hauteur de tir et au moins `192 px` de hauteur libre |
| Serpent + Serpent | Conditionnelle | Sol de `1280 px`, separation de `480 px` et hauteur libre de `192 px` |
| Slime + Chauve-souris | Conditionnelle | Zone de `1280 x 480 px` et separation initiale de `320 px` |
| Slime + Epeiste | Conditionnelle | Sol de `1280 px`, separation de `320 px` et zone d'atterrissage sure |
| Slime + Archer | Conditionnelle | Meme niveau de sol, `1280 px` de large et `192 px` de hauteur libre |
| Slime + Serpent | Conditionnelle | Sol de `1440 px`, separation de `480 px` et zone d'atterrissage sure |
| Chauve-souris + Epeiste | Conditionnelle | Zone de `1280 x 480 px` et atterrissage hors de la lame |
| Chauve-souris + Archer | Conditionnelle | Zone de `1440 x 480 px` et separation horizontale de `480 px` |
| Chauve-souris + Serpent | Conditionnelle | Zone de `1440 x 480 px` avec esquive horizontale obligatoire |
| Epeiste + Archer | Conditionnelle | Archer place `320 px` derriere l'Epeiste selon le sens d'entree |
| Epeiste + Serpent | Conditionnelle | Sol de `1440 px`, separation de `480 px` et preparation toujours visible |
| Archer + Serpent | Conditionnelle | Archer derriere le Serpent, sol de `1440 px` et separation de `480 px` |

## Paires validees

### Slime + Slime

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement apres la presentation d'un Slime seul.
- La surface praticable mesure au moins `960 px` de large.
- Les positions initiales des deux Slimes sont separees d'au moins `256 px`.
- Aucun passage etroit ou gouffre ne supprime les trajectoires d'esquive.
- Les deux Slimes peuvent preparer et executer leur bond simultanement.
- Ils peuvent donc occuper `2` emplacements d'attaque.
- Leurs compressions restent visibles avant chaque bond.
- Imran conserve la possibilite de sauter, reculer ou utiliser son Dash.
- Le placement doit eviter qu'un degat devienne inevitable.
- Cette combinaison reprend le comportement observe dans les captures Wonder Boy validees.

### Chauve-souris + Chauve-souris

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement apres la presentation d'une Chauve-souris seule.
- La zone visible mesure au moins `1280 px` de large.
- Elle offre au moins `480 px` de hauteur libre dans le plan 2D.
- Les points aeriens initiaux sont separes d'au moins `480 px` horizontalement.
- Aucun plafond bas, mur ou colonne ne bloque les plongees autorisees.
- Les deux Chauves-souris peuvent preparer et executer leur attaque simultanement.
- Elles peuvent donc occuper `2` emplacements d'attaque.
- Leurs courbes peuvent se croiser sans collision physique.
- Une trajectoire horizontale ou aerienne reste disponible pour Imran dans le meme plan 2D.
- Le joueur ne doit jamais avoir besoin d'une esquive vers l'avant ou l'arriere du decor.

### Epeiste + Epeiste

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement apres la presentation d'un Epeiste seul.
- La surface horizontale praticable mesure au moins `1280 px`.
- Les positions initiales sont separees d'au moins `320 px`.
- Aucun passage etroit ne place Imran entre deux lames sans sortie.
- Les Epeistes ne sont pas places de maniere a creer un encerclement ferme a courte distance.
- Ils peuvent se traverser selon les regles communes.
- Une trajectoire de saut, de Double saut ou de Dash au sol reste disponible.
- Les Epeistes n'occupent aucun emplacement d'attaque.
- Leur combinaison doit donc etre controlee par le placement et non par la limite des `3 emplacements`.

### Archer + Archer

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement apres la presentation d'un Archer seul.
- La surface horizontale praticable mesure au moins `1280 px`.
- Les positions initiales sont separees d'au moins `320 px`.
- Les deux Archers sont places sur le meme niveau de sol.
- Leurs fleches utilisent ainsi une hauteur de tir similaire.
- La zone offre au moins `192 px` de hauteur libre pour le saut.
- Aucun plafond bas ne supprime l'esquive verticale.
- Les Archers ne sont pas places aux deux extremites d'un passage etroit.
- Les deux tirs peuvent occuper `2` emplacements simultanement.
- Si des fleches arrivent de directions opposees, une esquive verticale reste possible.
- Le Bouclier protege uniquement contre la fleche arrivant de face.

### Serpent + Serpent

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement dans une progression avancee.
- Chaque Serpent a deja ete presente seul auparavant.
- La surface horizontale praticable mesure au moins `1280 px`.
- Les positions initiales sont separees d'au moins `480 px`.
- Aucun Serpent ne commence a moins de `160 px` d'Imran.
- La zone offre au moins `192 px` de hauteur libre.
- Aucun passage etroit ou encerclement initial ne supprime le saut ou le recul.
- Les deux Serpents peuvent preparer et executer leur projection simultanement.
- Ils peuvent donc occuper `2` emplacements d'attaque.
- Les deux preparations de `0.50 s` restent visibles avant les projections.

### Slime + Chauve-souris

- Statut : `Conditionnelle`.
- Les deux familles ont deja ete presentees seules.
- La zone visible mesure au moins `1280 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Le point aerien de la Chauve-souris est separe d'au moins `320 px` horizontalement de la position initiale du Slime.
- Aucun plafond bas, mur, colonne ou gouffre ne bloque les esquives.
- Le Slime et la Chauve-souris peuvent attaquer simultanement.
- Ils peuvent donc occuper `2` emplacements d'attaque.
- La compression du Slime et la preparation aerienne restent visibles.
- Une trajectoire horizontale ou verticale permet d'eviter les deux attaques dans le meme plan 2D.

### Slime + Epeiste

- Statut : `Conditionnelle`.
- Les deux familles ont deja ete presentees seules.
- La surface horizontale praticable mesure au moins `1280 px`.
- Les positions initiales sont separees d'au moins `320 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Aucun passage etroit ou placement initial de part et d'autre d'Imran ne cree un encerclement.
- Une zone d'atterrissage sure reste disponible apres l'esquive du bond.
- Le Slime peut occuper `1` emplacement d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- Le saut au-dessus du Slime ne doit pas obliger Imran a retomber sur l'Epeiste ou sa lame.

### Slime + Archer

- Statut : `Conditionnelle`.
- Les deux familles ont deja ete presentees seules.
- La surface horizontale praticable mesure au moins `1280 px`.
- Les positions initiales sont separees d'au moins `320 px`.
- Le Slime et l'Archer sont places sur le meme niveau de sol.
- La zone offre au moins `192 px` de hauteur libre.
- Aucun placement initial de part et d'autre d'Imran ne ferme un passage etroit.
- Le bond et le tir peuvent occuper `2` emplacements simultanement.
- Imran peut bloquer une fleche arrivant de face tout en se deplacant pour eviter le bond.
- Le saut utilise contre une fleche ne conduit pas automatiquement sur la trajectoire du Slime.

### Slime + Serpent

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement dans une progression avancee.
- Les deux familles ont deja ete presentees seules.
- La surface horizontale praticable mesure au moins `1440 px`.
- Les positions initiales sont separees d'au moins `480 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Aucun encerclement initial ou passage etroit ne ferme l'esquive.
- Le Slime et le Serpent peuvent occuper `2` emplacements simultanement.
- La compression de `0.10 s` du Slime reste visible avant son bond.
- La preparation de `0.50 s` du Serpent reste visible avant sa projection.
- Une zone d'atterrissage sure reste disponible apres le saut.
- La projection du Serpent ne traverse pas cette unique zone d'atterrissage au meme moment.

### Chauve-souris + Epeiste

- Statut : `Conditionnelle`.
- Les deux familles ont deja ete presentees seules.
- La zone visible mesure au moins `1280 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Le point aerien de la Chauve-souris est separe d'au moins `320 px` horizontalement de la position initiale de l'Epeiste.
- Aucun passage etroit, plafond bas, mur ou colonne ne bloque les esquives.
- La Chauve-souris peut occuper `1` emplacement d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- L'esquive de la plongee ne force pas Imran a atterrir sur l'Epeiste ou sa lame.
- Une zone d'atterrissage sure reste visible dans le plan 2D.

### Chauve-souris + Archer

- Statut : `Conditionnelle`.
- Les deux familles ont deja ete presentees seules.
- La zone visible mesure au moins `1440 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Le point aerien de la Chauve-souris et la position initiale de l'Archer sont separes d'au moins `480 px` horizontalement.
- L'Archer est place au sol sans second niveau de tir.
- Aucun passage etroit, plafond bas, mur ou colonne ne bloque les esquives.
- La plongee et le tir peuvent occuper `2` emplacements simultanement.
- Imran peut se tourner vers une fleche sans entrer automatiquement dans la plongee.
- Une trajectoire horizontale sure reste disponible lorsque la Chauve-souris descend.

### Chauve-souris + Serpent

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement dans une progression avancee.
- Les deux familles ont deja ete presentees seules.
- La zone visible mesure au moins `1440 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Le point aerien de la Chauve-souris et la position initiale du Serpent sont separes d'au moins `480 px` horizontalement.
- Aucun passage etroit, plafond bas, mur ou colonne ne bloque les esquives.
- La plongee et la projection peuvent occuper `2` emplacements simultanement.
- La preparation de `0.30 s` de la Chauve-souris reste visible.
- La preparation de `0.50 s` du Serpent reste visible.
- Le saut n'est jamais l'unique reponse a la projection du Serpent.
- Une esquive horizontale ou un Dash au sol evite la projection sans conduire automatiquement dans la plongee.

### Epeiste + Archer

- Statut : `Conditionnelle`.
- Les deux variantes ont deja ete presentees seules.
- La surface horizontale praticable mesure au moins `1280 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Les deux ennemis sont places sur le meme niveau de sol.
- L'Archer est place au moins `320 px` derriere l'Epeiste par rapport au sens d'entree dans la rencontre.
- Aucun placement initial de part et d'autre d'Imran ne produit un tir par-derriere.
- L'Archer peut occuper `1` emplacement d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- Imran peut faire face aux deux ennemis pour bloquer la fleche puis sauter au-dessus de l'Epeiste.
- Les Zombies utilisent exactement les memes conditions dans les niveaux 5 et 6.

### Epeiste + Serpent

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement dans une progression avancee.
- Les deux familles ont deja ete presentees seules.
- La surface horizontale praticable mesure au moins `1440 px`.
- Les positions initiales sont separees d'au moins `480 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Aucun encerclement initial ou passage etroit ne ferme l'esquive.
- Le Serpent peut occuper `1` emplacement d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- La preparation du Serpent ne peut pas etre masquee par la silhouette de l'Epeiste.
- Une zone d'atterrissage sure reste disponible apres le saut au-dessus de la lame ou de la projection.
- Le Zombie epeiste utilise exactement les memes conditions dans les niveaux 5 et 6.

### Archer + Serpent

- Statut : `Conditionnelle`.
- La combinaison apparait uniquement dans une progression avancee.
- Les deux familles ont deja ete presentees seules.
- La surface horizontale praticable mesure au moins `1440 px`.
- L'Archer et le Serpent sont places sur le meme niveau de sol.
- Leurs positions initiales sont separees d'au moins `480 px`.
- L'Archer est place derriere le Serpent par rapport au sens d'entree dans la rencontre.
- La zone offre au moins `192 px` de hauteur libre.
- Aucun placement initial de part et d'autre d'Imran ne produit une attaque par-derriere.
- Le tir et la projection peuvent occuper `2` emplacements simultanement.
- Imran peut bloquer la fleche de face tout en reculant, sautant ou utilisant son Dash contre le Serpent.
- Le Zombie archer utilise exactement les memes conditions dans les niveaux 5 et 6.

## Groupes de trois

Les groupes de trois ont ete etudies apres les paires.

- Chaque paire contenue dans un groupe doit deja etre autorisee ou conditionnelle.
- Trois preparations peuvent commencer simultanement si les trois emplacements sont libres.
- Une combinaison de trois familles doit conserver au moins une trajectoire d'esquive lisible.
- Les groupes de trois seront reserves a une progression avancee.
- Aucun groupe de trois ne sera utilise pour presenter une nouvelle famille.

Un groupe de trois designe ici la presence de trois familles distinctes dans la meme rencontre. Le nombre exact d'ennemis places sera fixe pendant la conception des niveaux, sans modifier la limite de `3 emplacements d'attaque`.

| Groupe de trois familles | Statut | Condition principale |
|---|---|---|
| Slime + Chauve-souris + Epeiste | Conditionnelle | Un ennemi par famille dans une zone de `1600 x 480 px` |
| Slime + Chauve-souris + Archer | Conditionnelle | Un ennemi par famille, tous places devant Imran dans `1600 x 480 px` |
| Slime + Chauve-souris + Serpent | Interdite | Pression mobile simultanee au sol et dans les airs |
| Slime + Epeiste + Archer | Conditionnelle | Un ennemi par famille, tous devant Imran dans `1600 x 192 px` |
| Slime + Epeiste + Serpent | Conditionnelle | Un ennemi par famille et deux zones d'atterrissage dans `1600 x 192 px` |
| Slime + Archer + Serpent | Conditionnelle | Tous devant Imran et deux zones d'atterrissage dans `1600 x 192 px` |
| Chauve-souris + Epeiste + Archer | Conditionnelle | Epeiste devant, Archer en soutien et zone de `1600 x 480 px` |
| Chauve-souris + Epeiste + Serpent | Interdite | Lame permanente sur la zone d'atterrissage pendant les attaques mobiles |
| Chauve-souris + Archer + Serpent | Conditionnelle | Tous devant Imran dans `1600 x 480 px`, avec Archer en soutien |
| Epeiste + Archer + Serpent | Conditionnelle | Epeiste devant, Serpent au milieu et Archer en soutien dans `1600 x 192 px` |

## Groupes de trois valides

### Slime + Chauve-souris + Epeiste

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La zone visible mesure au moins `1600 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Les positions initiales et le point aerien sont espaces d'au moins `480 px` horizontalement.
- Aucun passage etroit, plafond bas, mur, colonne ou gouffre ne bloque les esquives.
- Le Slime et la Chauve-souris peuvent occuper `2` emplacements d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- La plongee et le bond ne couvrent pas simultanement l'unique zone permettant d'eviter la lame.
- Une trajectoire d'atterrissage sure reste toujours visible dans le plan 2D.

### Slime + Chauve-souris + Archer

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La zone visible mesure au moins `1600 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Les positions initiales et le point aerien sont separes d'au moins `480 px` horizontalement.
- Le Slime et l'Archer sont places sur le meme niveau de sol.
- L'Archer est place derriere le Slime par rapport au sens d'entree.
- Aucun ennemi ne commence derriere Imran.
- Les trois attaques peuvent occuper les `3 emplacements` simultanement.
- Imran peut bloquer la fleche de face tout en esquivant le bond et la plongee.
- Une trajectoire horizontale et une zone d'atterrissage sure restent disponibles.

### Slime + Epeiste + Archer

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La surface horizontale praticable mesure au moins `1600 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Les positions initiales sont separees d'au moins `480 px`.
- Tous les ennemis commencent devant Imran.
- L'Epeiste occupe la premiere ligne, le Slime le milieu de la zone et l'Archer le soutien arriere.
- Le Slime et l'Archer peuvent occuper `2` emplacements d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- Une zone d'atterrissage sure reste disponible apres le bond.
- Les Zombies utilisent exactement les memes conditions dans les niveaux 5 et 6.

### Slime + Epeiste + Serpent

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression tres avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La surface horizontale praticable mesure au moins `1600 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Les positions initiales sont separees d'au moins `480 px`.
- Tous les ennemis commencent devant Imran sans produire d'encerclement.
- Le Slime et le Serpent peuvent occuper `2` emplacements d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- La compression de `0.10 s` du Slime et la preparation de `0.50 s` du Serpent restent visibles.
- Au moins deux zones d'atterrissage restent disponibles.
- La lame et la projection ne peuvent donc pas couvrir l'unique sortie.
- Le Zombie epeiste utilise exactement les memes conditions dans les niveaux 5 et 6.

### Slime + Archer + Serpent

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression tres avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La surface horizontale praticable mesure au moins `1600 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Les positions initiales sont separees d'au moins `480 px`.
- Tous les ennemis commencent devant Imran.
- L'Archer est place en soutien derriere le Slime et le Serpent.
- Les trois attaques peuvent occuper les `3 emplacements` simultanement.
- Imran peut bloquer la fleche de face pendant ses mouvements d'esquive.
- Au moins deux zones d'atterrissage restent disponibles face au bond et a la projection.
- Le Zombie archer utilise exactement les memes conditions dans les niveaux 5 et 6.

### Chauve-souris + Epeiste + Archer

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La zone visible mesure au moins `1600 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Les positions initiales et le point aerien sont separes d'au moins `480 px` horizontalement.
- Tous les ennemis commencent devant Imran.
- L'Epeiste occupe la premiere ligne et l'Archer le soutien arriere.
- La Chauve-souris et l'Archer peuvent occuper `2` emplacements d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- Imran peut bloquer la fleche de face sans perdre la lecture de la plongee.
- L'esquive aerienne ne conduit pas a un atterrissage sur la lame.
- Les Zombies utilisent exactement les memes conditions dans les niveaux 5 et 6.

### Chauve-souris + Archer + Serpent

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression tres avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La zone visible mesure au moins `1600 px` de large.
- Elle offre au moins `480 px` de hauteur libre.
- Les positions initiales et le point aerien sont separes d'au moins `480 px` horizontalement.
- Tous les ennemis commencent devant Imran.
- L'Archer est place en soutien derriere le Serpent.
- Les trois attaques peuvent occuper les `3 emplacements` simultanement.
- Imran peut bloquer la fleche de face pendant son esquive.
- Une trajectoire horizontale ou un Dash au sol evite la projection sans conduire automatiquement dans la plongee.
- Aucun passage etroit, plafond bas, mur ou colonne ne bloque cette trajectoire.
- Le Zombie archer utilise exactement les memes conditions dans les niveaux 5 et 6.

### Epeiste + Archer + Serpent

- Statut : `Conditionnelle`.
- Le groupe apparait uniquement dans une progression tres avancee.
- Les trois familles ont deja ete presentees seules et dans des paires plus simples.
- La premiere utilisation contient un seul ennemi de chaque famille.
- La surface horizontale praticable mesure au moins `1600 px`.
- La zone offre au moins `192 px` de hauteur libre.
- Les positions initiales sont separees d'au moins `480 px`.
- Tous les ennemis commencent devant Imran.
- L'Epeiste occupe la premiere ligne, le Serpent le milieu de la zone et l'Archer le soutien arriere.
- Le Serpent et l'Archer peuvent occuper `2` emplacements d'attaque.
- L'Epeiste reste un danger permanent sans occuper d'emplacement.
- Imran peut bloquer la fleche de face puis sauter ou utiliser son Dash contre les deux menaces terrestres.
- Une zone d'atterrissage sure reste disponible.
- Les deux versions Zombies utilisent exactement les memes conditions dans les niveaux 5 et 6.

## Groupes de trois interdits

### Slime + Chauve-souris + Serpent

- Statut : `Interdite` dans une meme rencontre.
- Les trois familles restent autorisees dans un meme niveau si elles sont reparties dans des rencontres separees.
- Le Slime, la Chauve-souris et le Serpent sont tous constamment mobiles apres leur activation.
- Le Serpent pousse Imran a sauter, reculer ou utiliser son Dash.
- La Chauve-souris controle l'espace aerien utilise par le saut.
- Le Slime traverse les zones d'atterrissage avec ses bonds.
- Les trois attaques peuvent occuper simultanement les `3 emplacements`.
- Aucune protection automatique ne simplifie la gestion du bond, de la plongee ou de la projection.
- Dans un seul plan 2D, cette combinaison peut supprimer simultanement l'esquive au sol et l'esquive aerienne.

### Chauve-souris + Epeiste + Serpent

- Statut : `Interdite` dans une meme rencontre.
- Les trois familles restent autorisees dans un meme niveau si elles sont reparties dans des rencontres separees.
- Le Serpent oblige Imran a quitter rapidement sa position au sol.
- La Chauve-souris controle l'espace aerien utilise pour le saut.
- L'Epeiste couvre en permanence une zone d'atterrissage avec sa lame.
- La Chauve-souris et le Serpent peuvent occuper `2` emplacements d'attaque.
- L'Epeiste reste dangereux sans utiliser le troisieme emplacement.
- La limite des `3 emplacements` ne reduit donc pas suffisamment la pression.
- Le Zombie epeiste prolongerait encore cette pression avec ses `3 PV`.

## Methode de verification d'une combinaison

Chaque combinaison est controlee selon les points suivants :

1. directions des attaques ;
2. superposition des preparations ;
3. possibilite de sauter, reculer, avancer, utiliser le Dash ou bloquer un projectile ;
4. espace horizontal et vertical disponible ;
5. presence d'un mur, d'un bord ou d'un gouffre ;
6. lisibilite dans le cadre de reference `1920 x 1080` ;
7. comportement avec `1 coeur` restant ;
8. comportement lorsque tous les emplacements d'attaque sont occupes ;
9. possibilite d'eviter les ennemis sans obligation generale de les vaincre ;
10. absence de degat inevitable.

## Principes de progression

- Une nouvelle famille apparait d'abord dans une rencontre simple.
- Son comportement est observe seul avant toute combinaison mixte.
- Sa premiere combinaison utilise une famille deja connue.
- Les paires complexes apparaissent apres les paires simples.
- Les groupes de trois apparaissent uniquement apres validation de toutes leurs paires.
- Les Zombies remplacent les Squelettes dans les niveaux 5 et 6 sans introduire de nouveau comportement.
- La difficulte augmente par les associations, le terrain et la resistance des Zombies, jamais par la suppression d'un signe d'attaque.

## Progression par niveau

| Niveau | Fonction ennemie | Familles et combinaisons | Statut |
|---|---|---|---|
| Niveau 0 - Village des Bles | Tutoriel des ennemis et du Bouclier | Slime seul puis Archer seul | Valide |
| Niveau 1 - Foret enchantee | Introduction de la Chauve-souris et premieres paires | Slime, Archer et Chauve-souris | Valide |
| Niveau 2 - Grotte mysterieuse | Introduction de l'Epeiste et progression des paires | Chauves-souris, Epeiste et Archer | Valide |
| Niveau 3 - Lac gele | Introduction du Serpent et pression rapide au sol | Slime, Archer et Serpent | Valide |
| Niveau 4 - Desert oublie | Paires avancees et premiers groupes de trois | Slime, Epeiste, Archer et Serpent | Valide |
| Niveau 5 - Volcan | Introduction des Zombies et augmentation de resistance | Slime, Zombies et Serpent | Valide |
| Niveau 6 - Chateau de Tata Lisa | Combinaisons finales autorisees | Chauves-souris, Zombies et Serpents | Valide |

## Progression validee par niveau

### Niveau 0 - Village des Bles

- Le Niveau 0 introduit uniquement le Slime et le Squelette archer.
- Le Slime utilise son apparence de base entierement bleue.
- La premiere rencontre contient un Slime seul apres la pancarte de l'attaque normale.
- La deuxieme rencontre contient un Squelette archer seul apres la pancarte du Bouclier automatique.
- Les deux rencontres sont separees par des pancartes et des phases de plateforme.
- Un seul ennemi est actif dans chaque sequence de tutoriel.
- La zone de l'Archer est plate et ne contient aucun autre danger.
- Imran peut apprendre a faire face au projectile sans pression supplementaire.
- Aucun Epeiste, Serpent, Zombie ou Chauve-souris n'apparait.
- Aucune paire mixte et aucun groupe de trois ne sont utilises.
- Les ennemis restent evitables et ne deviennent jamais une condition de sortie du Village.

### Niveau 1 - Foret enchantee

- Le Slime et l'Archer servent de rappels apres le tutoriel.
- Une Chauve-souris est d'abord presentee seule dans une zone verticale degagee.
- La premiere paire identique utilise `Slime + Slime`.
- La premiere paire mixte connue utilise `Slime + Archer`.
- Une combinaison de fin de parcours utilise `Slime + Chauve-souris`.
- Chaque combinaison respecte toutes les conditions de sa fiche.
- `Chauve-souris + Archer` n'est pas encore utilisee.
- Aucun Epeiste, Serpent ou Zombie n'apparait.
- Aucun groupe de trois n'est utilise.
- La progression interne suit : rappel simple, nouvel ennemi seul, paire identique, puis paires mixtes.

### Niveau 2 - Grotte mysterieuse

- La Chauve-souris et l'Archer sont deja connus.
- Le Squelette epeiste est d'abord presente seul dans un couloir large.
- La premiere paire aerienne utilise `Chauve-souris + Chauve-souris`.
- La premiere association des deux variantes de Squelettes utilise `Epeiste + Archer`.
- Une paire mixte de fin de parcours utilise `Chauve-souris + Epeiste`.
- Des rencontres simples avec un Archer ou une Chauve-souris servent de respiration.
- Chaque paire respecte toutes les conditions de terrain validees.
- Aucun Serpent ou Zombie n'apparait.
- Aucun groupe de trois n'est utilise.
- Les Slimes ne sont pas necessaires afin de renforcer l'identite Chauves-souris et Squelettes de la Grotte.

### Niveau 3 - Lac gele

- Le Slime utilise une apparence adaptee au Lac gele sans changer de comportement.
- Le Slime et l'Archer servent d'ennemis connus.
- Le Serpent est d'abord presente seul sur une longue surface horizontale.
- La premiere paire avec le Serpent utilise `Slime + Serpent`.
- Une paire de fin de parcours utilise `Archer + Serpent`.
- Chaque premiere rencontre avec le Serpent reste separee des autres dangers.
- `Serpent + Serpent` est conserve pour un niveau plus avance.
- Aucun Epeiste, Zombie ou Chauve-souris n'apparait.
- Aucun groupe de trois n'est utilise.

### Niveau 4 - Desert oublie

- Le Slime utilise une apparence adaptee au Desert sans changer de comportement.
- Les Squelettes epeistes, Archers et Serpents constituent les menaces principales.
- La premiere paire `Serpent + Serpent` apparait dans une grande zone degagee.
- Les paires avancees utilisent `Slime + Epeiste`, `Epeiste + Serpent` et `Archer + Serpent`.
- Le premier groupe de trois utilise `Slime + Epeiste + Archer`.
- Un groupe de fin de parcours utilise `Epeiste + Archer + Serpent`.
- La premiere utilisation de chaque groupe contient un ennemi de chaque famille.
- Chaque rencontre respecte toutes les conditions de largeur, de hauteur et de placement validees.
- Aucune combinaison interdite n'est utilisee.
- Aucune Chauve-souris n'apparait afin de conserver une identite centree sur les menaces terrestres.
- Aucun Zombie n'apparait avant le Volcan.

### Niveau 5 - Volcan

- Le Slime utilise une apparence adaptee au Volcan sans changer de comportement.
- Les Serpents et les deux variantes de Zombies constituent les autres menaces.
- Aucun Squelette n'apparait : les Zombies les remplacent entierement.
- Un Zombie epeiste est d'abord presente seul afin de montrer sa resistance de `3 PV`.
- Un Zombie archer est ensuite presente seul.
- Une paire utilise `Zombie epeiste + Zombie archer`.
- Les paires avancees utilisent `Slime + Zombie epeiste` et `Zombie archer + Serpent`.
- Un premier groupe utilise `Slime + Zombie epeiste + Zombie archer`.
- Un groupe de fin de parcours utilise `Slime + Zombie archer + Serpent`.
- Les conditions de terrain restent exactement celles des combinaisons equivalentes avec les Squelettes.
- Aucune Chauve-souris n'apparait afin de concentrer l'apprentissage sur la resistance des Zombies.
- Aucune combinaison interdite n'est utilisee.

### Niveau 6 - Chateau de Tata Lisa

- Les Chauves-souris, Serpents, Zombies epeistes et Zombies archers constituent les familles finales.
- Aucun Squelette n'apparait.
- Aucun Slime n'apparait afin de donner au Chateau une identite finale propre.
- Les paires de rappel utilisent `Chauve-souris + Zombie archer`, `Zombie epeiste + Zombie archer` et `Zombie archer + Serpent`.
- Un premier groupe utilise `Chauve-souris + Zombie epeiste + Zombie archer`.
- Un groupe tres avance utilise `Chauve-souris + Zombie archer + Serpent`.
- La derniere rencontre ordinaire utilise `Zombie epeiste + Zombie archer + Serpent`.
- La premiere utilisation de chaque groupe contient un ennemi de chaque famille.
- La combinaison interdite `Chauve-souris + Zombie epeiste + Serpent` n'est jamais utilisee.
- Aucune nouvelle regle de comportement n'est introduite.
- La difficulte finale vient uniquement des combinaisons deja apprises et des `3 PV` des Zombies.

## Verification dans le prototype

Les regles de ce document fixent les intentions du GDD. Le prototype Godot devra ensuite confirmer :

- la largeur et la hauteur reelles necessaires a chaque combinaison ;
- la lisibilite des effets et des sons ;
- l'absence de degats inevitables ;
- le confort avec un public a partir de 7 ans ;
- les ajustements de placement sans modifier les comportements valides.

## Criteres de validation

Le document sera valide si :

- chaque paire possede un statut et une condition claire ;
- les groupes de trois autorises sont listes ;
- les combinaisons interdites sont justifiees ;
- la progression indique quand introduire puis combiner chaque famille ;
- les Zombies remplacent correctement les Squelettes ;
- aucune rencontre recommandee ne produit de degat inevitable ;
- toutes les decisions peuvent etre appliquees pendant la conception des niveaux.

## Sources

- [Regles communes](Regles-Communes.md)
- [Slimes](Slimes.md)
- [Chauves-souris](Chauves-Souris.md)
- [Squelettes](Squelettes.md)
- [Serpents](Serpents.md)
- [Zombies](Zombies.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Camera](../Systemes/Camera.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Progression](../Systemes/Progression.md)
