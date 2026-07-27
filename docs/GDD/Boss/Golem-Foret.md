# Golem de la Foret

> **Statut :** Valide

## Objectif

Definir le premier gardien du jeu comme un combat d'apprentissage lisible. Le joueur doit pouvoir appliquer le saut, la Shadow Sword et le Bouclier de lumiere sans que le Dash ou le Double saut soient obligatoires.

## Role du combat

- Introduire les regles communes des combats de golems.
- Apprendre a reconnaitre une preparation avant une attaque.
- Encourager une defense adaptee puis une contre-attaque contre la tete.
- Proposer un premier boss simple sans supprimer la necessite d'observer.

## Structure du cycle validee

- Le Golem de la Foret possede exactement `3 attaques`.
- Ces attaques utilisent un ordre fixe et previsible.
- La premiere attaque reste identique a chaque tentative.
- Apres la troisieme attaque, le cycle reprend depuis la premiere.
- Chaque attaque respecte la recuperation commune de `0.30 s` puis la pause neutre de `1.80 s`.
- Les trois attaques doivent pouvoir etre evitees avec les actions disponibles des le niveau 0.
- Le Dash et le Double saut peuvent aider, mais ne sont jamais obligatoires.
- Le cycle utilise toujours l'ordre suivant :

| Ordre | Attaque | Fonction principale |
|---:|---|---|
| 1 | Projectile vegetal frontal | Utiliser le Bouclier de lumiere ou eviter le projectile |
| 2 | Onde de racines au sol | Sauter au-dessus du danger |
| 3 | Coup de poing direct | Gerer la distance et le placement |

- Apres le coup de poing direct, le cycle reprend avec le projectile vegetal frontal.
- Les comportements, les valeurs et les signaux des trois attaques sont valides dans les sections suivantes.

## Attaque 1 - Projectile vegetal frontal

> **Statut :** Validee

### Structure validee

- Le golem lance exactement `2 projectiles vegetaux consecutifs`.
- Les deux projectiles appartiennent a une seule attaque du cycle.
- Ils sont produits pendant la meme phase dangereuse.
- La preparation avant le premier lancement dure exactement `0.75 s`.
- La direction horizontale de toute la salve est verrouillee au debut de cette preparation.
- Le premier projectile est lance a la fin de ces `0.75 s`.
- Le Bouclier de lumiere peut bloquer chaque projectile selon les regles deja validees.
- Chaque projectile bloque disparait immediatement.
- Les deux projectiles peuvent egalement etre evites.
- Le lancement du second projectile ne constitue pas une nouvelle attaque et ne declenche pas la recuperation commune.
- La recuperation de `0.30 s` commence uniquement apres la fin complete de la salve.
- Le second projectile est lance exactement `0.75 s` apres le premier.
- Cet intervalle est mesure entre les instants de lancement des deux projectiles.
- Recevoir un degat pendant la salve ne modifie pas cet intervalle.
- Le premier projectile suit une ligne horizontale basse, pres du sol.
- Le second projectile suit une ligne horizontale a hauteur du torse d'Imran.
- Les deux projectiles avancent dans la direction verrouillee au debut de la preparation.
- Ils ne suivent pas Imran et ne corrigent jamais leur hauteur ou leur direction apres leur lancement.
- Un changement de cote, un saut ou une chute d'Imran ne modifie pas leur trajectoire.
- Les deux projectiles peuvent etre bloques par le Bouclier de lumiere lorsque Imran leur fait face.
- Chaque projectile utilise une zone dangereuse carree de `24 x 24 px`.
- L'effet visuel reste centre sur cette zone et permet d'identifier clairement ses limites.
- Son apparence est celle d'une petite pierre grise couverte de mousse.
- De fines racines lumineuses vertes entourent la pierre et indiquent sa nature magique.
- Le visuel ne depasse pas suffisamment la zone dangereuse pour rendre sa collision trompeuse.
- Le centre du premier projectile reste a `16 px` au-dessus du sol de reference de l'arene.
- Sa zone dangereuse couvre donc une hauteur comprise entre `4 px` et `28 px`.
- Le centre du second projectile reste a `40 px` au-dessus du meme sol de reference.
- Sa zone dangereuse couvre donc une hauteur comprise entre `28 px` et `52 px`.
- Un changement de relief propre a l'arene devra conserver des trajectoires visuellement coherentes et sans collision cachee dans le sol.
- Les deux projectiles avancent a une vitesse constante de `400 px/s`.
- Ils ne ralentissent et n'accelerent jamais pendant leur trajectoire.
- Chaque projectile possede une duree de vie maximale de `2.00 s`.
- Il peut donc parcourir au maximum `800 px`.
- Il disparait immediatement lors d'un blocage par le Bouclier, d'un impact valide avec Imran, d'une collision avec le decor ou a la fin de ces `2.00 s`.
- Un impact valide retire `1 coeur` a Imran.
- L'invulnerabilite standard de `1.30 s` empeche le second projectile de retirer un autre coeur si le premier vient deja de toucher Imran.
- La recuperation commence apres le lancement du second projectile.
- Si le second projectile ne rencontre rien, il disparait `0.10 s` avant la preparation suivante.

