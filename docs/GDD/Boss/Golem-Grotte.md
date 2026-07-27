# Golem de la Grotte

> **Statut :** Valide

## Objectif

Definir le deuxieme gardien du jeu comme un prolongement du premier combat. Le joueur doit reutiliser les regles apprises contre le Golem de la Foret dans une arene et face a des attaques propres au theme mineral de la grotte.

## Role du combat

- Verifier la comprehension des preparations visuelles et sonores.
- Demander au joueur de choisir entre defense, esquive et contre-attaque.
- Reutiliser la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.
- Autoriser le Dash et le Double saut sans les rendre obligatoires.
- Augmenter legerement la difficulte sans introduire une seconde phase.

## Structure du cycle validee

- Le Golem de la Grotte possede exactement `3 attaques`.
- Ces attaques utilisent un ordre fixe et previsible.
- La premiere attaque reste identique a chaque tentative.
- Apres la troisieme attaque, le cycle reprend depuis la premiere.
- Recevoir un degat ne modifie pas l'ordre du cycle.
- Chaque attaque respecte la recuperation commune de `0.30 s` puis la pause neutre de `1.80 s`.
- Les trois attaques doivent pouvoir etre evitees avec les actions disponibles depuis le niveau 0.
- Le Dash et le Double saut peuvent aider, mais ne sont jamais obligatoires.
- Le cycle utilise toujours l'ordre suivant :

| Ordre | Attaque | Fonction principale |
|---:|---|---|
| 1 | Eclat de cristal frontal | Utiliser le Bouclier de lumiere ou eviter le projectile |
| 2 | Piliers de cristal | Sauter au-dessus des cristaux surgissant du sol |
| 3 | Chute de stalactites | Observer les avertissements et changer de position |

- Apres la Chute de stalactites, le cycle reprend avec l'Eclat de cristal frontal.
- Les comportements, les valeurs et les signaux des trois attaques seront valides dans les sections suivantes.

## Attaque 1 - Eclat de cristal frontal

> **Statut :** Validee

### Structure validee

- Le golem lance un unique gros cristal en ligne droite.
- La preparation avant le lancement dure exactement `0.60 s`.
- Le projectile se deplace horizontalement a hauteur du torse d'Imran.
- Sa vitesse horizontale constante est de `480 px/s`.
- Cette vitesse est superieure de `20 %` aux `400 px/s` du projectile vegetal du Golem de la Foret.
- Sa zone dangereuse mesure exactement `48 x 32 px`.
- Son centre se trouve a `40 px` au-dessus du sol de l'arene.
- Sa zone verticale couvre donc la hauteur comprise entre `24 px` et `56 px`.
- La forme visuelle du cristal doit couvrir au minimum cette zone sans creer de danger invisible.
- Sa duree de vie maximale est de `2.00 s`.
- Sa portee maximale est donc de `960 px` a la vitesse de `480 px/s`.
- La direction horizontale est verrouillee au debut de la preparation.
- Le projectile ne suit pas Imran apres son lancement.
- Le Bouclier de lumiere bloque automatiquement le projectile lorsqu'Imran lui fait face.
- Le projectile bloque disparait immediatement.
- Imran peut egalement eviter le projectile en sautant au-dessus.
- Le projectile retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ce projectile et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- Le projectile disparait apres une collision valide ou a la fin de sa duree de vie.
- Le projectile disparait toujours avant la preparation de l'attaque suivante.

### Signal visuel valide

- Au debut de la preparation, le golem s'oriente vers la position d'Imran et verrouille cette direction.
- Il recule le poing utilise pour le lancement.
- Une energie violette se concentre progressivement autour de ce poing.
- Le gros cristal se forme devant le poing avant le lancement.
- La concentration, la formation et la posture du bras occupent toute la preparation de `0.60 s`.
- La forme du cristal et l'orientation du golem permettent de comprendre la direction du tir avant son depart.
- Le cristal devient dangereux uniquement au moment de son lancement.
- Le signal reste visible et comprehensible lorsque le son est coupe.

### Signal sonore valide

