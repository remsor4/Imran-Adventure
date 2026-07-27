# Golem du Lac gele

> **Statut :** Valide

## Objectif

Definir le troisieme gardien comme un combat centre sur le positionnement et la maitrise des deplacements sur la glace. Le joueur doit reutiliser les regles apprises contre les deux premiers golems dans une arene dont le sol modifie son inertie.

## Role du combat

- Verifier l'observation des preparations visuelles et sonores.
- Demander au joueur d'anticiper ses arrets et ses changements de direction.
- Reutiliser la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.
- Donner une utilite claire au Dash.
- Maintenir le Double saut comme une aide facultative.
- Augmenter la difficulte sans introduire une seconde phase.

## Capacites requises validees

- Le Dash est obligatoire pour reussir au moins une esquive du cycle.
- Le joueur doit donc avoir compris sa direction, sa distance et son delai de reutilisation.
- Le Double saut reste facultatif pendant tout le combat.
- Aucune attaque ne place son unique solution au-dessus de la hauteur du saut normal.
- Le Double saut peut offrir une marge supplementaire sans supprimer la necessite d'observer.
- Le combat doit rester terminable avec le deplacement glace, le saut normal, le Dash, la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.
- Le Golem du Desert pourra introduire plus tard une maitrise obligatoire du Dash et du Double saut combines.

## Structure du cycle validee

- Le Golem du Lac gele possede exactement `3 attaques`.
- Ces attaques utilisent un ordre fixe et previsible.
- La premiere attaque reste identique a chaque tentative.
- Apres la troisieme attaque, le cycle reprend depuis la premiere.
- Recevoir un degat ne modifie pas l'ordre du cycle.
- Chaque attaque respecte la recuperation commune de `0.30 s` puis la pause neutre de `1.80 s`.
- Une attaque doit utiliser clairement le Bouclier de lumiere.
- Une attaque doit pouvoir etre evitee avec le saut normal.
- Une attaque doit demander obligatoirement le Dash.
- Le Double saut peut faciliter certaines esquives, mais ne constitue jamais l'unique solution.
- Le cycle utilise toujours l'ordre suivant :

| Ordre | Attaque | Fonction principale |
|---:|---|---|
| 1 | Disque de glace frontal | Utiliser le Bouclier de lumiere contre un projectile |
| 2 | Vague gelee au sol | Franchir une attaque basse avec le saut normal |
| 3 | Tempete de givre ciblee | Quitter une grande zone avec le Dash |

- Apres la Tempete de givre ciblee, le cycle reprend avec le Disque de glace frontal.
- Les comportements, les valeurs et les signaux des trois attaques sont valides dans les sections suivantes.

## Deplacement du golem valide

- Le Golem du Lac gele reste a la position horizontale `x = 1024 px` pendant tout le combat.
- Il ne marche pas et ne glisse pas vers Imran.
- Ses attaques, les degats recus et les collisions ne modifient pas cette position.
- Il ne se deplace pas pendant les recuperations de `0.30 s` ni pendant les pauses neutres de `1.80 s`.
- Au debut de chaque preparation, il se tourne sur place vers la position actuelle d'Imran.
- Cette orientation determine la direction verrouillee de l'attaque lorsque celle-ci en utilise une.
- Il ne change plus d'orientation pendant la preparation ni pendant l'execution de cette attaque.
- Il peut de nouveau se retourner au debut de la preparation suivante.
- Dans l'etat `Etourdi`, il conserve sa position et son orientation.

## Attaque 1 - Disque de glace frontal

> **Statut :** Validee

### Structure validee

