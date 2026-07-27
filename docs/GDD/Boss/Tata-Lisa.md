# Tata Lisa

> **Statut :** Valide

## Objectif

Definir le combat final contre Tata Lisa devant la porte du donjon. Ce combat doit reutiliser toutes les capacites d'Imran, se distinguer des six golems par une magie plus expressive et conduire directement a la destruction de la Pierre du Chaos puis a la scene finale.

## Regles narratives deja validees

- Tata Lisa apparait apres la recuperation et la sauvegarde de la sixieme cle.
- Imran commence cette sequence avec `3 coeurs`, `3 vies` et les `6 cles`.
- Tata Lisa affronte Imran devant la porte du donjon.
- La Pierre du Chaos portee autour de son cou constitue la source de ses pouvoirs.
- Tata Lisa utilise directement la magie du Chaos.
- Sa personnalite reste jalouse, grincheuse, tyrannique et theatrale.
- Elle considere d'abord Imran comme un enfant incapable de lui resister.
- Son irritation augmente lorsqu'Imran dejoue ses attaques.
- La defaite de Tata Lisa brise la Pierre du Chaos.
- La sorciere perd ses pouvoirs puis prend la fuite.
- La protection magique des six verrous disparait.
- Les verrous physiques restent fermes jusqu'a l'interaction d'Imran avec la porte.
- Le donjon ne devient pas un niveau jouable.
- Le combat ne contient aucun coffre ni aucune cle supplementaire.

## Regles communes deja applicables

- La zone de combat mesure `1280 px` de largeur utile.
- Le sol principal se trouve a `y = 896 px`.
- Le sol reste unique, plat et sans plateforme, pente, fosse ou obstacle.
- La camera reste fixe pendant la presentation, le combat et la defaite.
- La barre de vie mesure `192 x 24 px` et reste centree en haut de l'ecran.
- Tata Lisa peut recevoir des degats pendant ses preparations, ses attaques, ses recuperations et ses pauses vulnerables.
- Sa tete constitue son unique zone vulnerable pendant le combat actif.
- Une attaque normale validee sur la tete retire `1 PV`.
- Un Smash Tranchant valide sur la tete retire `2 PV`.
- Un impact valide produit un retour visuel de `0.33 s`.
- Tata Lisa reste protegee contre un nouveau degat pendant ces memes `0.33 s`.
- Un impact valide ne ralentit, ne repousse et n'interrompt pas son action.
- La teleportation constitue l'unique exception de deplacement a la vulnerabilite commune des boss.
- Tata Lisa reste invulnerable pendant sa presentation, toutes ses teleportations, ses transitions de phase et sa defaite.
- Chaque attaque de Tata Lisa retire `1 coeur` par defaut.
- Une perte de vie d'Imran reinitialise Tata Lisa a sa vie maximale et a sa premiere phase.

## Structure des phases validee

- Tata Lisa possede exactement `2 phases`.
- Elle possede `24 PV` au debut du combat.
- La premiere phase couvre les valeurs de `24 PV` a `13 PV`.
- La transition commence immediatement lorsqu'un impact valide fait atteindre ou passer sous `12 PV`.
- La seconde phase couvre les valeurs de `12 PV` a `0 PV`.
- La premiere phase presente une sorciere sure d'elle, methodique et convaincue de sa superiorite.
- La seconde phase montre son irritation et une utilisation plus intense de la magie du Chaos.
- La transition interrompt temporairement le combat.
- Tata Lisa reste invulnerable pendant cette transition.
- Les projectiles et les dangers encore actifs disparaissent au debut de la transition.
- La seconde phase ne restaure aucun point de vie.
- Une attaque normale validee retire toujours `1 PV`.
- Un Smash Tranchant valide retire toujours `2 PV`.
- Aucun multiplicateur de degats ou resistance ne modifie ces valeurs.
- Une perte de vie d'Imran replace Tata Lisa au debut de la premiere phase avec tous ses points de vie.
- Les attaques, les valeurs et la duree exacte de la transition seront definies dans les sections suivantes.

## Dimensions et zones de collision validees

- L'enveloppe visuelle neutre de Tata Lisa mesure `128 x 160 px`.
- Sa hauteur represente exactement `2.5 fois` les `64 px` d'Imran.
- Sa tete volontairement disproportionnee occupe une grande partie de cette silhouette.
- Sa zone vulnerable de tete mesure exactement `72 x 64 px`.
- Cette zone reste centree sur la partie principale de la tete et suit toutes ses animations.
- Le voile, les bijoux, le nez, les sourcils et les effets magiques ne l'agrandissent pas.
- La zone reste active pendant les deplacements, les preparations, les attaques et les recuperations du combat actif.
- Elle est desactivee pendant la presentation, la transition entre les phases et la defaite.
- Sa zone dangereuse de contact mesure exactement `96 x 128 px`.
- Cette zone est centree sur le corps principal et suit tous ses deplacements.
- Le voile, la robe, les bijoux et les flammes magiques ne l'agrandissent pas.
- Un contact valide avec le corps retire `1 coeur` a Imran.
- Ce contact utilise la reaction, le recul et l'invulnerabilite standards d'Imran.
- Le Bouclier de lumiere ne protege pas contre le contact avec le corps.
- Le Dash ne rend pas Imran invulnerable a ce contact.
- L'enveloppe visuelle ne constitue ni une collision avec le decor, ni une zone vulnerable, ni une zone dangereuse.

## Direction visuelle de Tata Lisa validee

- Tata Lisa conserve sa silhouette validee pendant les deux phases.
- Sa tete reste volontairement tres grande par rapport a son corps.
- Son corps reste court, large et corpulent.
- Son voile de style hijab couvre entierement ses cheveux et son cou.
- Sa robe utilise le bordeaux, le violet sombre et le noir.
- Des bordures dorees et des bijoux violets completent sa tenue.
- La Pierre du Chaos reste le bijou principal place au centre de sa tenue.
- Ses grands yeux violets, ses sourcils arques et son visage cartoon restent tres expressifs.
- La seconde phase ne modifie ni sa taille, ni ses vetements, ni ses zones de collision.
- Son expression devient plus irritee et plus autoritaire.
- La lumiere de ses yeux devient plus intense.
- La Pierre du Chaos produit une pulsation plus forte.
- Une aura violette et noire entoure son corps.
- L'aura reste purement visuelle et ne masque jamais sa silhouette.
- Cette evolution montre que la puissance supplementaire provient de la Pierre du Chaos.
- Aucune transformation physique ni aucune nouvelle forme ne sont necessaires.

## Mode de deplacement valide

- Tata Lisa utilise la teleportation comme unique deplacement horizontal.
- Elle possede trois positions horizontales fixes : `x = 256 px`, `x = 640 px` et `x = 1024 px`.
- Elle commence le combat a la position `x = 1024 px`.
- Elle reste immobile pendant la preparation et l'execution de chaque attaque.
- Une teleportation standard du combat peut commencer uniquement entre deux attaques.
- Elle ne lance jamais une teleportation standard pendant la presentation, une attaque, la transition entre les phases ou la defaite.
- La presentation, la transition de phase et la defaite utilisent chacune une teleportation cinematographique propre a leur mise en scene.
- Ces teleportations cinematographiques ne modifient pas la sequence des teleportations standards, sauf lorsque la transition replace explicitement le cycle a `x = 640 px`.
- Une marque violette visible indique sa destination avant sa reapparition.
- Cette marque reste purement informative et ne retire aucun coeur.
- Tata Lisa ne peut pas commencer une nouvelle attaque avant la fin complete de sa reapparition.
- Les trois positions et la marque de destination restent identiques dans les deux phases.
- La premiere destination apres la position initiale est `x = 640 px`.
- Les destinations suivent toujours la sequence `1024 -> 640 -> 256 -> 640 -> 1024`.
- La sequence recommence ensuite dans le meme ordre.
- Tata Lisa ne reste jamais deux fois consecutivement sur la meme position.
- La position d'Imran ne modifie jamais la destination.
- Aucun choix aleatoire ne modifie cette sequence.
- Une perte de vie d'Imran replace Tata Lisa a `x = 1024 px` et reinitialise la sequence.
- Chaque teleportation dure exactement `0.75 s`.
- De `0.00 a 0.25 s`, Tata Lisa se dissout en magie violette sur sa position de depart.
- De `0.25 a 0.45 s`, elle reste entierement absente.
- De `0.45 a 0.75 s`, elle reapparait progressivement sur sa destination.
- La marque violette de destination apparait des le debut des `0.75 s`.
- Elle reste visible jusqu'a la reapparition complete.
- Tata Lisa devient invulnerable des le debut de la dissolution.
- Sa zone vulnerable, sa zone dangereuse et toutes ses collisions sont desactivees pendant toute la teleportation.
- Une attaque d'Imran traversant Tata Lisa ou sa marque pendant cette sequence ne produit aucun impact.
- Tata Lisa ne peut ni attaquer, ni blesser, ni bloquer Imran pendant cette sequence.
- Sa zone vulnerable et sa zone dangereuse sont reactivees exactement a `0.75 s`.
- Si Imran se trouve encore dans sa zone dangereuse a cet instant, les regles normales du contact avec le corps s'appliquent.
- La duree de teleportation reste identique dans les deux phases.

## Nombre d'attaques valide

- Tata Lisa possede exactement `4 attaques`.
- Les trois premieres attaques sont introduites pendant la premiere phase.
- La quatrieme attaque apparait uniquement pendant la seconde phase.
- Les trois attaques deja connues utilisent des versions plus intenses pendant la seconde phase.
- Une version renforcee ne constitue pas une attaque supplementaire.
- Les versions renforcees conservent la meme fonction, la meme silhouette generale et le meme principe d'evitement.
- Leurs changements de valeur et de signal seront definis dans chaque fiche d'attaque.
- La quatrieme attaque doit combiner plusieurs capacites deja apprises sans introduire un nouveau pouvoir.
- Tata Lisa ne possede aucune attaque aleatoire supplementaire en dehors de ces quatre attaques.

## Selection et ordre des attaques valides