### Signal visuel valide

- Au debut de la preparation, le golem rassemble ses deux poings devant son coeur magique vert.
- Le coeur et les fissures vertes augmentent progressivement en intensite pendant les `0.75 s`.
- Quelques feuilles et particules vegetales convergent vers ses poings.
- A la fin de la preparation, le golem abaisse un premier poing dans la direction verrouillee et lance le projectile bas.
- `0.75 s` plus tard, il tend son autre poing a hauteur du torse et lance le second projectile.
- Les deux gestes restent diriges vers le cote verrouille au debut de la preparation, meme si Imran change ensuite de cote.
- Le retour a la posture neutre commence immediatement apres le second lancement.
- Le signal reste comprehensible sans les effets lumineux et sans le son grace aux deux poses de tir distinctes.

### Assets visuels a produire

- pose de preparation avec les poings places devant le coeur ;
- variation lumineuse du coeur et des fissures vertes ;
- pose de lancement du projectile bas ;
- pose de lancement du projectile a hauteur du torse ;
- animation de recuperation vers la posture neutre ;
- petite pierre moussue de `24 x 24 px` entouree de racines lumineuses ;
- feuilles et particules d'energie verte sur des calques separes.

### Signal sonore valide

- Un grondement de pierre commence avec la preparation.
- Son intensite augmente progressivement pendant les `0.75 s`.
- Le premier lancement produit un impact sonore lourd et bref.
- Le second lancement produit le meme son `0.75 s` plus tard.
- Les sons de lancement indiquent la creation des projectiles et non leur collision avec une cible.
- Un blocage, un impact avec Imran ou une collision avec le decor conserve son propre retour sonore.
- Le grondement s'arrete au lancement du premier projectile afin de ne pas masquer le second signal.

## Attaque 2 - Onde de racines au sol

> **Statut :** Validee

### Structure validee

- L'attaque fait apparaitre les racines directement sous une position d'Imran.
- Cette position est memorisee au debut de la preparation.
- La cible correspond au point du sol situe sous Imran a cet instant.
- La zone cible ne suit plus Imran pendant le reste de la preparation.
- Un deplacement, un saut, une chute ou un Dash ne modifie donc pas le point memorise.
- Les racines surgissent uniquement au point annonce lorsque la preparation se termine.
- Si Imran se trouve dans les airs au debut de la preparation, le point utilise reste sa projection verticale sur le sol praticable de l'arene.
- La preparation dure exactement `0.75 s`.
- Le point cible est memorise au debut de ces `0.75 s`.
- Les racines surgissent a la fin de cette duree.
- L'attaque retire `1 coeur` lors d'un impact valide.
- Le Bouclier de lumiere ne bloque pas cette attaque de sol.
- L'attaque doit pouvoir etre evitee sans utiliser obligatoirement le Dash ou le Double saut.

### Signal visuel au sol valide

- Des fissures vertes apparaissent immediatement autour du point memorise.
- De petites racines deviennent progressivement visibles dans ces fissures.
- L'intensite lumineuse et le nombre de racines augmentent pendant les `0.75 s`.
- Le contour de cet avertissement correspond exactement a la largeur de la future zone dangereuse.
- Le signal reste sans danger pendant toute la preparation.
- Les racines dangereuses surgissent uniquement a la fin des `0.75 s`.
- Le contraste du vert doit conserver la lisibilite du signal sur la terre, l'herbe, la pierre et les autres surfaces de l'arene.