- Une resonance minerale grave commence au debut de la preparation.
- Son intensite augmente progressivement pendant les `0.60 s` de charge.
- Un impact cristallin court et sec marque exactement le lancement du projectile.
- Le son de charge s'arrete au moment de cet impact.
- Aucun son supplementaire n'est necessaire pendant le trajet du cristal.
- La collision avec Imran, le bouclier ou le decor utilise un bref son d'eclat cristallin.

### Apparence du projectile validee

- Le projectile prend la forme d'un gros cristal d'amethyste pointu.
- Plusieurs facettes violettes rendent son volume et sa direction immediatement lisibles.
- Sa pointe principale est orientee dans le sens du deplacement.
- Une courte trainee d'energie violette suit le cristal sans agrandir sa zone dangereuse.
- La trainee reste assez courte pour ne pas masquer Imran ou le decor.
- Le projectile se fragmente en petits eclats violets lors de sa disparition.
- Les fragments de disparition sont uniquement visuels et ne causent aucun degat.

### Assets visuels et sonores a produire

- Animation du golem reculant son poing.
- Animation de concentration de l'energie violette.
- Animation de formation du cristal devant le poing.
- Animation de lancement.
- Projectile en cristal d'amethyste pointu.
- Effet de trainee violette.
- Effet de fragmentation sans danger.
- Son de resonance minerale grave.
- Son d'impact cristallin au lancement.
- Son bref d'eclat lors de la collision ou de la disparition.

## Attaque 2 - Piliers de cristal

> **Statut :** Validee

### Structure validee

- Le golem fait surgir exactement `3 piliers` de cristal depuis le sol.
- La preparation avant l'apparition du premier pilier dure exactement `0.60 s`.
- Les piliers apparaissent successivement et progressent depuis le golem vers Imran.
- Un intervalle fixe de `0.20 s` separe le debut de deux apparitions consecutives.
- Le premier pilier apparait a `0.00 s` apres la preparation.
- Le deuxieme pilier apparait a `0.20 s`.
- Le troisieme pilier apparait a `0.40 s`.
- Chaque pilier reste dangereux pendant exactement `0.25 s`.
- Le dernier pilier cesse donc d'etre dangereux a `0.65 s`.
- La sequence dangereuse complete reste inferieure a la duree normale du saut d'environ `0.71 s`.
- La zone dangereuse de chaque pilier mesure exactement `56 x 72 px`.
- Chaque zone commence au niveau du sol et atteint une hauteur de `72 px`.
- Le saut normal de `89 px` conserve une marge verticale de `17 px` au-dessus des piliers.
- La forme visuelle de chaque pilier doit couvrir sa zone dangereuse sans creer de danger invisible.
- La direction horizontale est verrouillee au debut de la preparation.
- La position d'Imran utilisee par l'attaque est egalement verrouillee au debut de la preparation.
- Le premier pilier apparait le plus pres du golem.
- Le deuxieme apparait plus loin dans la direction verrouillee.
- Le troisieme termine la progression au plus pres de la position verrouillee d'Imran.
- Dans le placement standard, le troisieme pilier est centre exactement sur la position horizontale verrouillee d'Imran.
- Le centre du deuxieme pilier se trouve `96 px` plus pres du golem.
- Le centre du premier pilier se trouve `192 px` plus pres du golem.
- Deux centres consecutifs sont donc toujours separes de `96 px`.
- Avec une largeur dangereuse de `56 px`, un espace horizontal de `40 px` separe deux zones consecutives.
- Si le premier pilier standard se trouve a moins de `112 px` du centre du golem, les trois positions sont decalees ensemble dans la direction verrouillee.
- Ce decalage place le centre du premier pilier a exactement `112 px` du centre du golem.
- Le deuxieme et le troisieme conservent leur espacement de `96 px`.
- Dans ce cas particulier, le troisieme pilier peut apparaitre au-dela de la position initialement verrouillee d'Imran.
- L'attaque contient toujours trois piliers et ne peut pas etre annulee en restant pres du golem.
- Apres cette correction de courte distance, les limites gauche et droite de l'ensemble sont verifiees.
- Si une zone depasse `x = 0 px` ou `x = 1280 px`, les trois piliers sont decales ensemble vers l'interieur.
- Les centres conservent leur espacement de `96 px` et le premier reste a au moins `112 px` du centre du golem.
- Les trois piliers restent entierement visibles et aucune partie dangereuse ne traverse une barriere.
- Aucun pilier ne suit Imran apres le debut de la preparation.
- Chaque pilier retire `1 coeur` en cas de contact valide.
- Le Bouclier de lumiere ne protege pas contre les piliers.
- Un saut normal permet d'eviter toute la sequence.
- Le Dash et le Double saut peuvent faciliter l'esquive, mais ne sont jamais obligatoires.

