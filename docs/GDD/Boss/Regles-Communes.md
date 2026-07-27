# Regles communes des boss

> **Statut :** Valide

## Objectif

Definir la structure partagee par les six golems et Tata Lisa avant de fixer les valeurs, les phases et les attaques propres a chaque combat.

## Declenchement du combat valide

Le combat commence selon la sequence suivante :

1. Imran franchit le point d'entree de l'arene.
2. La sortie se ferme et il ne peut plus quitter l'arene.
3. Les commandes d'Imran sont temporairement bloquees.
4. Le golem joue son animation de reveil pendant `3.00 s`.
5. La barre de vie du boss apparait au centre de la partie haute de l'ecran.
6. Le controle d'Imran revient.
7. Le boss peut commencer son comportement de combat.

## Regles du declenchement

- Le boss ne peut pas recevoir de degat avant le debut officiel du combat.
- Le boss ne peut pas attaquer pendant sa presentation.
- Imran ne peut ni se deplacer, ni sauter, ni utiliser le Dash, ni attaquer, ni charger le Smash pendant cette presentation.
- Une commande effectuee pendant le blocage est ignoree et n'est pas executee au retour du controle.
- La fermeture de l'arene empeche toute fuite et toute attaque lancee depuis l'exterieur.
- La camera conserve Imran et le boss dans une composition lisible.
- Le combat devient actif uniquement lorsque la barre de vie est visible et que le controle est rendu.
- La presentation commune des six golems dure exactement `3.00 s`.
- Cette presentation complete est rejouee a chaque entree dans l'arene.
- Apres une perte de vie, le retour ulterieur dans l'arene rejoue donc les `3.00 s` avant la nouvelle tentative.
- Aucune tentative ne commence directement au milieu ou a la fin de la presentation.
- Tata Lisa possede une presentation distincte qui sera definie dans sa propre fiche.

## Fermeture magique des arenes des golems validee

- Les six arenes de golem utilisent deux barrieres magiques identiques.
- La barriere gauche ferme l'entree derriere Imran.
- La barriere droite bloque le passage vers la zone de recompense.
- Elles constituent des limites solides mais ne retirent aucun coeur.
- Imran, les ennemis, les boss et les projectiles ne peuvent pas les traverser.
- Elles empechent egalement une attaque lancee depuis l'exterieur d'entrer dans l'arene.
- Leur couleur reprend l'element et la palette du golem affronte.
- Leur apparence commune est celle de murs d'energie semi-transparents.
- Des particules elementaires animees circulent continuellement dans cette energie.
- Le decor situe derriere les barrieres reste visible sans affaiblir la lecture des limites.
- Les collisions solides restent identiques quelle que soit la densite visible des particules.
- La structure visuelle reste commune aux douze barrieres afin de rendre leur fonction immediate.
- Leurs collisions deviennent actives des le declenchement de la fermeture.
- Les deux murs visibles montent depuis le sol jusqu'en haut de l'ecran en `0.50 s`.
- Leurs animations commencent au meme instant, pendant le debut de la presentation du golem.
- Une fois leur hauteur complete atteinte, les barrieres conservent leur animation continue de particules.
- Leur largeur visible et solide commune mesure `32 px`.
- Leur bord interieur reste aligne avec la limite correspondante de l'arene.
- Leur epaisseur ne reduit pas l'espace utile du combat.
- Les barrieres ne produisent aucun son pendant leur apparition ou leur disparition.
- Elles ne produisent aucun bourdonnement continu lorsqu'elles sont actives.
- Leur fermeture est communiquee uniquement par leur animation, leur couleur et leurs particules.
- Les six paires de barrieres utilisent une energie semi-transparente et des particules liees au theme du golem.
- Leur palette et leurs particules suivent le tableau commun :

| Golem | Couleur de l'energie | Particules |
|---|---|---|
| Foret | Vert | Petites feuilles et fragments de racines |
| Grotte | Violet | Fragments d'amethyste |
| Lac gele | Bleu glacier | Cristaux de glace et flocons |
| Desert | Dore et ambre | Grains de sable et fragments de gres |
| Volcan | Rouge-orange | Braises et fragments de basalte |
| Chateau | Violet sombre | Fragments d'obsidienne et eclats de metal sombre |