### Zone dangereuse validee

- L'eruption utilise une zone dangereuse de `96 x 64 px`.
- Cette zone est centree horizontalement sur le point memorise.
- Elle couvre donc `48 px` a gauche et `48 px` a droite de ce point.
- Sa base suit le sol praticable utilise pour placer l'avertissement.
- Elle s'etend jusqu'a `64 px` au-dessus de ce sol.
- Le signal de preparation dessine la meme largeur de `96 px`.
- La hauteur visuelle des racines correspond a la hauteur dangereuse afin de ne pas creer de collision invisible.
- La zone devient dangereuse au moment ou les racines surgissent.
- Elle reste active pendant exactement `0.40 s`.
- Les racines restent entierement visibles pendant cette periode.
- A la fin des `0.40 s`, la zone dangereuse est desactivee avant le debut de leur retrait visuel.
- Les racines se retirent pendant la recuperation commune de `0.30 s`.
- Entrer dans les racines pendant leur retrait ne retire aucun coeur.

### Animation du golem validee

- Au debut de la preparation, le golem se penche vers l'avant.
- Il place ses deux mains au sol et conserve cette pose.
- Les fissures vertes apparaissent au point cible des le debut de ce mouvement.
- Le golem appuie visiblement ses deux mains contre le sol pendant les `0.75 s`.
- Les racines surgissent lorsqu'il termine cette pression.
- Il maintient ses mains au sol pendant les `0.40 s` de danger.
- Il se redresse et revient a sa posture neutre pendant la recuperation de `0.30 s`.
- Il ne se deplace pas pendant la preparation, l'eruption ou la recuperation.
- Sa tete reste vulnerable et sa zone vulnerable suit sa nouvelle position pendant toute cette animation.
- Recevoir un degat ne modifie ni la pose, ni le point cible, ni le moment de l'eruption.

### Assets visuels a produire

- transition de la posture neutre vers la pose penchee ;
- pose avec les deux mains appuyees au sol ;
- mouvement de pression qui declenche l'eruption ;
- retour vers la posture neutre ;
- fissures vertes et petites racines pour les `0.75 s` d'avertissement ;
- eruption de racines correspondant a une zone de `96 x 64 px` ;
- animation de retrait non dangereuse pendant `0.30 s`.

### Signal sonore valide

- Un grondement grave commence au debut de la preparation.
- Il accompagne la pression des deux mains contre le sol pendant les `0.75 s`.
- Son intensite augmente jusqu'au surgissement des racines.
- Un impact lourd et bref est joue exactement lorsque la zone devient dangereuse.
- Le grondement s'arrete au moment de cet impact afin de ne pas masquer les autres sons du combat.
- Un degat inflige a Imran conserve le retour sonore standard des degats.
- La fin des `0.40 s` de danger ne produit aucun second impact susceptible de faire croire a une nouvelle attaque.

## Attaque 3 - Coup de poing direct

> **Statut :** Validee

### Structure validee