- Tata Lisa utilise des cycles fixes et entierement previsibles.
- La premiere phase utilise toujours l'ordre `attaque 1 -> attaque 2 -> attaque 3`.
- Apres la troisieme attaque, la premiere phase reprend avec l'attaque 1.
- La seconde phase commence toujours par l'attaque 4.
- Elle utilise ensuite l'ordre `attaque 1 renforcee -> attaque 2 renforcee -> attaque 3 renforcee`.
- Apres l'attaque 3 renforcee, la seconde phase reprend avec l'attaque 4.
- Une teleportation se produit apres chaque attaque terminee.
- Tata Lisa ne choisit jamais son attaque selon la position d'Imran.
- Aucun tirage aleatoire ne modifie les cycles.
- Recevoir un degat ne modifie ni l'attaque en cours, ni la prochaine attaque.
- La transition de phase interrompt le cycle de la premiere phase.
- Toute attaque encore active disparait au debut de cette transition.
- Le cycle de la seconde phase commence toujours depuis l'attaque 4, quelle que soit l'attaque interrompue.
- Une perte de vie d'Imran reinitialise le combat sur l'attaque 1 de la premiere phase.

## Attaque 1 - Flamme du Chaos

> **Statut :** Validee

### Fonction validee

- Tata Lisa lance une flamme violette horizontale vers Imran.
- La premiere phase utilise un seul projectile.
- La seconde phase utilise deux projectiles successifs.
- Le Bouclier de lumiere constitue la reponse principale.
- Le projectile est bloque automatiquement lorsqu'Imran lui fait face.
- Un projectile bloque se dissipe et disparait immediatement.
- Le Double saut constitue une solution d'evitement alternative.
- Le projectile ne suit jamais Imran apres son lancement.
- La direction est verrouillee au debut de la preparation.
- Un contact valide retire `1 coeur` a Imran.
- L'invulnerabilite standard empeche les deux projectiles de phase 2 de retirer plusieurs coeurs pendant la meme periode.
- Les valeurs des deux phases sont definies ci-dessous.

### Valeurs de la premiere phase validees

- La preparation dure exactement `0.45 s`.
- Tata Lisa lance exactement `1 projectile`.
- Sa zone dangereuse mesure `64 x 64 px`.
- Son centre se trouve a `64 px` au-dessus du sol.
- Sa zone verticale couvre donc la hauteur comprise entre `32 px` et `96 px`.
- Le saut normal de `89 px` reste inferieur de `7 px` au sommet du projectile.
- Un Double saut permet de passer au-dessus.
- Sa vitesse horizontale constante est de `640 px/s`.
- Sa duree de vie maximale est de `1.90 s`.
- Sa portee maximale est donc de `1216 px`.
- La forme visible couvre toute la zone dangereuse sans creer de danger invisible.
- Le projectile disparait lorsqu'il touche Imran, le Bouclier de lumiere, une limite de l'arene ou la fin de sa duree de vie.
- Le projectile devient dangereux uniquement lorsqu'il quitte les mains de Tata Lisa.
- La version renforcee conserve cette silhouette et cette hauteur.

### Valeurs de la seconde phase validees

- La preparation dure exactement `0.40 s`.
- Tata Lisa lance exactement `2 projectiles`.
- Le premier projectile part au terme des `0.40 s`.
- Le second projectile part exactement `0.30 s` apres le premier.
- Les deux projectiles utilisent la meme direction verrouillee au debut de la preparation.
- Ils possedent chacun une zone dangereuse de `64 x 64 px`.
- Leur centre reste place a `64 px` au-dessus du sol.
- Leurs zones verticales couvrent donc la hauteur comprise entre `32 px` et `96 px`.
- Leur vitesse horizontale constante est de `680 px/s`.
- Leur duree de vie maximale est de `1.80 s`.
- Leur portee maximale est donc de `1224 px`.
- Le Bouclier de lumiere peut detruire les deux flammes l'une apres l'autre.
- Un saut normal suivi du Double saut permet egalement de franchir les deux projectiles.
- Tata Lisa reste immobile jusqu'au depart du second projectile.
- La phase dangereuse se termine lorsque le dernier projectile actif disparait.
- La teleportation suivante ne peut pas commencer avant cette disparition.

### Signal visuel valide

- Tata Lisa saisit la Pierre du Chaos au debut de la preparation.
- Une impulsion violette se propage du bijou jusque dans son bras.
- Elle tend ensuite une main vers Imran.
- Pendant la premiere phase, une flamme unique se forme dans sa paume.
- Pendant la seconde phase, deux petites flammes tournent autour de sa main.
- Le nombre de flammes visibles annonce donc le nombre exact de projectiles.
- Tata Lisa effectue un geste horizontal sec pour lancer chaque flamme.
- Le premier geste termine exactement la preparation.
- Le second geste de la phase 2 se produit `0.30 s` plus tard.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence des projectiles validee

- Chaque projectile prend la forme d'une flamme violette avec un coeur noir.
- Un contour violet clair separe le projectile des decors sombres.
- De courtes particules violettes et noires suivent son trajet.
- Une legere deformation magique donne a la flamme une apparence instable.
- La trainee et la deformation restent purement visuelles.
- Aucun effet ne depasse la zone dangereuse de `64 x 64 px`.
- Lors de sa disparition, la flamme se replie vers son coeur noir puis se dissipe.
- Une flamme bloquee par le Bouclier de lumiere utilise la meme disparition.

### Signal sonore valide

- Une pulsation cristalline de la Pierre du Chaos commence au debut de la preparation.
- Un crepitement magique accompagne la formation de chaque flamme.
- Un claquement sec marque exactement chaque lancement.
- Un leger sifflement accompagne le trajet de chaque projectile.
- Une dissolution vitreuse accompagne sa disparition.
- Deux claquements distincts annoncent les deux tirs de la seconde phase.
- Les sons de magie ne ressemblent pas aux sons de feu utilises dans le Volcan.
- Le son complete le signal visuel sans constituer le seul avertissement.

### Assets visuels et sonores a produire

- Animation de Tata Lisa saisissant la Pierre du Chaos.
- Propagation violette du bijou vers le bras.
- Animation de la main tendue.
- Formation d'une flamme dans la premiere phase.
- Formation et rotation de deux flammes dans la seconde phase.
- Gestes de lancement horizontal.
- Projectile de `64 x 64 px` avec coeur noir.
- Contour clair, trainee et deformation magique.
- Effet de repli et de dissolution.
- Pulsation cristalline de la Pierre du Chaos.
- Crepitement de formation.
- Claquement de lancement.
- Sifflement de trajet.
- Dissolution vitreuse.

## Attaque 2 - Vague du Chaos

> **Statut :** Validee

### Fonction validee

- Tata Lisa envoie une vague d'energie violette le long du sol.
- La premiere phase utilise une seule vague basse.
- Cette vague basse doit etre franchie avec un saut normal.
- La seconde phase utilise une vague basse suivie d'une vague haute.
- La vague haute doit etre franchie avec le Double saut.
- Les vagues se deplacent horizontalement dans la direction verrouillee au debut de la preparation.
- Elles ne suivent jamais Imran apres leur depart.
- Le Bouclier de lumiere ne protege pas contre les vagues.
- Le Dash ne rend pas Imran invulnerable a leur contact.
- Chaque contact valide retire `1 coeur` a Imran.
- L'invulnerabilite standard empeche deux vagues de retirer plusieurs coeurs pendant la meme periode.
- Les valeurs des deux phases sont definies ci-dessous.

### Valeurs de la premiere phase validees

- La preparation dure exactement `0.55 s`.
- Tata Lisa produit exactement `1 vague basse`.
- Sa zone dangereuse mesure `144 x 64 px`.
- Le saut normal de `89 px` conserve une marge verticale de `25 px`.
- Sa vitesse horizontale constante est de `560 px/s`.
- Sa duree de vie maximale est de `2.15 s`.
- Sa portee maximale est donc de `1204 px`.
- La forme visible couvre toute la zone dangereuse sans creer de danger invisible.
- La vague devient dangereuse uniquement lorsqu'elle quitte son point d'apparition.
- Elle disparait lorsqu'elle touche une limite de l'arene ou atteint la fin de sa duree de vie.
- La phase dangereuse se termine lorsque la vague disparait.
- La version renforcee conserve cette premiere vague et ajoute une seconde vague plus haute.

### Valeurs de la seconde phase validees

- La preparation dure exactement `0.50 s`.
- Tata Lisa produit exactement `2 vagues`.
- La premiere vague part au terme des `0.50 s`.
- La seconde vague part exactement `0.30 s` apres la premiere.
- La premiere vague possede une zone dangereuse de `144 x 64 px`.
- Le saut normal de `89 px` conserve `25 px` de marge au-dessus de cette premiere vague.
- La seconde vague possede une zone dangereuse de `176 x 120 px`.
- Le saut normal reste inferieur de `31 px` au sommet de la seconde vague.
- Un saut normal suivi du Double saut peut atteindre environ `167 px`.
- Cette combinaison conserve une marge verticale maximale d'environ `47 px`.
- Les deux vagues se deplacent a une vitesse horizontale constante de `600 px/s`.
- Leur duree de vie maximale est de `2.05 s`.
- Leur portee maximale est donc de `1230 px`.
- Les deux vagues utilisent la meme direction verrouillee.
- Tata Lisa reste immobile jusqu'au depart de la seconde vague.
- La phase dangereuse se termine lorsque la derniere vague active disparait.
- La teleportation suivante ne peut pas commencer avant cette disparition.

### Signal visuel valide

- Tata Lisa abaisse une main vers le sol au debut de la preparation.
- Une impulsion quitte la Pierre du Chaos et rejoint cette main.
- Elle trace un arc violet bas devant elle.
- Une rune basse apparait sur le sol et indique la hauteur de la premiere vague.
- Pendant la premiere phase, elle libere cette unique vague avec un mouvement horizontal de la main.
- Pendant la seconde phase, une seconde rune plus grande apparait derriere la premiere.
- Apres le depart de la vague basse, Tata Lisa leve ses deux mains.
- Elle trace un arc plus haut et libere la seconde vague `0.30 s` apres la premiere.
- La taille des runes, la hauteur des mains et l'intensite violette distinguent les deux vagues.
- Les runes restent sans danger avant le depart de leur vague.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence des vagues validee