- Les particules sont uniquement visuelles et ne possedent aucune collision.
- Leur densite ne peut jamais masquer Imran, le boss, un projectile ou un avertissement d'attaque.
- La structure, les dimensions et le fonctionnement des barrieres restent identiques pour les six themes.
- La barriere gauche reste active pendant la presentation, le combat, l'etat `Etourdi`, la defaite et l'acces au coffre.
- Elle disparait uniquement lorsque la cle est recuperee et que le niveau se termine.
- La barriere droite reste active pendant la presentation, le combat, l'etat `Etourdi` et la premiere moitie de la defaite.
- Elle redescend pendant les `0.50 s` finales de la sequence commune de defaite.
- Sa collision reste active pendant cette descente.
- Elle disparait completement et ouvre le passage au retour du controle.
- Apres une perte de vie, les deux barrieres reviennent a leur etat inactif afin de permettre une nouvelle entree dans l'arene.
- La fermeture du combat final contre Tata Lisa sera definie separement.

## Largeur commune des arenes de boss validee

- Les zones de combat des six golems et de Tata Lisa possedent une largeur utile commune de `1280 px`.
- Cette largeur correspond exactement a `20 grilles` de `64 px`.
- La mesure commence a la limite interieure gauche de la zone de combat et se termine a sa limite interieure droite.
- Les barrieres, les murs et leurs epaisseurs visibles ne reduisent pas ces `1280 px` utiles.
- Les couloirs d'entree, les zones de recompense et les espaces de transition ne sont pas inclus dans cette largeur.
- Les sept arenes de boss utilisent un sol unique et entierement plat.
- Aucune arene de boss ne contient de plateforme, de pente, de fosse ni d'obstacle de deplacement.
- Cette regle s'applique aux six golems et a Tata Lisa.
- Le theme, la matiere du sol, les plafonds et les decorations peuvent varier selon le boss.
- Les decorations restent hors des zones de collision et ne modifient jamais la surface jouable.
- Aucune fiche de boss ne peut modifier cette largeur sans une nouvelle validation commune.

## Hauteur commune du sol des arenes validee

- Dans la resolution de reference `1920 x 1080`, le sol principal des sept arenes de boss se trouve a `y = 896 px`.
- Cette hauteur commune s'applique aux six golems et a Tata Lisa.
- Les pieds d'Imran et la base visuelle du boss reposent sur cette ligne lorsqu'ils sont au sol.
- Aucune plateforme ni aucun element de collision ne se trouve au-dessus de cette ligne.
- Aucune fosse ni aucune interruption ne coupe le sol de l'arene.
- Les decorations peuvent apparaitre au-dessus de cette ligne sans modifier les collisions.
- La camera conserve ce repere vertical pendant le combat.
- Aucune fiche de boss ne peut modifier cette hauteur principale sans une nouvelle validation commune.

## Cadrage horizontal commun des arenes valide

- Dans la resolution de reference `1920 x 1080`, les `1280 px` utiles de chaque arene sont centres horizontalement.
- La limite gauche utile apparait a `x = 320 px` dans l'ecran.
- La limite droite utile apparait a `x = 1600 px` dans l'ecran.
- Ce cadrage s'applique aux six golems et a Tata Lisa.
- La camera reste fixe sur ce cadrage pendant la presentation, le combat actif, l'etat `Etourdi` et la sequence de defaite.
- Aucun suivi, recentrage ou zoom ne se produit pendant ces etats.
- Les positions locales propres a chaque fiche sont converties a l'ecran en ajoutant `320 px`.
- Le defilement vers une zone de recompense commence uniquement apres la fin du combat et suit ses regles propres.
- Aucune fiche de boss ne peut decaler ce cadrage de combat sans une nouvelle validation commune.

## Regles deja acquises

- Les sept combats de boss sont obligatoires.
- Chaque attaque de boss retire `1 coeur` par defaut.
- L'attaque normale de la Shadow Sword inflige `1 degat`.
- Le Smash Tranchant inflige `2 degats` au premier boss touche puis disparait.
- Un projectile frontal peut etre bloque automatiquement par le Bouclier de lumiere.
- Une perte de vie restaure le boss a sa vie maximale et a sa premiere phase.
- La barre de vie est centree en haut de l'ecran pendant le combat.
- Toutes les zones de combat de boss mesurent `1280 px` de largeur utile.
- Le sol principal des sept arenes de boss se trouve a `y = 896 px`.
- Les zones de combat apparaissent entre `x = 320 px` et `x = 1600 px` dans le cadre de reference.
- Un golem vaincu rend son coffre accessible.
- Tata Lisa vaincue perd ses pouvoirs lorsque la Pierre du Chaos se brise.