- Le golem avance d'un pas avant de porter son coup de poing.
- La direction horizontale est verrouillee au debut de la preparation.
- Le pas et le coup sont toujours effectues dans cette direction.
- Le golem ne poursuit pas Imran et ne change jamais de cote pendant cette attaque.
- Le coup est porte immediatement apres la fin du pas.
- Le joueur peut eviter l'attaque en creant de la distance ou en sautant.
- Le Dash et le Double saut ne sont pas obligatoires.
- Le corps du golem conserve sa zone dangereuse permanente pendant son avancee.
- Le poing utilise une zone dangereuse propre uniquement pendant la fenetre active du coup.
- Un impact valide du poing retire `1 coeur`.
- Le pas couvre exactement `96 px` dans la direction verrouillee.
- Cette distance ne change pas selon la position d'Imran.
- Le pas dure exactement `0.40 s`.
- Sa vitesse moyenne est donc de `240 px/s`.
- La preparation avant le debut du pas dure exactement `0.75 s`.
- Le golem reste immobile pendant cette preparation.
- La direction est verrouillee au debut de ces `0.75 s`.
- Le pas commence immediatement a la fin de la preparation.
- La zone dangereuse du poing mesure `64 x 48 px`.
- Son bord interieur reste aligne avec le bord avant de la zone corporelle du golem.
- Elle s'etend donc de `64 px` devant le golem, sans espace entre les deux zones.
- Son centre reste place a `48 px` au-dessus du sol de l'arene.
- Elle couvre donc une hauteur comprise entre `24 px` et `72 px`.
- Un saut simple complet permet de passer au-dessus de cette zone.
- Elle devient active lorsque le poing commence son extension apres le pas.
- Elle suit le poing pendant exactement `0.20 s`.
- Elle disparait avec la fin de cette fenetre active.
- Un meme coup ne peut retirer qu'un seul coeur.
- Le bras et le poing reviennent ensuite a leur posture neutre pendant la recuperation commune de `0.30 s`.
- Le poing ne reste pas dangereux pendant ce retrait.

### Signal visuel valide

- Au debut de la preparation, le golem ramene son poing d'attaque derriere lui.
- Il avance son epaule opposee et prend appui sur ses jambes.
- Cette pose reste lisible pendant les `0.75 s`.
- La silhouette et l'orientation du poing indiquent le cote verrouille de l'attaque.
- Aucun effet lumineux n'est necessaire pour comprendre le danger.
- Le golem conserve son poing arme pendant le pas de `0.40 s`.
- Il tend le poing immediatement apres avoir parcouru les `96 px`.
- Sa tete reste vulnerable et sa zone vulnerable suit son animation.
- Recevoir un degat ne modifie ni la pose, ni le pas, ni le coup.

### Assets visuels a produire

- transition de la posture neutre vers la pose d'armement ;
- pose avec le poing ramene et l'epaule opposee avancee ;
- pas offensif de `96 px` ;
- extension du bras et du poing ;
- recuperation vers la posture neutre.

### Signal sonore valide

- Un frottement de pierre accompagne l'armement du poing pendant les `0.75 s`.
- Un pas lourd accompagne l'avancee de `96 px` pendant `0.40 s`.
- Un souffle puissant est joue lorsque le poing commence son extension.
- Ce souffle annonce la fenetre dangereuse de `0.20 s`.
- Le souffle ne produit pas un faux son d'impact lorsque le coup ne touche rien.
- Un impact valide avec Imran ajoute le retour sonore standard des degats.
- Les sons s'arretent avant la recuperation afin de rendre la fin du danger identifiable.

### Limite de l'avancee validee

- Le golem ne traverse jamais un mur, un obstacle solide ou une limite de son arene.
- Si un obstacle empeche les `96 px`, il s'arrete au dernier point valide.
- La distance du pas est alors raccourcie.
- La phase d'avancee conserve cependant sa duree totale de `0.40 s`.
- Le golem attend immobile pendant le temps restant si son deplacement est termine plus tot.
- Le coup de poing commence toujours a la fin de ces `0.40 s`.
- La zone du poing conserve ses dimensions, sa hauteur et sa duree active normales.
- L'attaque n'est ni annulee, ni retournee vers l'autre cote.
- Apres le coup et la recuperation, le golem conserve sa nouvelle position.
- Il ne recule pas vers sa position precedente et ne revient pas automatiquement a son point de depart.
- Les attaques suivantes commencent depuis cette nouvelle position.
- Le projectile vegetal et l'onde de racines ne deplacent pas le golem.
- Seul un nouveau coup de poing direct peut donc modifier durablement sa position.

## Points de vie

- Le Golem de la Foret possede `12 PV`.
- Les degats et la finition au Smash Tranchant suivent les regles communes validees.

## Recompense

- La victoire rend le coffre de la Foret disponible.
- Le coffre contient la premiere cle.
- La recuperation de la cle sauvegarde la progression et termine le niveau.

### Coffre, cle et transition

> **Statut :** Valide