### Animation du golem validee

- Au debut de la preparation, le golem s'oriente vers la position d'Imran et verrouille la direction.
- Il leve une jambe et maintient son pied au-dessus du sol.
- Cette posture rend l'attaque differente des actions lancees avec les poings.
- Au terme des `0.60 s`, il frappe fortement le sol avec son pied.
- L'impact du pied declenche immediatement l'apparition du premier pilier.
- Le deuxieme et le troisieme piliers suivent selon les intervalles deja valides.
- Aucune zone ne devient dangereuse avant l'impact du pied.

### Signal visuel au sol valide

- Les trois futures zones dangereuses sont visibles pendant la preparation.
- Des fissures violettes apparaissent au sol a chacun des trois emplacements verrouilles.
- La premiere zone commence a briller avant la deuxieme, puis la troisieme suit.
- Cet ordre lumineux reprend exactement l'ordre d'apparition des piliers.
- Les fissures restent visibles jusqu'a l'apparition du pilier correspondant.
- Les fissures sont uniquement des avertissements et ne causent aucun degat.
- Leur couleur violette reste suffisamment contrastee avec le sol sombre de la grotte.
- Le joueur peut identifier les trois zones et leur ordre meme lorsque le son est coupe.

### Signal sonore valide

- Un grondement mineral commence au debut de la preparation de `0.60 s`.
- Le grondement augmente legerement pendant que le golem leve sa jambe.
- Un impact lourd marque le contact du pied avec le sol.
- Un craquement cristallin distinct accompagne l'apparition de chaque pilier.
- Les trois craquements suivent les intervalles de `0.20 s` deja valides.
- Le grondement s'arrete apres le troisieme craquement.
- Aucun son n'est necessaire lorsque les piliers cessent d'etre dangereux.

### Apparence et disparition validees

- Chaque pilier prend la forme d'un groupe de pointes d'amethyste irregulieres.
- Les facettes violettes restent visibles sur le sol sombre de la grotte.
- Les pointes sortent rapidement du sol au moment de leur activation.
- Leur forme visuelle couvre la zone dangereuse de `56 x 72 px`.
- A la fin des `0.25 s` de danger, chaque groupe se brise en petits fragments violets.
- Les fragments disparaissent rapidement et ne causent aucun degat.
- Aucun pilier ne reste comme obstacle apres sa fragmentation.

### Assets visuels et sonores a produire

- Animation du golem levant une jambe.
- Animation du coup de pied au sol.
- Trois avertissements de fissures violettes.
- Groupe de pointes d'amethyste irregulieres.
- Animation de sortie du sol.
- Effet de fragmentation violette sans danger.
- Son de grondement mineral.
- Son d'impact lourd du pied.
- Trois craquements cristallins successifs.

## Attaque 3 - Chute de stalactites

> **Statut :** Validee

### Structure validee