## Vulnerabilite validee

- Les six golems et Tata Lisa peuvent recevoir des degats pendant tout le combat actif.
- Ils restent vulnerables pendant leurs deplacements, leurs preparations, leurs attaques et leurs recuperations.
- La tete constitue leur unique zone vulnerable.
- Une attaque normale touchant la tete inflige `1 degat`.
- Un Smash Tranchant touchant la tete inflige `2 degats` puis disparait.
- Le Smash conserve ces `2 degats` pendant tout le combat actif.
- Toucher la tete avec ce projectile constitue une action exigeante mais pleinement autorisee.
- Aucun plafond de degats, aucune resistance speciale et aucune penalite ne reduisent cette recompense.
- Le contact doit reellement atteindre la zone vulnerable de la tete.
- Le projectile ne possede aucune assistance, correction de trajectoire ou zone d'impact agrandie contre un boss.
- Un impact sur le corps, les bras, les jambes, une arme ou un autre element du boss ne retire aucun point de vie.
- Un contact sur une partie non vulnerable ne produit aucun flash, aucun effet visuel et aucun son de blocage supplementaire.
- L'attaque normale termine simplement son animation sans modifier le boss.
- Le Smash Tranchant disparait au premier contact avec le boss, meme si ce contact ne touche pas la tete.
- Le boss est invulnerable pendant sa presentation, ses transitions de phase et sa phase de defaite.
- Une attaque touchant la tete pendant un etat invulnerable ne retire aucun point de vie.
- La zone vulnerable commune des golems est definie dans la section consacree a leurs dimensions.
- La zone vulnerable de Tata Lisa sera fixee dans sa propre fiche.
- Un impact valide ne ralentit, ne repousse et n'interrompt jamais le boss.
- Le deplacement, la preparation, l'attaque ou la recuperation en cours continue normalement.
- Le retour visuel et sonore confirme le degat sans creer un etat de blocage.
- Le boss produit un flash visuel pendant `0.33 s` apres un degat.
- Il est protege contre un nouveau degat pendant ces memes `0.33 s`.
- Une attaque touchant la tete pendant cette protection ne retire aucun point de vie.
- Un impact ignore ne relance ni le flash, ni la duree de protection.
- La fin de la protection ne modifie pas l'action ou la phase en cours.

## Dimensions visuelles communes des golems validees

- Les six golems utilisent une enveloppe visuelle commune de `144 x 152 px`.
- Leur largeur visuelle de reference est de `144 px`.
- Leur hauteur visuelle de reference est de `152 px`.
- Cette hauteur represente environ `2.375 fois` les `64 px` d'Imran.
- Ces proportions sont adaptees des mesures realisees dans les captures Wonder Boy.
- Les golems restent presque aussi larges que hauts afin de conserver une silhouette courte et massive.
- Une animation, une arme ou un effet peut depasser temporairement cette enveloppe sans agrandir automatiquement les zones de gameplay.
- L'enveloppe visuelle ne constitue ni une collision avec le decor, ni une zone dangereuse, ni une zone vulnerable.
- Tata Lisa possede ses propres dimensions et n'utilise pas cette enveloppe.

## Zone vulnerable de la tete des golems validee

- La zone vulnerable commune de la tete mesure `64 x 48 px`.
- Elle est centree sur la masse principale de la tete et suit son mouvement pendant les animations.
- Les cornes, feuilles, cristaux, flammes, ornements, pieces d'armure et autres decorations ne l'agrandissent pas.
- Elle reste active pendant les deplacements, les preparations, les attaques et les recuperations du combat actif.
- Elle est desactivee pendant la presentation, les transitions de phase et la phase de defaite.
- Pendant l'etat `Etourdi` a `0 point de vie`, la finition au Smash utilise tout le corps et ne depend plus de cette zone.
- La zone vulnerable propre a Tata Lisa sera fixee dans sa fiche.

## Phase unique des golems validee