- Le coffre se trouve dans une zone de recompense situee hors du cadre de combat, a droite.
- Il ne doit jamais etre visible pendant la presentation ou le combat.
- Il utilise du bois, des racines, des feuilles et des motifs naturels.
- Il ne produit aucun rayon, aucune lumiere doree et aucun effet lumineux.
- Il passe a l'etat `Disponible` a la fin de la sequence de defaite du golem.
- Imran doit se placer a `56 px` ou moins du coffre puis utiliser la commande `Interaction`.
- Cette interaction lance une sequence de `2.00 s`.
- Le deplacement, le saut, le Dash et les attaques restent bloques pendant cette sequence.
- Le couvercle s'ouvre et la premiere cle sort du coffre.
- De `0.00 a 0.75 s`, le couvercle et son mecanisme s'ouvrent.
- De `0.75 a 1.50 s`, la premiere cle sort progressivement du coffre.
- De `1.50 a 2.00 s`, elle reste visible au-dessus du coffre.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- La cle est ajoutee automatiquement a la progression a la fin des `2.00 s`.
- La sauvegarde automatique commence immediatement apres cet ajout.
- Les coeurs et les vies sont restaures a `3`.
- Le niveau suivant devient la Grotte mysterieuse.
- La transition attend la confirmation de la sauvegarde.
- La barriere magique verte disparait avec la fin du niveau.
- Le coffre utilise le son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.
- Ce son commence avec l'interaction et dure pendant les `2.00 s` de la sequence.
- Aucun son supplementaire propre au bois, aux racines, aux feuilles ou a la premiere cle n'est ajoute.
- Le controle reste bloque apres la fin des `2.00 s`.
- Une fois la sauvegarde confirmee, un fondu au noir commence.
- La barriere disparait pendant ce fondu avec le reste de l'arene.
- La Grotte mysterieuse est chargee pendant l'ecran noir.
- Imran ne reprend pas le controle dans l'arene de la Foret.
- Le fondu au noir dure exactement `0.75 s`.
- L'arene de la Foret est retiree uniquement lorsque l'ecran est entierement noir.
- L'ecran reste noir tant que la Grotte mysterieuse n'est pas prete.
- La Grotte mysterieuse apparait ensuite avec un fondu depuis le noir de `0.75 s`.
- Le controle d'Imran reste bloque pendant ce fondu.
- Il est rendu lorsque la Grotte est entierement visible.
- Imran commence ce niveau avec `3 coeurs` et `3 vies`.

## Arene

> **Statut :** Valide

### Structure validee

- L'arene utilise un sol unique et entierement plat.
- Elle ne contient aucune plateforme surelevee.
- Elle ne contient aucune pente, aucun trou et aucun passage traversable.
- Aucun piege et aucun danger environnemental ne peuvent blesser Imran.
- La limite gauche et le passage droit ferme empechent Imran ainsi que le golem de quitter l'espace de combat.
- L'onde de racines peut utiliser tout point valide de ce sol.
- Les projectiles disparaissent lorsqu'ils rencontrent une limite solide.
- Les trois attaques restent evitables sans utiliser le decor comme protection.
- La largeur utile entre les deux limites solides mesure exactement `1280 px`.
- Cette largeur correspond a `20` grilles logiques de `64 px`.
- Les positions horizontales sont mesurees depuis la limite interieure gauche de l'arene.
- Imran commence la presentation avec son centre a `128 px`.
- Le Golem de la Foret commence avec son centre a `1024 px`.
- Le golem est tourne vers la gauche et fait face a Imran.
- La distance initiale entre les centres d'Imran et du golem est de `896 px`.
- Le projectile apparait devant le poing du golem et sa portee de `800 px` lui permet encore d'atteindre la zone d'Imran.
- Le coffre reste inaccessible tant que la sequence de defaite du golem n'est pas terminee.

### Camera validee

- La camera reste fixe pendant la presentation, le combat, l'etat `Etourdi` et la sequence de defaite.
- Le cadrage de combat montre simultanement Imran, le golem et les limites de la zone de combat.
- Le coffre reste entierement hors du cadre, a droite.
- Elle ne suit ni Imran, ni le golem.
- Elle ne se recentre pas lorsque le golem conserve une nouvelle position apres son coup de poing.
- A la resolution de reference `1920 x 1080`, la largeur utile de `1280 px` est centree horizontalement.
- La limite gauche utile se trouve donc a `320 px` de l'ecran.
- La limite droite utile se trouve a `1600 px` de l'ecran.
- Les positions initiales du combat apparaissent a l'ecran aux coordonnees horizontales suivantes :