- Le golem lance un unique grand disque de glace.
- La preparation avant le lancement dure exactement `0.60 s`.
- Le disque tourne continuellement autour de son centre pendant son trajet.
- Sa zone dangereuse mesure exactement `64 x 64 px`.
- Sa vitesse horizontale constante est de `520 px/s`.
- Cette vitesse est superieure de `40 px/s` a celle de l'Eclat de cristal du Golem de la Grotte.
- Son centre se trouve a `48 px` au-dessus du sol glace.
- Sa zone verticale couvre donc la hauteur comprise entre `16 px` et `80 px`.
- Le saut normal de `89 px` conserve une marge verticale de `9 px`.
- La forme visuelle du disque doit couvrir cette zone sans creer de danger invisible.
- Sa duree de vie maximale est de `2.00 s`.
- Sa portee maximale est donc de `1040 px` a la vitesse de `520 px/s`.
- Il se deplace horizontalement en ligne droite.
- La direction horizontale est verrouillee au debut de la preparation.
- Le projectile ne suit pas Imran apres son lancement.
- Le Bouclier de lumiere bloque automatiquement le disque lorsqu'Imran lui fait face.
- Le disque bloque disparait immediatement.
- Imran peut egalement franchir le disque avec un saut normal bien place.
- Le disque retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ce projectile et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- Le projectile disparait apres une collision valide ou a la fin de sa duree de vie.
- Le projectile disparait toujours avant la preparation de l'attaque suivante.

### Signal visuel valide

- Au debut de la preparation, le golem s'oriente vers la position d'Imran et verrouille cette direction.
- Il rapproche ses deux mains devant son torse.
- Une energie bleu glacier se condense entre ses paumes.
- Le disque de glace se forme progressivement et commence a tourner.
- Le golem recule ensuite le bras utilise pour le lancer.
- L'autre main reste dirigee vers Imran et rend la trajectoire lisible.
- La formation, la rotation et le recul du bras occupent toute la preparation de `0.60 s`.
- Le disque devient dangereux uniquement au moment de son lancement.
- Le signal reste comprehensible lorsque le son est coupe.

### Signal sonore valide

- Un souffle froid commence au debut de la preparation.
- Son intensite augmente pendant la condensation de l'energie bleu glacier.
- Un frottement de glace accompagne la rotation du disque entre les mains.
- Un claquement sec marque exactement le lancement.
- Le souffle de formation s'arrete au moment du claquement.
- Le disque conserve un leger sifflement de rotation pendant son trajet.
- Sa collision avec Imran, le bouclier ou le decor produit un bref son d'eclat de glace.

### Apparence du projectile validee

- Le disque utilise une glace bleu pale semi-transparente.
- Son bord irregulier forme plusieurs pointes de glace clairement visibles.
- Un coeur bleu lumineux marque son centre et facilite la lecture de sa rotation.
- Une courte trainee de neige et de petits cristaux suit son trajet.
- La trainee reste purement visuelle et n'agrandit pas la zone dangereuse.
- Le disque se brise en eclats de glace sans danger lors de sa disparition.

### Assets visuels et sonores a produire

- Animation du golem rapprochant ses deux mains.
- Animation de condensation de l'energie bleu glacier.
- Formation et rotation du disque entre les paumes.
- Animation du bras recule puis du lancer.
- Disque de glace bleu pale avec coeur lumineux.
- Effet de trainee de neige.
- Effet de fragmentation sans danger.
- Son de souffle froid progressif.
- Son de frottement pendant la rotation.
- Son de claquement sec au lancement.
- Son leger de sifflement pendant le trajet.
- Son bref d'eclat de glace lors de la collision.

## Attaque 2 - Vague gelee au sol

> **Statut :** Validee

### Structure validee

- Le golem produit une unique vague composee de glace et de neige.
- La preparation avant le depart de la vague dure exactement `0.60 s`.
- La vague progresse horizontalement en restant en contact avec le sol glace.
- Sa zone dangereuse mesure exactement `128 x 56 px`.
- Sa vitesse horizontale constante est de `480 px/s`.
- Elle reste ainsi plus lente que le Disque de glace de `520 px/s`.
- La zone commence au niveau du sol et atteint une hauteur de `56 px`.
- Le saut normal de `89 px` conserve une marge verticale de `33 px`.
- La forme visuelle de la vague doit couvrir cette zone sans creer de danger invisible.
- Sa duree de vie maximale est de `2.00 s`.
- Sa portee maximale est donc de `960 px` a la vitesse de `480 px/s`.
- La direction horizontale est verrouillee au debut de la preparation.
- La vague ne suit pas Imran apres son depart.
- Le Bouclier de lumiere ne bloque pas cette attaque.
- Imran doit franchir la vague avec un saut normal.
- Le Double saut peut augmenter la marge, mais il n'est jamais obligatoire.
- La vague retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche cette vague et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- La vague disparait lorsqu'elle atteint une limite solide ou la fin de sa duree de vie.
- La vague disparait toujours avant la preparation de l'attaque suivante.