- La vague basse forme un arc d'energie violette proche du sol.
- La vague haute forme un arc plus large et plus lumineux.
- Un coeur noir et un contour violet clair restent visibles dans chaque vague.
- Des fragments de runes et de faibles particules noires suivent leur trajet.
- Les fragments et les particules restent purement visuels.
- Aucun effet n'agrandit les zones dangereuses validees.
- Chaque vague se replie en fragments de runes avant de disparaitre.

### Signal sonore valide

- Une resonance runique grave commence au debut de la preparation.
- Un frottement magique accompagne le dessin de chaque arc sur le sol.
- Un impact sec marque exactement le depart de chaque vague.
- Un grondement leger accompagne chaque trajet.
- La vague haute utilise un impact et un grondement plus graves.
- Les deux signatures restent distinctes des sons de lave et de glace des autres boss.
- Chaque disparition produit un bref son de rune eteinte.
- Le son complete le signal visuel sans constituer le seul avertissement.

### Assets visuels et sonores a produire

- Animation d'une main abaissee vers le sol.
- Propagation de la Pierre du Chaos vers cette main.
- Animation de l'arc bas et de la premiere rune.
- Animation des deux mains levees.
- Animation de l'arc haut et de la seconde rune.
- Vague basse de `144 x 64 px`.
- Vague haute de `176 x 120 px`.
- Coeurs noirs, contours violets et fragments de runes.
- Effets de repli et de disparition.
- Resonance runique de preparation.
- Frottement magique sur le sol.
- Impacts distincts des deux vagues.
- Grondements distincts pendant les trajets.
- Son bref de rune eteinte.

## Attaque 3 - Colonne du Chaos

> **Statut :** Validee

### Fonction validee

- Tata Lisa fait apparaitre une colonne verticale autour de la position d'Imran.
- Le centre de la zone correspond a la position d'Imran au debut de la preparation.
- Ce centre est immediatement verrouille.
- La zone ne suit jamais Imran apres ce verrouillage.
- La zone reste sans danger pendant toute la preparation.
- Le deplacement normal ne suffit pas pour quitter completement la zone depuis son centre.
- Imran doit utiliser son Dash au sol puis terminer sa sortie avec son deplacement normal.
- Le Dash aerien reste impossible.
- Le Dash ne rend pas Imran invulnerable a l'activation de la colonne.
- Le Bouclier de lumiere ne protege pas contre la colonne.
- La colonne remplit toute la hauteur jouable et ne peut pas etre franchie avec un saut.
- Un contact valide retire `1 coeur` a Imran.
- La premiere phase utilise une zone ciblee large.
- La seconde phase utilise une zone plus large qui conserve exactement la meme logique.
- Les valeurs des deux phases sont definies ci-dessous.

### Valeurs de la premiere phase validees

- La zone ciblee mesure exactement `384 px` de largeur.
- La preparation dure exactement `0.70 s`.
- La colonne reste dangereuse pendant exactement `0.55 s`.
- Depuis le centre, la zone vulnerable de `32 px` d'Imran doit parcourir `208 px` pour sortir completement.
- En `0.70 s`, un deplacement normal a pleine vitesse ne peut parcourir que `168 px`.
- Le deplacement normal reste donc inferieur de `40 px` a la distance de sortie.
- Un Dash de `124 px` laisse ensuite `0.50 s` de mouvement.
- A `240 px/s`, ce mouvement permet de parcourir `120 px` supplementaires.
- La sequence peut donc couvrir environ `244 px`.
- Elle conserve une marge horizontale d'environ `36 px`.
- Si la zone depasse une limite de l'arene, seule sa partie interieure reste visible et dangereuse.
- Le centre verrouille n'est jamais decale.
- Imran doit alors sortir vers l'interieur de l'arene.
- La colonne devient dangereuse exactement a la fin des `0.70 s`.
- Elle disparait completement a la fin des `0.55 s`.
- Aucun danger ne persiste sur le sol apres sa disparition.
- La version renforcee conserve le meme ciblage et le meme principe de sortie.

### Valeurs de la seconde phase validees

- La zone ciblee mesure exactement `432 px` de largeur.
- La preparation dure exactement `0.70 s`.
- La colonne reste dangereuse pendant exactement `0.65 s`.
- Depuis le centre, la zone vulnerable de `32 px` d'Imran doit parcourir `232 px` pour sortir completement.
- En `0.70 s`, un deplacement normal a pleine vitesse ne peut parcourir que `168 px`.
- Le deplacement normal reste donc inferieur de `64 px` a la distance de sortie.
- Un Dash de `124 px` laisse ensuite `0.50 s` de mouvement.
- A `240 px/s`, ce mouvement permet de parcourir `120 px` supplementaires.
- La sequence peut donc couvrir environ `244 px`.
- Elle conserve une marge horizontale d'environ `12 px`.
- Les regles de verrouillage et de decoupage aux limites restent identiques a celles de la premiere phase.
- La colonne devient dangereuse exactement a la fin des `0.70 s`.
- Elle disparait completement a la fin des `0.65 s`.
- Aucun danger ne persiste apres sa disparition.

### Signal visuel valide

- Tata Lisa dirige ses deux mains vers la position d'Imran au debut de la preparation.
- Une impulsion quitte la Pierre du Chaos et rejoint ses deux bras.
- Deux limites violettes verticales apparaissent aux bords exacts de la zone ciblee.
- Une grande rune se dessine progressivement au sol entre ces deux limites.
- Le centre et les limites sont verrouilles des leur apparition.
- Les limites de la seconde phase sont plus eloignees mais conservent exactement la meme forme.
- Tata Lisa rapproche progressivement ses mains pendant les `0.70 s`.
- Elle les referme brusquement a la fin de la preparation.
- La fermeture declenche exactement l'apparition de la colonne.
- La zone, les limites et la rune restent sans danger avant cet instant.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence de la colonne validee

- La colonne melange des flammes violettes verticales et un coeur d'energie noire semi-transparent.
- Un contour violet clair conserve les deux limites visibles pendant le danger.
- Des fragments de runes montent dans la colonne.
- De faibles etincelles noires apparaissent entre les fragments.
- La transparence permet de conserver Imran visible lorsqu'il se trouve encore dans la zone.
- Les flammes, les fragments et les etincelles restent contenus dans la largeur validee.
- Aucun effet ne cree une collision ou un danger supplementaire.
- La colonne se contracte vers la rune puis disparait completement.

### Signal sonore valide

- Une pulsation de la Pierre du Chaos marque le verrouillage de la cible.
- Une tonalite runique montante accompagne toute la preparation de `0.70 s`.
- La hauteur de cette tonalite augmente progressivement jusqu'a l'activation.
- Un claquement magique sec accompagne exactement la fermeture des mains.
- Un grondement vertical accompagne la colonne pendant sa duree dangereuse.
- Ce grondement dure `0.55 s` en phase 1 et `0.65 s` en phase 2.
- Le grondement s'arrete avec la contraction complete de la colonne.
- Le son complete le signal visuel sans constituer le seul avertissement.

### Assets visuels et sonores a produire

- Animation des deux mains dirigees vers Imran.
- Propagation de la Pierre du Chaos vers les deux bras.
- Limites verticales pour les largeurs de `384 px` et `432 px`.
- Rune ciblee progressive pour les deux largeurs.
- Animation des mains qui se rapprochent puis se ferment.
- Colonne de flammes violettes et d'energie noire.
- Fragments de runes et etincelles noires.
- Contraction finale vers la rune.
- Pulsation de ciblage.
- Tonalite runique montante de `0.70 s`.
- Claquement magique d'activation.
- Grondement vertical declinable en `0.55 s` et `0.65 s`.

## Attaque 4 - Rituel de la Pierre du Chaos

> **Statut :** Validee

### Fonction validee

- Le Rituel de la Pierre du Chaos apparait uniquement pendant la seconde phase.
- Il ouvre chaque cycle de la seconde phase.
- Il constitue une seule attaque composee de trois epreuves successives.
- Les trois dangers ne deviennent jamais actifs simultanement.
- La premiere epreuve lance une flamme que le Bouclier de lumiere peut detruire.
- La deuxieme epreuve verrouille un sceau autour d'Imran et exige un Dash au sol.
- La troisieme epreuve produit une impulsion sur tout le sol et exige un saut prolonge par le Double saut.
- Chaque epreuve conserve une silhouette et un signal issus des trois attaques precedentes.
- Les trois epreuves utilisent cependant une couleur violette plus intense et une lumiere plus forte provenant de la Pierre du Chaos.
- Tata Lisa reste immobile pendant tout le rituel.
- Elle reste vulnerable a la tete pendant la preparation et l'execution des trois epreuves.
- Un impact valide ne ralentit, ne repousse et n'interrompt pas le rituel.
- Chaque danger retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche plusieurs dangers du rituel de retirer plusieurs coeurs pendant la meme periode.
- Le rituel se termine uniquement apres la disparition complete de l'impulsion du sol.
- La teleportation suivante ne peut pas commencer avant cette fin.

### Valeurs et deroulement valides

- Tata Lisa charge la Pierre du Chaos pendant exactement `0.60 s`.
- La pierre, ses mains et les marques au sol deviennent progressivement plus lumineuses.
- Au terme de cette charge, Tata Lisa lance exactement `1 Flamme du Chaos`.
- Cette flamme utilise la zone de `64 x 64 px`, la hauteur de `64 px`, la vitesse de `640 px/s` et la duree de vie de `1.90 s` de la premiere phase.
- La premiere epreuve se termine lorsque cette flamme disparait.
- Une pause sans danger de `0.30 s` commence alors.
- Au terme de cette pause, une zone ciblee de `384 px` est verrouillee autour de la position actuelle d'Imran.
- Cette zone utilise une preparation de `0.70 s`.
- Elle devient ensuite une colonne dangereuse pendant `0.55 s`.
- Les calculs de sortie et la marge de Dash de `36 px` restent identiques a ceux de la Colonne du Chaos de la premiere phase.
- Une seconde pause sans danger de `0.30 s` commence lorsque cette colonne disparait.
- Au terme de cette pause, une lueur violette avertit que tout le sol sera affecte.
- Cet avertissement dure exactement `0.60 s`.
- Le sol reste sans danger pendant cet avertissement.
- A la fin des `0.60 s`, une impulsion rend tout le sol dangereux sur une hauteur de `56 px`.
- Cette impulsion reste active pendant exactement `0.80 s`.
- La duree du saut normal d'environ `0.71 s` ne suffit pas pour rester au-dessus du danger jusqu'a sa fin.
- Imran doit utiliser le saut normal puis le Double saut.
- Le Bouclier de lumiere ne protege pas contre le sceau, la colonne ou l'impulsion du sol.
- Le Dash ne rend pas Imran invulnerable a la colonne ou a l'impulsion.
- Aucun danger ne persiste lorsque l'impulsion atteint la fin des `0.80 s`.
- La phase dangereuse complete du rituel se termine a cet instant.