| Element | Position locale | Position a l'ecran |
|---|---:|---:|
| Imran | `128 px` | `448 px` |
| Golem | `1024 px` | `1344 px` |

### Defilement vers la recompense valide

- A la fin de la sequence de defaite, le passage situe a droite devient accessible.
- Le controle d'Imran revient, mais la camera ne se deplace pas automatiquement.
- Imran doit avancer lui-meme vers la droite.
- La camera commence alors a defiler horizontalement avec lui.
- La position verticale et le cadrage vertical restent fixes.
- Le coffre apparait progressivement pendant ce deplacement.
- Si Imran reste immobile dans la zone de combat, le coffre reste hors champ.
- Le defilement s'arrete lorsque la zone de recompense et le coffre sont entierement cadres.
- Aucun ennemi, projectile ou danger n'apparait pendant ce trajet.
- La zone de recompense commence apres la limite droite du combat, a `x = 1280 px`.
- Elle mesure exactement `640 px`, soit `10` grilles logiques.
- La longueur totale accessible de l'arene et de sa zone de recompense atteint donc `1920 px`.
- Son sol prolonge le sol plat du combat et reste place a `y = 896 px`.
- Elle ne contient aucune plateforme, aucun trou, aucun piege et aucun ennemi.
- Le coffre possede son centre a la position locale `x = 1824 px`.
- Il reste a `96 px` de la limite droite finale placee a `x = 1920 px`.
- Le coffre est entierement hors du cadre de combat, dont la vue initiale se termine a la position locale `x = 1600 px`.
- Lorsque la camera atteint son decalage maximal de `640 px`, le coffre apparait a `x = 1504 px` dans l'ecran.
- La camera reste fixe tant que le centre d'Imran ne depasse pas la position locale `x = 1280 px`.
- Le defilement commence uniquement lorsque son centre franchit cette limite et entre dans la zone de recompense.
- Imran se trouve donc temporairement au bord droit du cadre de combat avant le debut du mouvement de camera.
- Lors du declenchement, Imran apparait a environ `x = 1600 px` dans l'ecran.
- La camera effectue alors un recentrage horizontal de `128 px` pendant `0.50 s`.
- Imran est ainsi replace progressivement a `x = 1472 px` dans l'ecran.
- Le joueur conserve le controle pendant ce recentrage.
- Apres ces `0.50 s`, la camera suit la marche d'Imran vers la droite et le maintient a cette position de reference.
- Le decalage horizontal de la camera ne peut jamais depasser `640 px`.
- La camera ne change jamais sa position verticale.
- Le decalage maximal deja atteint ne diminue jamais.
- Si Imran repart vers la gauche, la camera reste donc a sa position actuelle.
- Imran peut se deplacer vers la gauche dans la portion encore visible de l'arene.
- Le bord gauche de l'ecran l'empeche de quitter le cadre.
- La camera ne montre plus une zone abandonnee une fois qu'elle l'a depassee.

### Cadrage vertical valide

- La surface praticable du sol se trouve a `y = 896 px` dans l'ecran de reference `1920 x 1080`.
- Cette position reste fixe pendant toute la sequence de l'arene.
- Les pieds d'Imran et la base du golem reposent sur cette ligne.
- Avec sa hauteur visuelle de `64 px`, Imran occupe verticalement la zone comprise entre `832 px` et `896 px`.
- Avec sa hauteur visuelle de `152 px`, le golem occupe verticalement la zone comprise entre `744 px` et `896 px`.
- Le premier projectile vegetal possede son centre a `y = 880 px`.
- Le second projectile vegetal possede son centre a `y = 856 px`.
- L'onde de racines peut atteindre `y = 832 px`.
- Le coup de poing possede son centre a `y = 848 px` et couvre la zone comprise entre `824 px` et `872 px`.
- Les `184 px` situes sous la surface du sol servent au premier plan et a l'epaisseur visuelle du terrain, sans creer une zone jouable supplementaire.
- Ce cadrage reprend l'intention de composition observee dans la reference Wonder Boy tout en respectant la grille logique du projet.