### Signal visuel valide

- Au debut de la preparation, le golem s'oriente vers la position d'Imran et verrouille cette direction.
- Il abaisse un poing jusqu'au sol glace.
- Il fait glisser ce poing devant lui en rassemblant de la neige et du givre.
- Une petite masse gelee se forme devant le poing sans etre encore dangereuse.
- Au terme des `0.60 s`, le golem pousse brusquement son bras vers Imran.
- Cette poussee transforme la masse en vague et declenche son deplacement.
- La vague devient dangereuse uniquement lorsqu'elle quitte le poing.
- Le mouvement du bras, le givre rassemble et la direction du golem restent lisibles lorsque le son est coupe.

### Signal sonore valide

- Un frottement de glace commence lorsque le poing touche le sol.
- Ce frottement accompagne le rassemblement de neige et de givre pendant la preparation.
- Un craquement de glace marque exactement la poussee finale du bras.
- Un souffle de neige accompagne ensuite le trajet de la vague.
- Le souffle s'arrete lorsque la vague disparait.
- La collision avec une limite solide produit un bref son d'eclatement glace.

### Apparence de la vague validee

- La vague prend la forme d'une crete de glace bleu pale semi-transparente.
- Une ecume de neige blanche souligne son sommet et sa direction.
- Une courte brume froide suit son deplacement sans masquer le sol.
- La brume et l'ecume restent purement visuelles et n'agrandissent pas la zone dangereuse.
- La forme visible couvre la zone de `128 x 56 px`.
- Lors de sa disparition, la vague se brise en petits cristaux et se dissipe en neige sans danger.

### Assets visuels et sonores a produire

- Animation du golem abaissant son poing.
- Animation du poing glissant sur le sol.
- Effet de rassemblement de neige et de givre.
- Animation de poussee finale du bras.
- Crete de glace bleu pale.
- Effet d'ecume de neige.
- Effet de brume froide courte.
- Effet de fragmentation sans danger.
- Son de frottement sur la glace.
- Son de craquement pendant la poussee.
- Son de souffle de neige pendant le trajet.
- Son bref d'eclatement contre une limite solide.

## Attaque 3 - Tempete de givre ciblee

> **Statut :** Validee

### Structure validee

- Le golem cree une unique zone de tempete fixe.
- La zone mesure exactement `384 px` de largeur.
- La preparation avant son activation dure exactement `0.75 s`.
- La tempete reste dangereuse pendant exactement `0.50 s` apres son activation.
- Son centre horizontal correspond a la position d'Imran au debut de la preparation.
- Cette position est verrouillee pendant toute l'attaque.
- La tempete ne suit pas Imran apres le debut de la preparation.
- La zone s'etend du sol jusqu'en haut de la hauteur jouable.
- Le saut et le Double saut ne permettent pas de rester dans la zone sans subir de degat.
- Le Bouclier de lumiere ne protege pas contre la tempete.
- Imran doit quitter horizontalement la zone avec le Dash.
- Depuis le centre, la zone vulnerable de `32 px` d'Imran doit parcourir `208 px` pour sortir completement.
- En `0.75 s`, un deplacement normal a pleine vitesse ne peut parcourir que `180 px`.
- Un Dash de `124 px` suivi du mouvement normal restant peut parcourir environ `256 px`.
- L'esquive au Dash conserve donc une marge horizontale d'environ `48 px`.
- Si la zone standard depasse une barriere, seule sa partie situee dans les `1280 px` de combat reste active et visible.
- Le centre de la zone n'est jamais decale.
- Cette coupure aux limites conserve une distance maximale de sortie de `208 px`.
- La tempete retire `1 coeur` en cas de contact valide.
- Le contact applique uniquement la reaction standard aux degats d'Imran.
- La tempete ne ralentit pas Imran et ne l'immobilise pas dans la glace.
- L'invulnerabilite standard empeche la zone de retirer plusieurs coeurs pendant une meme activation.
- La zone disparait entierement a la fin des `0.50 s`.
- La recuperation commune de `0.30 s` commence apres cette disparition.