- Chacun des six golems possede une seule phase de combat.
- Aucun seuil de points de vie ne change son comportement.
- Ses attaques, ses vitesses, sa cadence et ses regles restent identiques du debut du combat jusqu'a `0 point de vie`.
- Un golem peut posseder plusieurs attaques differentes sans que celles-ci constituent des phases.
- Aucune transition de phase ne suspend le combat d'un golem.
- L'etat `Etourdi` a `0 point de vie` constitue une finition et non une seconde phase.
- Le nombre de phases de Tata Lisa sera defini separement dans sa fiche.

## Cycle d'attaques des golems valide

- Chaque golem utilise un cycle d'attaques fixe et previsible.
- L'ordre exact de ses attaques est defini dans sa propre fiche.
- La premiere attaque du cycle reste identique a chaque tentative.
- Apres la derniere attaque, le cycle reprend depuis la premiere.
- Une attaque terminee ne peut pas etre choisie aleatoirement ou remplacee par une autre attaque du cycle.
- Recevoir un degat ne modifie ni l'ordre du cycle, ni l'attaque en cours.
- Pour une attaque dirigee, le golem observe la position d'Imran au debut de la preparation.
- Il verrouille alors la direction horizontale de cette attaque.
- Un changement de cote d'Imran pendant la preparation ne modifie plus cette direction.
- La direction reste identique pendant la phase dangereuse et la recuperation.
- Le golem peut choisir une nouvelle direction uniquement au debut de la preparation de l'attaque suivante.
- Une attaque sans direction horizontale conserve les regles propres indiquees dans la fiche du golem.
- Une attaque dont la preparation a commence continue meme si Imran quitte sa portee.
- Elle n'est ni annulee, ni retardee, ni remplacee par une autre attaque.
- Elle peut donc se terminer sans toucher Imran.
- Chaque attaque commence par une animation de preparation identifiable.
- Un son distinct accompagne cette preparation.
- L'animation et le son commencent avant l'activation de la zone dangereuse de l'attaque.
- La duree entre le debut de cet avertissement et l'activation du danger ne peut pas etre inferieure a `0.50 s`.
- Une attaque peut utiliser une preparation plus longue lorsque sa puissance, sa portee ou sa complexite le justifie.
- La duree exacte de chaque preparation est definie dans la fiche du golem concerne.
- Le signal visuel reste suffisant pour comprendre l'attaque lorsque le son est coupe.
- Le signal sonore complete l'animation mais ne constitue jamais le seul avertissement.
- Une meme attaque conserve les memes signaux visuel et sonore a chaque utilisation.
- Recevoir un degat pendant la preparation ne relance ni l'animation, ni le son.
- Les signaux exacts sont definis dans la fiche de chaque golem.
- Lorsque la phase dangereuse d'une attaque se termine, le golem entre dans une phase de recuperation.
- Cette recuperation utilise une animation qui le ramene a sa posture neutre.
- La recuperation commune des six golems dure `0.30 s`.
- Aucune nouvelle attaque ne peut commencer pendant cette recuperation.
- Une pause neutre distincte commence lorsque la recuperation est terminee.
- Le golem reste dans sa posture neutre pendant cette pause.
- La pause neutre commune des six golems dure `1.80 s`.
- L'intervalle total entre la fin d'une phase dangereuse et la preparation suivante dure donc `2.10 s`.
- La preparation de l'attaque suivante commence uniquement apres la fin de la pause.
- Le golem reste vulnerable pendant la recuperation et la pause neutre.
- Son danger de contact permanent reste actif pendant ces deux periodes.
- Recevoir un degat ne raccourcit, ne prolonge et ne relance ni la recuperation, ni la pause.
- Un projectile deja lance continue normalement pendant la recuperation et la pause.
- Sa trajectoire, sa vitesse, ses degats et sa duree de vie ne sont pas modifies par le changement d'etat du golem.
- Il disparait uniquement lors de sa collision valide ou a la fin de sa duree de vie.
- Recevoir un degat ne supprime pas les projectiles deja lances.
- La duree maximale de chaque projectile doit se terminer avant la preparation de l'attaque suivante.
- La recuperation et la pause sont dimensionnees pour garantir cette disparition.
- Deux phases dangereuses consecutives ne peuvent donc jamais se superposer.
- La disparition anticipee d'un projectile ne raccourcit pas la recuperation ou la pause en cours.
- L'etat `Etourdi`, une perte de vie ou la phase de defaite les suppriment selon les regles deja validees.
- Atteindre `0 point de vie` interrompt immediatement le cycle et declenche l'etat `Etourdi`.
- Une perte de vie d'Imran reinitialise le cycle du golem.
- La tentative suivante recommence donc avec la premiere attaque apres la presentation de `3.00 s`.
- Les durees de preparation et de danger sont mesurees dans la fiche de chaque golem.
- La recuperation de `0.30 s` et la pause de `1.80 s` restent communes aux six golems.
- Tata Lisa possede sa propre logique de selection des attaques, definie dans sa fiche.