### Fermeture de la zone de combat validee

- Deux barrieres magiques identiques ferment la zone de combat.
- La premiere apparait derriere Imran, sur la limite gauche.
- La seconde apparait devant le passage vers la recompense, sur la limite droite.
- Les deux barrieres utilisent une energie verte correspondant au Golem de la Foret.
- Elles forment des murs d'energie semi-transparents.
- Des particules vertes et de petites formes rappelant des feuilles circulent dans chaque mur.
- Le decor reste visible a travers leur energie.
- La densite des particules permet cependant d'identifier clairement deux limites infranchissables.
- Elles ne retirent aucun coeur lors d'un contact.
- Imran, le golem et les projectiles ne peuvent pas les traverser.
- Un projectile vegetal du golem disparait lorsqu'il entre en collision avec une barriere.
- Leurs collisions deviennent actives immediatement lorsque le combat est declenche.
- Leurs energies visibles montent depuis le sol place a `y = 896 px` jusqu'en haut de l'ecran.
- Les deux apparitions commencent au meme instant et durent exactement `0.50 s`.
- Elles se deroulent pendant le debut de la presentation de `3.00 s`.
- Les barrieres conservent ensuite leur hauteur complete et leur mouvement continu de particules.
- Leur largeur visible et solide mesure `32 px`.
- Le bord interieur de la barriere gauche se trouve a la position locale `x = 0 px`.
- Elle s'etend vers l'exterieur de la zone de combat, entre `x = -32 px` et `x = 0 px`.
- Le bord interieur de la barriere droite se trouve a la position locale `x = 1280 px`.
- Elle s'etend vers la zone de recompense, entre `x = 1280 px` et `x = 1312 px`.
- Les barrieres ne reduisent donc pas les `1280 px` de largeur utile du combat.
- Leur apparition et leur maintien ne produisent aucun son.
- Aucun bourdonnement continu n'accompagne leurs particules.
- La barriere gauche reste active jusqu'a la recuperation de la premiere cle et la fin du niveau.
- La barriere droite reste active pendant la presentation, le combat, l'etat `Etourdi` et la sequence de defaite.
- La barriere droite commence a redescendre lorsque la sequence de defaite atteint `0.50 s`.
- Cette descente dure exactement `0.50 s`.
- Elle conserve sa collision solide pendant toute la descente.
- Sa collision est desactivee lorsqu'elle disparait completement a `1.00 s`.
- Le passage vers la zone de recompense devient donc accessible au retour du controle.
- Cette disparition reste silencieuse comme son apparition.
- Apres une perte de vie, les deux barrieres disparaissent pendant la reinitialisation et peuvent etre activees de nouveau lors de la tentative suivante.

## Presentation du Golem de la Foret

> **Statut :** Validee

### Deroulement visuel valide

- Avant le declenchement, le golem reste immobile devant le passage qui conduit au coffre cache.
- Sa posture et sa mousse le font ressembler a une ancienne statue de pierre.
- Il ne possede aucune zone dangereuse ou vulnerable pendant cet etat.
- La presentation commence lorsque Imran franchit le point d'entree de l'arene.
- Les commandes d'Imran sont bloquees pendant toute la presentation.
- La sequence dure exactement `3.00 s`.

| Periode | Animation |
|---|---|
| `0.00 a 1.00 s` | Les racines qui entourent le golem commencent a bouger. |
| `1.00 a 2.00 s` | Les yeux, le coeur magique et les fissures vertes s'allument progressivement. |
| `2.00 a 3.00 s` | Le golem se redresse et prend sa posture de garde face a Imran. |

- La barriere magique verte monte silencieusement pendant les `0.50 s` du debut de cette sequence.
- Le golem ne se deplace pas horizontalement pendant son reveil.
- La barre de vie apparait lorsque la presentation atteint `3.00 s`.
- Le controle d'Imran revient au meme instant.
- Le golem devient vulnerable et son corps devient dangereux a cet instant.
- La preparation du premier projectile vegetal peut alors commencer.
- Une commande effectuee avant la fin des `3.00 s` reste ignoree.
- Une nouvelle tentative rejoue cette sequence complete depuis l'etat de statue.