### Signal visuel valide

- Au debut de la preparation, deux limites verticales bleu glacier apparaissent aux bords exacts de la future zone dangereuse.
- Ces limites couvrent toute la hauteur jouable et restent fixes pendant les `0.75 s`.
- Du givre se forme sur le sol entre les deux limites.
- De la neige et de petits cristaux remplissent progressivement l'interieur de la zone.
- Leur densite augmente jusqu'a l'activation de la tempete.
- La zone reste sans danger pendant toute la preparation.
- A l'activation, les deux limites produisent un bref eclat et la tempete remplit toute la hauteur comprise entre elles.
- La tempete reste suffisamment transparente pour conserver Imran et les limites de la zone visibles.
- Les limites, le givre et les particules disparaissent entierement a la fin des `0.50 s` de danger.
- Aucun effet visuel residuel ne represente une zone encore dangereuse.
- Le signal reste comprehensible lorsque le son est coupe.

### Animation du golem validee

- Au debut de la preparation, le golem leve simultanement ses deux bras.
- Son coeur de cristal emet une lumiere bleu glacier de plus en plus intense.
- La meme energie se propage du torse jusqu'aux deux mains.
- Ses mains brillent progressivement pendant la formation des limites et du givre dans la zone.
- Le golem conserve les bras leves jusqu'au terme des `0.75 s`.
- Il rabat alors brusquement les deux bras.
- Le mouvement descendant des bras declenche exactement l'eclat des limites et le debut de la phase dangereuse.
- La posture et le mouvement restent distincts des animations utilisees par les deux premieres attaques.

### Signal sonore valide

- Un vent glacial commence au debut de la preparation.
- Son intensite augmente progressivement pendant les `0.75 s`.
- De petits tintements de glace accompagnent la lumiere du coeur et des mains.
- Une forte rafale marque exactement le mouvement descendant des bras et l'activation de la tempete.
- Un son de blizzard accompagne ensuite la phase dangereuse pendant `0.50 s`.
- Le blizzard sonore s'arrete lorsque la zone disparait.
- Aucun son residuel ne laisse croire que la zone reste dangereuse.

### Assets visuels et sonores a produire

- Animation du golem levant simultanement les deux bras.
- Animation de la lumiere se propageant du coeur jusqu'aux mains.
- Animation du golem rabattant brusquement les deux bras.
- Limites verticales bleu glacier.
- Effet progressif de givre sur le sol.
- Particules progressives de neige et de cristaux.
- Eclat bref des limites lors de l'activation.
- Tempete verticale bleu pale semi-transparente.
- Effet de disparition complete de la zone.
- Son de vent glacial progressif.
- Tintements de glace pendant la preparation.
- Son de forte rafale lors de l'activation.
- Son de blizzard pendant la phase dangereuse.

## Regles de combat validees

- Le Golem du Lac gele possede une seule phase.
- Il possede `16 PV`.
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
- Sa defaite donne acces au coffre du Lac et a la troisieme cle.
- Aucun nouveau pouvoir n'est debloque apres ce combat.

## Arene

> **Statut :** Validee

- La zone de combat mesure `1280 px`, soit `20 grilles` de `64 px`.
- Le sol principal se trouve a `y = 896 px`.
- La zone de combat apparait entre `x = 320 px` et `x = 1600 px` dans le cadre de reference.
- La camera reste fixe pendant le combat.
- La zone de recompense commence a la position locale `x = 1280 px`.
- Elle mesure `640 px`.
- Le centre du coffre se trouve a la position locale `x = 1824 px`.
- Le defilement vers la recompense utilise le recentrage commun de `128 px` en `0.50 s`.
- Les deux barrieres utilisent une energie bleu glacier semi-transparente.
- Des cristaux de glace et des flocons circulent dans cette energie.

### Terrain de l'arene valide