### Signal visuel valide

- La Pierre du Chaos se detache legerement du bijou et flotte devant Tata Lisa pendant la charge initiale.
- Trois fragments de rune tournent autour de la pierre.
- Le premier fragment utilise un symbole de flamme.
- Le deuxieme fragment utilise deux limites verticales.
- Le troisieme fragment utilise une ligne horizontale.
- Ces symboles annoncent respectivement le projectile, la colonne ciblee et l'impulsion du sol.
- Le fragment de flamme brille pendant la premiere epreuve.
- Il s'eteint lorsque le projectile disparait.
- Le fragment vertical brille pendant la premiere pause puis pendant le ciblage de la colonne.
- Il s'eteint lorsque la colonne disparait.
- Le fragment horizontal brille pendant la seconde pause puis pendant l'avertissement au sol.
- Il s'eteint lorsque l'impulsion du sol disparait.
- Les fragments encore actifs permettent de connaitre le nombre d'epreuves restantes.
- Tata Lisa reutilise les gestes deja valides pour lancer la flamme et fermer ses mains sur la colonne.
- Pendant le dernier avertissement, elle leve lentement les deux mains.
- Elle les abaisse brusquement pour declencher l'impulsion du sol.
- La Pierre du Chaos reprend sa position sur son bijou a la fin de l'attaque.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence de l'impulsion finale validee

- Une ligne violette parcourt tout le sol pendant l'avertissement de `0.60 s`.
- Des runes horizontales apparaissent progressivement le long de cette ligne.
- Elles restent sans danger pendant toute la preparation.
- A l'activation, une onde violette traverse instantanement toute la surface.
- Des flammes courtes et de petites pointes d'energie restent contenues sous la hauteur de `56 px`.
- Des particules noires montent legerement depuis les runes.
- Aucun effet ne masque Imran ou Tata Lisa.
- Aucun effet ne cree une collision ou un danger au-dessus de `56 px`.
- Toutes les runes s'eteignent completement a la fin des `0.80 s`.

### Signal sonore valide

- Un bourdonnement cristallin continu provient de la Pierre du Chaos pendant tout le rituel.
- Trois notes distinctes accompagnent l'apparition des trois fragments.
- La premiere epreuve reutilise les sons valides de la Flamme du Chaos.
- La deuxieme epreuve reutilise les sons valides de la Colonne du Chaos.
- La troisieme epreuve utilise une resonance runique propre au sol.
- L'extinction de chaque fragment produit un tintement descendant.
- Le tintement permet de confirmer qu'une epreuve est terminee.
- Un impact grave accompagne exactement l'abaissement des mains et l'activation de l'impulsion.
- Une vibration basse accompagne les `0.80 s` de danger au sol.
- Le bourdonnement et la vibration s'arretent avec l'extinction du dernier fragment.
- Le son complete les indicateurs visuels sans constituer le seul moyen de suivre le rituel.

### Assets visuels et sonores a produire

- Animation de la Pierre du Chaos flottant devant Tata Lisa.
- Trois fragments de rune en rotation.
- Symboles de flamme, de limites verticales et de ligne horizontale.
- Etats actif et eteint de chaque fragment.
- Reutilisation des animations de la Flamme du Chaos.
- Reutilisation des animations de la Colonne du Chaos.
- Animation des deux mains levees puis abaissees.
- Ligne violette et runes d'avertissement sur tout le sol.
- Onde violette d'activation.
- Flammes et pointes d'energie contenues sous `56 px`.
- Particules noires et extinction complete du sol.
- Bourdonnement cristallin continu.
- Trois notes d'apparition distinctes.
- Tintement descendant d'extinction.
- Resonance runique du sol.
- Impact grave d'activation.
- Vibration basse de `0.80 s`.

## Recuperations et fenetres de contre-attaque validees

- Aucun danger d'une attaque ne reste actif lorsque sa recuperation commence.
- La recuperation commence immediatement apres la fin de la phase dangereuse.
- Tata Lisa revient vers sa posture neutre pendant cette recuperation.
- La recuperation dure `0.30 s` dans les deux phases.
- Une pause neutre et vulnerable commence ensuite.
- Cette pause dure `0.75 s` pendant la premiere phase.
- Elle dure `0.50 s` pendant la seconde phase.
- Tata Lisa reste immobile pendant la recuperation et la pause.
- Sa tete reste vulnerable pendant ces deux periodes.
- Sa zone dangereuse de contact reste active.
- Elle ne lance aucune attaque et ne produit aucun danger temporaire.
- La teleportation de `0.75 s` commence a la fin de la pause.
- Tata Lisa devient alors invulnerable et sans collision selon les regles deja validees.
- La preparation de l'attaque suivante commence uniquement apres sa reapparition complete.
- L'intervalle total entre la fin d'un danger et la prochaine preparation dure `1.80 s` en phase 1.
- Cet intervalle total dure `1.55 s` en phase 2.
- La premiere attaque de la premiere phase commence sans teleportation apres la presentation.
- Recevoir un degat ne relance ni la recuperation, ni la pause, ni la teleportation.
- Si Tata Lisa atteint le seuil de la seconde phase pendant la recuperation ou la pause, la transition commence immediatement.
- Dans ce cas, la teleportation normalement prevue est annulee.

## Presentation de Tata Lisa

> **Statut :** Validee

### Mise en scene validee

- La sequence commence apres le chargement de la zone situee devant la porte du donjon.
- Imran possede `3 coeurs`, `3 vies` et les `6 cles`.
- Il avance jusqu'au point de declenchement place devant les six verrous.
- La camera adopte alors le cadrage fixe de l'arene.
- Les commandes d'Imran sont immediatement bloquees.
- Les six cles reagissent et les six verrous produisent une courte lumiere.
- Les verrous physiques restent fermes.
- Tata Lisa se teleporte entre Imran et la porte avant toute interaction possible.
- Elle termine son apparition a la position locale `x = 1024 px`.
- Imran reste a la position locale `x = 128 px`.
- Tata Lisa saisit la Pierre du Chaos et prononce une courte provocation.
- Elle utilise ensuite sa magie pour fermer l'arene.
- Tata Lisa reste invulnerable et sans zone dangereuse pendant toute la presentation.
- Elle ne peut lancer aucune attaque pendant cette sequence.
- Une commande effectuee pendant le blocage reste ignoree.
- La barre de vie apparait uniquement a la fin de la presentation.
- Le controle d'Imran revient au meme instant.
- Tata Lisa devient vulnerable et dangereuse a cet instant.
- La premiere preparation de la Flamme du Chaos peut alors commencer.
- La sequence complete dure exactement `5.00 s`.

### Decoupage temporel valide

| Periode | Evenement |
|---|---|
| `0.00 a 0.75 s` | Les six cles et les six verrous reagissent par une courte lumiere. |
| `0.75 a 1.50 s` | Tata Lisa se teleporte entre Imran et la porte, a `x = 1024 px`. |
| `1.50 a 3.00 s` | Tata Lisa saisit la Pierre du Chaos et prononce sa provocation. |
| `3.00 a 4.00 s` | Elle utilise la pierre pour fermer l'arene. |
| `4.00 a 5.00 s` | Elle prend sa posture de combat face a Imran. |

- Les reactions des cles et des verrous restent purement visuelles.
- Aucun verrou physique ne s'ouvre pendant la premiere periode.
- La teleportation de presentation utilise une animation plus theatrale que les teleportations du combat.
- La fermeture devient entierement solide avant la fin de la quatrieme seconde.
- La barre de vie apparait exactement a `5.00 s`.
- Le controle revient exactement a `5.00 s`.
- Tata Lisa prononce exactement : `Tu n'ouvriras jamais cette porte !`
- Cette phrase commence a `1.50 s`.
- La phrase utilise une voix enregistree de Tata Lisa.
- Sa voix reste mature, autoritaire, grincheuse et theatrale.
- Aucun filtre ne doit masquer la comprehension des mots.
- Le sous-titre apparait a `1.50 s` et reste visible jusqu'a `5.00 s`.
- Il affiche le nom `Tata Lisa` avec la phrase.
- Le texte ne depend pas uniquement d'une couleur pour identifier le personnage.
- Le volume de la voix utilise le reglage separe des voix.
- Le sous-titre reste actif meme lorsque le volume des voix est coupe.
- Le sous-titre disparait lorsque le controle revient.

## Transition vers la seconde phase

> **Statut :** Validee

### Mise en scene validee

- La transition commence immediatement lorsqu'un impact valide fait atteindre ou passer sous `12 PV`.
- L'attaque, la recuperation, la pause ou la teleportation en cours est interrompue.
- Tous les projectiles, toutes les vagues, toutes les colonnes et tous les dangers temporaires disparaissent.
- La zone dangereuse de contact de Tata Lisa est desactivee.
- Sa zone vulnerable est desactivee.
- Tata Lisa devient invulnerable pendant toute la transition.
- Les commandes d'Imran restent disponibles.
- Imran peut se deplacer, sauter et utiliser le Dash, mais aucune attaque ne peut blesser Tata Lisa.
- Tata Lisa se teleporte jusqu'a la position centrale `x = 640 px`.
- La Pierre du Chaos produit une forte pulsation violette.
- La pierre reste entierement intacte.
- Tata Lisa montre clairement sa colere et son irritation.
- Une aura violette et noire plus intense apparait autour de son corps.
- Cette aura reste visible pendant toute la seconde phase.
- Elle reste purement visuelle et n'agrandit aucune zone de collision.
- La barre de vie reste visible avec la valeur reelle atteinte.
- Aucun point de vie n'est restaure.
- Le cycle de teleportation est replace sur la position `x = 640 px`.
- La premiere attaque apres la transition est toujours le Rituel de la Pierre du Chaos.
- La transition dure exactement `2.50 s`.