## Points de vie des golems valides

| Golem | Points de vie |
|---|---:|
| Foret | `12 PV` |
| Grotte | `14 PV` |
| Lac gele | `16 PV` |
| Desert | `18 PV` |
| Volcan | `20 PV` |
| Chateau | `22 PV` |

- La resistance augmente de `2 PV` entre deux golems consecutifs.
- Une attaque normale a la tete retire `1 PV`.
- Un Smash Tranchant a la tete retire `2 PV`.
- Aucun autre multiplicateur de degats ou resistance ne modifie ces valeurs.
- Les points de vie ne se restaurent jamais pendant une tentative de combat.
- Une perte de vie restaure le golem a sa valeur maximale.
- Atteindre `0 PV` declenche l'etat `Etourdi` et la finition obligatoire au Smash.
- Les points de vie de Tata Lisa seront fixes dans sa propre fiche.

## Collision dangereuse avec le corps validee

- Pendant le combat actif, le corps du boss constitue une zone dangereuse pour Imran.
- Cette zone dangereuse ne constitue pas un obstacle solide pour Imran.
- La zone dangereuse commune du corps des golems mesure `112 x 136 px`.
- Elle est centree sur la masse principale du golem et suit ses deplacements ainsi que ses animations.
- Elle conserve ces dimensions pendant tout le combat actif.
- Les cornes, feuilles, cristaux, flammes, armes, ornements et autres decorations ne l'agrandissent pas.
- Une zone dangereuse propre a une attaque reste separee de cette zone de contact permanente.
- Tata Lisa possede une zone dangereuse propre qui sera definie dans sa fiche.
- Un contact valide retire `1 coeur` a Imran.
- Il declenche sa reaction standard de `0.33 s`.
- Le recul horizontal de `220 px/s` eloigne Imran du boss.
- L'invulnerabilite standard de `1.30 s` commence au moment de la perte du coeur.
- Pendant cette invulnerabilite, Imran peut traverser le boss sans recevoir un nouveau degat.
- La collision dangereuse ne ralentit, ne repousse et n'interrompt jamais l'action du boss.
- Le Bouclier de lumiere ne protege pas contre ce contact.
- Le Dash ne rend pas Imran invulnerable a ce contact.
- Une attaque d'Imran et un contact dangereux peuvent etre valides pendant la meme image.
- Dans ce cas, le degat inflige au boss et le degat recu par Imran sont resolus independamment.
- Le contact reste dangereux quel que soit le cote du boss touche.
- La zone dangereuse est desactivee pendant la presentation, la phase de defaite et l'etat `Etourdi` a `0 point de vie`.
- Une nouvelle perte de coeur reste impossible tant que l'invulnerabilite d'Imran est active.
- Les collisions du boss avec le decor et les limites de son arene restent independantes de cette regle.

## Perte de vie et reinitialisation de l'arene validees

- La perte du dernier coeur d'Imran interrompt immediatement le combat contre le golem.
- Une vie est retiree selon les regles communes des coeurs et des vies.
- S'il reste au moins une vie, Imran reapparait au debut du niveau ou au checkpoint temporaire actif.
- Il ne reapparait jamais directement dans l'arene fermee.
- Sa nouvelle vie commence avec `3 coeurs`.
- Le golem retrouve sa valeur maximale de points de vie.
- Son cycle est replace sur sa premiere attaque.
- Tous ses projectiles, dangers temporaires et effets de combat disparaissent.
- La barre de vie du boss est masquee.
- La fermeture de l'arene revient a son etat initial et permet une nouvelle entree.
- Le feu de camp redevient disponible selon les regles deja validees.
- Aucun degat ou autre progres temporaire du combat precedent n'est conserve.
- Lorsque Imran entre de nouveau dans l'arene, la fermeture et la presentation complete de `3.00 s` sont rejouees.
- Si aucune vie ne reste, le Game Over remplace cette reapparition selon ses propres regles.
- La reinitialisation du combat final contre Tata Lisa sera verifiee dans sa fiche.