- Le sol glace est unique et entierement plat.
- L'arene ne contient aucune plateforme.
- Elle ne contient aucune pente.
- Elle ne contient aucune fosse.
- Elle ne contient aucun obstacle de deplacement.
- Les decorations du Lac gele restent hors des zones de collision.
- Cette structure respecte la regle commune des sept arenes de boss.
- Les positions horizontales locales sont mesurees depuis la limite interieure gauche de la zone de combat.
- Imran commence la presentation avec son centre horizontal a `x = 128 px`.
- Le Golem du Lac gele commence avec son centre horizontal a `x = 1024 px`.
- Le golem est tourne vers la gauche et fait face a Imran.
- La distance initiale entre leurs centres est de `896 px`.
- Il reste `256 px` entre le centre initial du golem et la limite droite de la zone de combat.
- Dans le cadre de reference, Imran apparait a `x = 448 px` dans l'ecran.
- Dans le cadre de reference, le golem apparait a `x = 1344 px` dans l'ecran.
- Les positions initiales permettent au Disque de glace frontal et a la Vague gelee au sol d'atteindre la zone d'Imran.

### Direction visuelle de l'arene validee

- L'arene se trouve en plein air sur la surface du Lac gele.
- Le sol jouable utilise une glace bleu pale legerement transparente.
- Des fissures et des bulles gelees apparaissent sous la surface sans representer un danger.
- Une grande paroi de glace se trouve derriere la position initiale du golem.
- Cette paroi sert a sa presentation et reste en dehors des zones de collision jouables.
- Des montagnes enneigees forment l'arriere-plan le plus eloigne.
- Des silhouettes de sapins couverts de neige occupent le plan intermediaire.
- La palette utilise principalement du bleu pale, du blanc neige et des ombres bleu gris.
- Les contrastes conservent Imran, le golem, les projectiles et les signaux d'attaque clairement visibles.
- Les montagnes, les sapins, les fissures et les bulles restent purement visuels.
- Aucun element du decor ne cree une plateforme, une pente, une fosse ou un obstacle.
- Le meme sol glace continue sans rupture dans la zone de recompense.
- Une neige fine tombe continuellement pendant la presentation, le combat et la sequence de recompense.
- La majorite des flocons reste en arriere-plan.
- Quelques flocons legers passent au premier plan pour donner de la profondeur.
- Leur densite et leur opacite restent faibles.
- Les flocons ne masquent jamais Imran, le golem, les zones dangereuses, les signaux d'attaque ou l'interface.
- Les flocons ne possedent aucune collision et ne modifient pas le comportement du sol.
- La densite de cette neige ambiante reste distincte de celle de la Tempete de givre ciblee.

## Comportement du sol glace

> **Statut :** Valide

### Surface validee

- Toute la largeur utile de `1280 px` de la zone de combat utilise un sol glace.
- La glissade reste identique en tout point de cette surface.
- Aucune plaque de sol normal ne coupe la zone de combat.
- Le changement de comportement commence lorsque Imran entre dans l'arene.
- Il reste actif pendant la presentation, le combat, l'etat `Etourdi` et la sequence de defaite.
- La glace modifie uniquement le mouvement au sol.
- Le saut, le Double saut et le controle aerien conservent leurs valeurs deja validees.
- Apres la defaite, la meme glace continue dans la zone de recompense de `640 px`.
- La surface glissante couvre donc toute la longueur accessible de `1920 px` jusqu'au coffre.
- Les valeurs d'acceleration et de freinage ne changent pas au passage de la barriere droite.
- La distance d'interaction de `56 px` reste superieure a la glissade maximale de `48 px`.
- Le chargement du niveau suivant termine ce comportement propre au Lac gele.

### Valeurs de deplacement validees

| Element | Valeur sur la glace |
|---|---:|
| Vitesse horizontale maximale | `240 px/s` |
| Acceleration au sol | `900 px/s2` |
| Freinage au sol | `600 px/s2` |
| Temps theorique pour atteindre la vitesse maximale | Environ `0.27 s` |
| Temps theorique pour s'arreter a pleine vitesse | `0.40 s` |
| Distance theorique de glissade a pleine vitesse | `48 px` |