- Le golem provoque la chute de `3 stalactites` exactement.
- La preparation avant leur chute dure exactement `0.60 s`.
- Les trois stalactites tombent simultanement.
- Les trois stalactites se detachent au terme de la preparation.
- Leur chute jusqu'au sol dure exactement `0.40 s`.
- Chaque stalactite reste dangereuse pendant toute cette descente.
- Les trois positions sont calculees autour de la position horizontale d'Imran au debut de la preparation.
- Ces positions sont verrouillees pendant toute l'attaque.
- Aucun stalactite ne suit Imran apres le debut de la preparation.
- Hors correction aux limites de l'arene, une stalactite est centree sur la position verrouillee d'Imran.
- Les deux autres sont placees de chaque cote de cette position.
- La zone dangereuse de chaque stalactite mesure exactement `48 x 96 px`.
- Les centres de deux stalactites voisines sont separes de `64 px`.
- Les deux stalactites laterales sont donc centrees a `64 px` de la position verrouillee d'Imran.
- L'ensemble des trois zones couvre une largeur totale de `176 px`.
- Si le bord gauche de l'ensemble depasse la limite locale `x = 0 px`, les trois positions sont decalees ensemble vers la droite.
- Si le bord droit de l'ensemble depasse la limite locale `x = 1280 px`, les trois positions sont decalees ensemble vers la gauche.
- Le decalage s'arrete des que les trois zones dangereuses se trouvent entierement dans l'arene.
- Les centres conservent toujours leur espacement de `64 px`.
- Les trois stalactites restent visibles et aucune partie dangereuse ne traverse une barriere.
- Depuis la position centrale, la zone vulnerable d'Imran doit parcourir environ `104 px` pour sortir completement de l'ensemble.
- En partant de l'arret, Imran peut parcourir environ `128 px` pendant les `0.60 s` de preparation.
- L'esquive normale conserve donc une marge horizontale d'environ `24 px`.
- Imran doit quitter horizontalement l'ensemble des zones annoncees avant la chute.
- Le deplacement normal permet d'eviter toute l'attaque.
- Le Dash peut faciliter l'esquive, mais il n'est jamais obligatoire.
- Le Bouclier de lumiere ne protege pas contre les stalactites.
- Chaque stalactite retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche les trois stalactites de retirer plusieurs coeurs pendant la meme chute.

### Signal visuel des zones valide

- Des fissures violettes apparaissent au plafond au debut de la preparation.
- Chaque fissure correspond a la position horizontale d'une stalactite.
- Trois ombres violettes apparaissent simultanement sur le sol.
- Chaque ombre couvre exactement la largeur dangereuse de `48 px` de sa stalactite.
- Les ombres indiquent les positions d'impact pendant toute la preparation de `0.60 s`.
- Les fissures et les ombres restent fixes pendant la chute de `0.40 s`.
- Les ombres sont uniquement des avertissements et ne causent aucun degat.
- Leur couleur reste suffisamment contrastee avec le sol sombre de la grotte.
- Les trois zones restent comprehensibles lorsque le son est coupe.

### Animation du golem validee

- Au debut de la preparation, le golem leve ses deux mains vers le plafond.
- Son coeur d'amethyste produit des pulsations violettes pendant les `0.60 s`.
- Les fissures du plafond reagissent visuellement a chaque pulsation.
- Le golem maintient ses deux mains levees jusqu'a la fin de la preparation.
- Il referme brusquement ses deux poings au moment du detachement des stalactites.
- Les trois stalactites commencent leur chute exactement au meme instant.
- Le golem conserve sa posture jusqu'a leur impact au sol.
- Il commence ensuite la recuperation commune de `0.30 s`.

### Signal sonore valide

- Une resonance profonde de grotte commence au debut de la preparation.
- Des craquements rocheux accompagnent les fissures qui apparaissent au plafond.
- Les trois stalactites produisent un sifflement commun pendant leur chute de `0.40 s`.
- Trois impacts cristallins simultanes marquent leur contact avec le sol.
- La resonance et le sifflement s'arretent au moment des impacts.
- Le signal sonore complete les avertissements visuels sans les remplacer.

### Impact valide

- Les stalactites se brisent immediatement au contact du sol.
- Leurs zones dangereuses disparaissent exactement au moment de cet impact.
- La fragmentation produit de petits eclats violets et des particules de roche.
- Ces fragments sont uniquement visuels et ne causent aucun degat.
- Aucun morceau ne reste comme obstacle dans l'arene.
- Aucune onde de choc et aucun danger secondaire ne sont produits.
- La recuperation commune du golem commence apres cette disparition.

### Apparence validee