### Decoupage temporel valide

| Periode | Evenement |
|---|---|
| `0.00 a 0.25 s` | L'action en cours est interrompue et tous les dangers disparaissent. |
| `0.25 a 0.75 s` | Tata Lisa se teleporte jusqu'a `x = 640 px`. |
| `0.75 a 1.50 s` | La Pierre du Chaos produit une pulsation violette croissante. |
| `1.50 a 2.25 s` | Tata Lisa montre sa colere et son aura violette et noire apparait. |
| `2.25 a 2.50 s` | Elle prend sa posture de combat de la seconde phase. |

- Tata Lisa reste invulnerable jusqu'a la fin exacte des `2.50 s`.
- Sa zone vulnerable et sa zone dangereuse sont reactivees a cet instant.
- Le Rituel de la Pierre du Chaos commence immediatement apres cette reactivation.
- La premiere teleportation suivant ce rituel conduit Tata Lisa a `x = 256 px`.
- Les transitions suivantes du cycle utilisent ensuite `640`, `1024`, `640` et `256 px`.
- Apres une reinitialisation, la transition complete est rejouee uniquement lorsque Tata Lisa atteint de nouveau le seuil de `12 PV`.
- Tata Lisa crie exactement `Assez !` au debut de la periode `1.50 a 2.25 s`.
- Cette exclamation utilise sa voix mature, autoritaire et irritee.
- Le sous-titre affiche `Tata Lisa - Assez !` de `1.50 a 2.50 s`.
- Le sous-titre reste visible lorsque le volume des voix est coupe.
- Une pulsation cristalline croissante accompagne la Pierre entre `0.75 et 1.50 s`.
- Un souffle inverse accompagne l'apparition de l'aura entre `1.50 et 2.25 s`.
- Une courte resonance grave confirme la posture finale entre `2.25 et 2.50 s`.
- Tous les sons de transition s'arretent avant le debut du rituel.

### Assets visuels et sonores a produire

- Effet d'interruption et de disparition des dangers.
- Teleportation speciale vers `x = 640 px`.
- Pulsation croissante de la Pierre du Chaos.
- Expression et posture de colere.
- Apparition de l'aura violette et noire.
- Posture de combat de la seconde phase.
- Exclamation enregistree `Assez !`.
- Sous-titre associe.
- Pulsation cristalline croissante.
- Souffle inverse de l'aura.
- Resonance grave de fin de transition.

## Arene

> **Statut :** Validee

### Structure validee

- Le combat se deroule dans une grande antichambre du Chateau de Tata Lisa.
- Cette antichambre se trouve directement devant la porte du donjon.
- La zone de combat mesure exactement `1280 px`, soit `20 grilles` de `64 px`.
- Le sol principal se trouve a `y = 896 px`.
- Le sol est unique et entierement plat.
- L'arene ne contient aucune plateforme, pente, fosse ni obstacle de deplacement.
- La camera reste fixe pendant la presentation, le combat actif, la transition et la defaite.
- Les positions locales sont mesurees depuis la limite interieure gauche.
- Imran commence la presentation avec son centre a `x = 128 px`.
- Tata Lisa termine son apparition avec son centre a `x = 1024 px`.
- La distance initiale entre leurs centres est de `896 px`.
- Les trois positions de teleportation restent `256`, `640` et `1024 px`.
- La porte du donjon et ses six verrous restent visibles dans la partie droite du decor.
- Aucun coffre ni aucune zone de recompense supplementaire ne prolonge l'arene.
- La fermeture utilise la barriere gauche et la protection magique de la porte definies ci-dessous.

### Direction visuelle validee

- Le sol utilise de grandes dalles de pierre noire et gris anthracite.
- Les murs emploient une pierre sombre aux formes massives mais lisibles.
- De grands piliers encadrent la salle sans entrer dans l'espace jouable.
- Des bannieres bordeaux et violettes rappellent les couleurs de Tata Lisa.
- Des bordures dorees relient visuellement la salle a ses bijoux et a sa tenue.
- De hautes ouvertures diffusent une faible lumiere violette.
- La porte du donjon utilise du bois noir, du metal sombre et six verrous distincts.
- Une protection magique violette recouvre les verrous avant la defaite de Tata Lisa.
- Une lumiere faible derriere la porte rappelle qu'Aliyah se trouve de l'autre cote.
- La palette associe le noir, le gris anthracite, le bordeaux, le violet sombre et de petites touches dorees.
- Les signaux violets des attaques utilisent des contours plus clairs que le decor.
- Imran, Tata Lisa, les projectiles et les avertissements restent lisibles en permanence.
- Les piliers, les bannieres, les bordures et les ouvertures restent purement decoratifs.
- Aucun element du decor ne modifie les collisions ou la surface jouable.
- De faibles particules du Chaos circulent en arriere-plan.
- Leur densite augmente legerement pendant la seconde phase.
- Elles ne masquent jamais l'action et ne possedent aucune collision.

### Fermeture de l'arene validee

- Une barriere de magie du Chaos ferme l'entree gauche derriere Imran.
- La protection magique de la porte constitue la limite droite de l'arene.
- Les deux fermetures commencent leur animation entre `3.00 et 4.00 s` pendant la presentation.
- Elles deviennent entierement visibles et solides avant la fin de cette seconde.
- La barriere gauche utilise une energie violette sombre semi-transparente.
- Des fragments de runes et de faibles particules noires circulent dans cette energie.
- La protection droite recouvre directement la porte et les six verrous.
- Elle utilise les memes couleurs, mais ses runes reprennent la forme des six serrures.
- Chaque fermeture possede une largeur solide de `32 px`.
- Leur bord interieur reste aligne avec la limite utile correspondante de l'arene.
- Elles ne reduisent pas les `1280 px` de largeur utile.
- Elles bloquent Imran, Tata Lisa, les projectiles et les attaques.
- Une Flamme du Chaos ou une Vague du Chaos disparait immediatement lorsqu'elle touche une fermeture.
- Cette disparition utilise son effet normal de repli et de dissolution.
- La disparition met immediatement fin a l'activite de ce projectile ou de cette vague.
- Les colonnes, les runes et les dangers au sol restent limites aux `1280 px` utiles et ne traversent jamais les fermetures.
- Elles ne retirent aucun coeur.
- Elles restent actives pendant les deux phases et la transition.
- La porte reste impossible a utiliser tant que la protection droite existe.
- La disparition des deux fermetures commence uniquement pendant la sequence de defaite.
- Leur instant precis de disparition sera synchronise avec la destruction de la Pierre du Chaos.
- Apres une perte de vie ou un Game Over, les deux fermetures reviennent a leur etat initial.
- La presentation complete les recree lors de la tentative suivante.

## Musique et ambiance du combat validees

### Intention musicale

- Le combat utilise un theme orchestral epique, rapide et theatral.
- La reference d'intention fournie est `Yuki Hayashi - Yoshiwara Ura Doushin`.
- Le fichier de reference dure environ `3 min 20 s`.
- Sa structure generale repose sur une introduction progressive, plusieurs montees, une respiration centrale et un long climax final.
- Le morceau du jeu reprend cette architecture emotionnelle sans copier la melodie, l'harmonie, le rythme exact ou l'arrangement de la reference.
- La composition d'Imran Adventure reste entierement originale.
- Le motif descendant et instable du Chaos constitue l'identite principale de Tata Lisa.
- De courts fragments du theme courageux d'Imran repondent a ce motif.
- Le violon est l'instrument principal et porte clairement la melodie du combat.
- Le violon apparait des l'introduction et reste present dans les deux phases.
- Son registre devient plus haut et son jeu plus dense pendant la seconde phase.
- Les autres cordes creent les motifs rapides et les nappes harmoniques.
- Les violoncelles soutiennent les graves et la tension liee a la Pierre du Chaos.
- Les cors, les percussions orchestrales et le choeur renforcent le violon sans le remplacer.
- La pulsation reste rapide et constante a `176 BPM`.
- Des impacts magiques et des textures inversees rappellent la Pierre du Chaos.
- Le ton reste epique et impressionnant sans devenir horrifique.

### Structure dynamique

- Une introduction reduite commence pendant la presentation de `5.00 s`.
- Elle utilise un violon grave, des violoncelles, une pulsation discrete et un choeur lointain.
- Le theme complet commence lorsque la barre de vie apparait et que le controle revient.
- La premiere phase place le violon principal devant les cordes rapides, les cors, les percussions et un choeur contenu.
- La transition de `2.50 s` utilise une montee chromatique du violon synchronisee avec la pulsation de la Pierre.
- La seconde phase ajoute un second contre-chant de violon, des cordes plus denses, des percussions plus puissantes, des cors plus presents et un choeur plus large.
- Les couches supplementaires ne modifient pas brutalement le tempo ou le point de la boucle.
- Le Rituel de la Pierre du Chaos recoit des accents de cors et de tambours sans masquer ses avertissements sonores.
- Lorsque Tata Lisa atteint `0 PV`, les percussions et les cors s'interrompent.
- Un violon instable, des cordes tenues et un choeur accompagnent l'attente du Smash final.
- La destruction de la Pierre retire progressivement toutes les couches liees au Chaos.
- Les sons de tension disparaissent avant la fin des `6.00 s` de defaite.
- Apres l'ouverture du sixieme verrou, un motif lumineux annonce la liberation d'Aliyah.
- La scene finale utilise ensuite le theme de victoire et le motif familial.
- La musique finale est organisee en segments adaptatifs commandes par l'etat du combat.
- Le segment de presentation dure `5.00 s`.
- La boucle de premiere phase continue jusqu'au declenchement reel de la transition.
- Le segment de transition dure exactement `2.50 s`.
- La boucle de seconde phase continue jusqu'a l'arrivee a `0 PV`.
- Un segment d'attente peut se repeter sans limite pendant l'etat `Etourdie`.
- Le Smash final lance le segment de defaite de `6.00 s`.
- L'interaction avec la porte lance ensuite le segment d'ouverture des verrous de `6.00 s`.
- Chaque changement de segment conserve le tempo de `176 BPM` ou utilise une transition musicale prevue.
- La duree du combat ne depend donc jamais de la duree fixe de la maquette.