- La vitesse maximale reste identique au deplacement normal.
- Maintenir une direction rapproche progressivement la vitesse de `240 px/s`.
- Relacher la direction applique le freinage de `600 px/s2` jusqu'a l'arret.
- Une direction opposee freine d'abord Imran jusqu'a `0 px/s`, puis applique l'acceleration de `900 px/s2` dans le nouveau sens.
- Maintenir gauche et droite en meme temps produit une direction neutre et applique le freinage.
- La glissade ne modifie pas automatiquement l'orientation d'Imran.

### Dash sur la glace valide

- Le Dash conserve sa vitesse de `620 px/s`.
- Sa duree reste `0.20 s`.
- Sa distance theorique sans obstacle reste `124 px`.
- La glace n'augmente ni sa vitesse, ni sa duree, ni sa distance.
- La direction reste verrouillee pendant le Dash.
- A la fin, Imran conserve au maximum `240 px/s` dans la direction du Dash.
- Le freinage glace de `600 px/s2` s'applique ensuite si aucune direction n'est maintenue.
- A pleine vitesse normale, cette sortie de Dash peut donc produire une glissade maximale de `48 px`.
- L'intervalle commun de `1.00 s` entre deux Dash reste inchange.

### Reactions aux degats validees

- Recevoir un degat conserve la reaction standard d'Imran.
- La vitesse horizontale initiale du recul reste `220 px/s` loin de la source.
- L'impulsion verticale initiale au sol reste `280 px/s` vers le haut.
- La duree sans controle reste `0.33 s`.
- L'invulnerabilite reste `1.30 s`.
- La glace ne prolonge ni la reaction, ni le recul obligatoire.
- Pendant le mouvement aerien produit par le recul, les valeurs aeriennes normales restent actives.
- Le freinage de `600 px/s2` reprend uniquement lorsque Imran touche de nouveau le sol glace et que son etat autorise le controle.

## Direction visuelle du golem validee

- Le corps utilise de grands blocs de glace bleu pale aux formes arrondies.
- Quelques plaques de pierre gelee restent visibles sous la glace.
- Des cristaux de glace apparaissent sur les epaules, les avant-bras et le dos.
- Une fine couche de neige repose sur la tete et les epaules.
- De petits glacons completent la silhouette sans la surcharger.
- Une energie bleu clair parcourt les fissures du corps.
- Les yeux emettent une lumiere bleu glacier.
- Le coeur magique prend la forme d'un cristal de glace place au centre du torse.
- La silhouette et les dimensions respectent les regles visuelles communes des six golems.
- Les cristaux, la neige et les glacons restent decoratifs et n'agrandissent pas les zones de collision.

## Presentation du Golem du Lac gele

> **Statut :** Validee

### Deroulement visuel valide

- Avant le combat, le golem est prisonnier dans une grande paroi de glace.
- Il ne possede aucune zone dangereuse ou vulnerable pendant cet etat.
- La presentation commence lorsque Imran franchit le point d'entree de l'arene.
- Les commandes d'Imran sont bloquees pendant toute la presentation.
- La sequence dure exactement `3.00 s`.

| Periode | Animation |
|---|---|
| `0.00 a 1.00 s` | Le coeur bleu s'allume et des fissures lumineuses commencent a parcourir la paroi de glace. |
| `1.00 a 2.00 s` | Les yeux s'allument, les fissures se propagent et la neige tombe de la tete et des epaules. |
| `2.00 a 3.00 s` | Le golem brise la paroi de glace, se libere et prend sa posture de garde face a Imran. |

- Les deux barrieres bleu glacier montent silencieusement pendant les `0.50 s` du debut de la sequence.
- Le golem ne se deplace pas horizontalement pendant son reveil.
- Les fragments de la paroi restent uniquement visuels et disparaissent avant la fin de la sequence.
- La barre de vie apparait lorsque la presentation atteint `3.00 s`.
- Le controle d'Imran revient au meme instant.
- Le golem devient vulnerable et son corps devient dangereux a cet instant.
- La preparation du Disque de glace frontal peut alors commencer.
- Une commande effectuee avant la fin des `3.00 s` reste ignoree.
- Une nouvelle tentative rejoue la sequence complete depuis l'etat prisonnier dans la paroi de glace.