- Chaque stalactite est principalement composee de roche gris fonce.
- Des veines d'amethyste violette lumineuse parcourent sa surface.
- La pointe reste assez claire pour montrer la direction verticale du danger.
- Les veines deviennent plus lumineuses pendant les `0.60 s` de preparation.
- La forme visuelle couvre la zone dangereuse de `48 x 96 px`.
- Les eclats produits a l'impact reprennent la roche sombre et la lumiere violette.

### Assets visuels et sonores a produire

- Animation du golem levant les deux mains.
- Animation des pulsations du coeur d'amethyste.
- Animation des poings qui se referment.
- Trois fissures violettes au plafond.
- Trois ombres violettes au sol.
- Stalactite en roche sombre avec veines d'amethyste.
- Animation de chute.
- Effet de fragmentation en roche et eclats violets sans danger.
- Son de resonance profonde de la grotte.
- Son de craquement du plafond.
- Son de sifflement pendant la chute.
- Son des trois impacts cristallins simultanes.

## Arene

> **Statut :** Validee

### Structure validee

- La zone de combat utilise un sol entierement plat.
- Elle ne contient aucune plateforme, pente, fosse ou difference de hauteur.
- Aucun piege et aucun danger independant du golem ne sont presents.
- Un plafond rocheux visible permet d'integrer les trois stalactites.
- Les stalactites de l'attaque apparaissent uniquement aux positions annoncees.
- Les autres stalactites visibles au plafond restent purement decoratives.
- Les cristaux, minerais et rochers places au premier plan ou a l'arriere-plan ne possedent aucune collision dangereuse.
- Les decorations ne masquent jamais Imran, le golem, les fissures, les ombres ou les projectiles.
- Le sol reste suffisamment contraste avec les fissures et les ombres violettes.
- La zone de combat mesure exactement `1280 px` de largeur utile.
- Cette largeur correspond a `20 grilles` de `64 px`.
- Les couloirs d'entree et la future zone de recompense ne sont pas inclus dans cette mesure.
- Les positions horizontales locales sont mesurees depuis la limite interieure gauche de la zone de combat.
- Imran commence avec son centre horizontal a `128 px`.
- Le Golem de la Grotte commence avec son centre horizontal a `944 px`.
- La distance initiale entre leurs centres est donc de `816 px`.
- Il reste `336 px` entre le centre initial du golem et la limite droite de la zone de combat.
- Cet espace permet a la sequence de trois piliers de fonctionner lorsque Imran passe du cote droit du golem.
- Dans le cadre de reference `1920 x 1080`, le sol principal se trouve a `y = 896 px`.
- Imran et le golem reposent sur cette ligne lorsqu'ils sont au sol.
- Le bord inferieur visible du plafond rocheux se trouve a `y = 480 px`.
- Une stalactite attachee occupe initialement la hauteur comprise entre `480 px` et `576 px`.
- Sa pointe inferieure parcourt donc `320 px` avant d'atteindre le sol a `y = 896 px`.
- La chute de `0.40 s` utilise une vitesse verticale constante de `800 px/s`.
- Les stalactites decoratives ne se detachent jamais et ne partagent pas ces zones dangereuses.

### Fermeture magique validee

- Les deux barrieres utilisent une energie violette semi-transparente.
- Des fragments d'amethyste circulent continuellement dans cette energie.
- Les fragments sont uniquement visuels et ne possedent aucune collision.
- La barriere gauche occupe la position locale comprise entre `x = -32 px` et `x = 0 px`.
- La barriere droite occupe la position locale comprise entre `x = 1280 px` et `x = 1312 px`.
- Les deux barrieres montent en `0.50 s` au debut de la presentation.
- Elles restent silencieuses pendant leur apparition, leur activite et leur disparition.
- Leur fonctionnement pendant le combat, la defaite et l'acces au coffre suit les regles communes.

### Camera validee

- La camera reste fixe pendant la presentation, le combat actif, l'etat `Etourdi` et la sequence de defaite.
- Les `1280 px` utiles de l'arene sont centres dans le cadre de reference `1920 x 1080`.
- La limite gauche utile apparait a `x = 320 px` dans l'ecran.
- La limite droite utile apparait a `x = 1600 px` dans l'ecran.
- La camera ne suit ni Imran, ni le golem pendant le combat.
- Aucun zoom ni recentrage ne se produit avant la fin de la defaite.
- Les positions initiales apparaissent a l'ecran aux coordonnees suivantes :