### Regles de mixage

- Les signaux d'attaque restent audibles au-dessus de la musique.
- Les voix et les sous-titres conservent la priorite pendant la presentation, la transition et la defaite.
- Le volume musical diminue legerement pendant les phrases de Tata Lisa.
- Les percussions graves ne masquent jamais les impacts recus par Imran.
- Le violon reste assez present pour identifier le theme sans masquer les signaux de gameplay.
- Les boucles ne produisent aucune coupure audible.
- Une reprise apres une perte de vie recommence depuis l'introduction de presentation.
- La musique s'arrete proprement avant le passage a la scene finale.
- Le morceau de reference reste un document d'intention externe et ne doit pas etre distribue avec le jeu.

### Maquette originale disponible

- Une maquette originale de `60.00 s` est disponible dans `assets/audio/music/theme-tata-lisa-maquette.mp3`.
- Une version OGG destinee aux essais dans Godot est disponible dans `assets/audio/music/theme-tata-lisa-maquette.ogg`.
- La quatrieme version utilise un tempo de `176 BPM`.
- Elle remplace la palette instrumentale de la troisieme version.
- Le violon devient l'instrument principal de la melodie, des montees et du climax.
- Sa palette secondaire comprend les autres cordes, les violoncelles, les cors, les percussions orchestrales et le choeur.
- Son introduction est volontairement courte afin d'atteindre rapidement le rythme du combat final.
- De `0.00 a 2.73 s`, la maquette condense la presentation.
- De `2.73 a 21.82 s`, elle represente la premiere phase.
- De `21.82 a 24.55 s`, elle represente la transition vers la seconde phase.
- De `24.55 a 53.18 s`, elle represente la seconde phase plus intense.
- De `53.18 a 60.00 s`, elle represente la defaite et le passage vers une couleur musicale plus lumineuse.
- Dans le jeu, la couche d'introduction pourra etre prolongee jusqu'a la fin des `5.00 s` de presentation sans ralentir la boucle principale.
- La maquette constitue une demonstration condensee et ne sera pas lue lineairement pendant le combat definitif.
- Les segments adaptatifs definitifs seront produits a partir de cette direction musicale.
- Cette maquette sert a valider l'ambiance et la progression dynamique.
- Elle ne constitue pas encore la composition definitive, le mixage final ou une boucle terminee.
- Sa melodie et son arrangement sont originaux.

## Perte de vie, Game Over et reinitialisation valides

### Perte d'une vie

- La perte du dernier coeur d'Imran interrompt immediatement le combat.
- L'attaque, la recuperation, la pause, la teleportation ou la transition en cours est annulee.
- Tous les projectiles, vagues, colonnes, runes et dangers temporaires disparaissent.
- La barre de vie de Tata Lisa est masquee.
- Une vie est retiree selon les regles communes.
- S'il reste au moins une vie, Imran reapparait devant la porte du donjon avec `3 coeurs`.
- Le nombre de vies restantes ne change pas une seconde fois pendant cette reprise.
- Tata Lisa retrouve exactement `24 PV`.
- Elle revient dans sa premiere phase a la position `x = 1024 px`.
- Son aura de seconde phase disparait.
- Son cycle recommence avec la Flamme du Chaos.
- Son cycle de teleportation recommence depuis `1024 -> 640 -> 256 -> 640`.
- Les deux fermetures reviennent a leur etat inactif.
- La musique recommence depuis son introduction.
- La presentation complete de `5.00 s` est rejouee.
- Les reactions des cles et des verrous sont rejouees.
- La phrase `Tu n'ouvriras jamais cette porte !` est rejouee avec son sous-titre.
- Le controle revient uniquement a la fin de cette presentation.

### Game Over

- Si aucune vie ne reste, l'ecran de Game Over remplace la reapparition.
- Aucun progres temporaire du combat n'est conserve.
- Les six cles deja sauvegardees restent acquises.
- `Recommencer le niveau` replace Imran devant la porte du donjon.
- Cette reprise commence avec `3 coeurs` et `3 vies`.
- Tata Lisa revient a `24 PV`, en premiere phase et a `x = 1024 px`.
- La presentation complete de `5.00 s` est rejouee.
- `Retour au menu principal` conserve uniquement la sauvegarde permanente de la sixieme cle.
- `Continuer` replace ensuite Imran devant la porte avant Tata Lisa avec `3 coeurs` et `3 vies`.

### Fermeture ou interruption

- Aucune sauvegarde n'est creee pendant le combat.
- Vaincre Tata Lisa ne cree pas encore la sauvegarde finale.
- Fermer le jeu avant la liberation d'Aliyah replace Imran devant la porte avant Tata Lisa.
- Une presentation, une transition, une defaite ou une ouverture des verrous interrompue n'est jamais reprise au milieu.
- Tata Lisa, la Pierre du Chaos et les protections retrouvent leur etat initial.
- Les six verrous redeviennent fermes et magiquement proteges.
- Les six cles restent conservees.
- La reprise commence avec `3 coeurs` et `3 vies`.

## Etat a 0 PV et finition

> **Statut :** Valide

### Etat Etourdie valide

- Atteindre `0 PV` ne declenche pas immediatement la sequence de defaite.
- Tata Lisa entre dans l'etat `Etourdie`.
- Son attaque, sa recuperation, sa pause ou sa teleportation en cours est interrompue.
- Tous ses projectiles, ses vagues, ses colonnes, ses runes et ses dangers temporaires disparaissent immediatement.
- Sa zone dangereuse de contact est desactivee.
- Elle ne peut plus se teleporter, attaquer, blesser ou bloquer Imran.
- Sa barre de vie reste visible avec la valeur `0`.
- L'etat ne possede aucune limite de temps.
- Tata Lisa ne recupere aucun point de vie et ne reprend jamais le combat.
- Le joueur conserve toutes ses commandes.
- Il peut se placer librement et charger son Smash Tranchant sans danger propre au boss.
- Une attaque normale ne termine pas le combat.
- Le Smash Tranchant final constitue l'unique action capable de declencher la defaite.
- Ce Smash sert de declencheur cinematographique et n'inflige aucun degat supplementaire.
- La Pierre du Chaos se brise uniquement apres ce contact final.
- N'importe quelle partie du corps visible de Tata Lisa peut recevoir ce Smash final.
- La zone de finition utilise l'enveloppe complete de `128 x 160 px`.
- La tete, le corps, la robe, le voile et les bijoux sont donc des cibles valides pendant cet etat.
- Le premier contact valide du Smash declenche immediatement la sequence de defaite.
- Le controle d'Imran est bloque au moment de ce contact.
- La barre de vie disparait au meme instant.
- Une trajectoire d'energie relie visuellement le point d'impact a la Pierre du Chaos.
- Cette redirection est cinematographique et ne demande aucune seconde attaque.
- Un Smash qui ne touche pas Tata Lisa disparait selon ses regles normales.
- Tata Lisa reste etourdie jusqu'au prochain Smash valide.

## Destruction de la Pierre du Chaos et fuite

> **Statut :** Validee

### Principe de fuite valide

- Le Smash Tranchant final transmet son energie jusqu'a la Pierre du Chaos.
- La pierre se fissure puis se brise pendant la sequence de defaite.
- La magie de Tata Lisa disparait avec la destruction de la pierre.
- Une ultime energie residuelle est liberee au moment exact de cette destruction.
- Tata Lisa utilise cette energie residuelle pour effectuer une derniere teleportation violette.
- Cette teleportation ne signifie pas qu'elle conserve ses pouvoirs.
- Elle commence avant l'extinction complete de l'energie liberee par les fragments.
- Tata Lisa disparait vers une destination situee hors de l'arene et non montree a l'ecran.
- Elle ne revient pas pendant la conclusion.
- Son aura, ses flammes, ses runes et tous ses autres effets magiques disparaissent definitivement.
- La fuite reste cartoon, non violente et adaptee au public vise.
- La sequence complete dure exactement `6.00 s`.

### Decoupage temporel valide

| Periode | Evenement |
|---|---|
| `0.00 a 1.00 s` | L'energie du Smash rejoint la Pierre du Chaos et des fissures apparaissent. |
| `1.00 a 2.00 s` | La pierre se brise en fragments et l'aura de Tata Lisa devient instable. |
| `2.00 a 3.00 s` | La barriere gauche et la protection de la porte se dissipent completement. |
| `3.00 a 4.00 s` | Tata Lisa reagit a la perte de la pierre et de ses pouvoirs. |
| `4.00 a 5.00 s` | Les fragments liberent leur derniere energie et Tata Lisa se teleporte hors de l'arene. |
| `5.00 a 6.00 s` | Les derniers effets du Chaos disparaissent et l'antichambre retrouve son calme. |

- Le controle d'Imran reste bloque pendant toute la sequence.
- Tata Lisa, les fragments et les effets ne possedent aucune collision dangereuse ou solide.
- La barre de vie reste masquee.
- Une secousse de camera maximale de `12 px` pendant `0.25 s` accompagne la destruction de la pierre.
- Cette secousse ne masque ni Tata Lisa, ni Imran, ni les verrous.
- Les six verrous physiques restent fermes lorsque leur protection disparait.
- La lumiere violette ambiante diminue progressivement entre `2.00 et 6.00 s`.
- Aucun objet, coeur, vie, cle ou coffre n'apparait.
- La porte devient disponible uniquement a la fin exacte des `6.00 s`.
- Le controle d'Imran revient au meme instant.
- Tata Lisa prononce exactement : `Non... ma Pierre du Chaos !`
- La phrase commence a `3.00 s`.
- La voix transmet la surprise, la colere et la perte soudaine de controle.
- Aucun filtre ne masque les mots.
- Le sous-titre affiche `Tata Lisa - Non... ma Pierre du Chaos !`
- Il reste visible de `3.00 a 5.00 s`.
- Le sous-titre reste actif lorsque le volume des voix est coupe.
- Un impact net de la Shadow Sword marque le contact final.
- Des fissures cristallines croissantes accompagnent le trajet de l'energie vers la pierre.
- Une brisure claire et non violente accompagne la destruction entre `1.00 et 2.00 s`.
- Un souffle inverse accompagne la disparition des deux protections entre `2.00 et 3.00 s`.
- Les effets diminuent afin de laisser la phrase de Tata Lisa intelligible entre `3.00 et 4.00 s`.
- La teleportation finale utilise un son instable, plus court et moins puissant que pendant le combat.
- Un bourdonnement decroissant accompagne l'extinction du Chaos entre `5.00 et 6.00 s`.
- Tous les sons du Chaos s'arretent a la fin exacte de la sequence.