### Signal sonore valide

- Un grondement glace commence au debut de la presentation.
- Il reste continu pendant les `3.00 s`.
- Des resonances cristallines apparaissent lorsque le coeur et les fissures commencent a s'allumer.
- Leur intensite augmente pendant l'allumage des yeux et la propagation des fissures.
- De forts craquements de glace accompagnent la liberation du golem pendant la derniere seconde.
- Aucun cri ni aucun rugissement n'est joue.
- Les barrieres restent silencieuses.
- Tous les sons de presentation s'arretent lorsque la barre de vie apparait et que le controle revient.

### Assets visuels et sonores a produire

- Pose du golem prisonnier dans la paroi de glace.
- Animation progressive du coeur bleu.
- Animation de propagation des fissures lumineuses.
- Animation d'allumage des yeux.
- Effet de neige tombant de la tete et des epaules.
- Animation du golem brisant la paroi.
- Transition vers la posture de garde.
- Fragments de glace sans danger.
- Son de grondement glace continu.
- Resonances cristallines progressives.
- Craquements de glace pendant la liberation.

## Defaite du Golem du Lac gele

> **Statut :** Validee

### Deroulement visuel valide

- La sequence commence au contact du Smash Tranchant final avec le golem etourdi.
- Elle dure exactement `1.00 s`.
- La barre de vie disparait au debut de cette sequence.
- Le golem, ses fragments et ses particules ne possedent plus aucune zone dangereuse ou solide.

| Periode | Animation |
|---|---|
| `0.00 a 0.20 s` | Le coeur de cristal produit un dernier eclat, puis sa lumiere et celle des fissures s'eteignent. |
| `0.20 a 0.70 s` | Le corps se fragmente en blocs de glace et en cristaux bleu pale. |
| `0.70 a 1.00 s` | Les fragments deviennent de la neige et des particules bleues qui se dispersent et disparaissent. |

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

- Un bref eclat magique accompagne la derniere lumiere du coeur entre `0.00 s` et `0.20 s`.
- Des craquements de glace accompagnent la fragmentation entre `0.20 s` et `0.70 s`.
- Une resonance cristalline accompagne la transformation des fragments en particules.
- Un souffle de neige accompagne leur dispersion entre `0.70 s` et `1.00 s`.
- La resonance et le souffle diminuent progressivement.
- Ils s'arretent avec la disparition des dernieres particules.
- Aucun son d'explosion violent n'est utilise.
- Le son d'ouverture du coffre reste distinct et commence uniquement apres une interaction valide.

### Assets visuels et sonores a produire

- Dernier eclat du coeur de cristal.
- Extinction du coeur, des yeux et des fissures bleu glacier.
- Fragmentation en blocs de glace et cristaux bleu pale.
- Transformation des fragments en neige et particules bleues.
- Dispersion et disparition complete des particules.
- Son bref d'eclat magique.
- Craquements de glace pendant la fragmentation.
- Resonance cristalline decroissante.
- Souffle de neige decroissant.

## Recompense

> **Statut :** Validee

### Apparence du coffre validee

- Le coffre utilise une base en bois bleu sombre.
- Des renforts en metal gris bleute protegent ses angles, ses bords et son couvercle.
- Une couche de givre recouvre partiellement le bois et le metal sans masquer leur structure.
- De petits cristaux de glace decorent les quatre angles.
- La serrure utilise une forme simple de cristal bleu glacier.
- Le givre et les cristaux restent decoratifs et ne produisent aucun effet dangereux.
- Le coffre ne produit aucun rayon, aucune lumiere doree et aucun effet lumineux.
- Sa silhouette reste immediatement identifiable comme celle d'un coffre interactif.
- Son fonctionnement et son animation utilisent les regles communes des six coffres.

### Coffre, cle et transition valides