### Signal sonore valide

- Un grondement grave commence au debut de la presentation.
- Il reste continu pendant les `3.00 s`.
- Son intensite augmente progressivement pendant le reveil du golem.
- Il accompagne successivement le mouvement des racines, l'illumination magique et le redressement.
- Aucun son distinct de barriere ne se superpose a ce grondement.
- Le grondement s'arrete lorsque la barre de vie apparait et que le controle d'Imran revient.
- Aucun cri ou rugissement supplementaire n'est joue a la fin de la presentation.

### Assets visuels a produire

- pose immobile de statue couverte de mousse ;
- animation des racines autour du corps ;
- illumination progressive des yeux ;
- illumination progressive du coeur et des fissures vertes ;
- redressement complet du golem ;
- transition vers la posture de garde ;
- particules de mousse, feuilles et poussiere liberees pendant le reveil.

## Defaite du Golem de la Foret

> **Statut :** Validee

### Deroulement visuel valide

- La sequence commence au contact du Smash Tranchant final avec le golem etourdi.
- Elle dure exactement `1.00 s`.
- La barre de vie disparait au debut de cette sequence.
- Le golem, ses fragments et ses particules ne possedent plus aucune zone dangereuse ou solide.

| Periode | Animation |
|---|---|
| `0.00 a 0.20 s` | Le coeur vert produit un dernier eclat, puis sa lumiere et celle des fissures s'eteignent. |
| `0.20 a 0.70 s` | Le corps se fragmente doucement en pierres, racines et feuilles. |
| `0.70 a 1.00 s` | Les fragments se transforment en particules vertes qui se dispersent et disparaissent. |

- La disparition reste non violente et adaptee au public vise.
- Aucun corps, fragment solide ou obstacle ne reste dans l'arene.
- Aucune piece et aucun objet de soin ne sont produits.
- La camera conserve son cadrage fixe pendant toute la sequence.
- Le coffre devient disponible lorsque la sequence atteint `1.00 s`.
- Le controle d'Imran revient au meme instant.
- La barriere magique verte reste active jusqu'a la recuperation de la cle.

### Signal sonore valide

- Un eclat magique bref accompagne la derniere lumiere du coeur entre `0.00 s` et `0.20 s`.
- Des craquements de pierre et de racines accompagnent la fragmentation entre `0.20 s` et `0.70 s`.
- Un bruissement de feuilles accompagne la dispersion entre `0.70 s` et `1.00 s`.
- Tous les sons de defaite s'arretent a la disparition des dernieres particules.
- Aucun son d'explosion violent n'est utilise.
- Le son d'ouverture du coffre reste distinct et ne commence qu'apres le retour du controle.

### Assets visuels a produire

- dernier eclat du coeur magique vert ;
- extinction du coeur et des fissures ;
- fragmentation du corps en pierres, racines et feuilles ;
- transition des fragments vers des particules vertes ;
- dispersion et disparition des particules ;
- pose finale vide permettant de retirer completement le golem.

## Criteres de validation

La fiche sera validee si :

- les trois attaques sont mesurables et possedent un ordre fixe ;
- chaque attaque offre une preparation visuelle et sonore lisible ;
- les trois attaques peuvent etre evitees sans utiliser obligatoirement le Dash ou le Double saut ;
- le joueur peut atteindre la tete avec la Shadow Sword ;
- aucune situation ne produit un degat inevitable ;
- le coffre reste invisible pendant le combat puis est revele par le defilement a droite ;
- la victoire respecte les regles communes des golems.

## Sources

- [Regles communes des boss](Regles-Communes.md)
- [Golem de la Foret du Concept Game](../../Concept-Game/08-Boss/Golem-de-la-Foret.md)
- [Niveau 1 - Foret](../Niveaux/Niveau-1-Foret.md)
- [Coffres et cles](../Systemes/Coffres-et-Cles.md)
- [Camera](../Systemes/Camera.md)
- [Statistiques d'Imran](../Joueur/Statistiques-Imran.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