| Element | Position locale | Position a l'ecran |
|---|---:|---:|
| Imran | `128 px` | `448 px` |
| Golem de la Grotte | `944 px` | `1264 px` |

### Zone de recompense validee

- La zone de recompense commence apres la limite droite du combat, a la position locale `x = 1280 px`.
- Elle mesure exactement `640 px`, soit `10 grilles` de `64 px`.
- La longueur totale accessible du combat et de la recompense atteint donc `1920 px`.
- Son sol prolonge le sol plat du combat a `y = 896 px`.
- Elle ne contient aucune plateforme, pente, fosse, piege ou ennemi.
- Le centre du coffre se trouve a la position locale `x = 1824 px`.
- Le coffre reste a `96 px` de la limite finale placee a `x = 1920 px`.
- Le coffre reste entierement hors du cadre pendant le combat.

### Defilement vers la recompense valide

- La camera reste fixe tant que le centre d'Imran ne depasse pas la position locale `x = 1280 px`.
- Le defilement commence uniquement lorsque son centre entre dans la zone de recompense.
- Imran apparait alors a environ `x = 1600 px` dans l'ecran.
- La camera effectue un recentrage horizontal de `128 px` pendant `0.50 s`.
- Imran est progressivement replace a `x = 1472 px` dans l'ecran.
- Le joueur conserve le controle pendant ce recentrage.
- La camera suit ensuite Imran vers la droite en maintenant cette position de reference.
- Le decalage horizontal maximal de la camera mesure `640 px`.
- Le decalage maximal deja atteint ne diminue jamais.
- La camera ne defile jamais vers la gauche et ne change jamais sa position verticale.
- Le bord gauche de l'ecran empeche Imran de quitter le cadre visible.
- Au decalage maximal, le coffre apparait a `x = 1504 px` dans l'ecran.

## Presentation du Golem de la Grotte

> **Statut :** Validee

### Deroulement visuel valide

- Avant le declenchement, le golem est integre a la paroi rocheuse et ressemble a une formation naturelle.
- Il ne possede aucune zone dangereuse ou vulnerable pendant cet etat.
- La presentation commence lorsque Imran franchit le point d'entree de l'arene.
- Les commandes d'Imran sont bloquees pendant toute la presentation.
- La sequence dure exactement `3.00 s`.

| Periode | Animation |
|---|---|
| `0.00 a 1.00 s` | Les cristaux et la paroi autour du golem commencent a vibrer. |
| `1.00 a 2.00 s` | Les fissures violettes, les yeux et le coeur d'amethyste s'allument progressivement. |
| `2.00 a 3.00 s` | Le golem se detache de la paroi et prend sa posture de garde face a Imran. |

- Les deux barrieres violettes montent silencieusement pendant les `0.50 s` du debut de la sequence.
- Le golem ne se deplace pas horizontalement pendant son reveil.
- La barre de vie apparait lorsque la presentation atteint `3.00 s`.
- Le controle d'Imran revient au meme instant.
- Le golem devient vulnerable et son corps devient dangereux a cet instant.
- La preparation de l'Eclat de cristal frontal peut alors commencer.
- Une commande effectuee avant la fin des `3.00 s` reste ignoree.
- Une nouvelle tentative rejoue la sequence complete depuis l'etat integre a la paroi.

### Signal sonore valide

- Un grondement profond de grotte commence au debut de la presentation.
- Il reste continu pendant les `3.00 s`.
- Des resonances cristallines apparaissent lorsque les cristaux commencent a vibrer.
- Leur intensite augmente pendant l'illumination des fissures, des yeux et du coeur.
- Des craquements de roche accompagnent le detachement de la paroi pendant la derniere seconde.
- Aucun cri ou rugissement supplementaire n'est joue.
- Les barrieres restent silencieuses.
- Tous les sons de presentation s'arretent lorsque la barre de vie apparait et que le controle revient.

### Assets visuels et sonores a produire