## Victoire et arene de recompense validees

- Le Smash Tranchant final declenche la phase de defaite du golem.
- La barre reste visible a `0` pendant l'etat `Etourdi`, puis disparait lorsque la phase de defaite commence.
- Tous les dangers, projectiles et contacts dangereux du golem restent desactives.
- Le golem ne peut plus bloquer, pousser ou blesser Imran.
- La barriere gauche reste active apres la defaite.
- Imran ne peut donc pas quitter le niveau sans recuperer la cle.
- Le coffre reste entierement hors du cadre de combat, dans une zone de recompense situee a droite.
- La zone de recompense des six golems commence a la position locale `x = 1280 px`.
- Elle mesure exactement `640 px`, soit `10 grilles` de `64 px`.
- La longueur totale accessible du combat et de la recompense atteint donc `1920 px`.
- Le sol de la recompense prolonge le repere commun place a `y = 896 px`.
- Le centre du coffre de chaque golem se trouve a la position locale `x = 1824 px`.
- Chaque coffre reste ainsi a `96 px` de la limite finale placee a `x = 1920 px`.
- Le coffre passe de l'etat `Protege` a l'etat `Disponible` apres la fin de la sequence de defaite.
- Aucune interaction avec le coffre n'est possible pendant cette sequence.
- La barriere droite disparait completement au retour du controle.
- Lorsque le controle revient, l'arene et la zone de recompense constituent un espace sur sans ennemi ni danger.
- Imran doit avancer lui-meme vers la droite.
- La camera reste fixe tant que le centre d'Imran ne depasse pas la position locale `x = 1280 px`.
- Le defilement commence uniquement lorsque son centre franchit cette limite.
- Imran apparait alors a environ `x = 1600 px` dans l'ecran.
- La camera effectue un recentrage horizontal de `128 px` pendant `0.50 s`.
- Imran est ainsi replace progressivement a `x = 1472 px` dans l'ecran.
- Le joueur conserve le controle pendant ce recentrage.
- La camera suit ensuite la marche vers la droite en maintenant cette position de reference.
- Son decalage horizontal maximal mesure `640 px`.
- Ce defilement progresse uniquement vers la droite et ne revient jamais vers la zone abandonnee.
- Le decalage maximal deja atteint ne diminue jamais.
- La camera ne change jamais sa position verticale.
- Le bord gauche de l'ecran empeche Imran de quitter le cadre visible.
- Le coffre apparait progressivement pendant ce deplacement.
- Imran doit ensuite rejoindre le coffre et utiliser la commande `Interaction`.
- L'interaction devient disponible lorsque le centre d'Imran se trouve a `56 px` ou moins du coffre.
- Cette distance est identique pour les six coffres.
- L'ouverture du coffre ajoute automatiquement la cle, declenche la sauvegarde et termine le niveau selon les regles deja validees.
- La victoire contre le golem seule ne termine jamais le niveau.
- Le combat final contre Tata Lisa ne possede aucun coffre, aucune zone de recompense de `640 px` et suit une conclusion distincte.

## Dimensions de la barre de vie validees

- La barre de vie utilise une taille visible totale de `192 x 24 px`.
- Cette taille est fixee pour la resolution de reference `1920 x 1080`.
- La barre reste ancree au centre horizontal de l'ecran.
- Dans la resolution de reference, son bord gauche se trouve donc a `864 px`.
- Son bord superieur se trouve a `48 px`.
- A `1920 x 1080`, son rectangle visible va de la position `864, 48` a la position `1056, 72`.
- La diminution de la vie reduit le remplissage de droite vers la gauche.
- Le contour sombre reste fixe pendant toute la diminution.
- Seuls les points de vie actuellement restants sont affiches au centre de la barre.
- La valeur maximale et le symbole de pourcentage ne sont pas affiches.
- Aucun nom de boss, portrait, icone ou texte supplementaire n'accompagne la barre.
- La valeur numerique et le remplissage sont mis a jour immediatement apres chaque impact valide.