### Assets visuels et sonores a produire

- Trajectoire d'energie du point d'impact vers la Pierre du Chaos.
- Etats intact, fissure et brise de la pierre.
- Fragments violets sans collision.
- Aura de Tata Lisa devenant instable puis disparaissant.
- Dissolution de la barriere gauche.
- Dissolution de la protection de la porte.
- Animation de surprise et de colere de Tata Lisa.
- Teleportation finale instable.
- Extinction des dernieres particules du Chaos.
- Phrase enregistree `Non... ma Pierre du Chaos !`.
- Sous-titre associe.
- Impact final de la Shadow Sword.
- Fissures cristallines croissantes.
- Brisure claire de la pierre.
- Souffle inverse des protections.
- Teleportation instable.
- Bourdonnement decroissant du Chaos.

## Acces aux six verrous

> **Statut :** Valide

### Regles deja validees

- Le controle d'Imran revient a la fin de la sequence de defaite.
- L'arene ne contient plus aucun ennemi, projectile ou danger.
- Tata Lisa ne revient pas.
- La protection magique de la porte a entierement disparu.
- Les six verrous physiques restent fermes.
- La camera cadre Imran et la porte du donjon.
- Imran doit avancer lui-meme jusqu'a la porte.
- Un message d'interaction apparait lorsqu'il atteint la zone prevue.
- Le joueur utilise une seule fois la commande `Interaction`.
- Cette interaction utilise automatiquement les six cles.
- Les verrous s'ouvrent l'un apres l'autre.
- Aucune seconde interaction n'est demandee.
- Les cles restent inscrites dans la sauvegarde.
- Le controle d'Imran reste bloque pendant l'ouverture.
- L'ouverture conduit directement a la scene finale de liberation d'Aliyah.
- Le donjon ne devient jamais un niveau jouable.
- La sequence complete dure exactement `6.00 s`.

### Decoupage temporel valide

| Periode | Evenement |
|---|---|
| `0.00 a 0.50 s` | Les six cles apparaissent devant Imran et la porte. |
| `0.50 a 3.50 s` | Les six verrous s'ouvrent successivement, avec `0.50 s` pour chacun. |
| `3.50 a 5.00 s` | La porte du donjon s'ouvre. |
| `5.00 a 6.00 s` | Un fondu conduit directement a la scene finale. |

- Les verrous utilisent toujours l'ordre visuel de gauche a droite.
- Un verrou termine son ouverture avant que le suivant commence.
- Les six cles ne demandent aucune commande individuelle.
- La porte reste fermee jusqu'a l'ouverture complete du sixieme verrou.
- Le fondu commence uniquement lorsque la porte a atteint sa position ouverte.
- L'ecran reste noir tant que la scene finale n'est pas prete.
- La scene finale sera detaillee pendant l'etape 13 du GDD.
- Les six cles apparaissent en arc autour d'Imran pendant les premieres `0.50 s`.
- Chaque cle conserve les materiaux, les couleurs et le symbole de sa region.
- Les cles utilisent l'ordre de la Foret, de la Grotte, du Lac, du Desert, du Volcan puis du Chateau.
- La premiere cle rejoint le premier verrou entre `0.50 et 1.00 s`.
- La deuxieme cle rejoint le deuxieme verrou entre `1.00 et 1.50 s`.
- La troisieme cle rejoint le troisieme verrou entre `1.50 et 2.00 s`.
- La quatrieme cle rejoint le quatrieme verrou entre `2.00 et 2.50 s`.
- La cinquieme cle rejoint le cinquieme verrou entre `2.50 et 3.00 s`.
- La sixieme cle rejoint le sixieme verrou entre `3.00 et 3.50 s`.
- Chaque cle entre dans sa serrure, tourne puis disparait en lumiere claire.
- Cette disparition visuelle ne retire jamais la cle de la sauvegarde.
- Aucune lumiere doree excessive ni aucun objet supplementaire n'apparait.
- Le centre horizontal de la porte se trouve a la position locale `x = 1184 px`.
- La porte reste donc a `96 px` de la limite droite placee a `x = 1280 px`.
- Son interaction devient disponible lorsque le centre d'Imran se trouve a `64 px` ou moins de ce point.
- Cette distance correspond exactement a une grille du jeu.
- Le message `Interaction` apparait au-dessus de la partie basse de la porte.
- Il ne peut jamais apparaitre avant la fin de la defaite de Tata Lisa.
- Il disparait immediatement lorsque le joueur utilise la commande.
- Imran se tourne vers la porte au debut de la sequence.
- Son deplacement, son saut, son Dash et ses attaques sont bloques pendant les `6.00 s`.
- Une note claire differente accompagne l'apparition de chaque cle.
- Les six notes forment une courte progression ascendante.
- Chaque entree dans une serrure produit un mecanisme metallique distinct.
- Le mecanisme se termine par un clic lorsque le verrou est ouvert.
- Aucun nouveau son ne commence avant la fin du clic precedent.
- Un accord lumineux retentit apres l'ouverture du sixieme verrou.
- Un grondement lourd mais calme accompagne l'ouverture de la porte entre `3.50 et 5.00 s`.
- Le grondement s'arrete avant le debut du fondu.
- Les sons restent moins forts que les dialogues de la scene finale.

### Assets visuels et sonores a produire

- Porte du donjon fermee.
- Porte du donjon avec protection magique.
- Porte sans protection avec six verrous fermes.
- Six etats successifs des verrous ouverts.
- Porte pendant son ouverture.
- Porte entierement ouverte.
- Six cles dans leur apparence regionale.
- Formation en arc autour d'Imran.
- Trajectoire de chaque cle vers son verrou.
- Rotation et disparition claire de chaque cle.
- Message d'interaction de la porte.
- Six notes claires ascendantes.
- Six sons de mecanismes metalliques.
- Six clics de verrous.
- Accord lumineux final.
- Grondement calme de la porte.
- Fondu vers la scene finale.

## Inventaire unifie des assets valide

### Regles de production

- Cet inventaire regroupe les besoins deja valides sans modifier le fonctionnement du combat.
- Un asset reutilisable doit rester unique et recevoir des variantes de couleur, de taille ou d'intensite dans Godot.
- Les effets de la seconde phase reutilisent les bases de la premiere phase lorsque leur silhouette reste identique.
- L'aura de seconde phase reste un calque separe du personnage.
- Les zones de collision, les zones vulnerables et les zones dangereuses ne font pas partie des images.
- Les dimensions d'export, le nombre exact d'images, les atlas, les noms de fichiers et les reglages d'import seront fixes dans le TDD.
- Les signaux visuels doivent rester comprehensibles lorsque le son est coupe.
- Les sons d'avertissement doivent rester audibles sans masquer les impacts, les voix ou les commandes importantes.

### Personnage et animations de Tata Lisa

| ID | Asset a produire | Utilisation |
|---|---|---|
| `TL-PER-01` | Modele visuel principal de Tata Lisa | Base commune aux deux phases |
| `TL-PER-02` | Posture neutre de premiere phase | Attente et pauses vulnerables |
| `TL-PER-03` | Posture neutre irritee de seconde phase | Attente avec yeux et Pierre plus lumineux |
| `TL-PER-04` | Retour vers la posture neutre | Recuperation de `0.30 s` |
| `TL-PER-05` | Reaction visuelle a un impact | Retour de degat de `0.33 s` sans interruption |
| `TL-PER-06` | Saisie de la Pierre du Chaos | Presentation et preparation magique |
| `TL-PER-07` | Main tendue et geste de lancement | Flamme du Chaos |
| `TL-PER-08` | Main abaissee vers le sol | Vague du Chaos |
| `TL-PER-09` | Deux mains levees puis abaissees | Vague haute et Rituel |
| `TL-PER-10` | Deux mains dirigees vers Imran puis refermees | Colonne du Chaos |
| `TL-PER-11` | Provocation theatrale | Presentation du combat |
| `TL-PER-12` | Expression et posture de colere | Transition vers la seconde phase |
| `TL-PER-13` | Posture Etourdie | Etat a `0 PV` sans limite de temps |
| `TL-PER-14` | Surprise et colere apres la brisure | Sequence de defaite |
| `TL-PER-15` | Dissolution et reapparition standards | Teleportations du combat |
| `TL-PER-16` | Apparition theatrale | Presentation devant la porte |
| `TL-PER-17` | Teleportation speciale vers le centre | Transition vers la seconde phase |
| `TL-PER-18` | Teleportation finale instable | Fuite apres la destruction de la pierre |

### Pierre du Chaos et effets generaux

| ID | Asset a produire | Utilisation |
|---|---|---|
| `TL-EFF-01` | Pierre du Chaos intacte | Etat normal |
| `TL-EFF-02` | Pulsation faible de la pierre | Premiere phase |
| `TL-EFF-03` | Pulsation forte de la pierre | Transition et seconde phase |
| `TL-EFF-04` | Propagation violette vers un bras | Flamme et Vague |
| `TL-EFF-05` | Propagation violette vers les deux bras | Colonne et Rituel |
| `TL-EFF-06` | Aura violette et noire | Seconde phase |
| `TL-EFF-07` | Marque violette de destination | Toutes les teleportations de combat |
| `TL-EFF-08` | Interruption et disparition des dangers | Transition, perte de vie et etat Etourdie |
| `TL-EFF-09` | Retour visuel de degat | Impact valide sur la tete |
| `TL-EFF-10` | Trajectoire du Smash vers la pierre | Finition cinematographique |
| `TL-EFF-11` | Pierre fissuree | Premiere seconde de la defaite |
| `TL-EFF-12` | Pierre brisee et fragments violets | Destruction sans collision |
| `TL-EFF-13` | Aura instable puis eteinte | Perte des pouvoirs |
| `TL-EFF-14` | Extinction des particules du Chaos | Fin de la sequence de defaite |