- Pose du golem integre a la paroi rocheuse.
- Animation des cristaux et de la paroi qui vibrent.
- Animation progressive des fissures violettes.
- Illumination des yeux et du coeur d'amethyste.
- Animation de detachement de la paroi.
- Transition vers la posture de garde.
- Poussiere rocheuse et petits fragments sans danger.
- Son de grondement profond de grotte.
- Resonances cristallines progressives.
- Craquements de roche pendant le detachement.

## Defaite du Golem de la Grotte

> **Statut :** Validee

### Deroulement visuel valide

- La sequence commence au contact du Smash Tranchant final avec le golem etourdi.
- Elle dure exactement `1.00 s`.
- La barre de vie disparait au debut de cette sequence.
- Le golem, ses fragments et ses particules ne possedent plus aucune zone dangereuse ou solide.

| Periode | Animation |
|---|---|
| `0.00 a 0.20 s` | Le coeur d'amethyste produit un dernier eclat, puis sa lumiere et celle des fissures s'eteignent. |
| `0.20 a 0.70 s` | Le corps se fragmente en roches, minerais et morceaux d'amethyste. |
| `0.70 a 1.00 s` | Les fragments deviennent des particules violettes qui se dispersent et disparaissent. |

- La disparition reste non violente et adaptee au public vise.
- Aucun corps, fragment solide ou obstacle ne reste dans l'arene.
- Aucune piece et aucun objet de soin ne sont produits.
- La camera conserve son cadrage fixe pendant toute la sequence.
- La barriere droite redescend entre `0.50 s` et `1.00 s`.
- Sa collision reste active jusqu'a sa disparition complete.
- La barriere gauche reste active jusqu'a la recuperation de la cle.
- Le coffre devient disponible lorsque la sequence atteint `1.00 s`.
- Le controle d'Imran revient au meme instant.

### Signal sonore valide

- Un eclat magique bref accompagne la derniere lumiere du coeur entre `0.00 s` et `0.20 s`.
- Des craquements de roche et de minerais accompagnent la fragmentation entre `0.20 s` et `0.70 s`.
- Une resonance cristalline accompagne la transformation en particules entre `0.70 s` et `1.00 s`.
- Cette resonance diminue progressivement et s'arrete avec les dernieres particules.
- Aucun son d'explosion violent n'est utilise.
- Le son d'ouverture du coffre reste distinct et commence uniquement apres une interaction valide.

### Assets visuels et sonores a produire

- Dernier eclat du coeur d'amethyste.
- Extinction du coeur, des yeux et des fissures violettes.
- Fragmentation en roches, minerais et morceaux d'amethyste.
- Transformation des fragments en particules violettes.
- Dispersion et disparition complete des particules.
- Son bref d'eclat magique.
- Craquements de roche et de minerais.
- Resonance cristalline decroissante.

## Recompense

> **Statut :** Validee

### Apparence du coffre validee

- Le coffre utilise une base en bois sombre.
- Des renforts en metal gris protegent ses angles, ses bords et son couvercle.
- De petits cristaux d'amethyste decorent ses quatre coins.
- Sa serrure utilise une forme simple de cristal violet.
- Les cristaux restent des decorations et ne produisent aucun effet dangereux.
- Le coffre ne produit aucun rayon, aucune lumiere doree et aucun effet lumineux.
- Sa silhouette reste immediatement identifiable comme celle d'un coffre interactif.
- Son fonctionnement et son animation utilisent les regles communes des six coffres.

### Coffre, cle et transition valides