## Finition au Smash Tranchant validee

- Atteindre `0 point de vie` ne lance pas immediatement la phase de defaite.
- Le boss entre d'abord dans un etat `Etourdi`.
- Il interrompt son action en cours et ne peut plus se deplacer ni commencer une attaque.
- Tous ses projectiles actifs disparaissent immediatement.
- Tous ses dangers temporaires et toutes ses zones d'attaque sont desactives immediatement.
- Son corps ne peut plus retirer de coeur a Imran.
- Aucun danger propre au boss ne reste actif pendant la preparation de la finition.
- Sa barre reste visible a `0` pendant cet etat.
- L'etat `Etourdi` ne possede aucune limite de temps.
- Le boss ne recupere aucun point de vie et ne reprend jamais le combat.
- Il reste etourdi jusqu'au contact du Smash Tranchant final.
- La tete cesse d'etre l'unique cible requise pour la finition.
- Tout le corps du boss peut alors recevoir le contact final du Smash Tranchant.
- Une attaque normale touchant le boss etourdi ne termine pas le combat.
- Le joueur doit charger puis lancer un Smash Tranchant.
- Le premier Smash Tranchant touchant n'importe quelle partie du boss etourdi declenche la phase de defaite.
- Ce contact final n'inflige aucun degat supplementaire puisque la barre est deja a `0`.
- Le Smash sert ici de declencheur cinematographique et non de source de degats.
- La fin du combat reste bloquee tant que cette finition n'a pas ete effectuee.

## Sequence commune de defaite des golems validee

- Le contact du Smash Tranchant final declenche immediatement la sequence de defaite.
- Les six golems utilisent le meme decoupage temporel :

| Periode | Animation commune |
|---|---|
| `0.00 a 0.20 s` | Le coeur magique produit un dernier eclat, puis le coeur et les fissures s'eteignent. |
| `0.20 a 0.70 s` | Le corps se fragmente en materiaux lies au theme du golem. |
| `0.70 a 1.00 s` | Les fragments deviennent des particules elementaires puis disparaissent. |

- Les materiaux, les couleurs et les sons exacts restent propres au theme de chaque golem.
- Aucun corps, obstacle ou danger du golem ne reste dans l'arene.
- Aucune piece et aucun objet de soin ne sont produits.
- Le coffre constitue l'unique recompense materielle du combat.
- Le coffre devient disponible uniquement apres la disparition des dernieres particules.
- Le controle d'Imran revient au meme moment dans une arene sure.
- La sequence complete dure exactement `1.00 s`.
- Cette duree commence au contact du Smash Tranchant final.
- Elle se termine a la disparition des dernieres particules.
- Le coffre devient disponible et le controle d'Imran revient a la fin de cette seconde.
- Cette structure est adaptee de la fin de combat observee dans la capture Wonder Boy.
- Tata Lisa possede une sequence de defaite distincte.

## Exception reportee

Les particularites de Tata Lisa seront definies et validees dans sa propre fiche. Elles ne remettent pas en cause les regles communes des six golems.

## Criteres de validation

Les regles communes seront validees si :

- le debut et la fin d'un combat donnent toujours un resultat previsible ;
- les degats, reactions, phases et fenetres de vulnerabilite sont mesurables ;
- aucune attaque ne commence sans signe lisible ;
- une perte de vie reinitialise completement le combat ;
- la barre de vie transmet l'etat du boss sans masquer l'action ;
- les exceptions de Tata Lisa sont explicitement identifiees.

## Sources

- [Principes des golems](../../Concept-Game/08-Boss/Principes-des-Golems.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Degats](../Combat/Degats.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Checkpoints](../Systemes/Checkpoints.md)
- [HUD](../../Concept-Game/11-Interface/HUD.md)
- [Reference video des degats des boss](Reference-Video-Wonder-Boy-Degats-Boss.md)
- [Reference video des dimensions des boss](Reference-Video-Wonder-Boy-Dimensions-Boss.md)
- [Reference video des collisions avec le corps des boss](Reference-Video-Wonder-Boy-Collisions-Boss.md)
- [Reference video du rythme des attaques de boss](Reference-Video-Wonder-Boy-Rythme-Boss.md)
- [Reference video de la defaite d'un boss](Reference-Video-Wonder-Boy-Defaite-Boss.md)