- Le coffre devient disponible a la fin de la sequence de defaite du golem.
- Imran doit se placer a `56 px` ou moins du coffre puis utiliser la commande `Interaction`.
- L'interaction lance la sequence commune de `2.00 s`.
- Le deplacement, le saut, le Dash et les attaques restent bloques pendant cette sequence.
- De `0.00 a 0.75 s`, le couvercle et son mecanisme s'ouvrent.
- De `0.75 a 1.50 s`, la troisieme cle sort progressivement du coffre.
- De `1.50 a 2.00 s`, la cle reste visible au-dessus du coffre.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- La troisieme cle est ajoutee automatiquement a la progression a la fin des `2.00 s`.
- La sauvegarde automatique commence immediatement apres cet ajout.
- Les coeurs et les vies sont restaures a `3`.
- Le niveau suivant devient le Desert oublie.
- Le coffre utilise le son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.
- Ce son commence avec l'interaction et accompagne toute la sequence de `2.00 s`.
- Aucun son supplementaire propre au bois, au metal, au givre, aux cristaux ou a la troisieme cle n'est ajoute.
- Le controle reste bloque apres la fin des `2.00 s`.
- Une fois la sauvegarde confirmee, un fondu au noir de `0.75 s` commence.
- La barriere gauche disparait pendant ce fondu avec le reste de l'arene.
- Le Desert oublie est charge pendant l'ecran noir.
- L'ecran reste noir tant que le Desert oublie n'est pas pret.
- Le Desert oublie apparait avec un fondu depuis le noir de `0.75 s`.
- Le controle revient lorsque ce niveau est entierement visible.
- Imran commence le Desert oublie avec `3 coeurs` et `3 vies`.

## Inventaire complementaire des assets

> **Statut :** Valide

Les assets propres a chaque attaque, a la presentation et a la defaite sont enumeres dans leurs sections respectives. Les elements complementaires suivants doivent egalement etre produits :

### Golem

- Silhouette principale du Golem du Lac gele.
- Pose neutre orientee vers la gauche.
- Pose neutre orientee vers la droite.
- Animation de retournement sur place.
- Animation de reaction a un impact valide sur la tete.
- Effet visuel d'impact sur la zone vulnerable.
- Animation de passage a l'etat `Etourdi`.
- Pose immobile de l'etat `Etourdi`.
- Etats eteint et allume du coeur de cristal, des yeux et des fissures.

### Arene

- Sol glace bleu pale raccordable sur toute la longueur de `1920 px`.
- Fissures et bulles decoratives sous la glace.
- Paroi de glace intacte, fissuree et brisee.
- Arriere-plan de montagnes enneigees.
- Plan intermediaire de sapins couverts de neige.
- Systeme de neige fine en arriere-plan.
- Systeme de flocons legers au premier plan.
- Variante bleu glacier des deux barrieres communes.
- Particules de cristaux de glace et de flocons pour les barrieres.
- Prolongement du decor dans la zone de recompense.

### Recompense

- Coffre du Lac gele ferme.
- Coffre du Lac gele pendant l'ouverture.
- Coffre du Lac gele ouvert.
- Bois bleu sombre, renforts gris bleute, couche de givre et cristaux d'angle.
- Serrure en forme de cristal bleu glacier.
- Apparition et elevation de la troisieme cle selon l'animation commune.
- Son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.

## Criteres de validation

La fiche sera validee lorsque :

- le comportement de la glace sera mesurable et previsible ;
- le cycle complet sera fixe ;
- chaque attaque possedera une preparation, une phase dangereuse et une recuperation mesurables ;
- toutes les attaques pourront etre evitees sans degat inevitable ;
- les signaux visuels resteront comprehensibles sans le son ;
- l'arene permettra d'utiliser toutes les actions requises ;
- la presentation, la defaite et l'acces au coffre seront entierement decrits ;
- les regles resteront compatibles avec les regles communes des golems.

## Sources

- [Golem du Lac gele du Concept Game](../../Concept-Game/08-Boss/Golem-du-Lac.md)
- [Lac gele du Concept Game](../../Concept-Game/03-Univers/Lac-Gele.md)
- [Regles communes des boss](Regles-Communes.md)
- [Golem de la Grotte](Golem-Grotte.md)
- [Niveau 3 - Lac](../Niveaux/Niveau-3-Lac.md)