- Le coffre devient disponible a la fin de la sequence de defaite du golem.
- Imran doit se placer a `56 px` ou moins du coffre puis utiliser la commande `Interaction`.
- L'interaction lance la sequence commune de `2.00 s`.
- Le deplacement, le saut, le Dash et les attaques restent bloques pendant cette sequence.
- De `0.00 a 0.75 s`, le couvercle et son mecanisme s'ouvrent.
- De `0.75 a 1.50 s`, la deuxieme cle sort progressivement du coffre.
- De `1.50 a 2.00 s`, la cle reste visible au-dessus du coffre.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- La deuxieme cle est ajoutee automatiquement a la progression a la fin des `2.00 s`.
- La sauvegarde automatique commence immediatement apres cet ajout.
- Les coeurs et les vies sont restaures a `3`.
- Le niveau suivant devient le Lac gele.
- Le coffre utilise le son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.
- Ce son commence avec l'interaction et accompagne toute la sequence de `2.00 s`.
- Aucun son supplementaire propre au bois, au metal, aux amethystes ou a la deuxieme cle n'est ajoute.
- Le controle reste bloque apres la fin des `2.00 s`.
- Une fois la sauvegarde confirmee, un fondu au noir de `0.75 s` commence.
- La barriere gauche disparait pendant ce fondu avec le reste de l'arene.
- Le Lac gele est charge pendant l'ecran noir.
- L'ecran reste noir tant que le Lac gele n'est pas pret.
- Le Lac gele apparait avec un fondu depuis le noir de `0.75 s`.
- Le controle revient lorsque ce niveau est entierement visible.
- Imran commence le Lac gele avec `3 coeurs` et `3 vies`.

## Socle deja valide

- Le Golem de la Grotte possede une seule phase.
- Il possede `14 PV`.
- Il utilise un cycle d'attaques fixe et previsible.
- La premiere attaque et l'ordre du cycle restent identiques a chaque tentative.
- Chaque attaque utilise une preparation visuelle et sonore d'au moins `0.50 s`.
- Chaque attaque se termine par la recuperation commune de `0.30 s`.
- Une pause neutre de `1.80 s` separe ensuite cette recuperation de la preparation suivante.
- La tete constitue sa zone vulnerable pendant le combat actif.
- Une attaque normale validee sur la tete retire `1 PV`.
- Un Smash Tranchant valide sur la tete retire `2 PV`.
- Chaque attaque du golem retire `1 coeur` a Imran.
- Le contact avec son corps utilise les dimensions, les degats et la reaction definis dans les regles communes.
- A `0 PV`, le golem entre dans l'etat `Etourdi`.
- Le Smash Tranchant final peut toucher n'importe quelle partie de son corps et declenche sa defaite.
- Sa defaite donne acces au coffre de la Grotte et a la deuxieme cle.
- Aucun nouveau pouvoir n'est debloque apres ce combat.

## Direction visuelle acquise

- Le corps utilise de grandes pierres gris fonce aux formes arrondies.
- Des cristaux d'amethyste violets apparaissent sur les epaules, les avant-bras et le dos.
- De petits fragments de minerais argentes sont incrustes dans la roche.
- Une energie violette parcourt les fissures du corps.
- Les yeux emettent une lumiere violette.
- Le coeur magique prend la forme d'un cristal d'amethyste place au centre du torse.
- La silhouette et les dimensions respectent les regles visuelles communes des six golems.
- Les cristaux et les minerais restent des decorations et n'agrandissent pas les zones de collision.

## Apparition acquise

- Avant le combat, le golem est integre a une paroi rocheuse couverte de cristaux.
- Les cristaux vibrent lorsque la presentation commence.
- Une lumiere violette traverse progressivement les fissures de la paroi.
- Les yeux et le coeur magique s'allument.
- Le golem se detache ensuite de la roche et adopte sa posture de combat.
- La presentation complete dure `3.00 s` selon les regles communes.

## Criteres de validation

La fiche sera validee lorsque :

- le cycle complet sera fixe ;
- chaque attaque possedera une preparation, une phase dangereuse et une recuperation mesurables ;
- toutes les attaques pourront etre evitees sans degat inevitable ;
- les signaux visuels resteront comprensibles sans le son ;
- l'arene permettra d'utiliser toutes les actions requises ;
- la presentation, la defaite et l'acces au coffre seront entierement decrits ;
- les regles resteront compatibles avec les regles communes des golems.

## Sources

- [Golem de la Grotte du Concept Game](../../Concept-Game/08-Boss/Golem-de-la-Grotte.md)
- [Regles communes des boss](Regles-Communes.md)
- [Golem de la Foret](Golem-Foret.md)
- [Niveau 2 - Grotte](../Niveaux/Niveau-2-Grotte.md)