### Effets des quatre attaques

| ID | Asset a produire | Utilisation |
|---|---|---|
| `TL-ATQ-01` | Flamme du Chaos de `64 x 64 px` | Projectile commun aux deux phases |
| `TL-ATQ-02` | Coeur noir, contour clair et trainee | Lecture du projectile |
| `TL-ATQ-03` | Formation d'une flamme | Premiere phase |
| `TL-ATQ-04` | Formation et rotation de deux flammes | Seconde phase |
| `TL-ATQ-05` | Repli et dissolution de la flamme | Blocage, fin de portee ou interruption |
| `TL-ATQ-06` | Vague basse de `144 x 64 px` | Deux phases |
| `TL-ATQ-07` | Vague haute de `176 x 120 px` | Seconde phase |
| `TL-ATQ-08` | Arcs, coeurs noirs et fragments de runes | Formation des vagues |
| `TL-ATQ-09` | Repli et disparition des vagues | Fin de trajet ou interruption |
| `TL-ATQ-10` | Limites verticales de `384 px` et `432 px` | Avertissement de la colonne |
| `TL-ATQ-11` | Rune ciblee progressive | Preparation de la colonne |
| `TL-ATQ-12` | Colonne de flammes violettes et d'energie noire | Phase dangereuse |
| `TL-ATQ-13` | Contraction finale vers la rune | Fin de la colonne |
| `TL-ATQ-14` | Pierre flottant devant Tata Lisa | Rituel de la Pierre du Chaos |
| `TL-ATQ-15` | Trois fragments de rune en rotation | Progression des trois etapes du rituel |
| `TL-ATQ-16` | Symboles de flamme, de limites et de sol | Identification des etapes du rituel |
| `TL-ATQ-17` | Etats actif et eteint des fragments | Lecture de la progression |
| `TL-ATQ-18` | Ligne violette et runes sur tout le sol | Avertissement de l'impulsion finale |
| `TL-ATQ-19` | Onde violette d'activation | Debut du danger au sol |
| `TL-ATQ-20` | Flammes et pointes sous `56 px` | Danger final du rituel |
| `TL-ATQ-21` | Particules noires et extinction du sol | Fin du rituel |

### Arene, porte et verrous

| ID | Asset a produire | Utilisation |
|---|---|---|
| `TL-ARE-01` | Mur sombre de l'antichambre | Arriere-plan fixe |
| `TL-ARE-02` | Sol en grandes dalles anthracite | Surface jouable plate |
| `TL-ARE-03` | Piliers massifs | Encadrement decoratif |
| `TL-ARE-04` | Bannieres bordeaux et violettes | Rappel des couleurs de Tata Lisa |
| `TL-ARE-05` | Bordures dorees | Liaison avec la tenue de Tata Lisa |
| `TL-ARE-06` | Hautes ouvertures et lumiere violette | Eclairage du decor |
| `TL-ARE-07` | Particules faibles du Chaos | Ambiance des deux phases |
| `TL-ARE-08` | Barriere gauche active | Fermeture de l'entree |
| `TL-ARE-09` | Protection magique de la porte | Limite droite et protection des verrous |
| `TL-ARE-10` | Dissolution des deux protections | Sequence de defaite |
| `TL-ARE-11` | Porte fermee et protegee | Presentation et combat |
| `TL-ARE-12` | Porte sans protection avec six verrous | Apres la defaite |
| `TL-ARE-13` | Six etats successifs des verrous ouverts | Interaction avec les six cles |
| `TL-ARE-14` | Porte en cours d'ouverture | Sequence finale |
| `TL-ARE-15` | Porte entierement ouverte | Passage vers la scene finale |
| `TL-ARE-16` | Faible lumiere derriere la porte | Presence d'Aliyah |

### Cles, interface et textes

| ID | Asset a produire ou reutiliser | Utilisation |
|---|---|---|
| `TL-INT-01` | Designs valides des six cles regionales | Futurs assets definitifs partages avec les recompenses des golems |
| `TL-INT-02` | Reaction lumineuse des cles et des verrous | Debut de la presentation |
| `TL-INT-03` | Formation en arc des six cles | Debut de l'ouverture |
| `TL-INT-04` | Trajectoire vers chaque verrou | Ouverture dans l'ordre des niveaux |
| `TL-INT-05` | Rotation et disparition claire d'une cle | Confirmation de chaque verrou |
| `TL-INT-06` | Barre de vie commune des boss | Affichage des `24 PV` |
| `TL-INT-07` | Message d'interaction commun | Interaction avec la porte |
| `TL-INT-08` | Sous-titre de presentation | `Tu n'ouvriras jamais cette porte !` |
| `TL-INT-09` | Sous-titre de transition | `Assez !` |
| `TL-INT-10` | Sous-titre de defaite | `Non... ma Pierre du Chaos !` |
| `TL-INT-11` | Fondu vers la scene finale | Fin de l'ouverture de la porte |

### Voix, sons et musique

| ID | Asset a produire ou reutiliser | Utilisation |
|---|---|---|
| `TL-AUD-01` | Voix de la provocation | Presentation |
| `TL-AUD-02` | Voix `Assez !` | Transition vers la seconde phase |
| `TL-AUD-03` | Voix sur la perte de la pierre | Defaite |
| `TL-AUD-04` | Teleportation standard | Deplacement du combat |
| `TL-AUD-05` | Teleportation theatrale | Presentation |
| `TL-AUD-06` | Teleportation instable | Fuite finale |
| `TL-AUD-07` | Pulsations cristallines | Pierre du Chaos |
| `TL-AUD-08` | Propagation magique | Transfert de la pierre vers les mains |
| `TL-AUD-09` | Formation, lancement, trajet et dissolution | Flamme du Chaos |
| `TL-AUD-10` | Preparation, trajet, impact et extinction | Vagues du Chaos |
| `TL-AUD-11` | Ciblage, montee, activation et grondement | Colonne du Chaos |
| `TL-AUD-12` | Bourdonnement et trois notes distinctes | Etapes du Rituel |
| `TL-AUD-13` | Resonance, impact et vibration du sol | Impulsion finale du Rituel |
| `TL-AUD-14` | Apparition et disparition de l'aura | Transition de phase |
| `TL-AUD-15` | Fermeture des protections | Presentation |
| `TL-AUD-16` | Impact final de la Shadow Sword | Finition |
| `TL-AUD-17` | Fissures et brisure cristallines | Destruction de la pierre |
| `TL-AUD-18` | Souffle inverse des protections | Ouverture de l'arene |
| `TL-AUD-19` | Bourdonnement decroissant du Chaos | Fin de la defaite |
| `TL-AUD-20` | Six notes ascendantes | Trajet des cles |
| `TL-AUD-21` | Six mecanismes et six clics | Ouverture des verrous |
| `TL-AUD-22` | Accord lumineux final | Sixieme verrou |
| `TL-AUD-23` | Grondement calme de la porte | Ouverture |
| `TL-AUD-24` | Ensemble musical adaptatif au violon | Presentation, boucles des phases, transition, attente, defaite et ouverture a `176 BPM` |

### Assets communs ou produits dans les autres fiches

- Imran et toutes ses animations de combat.
- Shadow Sword et Smash Tranchant.
- Bouclier de lumiere.
- Coeurs, vies, reactions aux degats et invulnerabilite.
- Ecran de Game Over et commandes de reprise.
- Police, cadre et systeme communs des sous-titres.
- Cadre, fond et remplissage de la barre de vie commune aux boss.
- Systeme visuel commun des messages d'interaction.
- Designs des six cles regionales deja valides dans les fiches de recompense.
- Assets definitifs des six cles a produire une seule fois puis a partager avec cette sequence.
- Son commun d'impact de la Shadow Sword sur un ennemi.
- Effets communs de fondu et de changement de scene.

## Verification finale de coherence validee

- Les teleportations standards et cinematographiques sont distinguees sans modifier leurs durees.
- L'invulnerabilite pendant une teleportation constitue une exception explicite aux regles communes.
- Les deux phases, leurs seuils, leurs cycles et leur reinitialisation ne se contredisent pas.
- Les quatre attaques possedent un avertissement, une reponse et une fin mesurables.
- Les projectiles et les dangers respectent les limites solides de l'arene.
- La musique adaptative suit les etats du combat sans dependre de la duree de la maquette.
- La defaite, la destruction de la pierre, la fuite et l'ouverture des verrous suivent un ordre unique.
- La progression reste compatible avec les six cles sauvegardees et l'absence de niveau jouable dans le donjon.
- Les assets propres, communs et encore a produire sont distingues.
- Tous les liens vers les documents de reference sont valides.

## Criteres de validation

La fiche sera validee lorsque :

- la structure complete du combat sera mesurable ;
- toutes les capacites d'Imran auront une utilite claire ;
- chaque attaque possedera un avertissement visuel comprehensible sans le son ;
- aucune attaque ne produira de degat inevitable ;
- Tata Lisa se distinguera clairement des six golems ;
- la Pierre du Chaos restera lisible comme source de ses pouvoirs ;
- la defaite conduira sans contradiction a l'ouverture des six verrous ;
- tous les assets necessaires seront identifies.

## Sources

- [Tata Lisa du Concept Game](../../Concept-Game/08-Boss/Tata-Lisa.md)
- [Personnage de Tata Lisa](../../Concept-Game/04-Personnages/Tata-Lisa.md)
- [Fin du Concept Game](../../Concept-Game/02-Histoire/Fin.md)
- [Chateau de Tata Lisa](../../Concept-Game/03-Univers/Chateau-de-Tata-Lisa.md)
- [Regles communes des boss](Regles-Communes.md)
- [Progression du GDD](../Systemes/Progression.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
