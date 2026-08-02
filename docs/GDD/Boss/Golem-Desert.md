# Golem du Desert

> **Statut :** Valide

## Objectif

Definir le quatrieme gardien comme un combat centre sur une maitrise plus avancee du Dash et du Double saut. Le joueur doit combiner ses capacites de deplacement avec l'observation des preparations du boss.

## Role du combat

- Verifier l'observation des preparations visuelles et sonores.
- Reutiliser la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.
- Demander une utilisation plus avancee du Dash.
- Donner au Double saut une utilite importante.
- Augmenter la difficulte sans introduire une seconde phase.
- Preparer le joueur aux deux derniers golems.

## Capacites requises validees

- Au moins une attaque exige une sequence combinant le Dash et le Double saut.
- Le Dash est effectue uniquement au sol.
- Le Dash aerien reste impossible.
- Apres le Dash, Imran doit utiliser un saut normal puis son Double saut pour terminer l'esquive.
- Le Dash seul ne permet pas d'eviter entierement cette attaque.
- Le saut et le Double saut sans Dash ne permettent pas non plus de l'eviter entierement.
- La sequence doit laisser une marge suffisante pour que les trois actions puissent etre enchainees de facon volontaire.
- Aucune attaque ne demande une capacite qui n'est pas disponible depuis le niveau 0.
- Le combat doit rester terminable avec le deplacement normal, le saut, le Double saut, le Dash au sol, la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.

## Structure du combat validee

- Le Golem du Desert possede une seule phase.
- Il possede `18 PV`.
- Ses points de vie ne modifient ni son comportement, ni la vitesse de ses attaques, ni l'ordre de son cycle.
- Il utilise les recuperations communes de `0.30 s`.
- Chaque recuperation est suivie par la pause neutre commune de `1.80 s`.
- La tete constitue sa zone vulnerable pendant le combat actif.
- Une attaque normale validee sur la tete retire `1 PV`.
- Un Smash Tranchant valide sur la tete retire `2 PV`.
- Chaque attaque du golem retire `1 coeur` a Imran.
- Le contact avec son corps utilise la zone dangereuse commune de `112 x 136 px`.
- A `0 PV`, le golem entre dans l'etat `Etourdi`.
- Le Smash Tranchant final peut toucher n'importe quelle partie de son corps.
- Ce Smash final declenche la sequence commune de defaite.

## Structure du cycle validee

- Le Golem du Desert possede exactement `3 attaques`.
- Ces attaques utilisent un ordre fixe et previsible.
- La premiere attaque reste identique a chaque tentative.
- Apres la troisieme attaque, le cycle reprend depuis la premiere.
- Recevoir un degat ne modifie pas l'ordre du cycle.
- Les points de vie restants ne modifient ni l'ordre, ni les valeurs, ni le rythme.
- Chaque attaque respecte la recuperation commune de `0.30 s`.
- La pause neutre commune de `1.80 s` commence apres cette recuperation.
- La preparation suivante commence uniquement apres la fin de cette pause.
- Une perte de vie d'Imran reinitialise le cycle sur la premiere attaque.
- Le cycle utilise toujours l'ordre suivant :

| Ordre | Attaque | Fonction principale |
|---:|---|---|
| 1 | Javelot de gres | Bloquer un projectile avec le Bouclier de lumiere |
| 2 | Mur de sable | Franchir un danger haut avec le Double saut |
| 3 | Piege des ruines | Enchainer Dash au sol, saut et Double saut |

- Le Javelot de gres constitue une entree de cycle lisible.
- Le Mur de sable rend le Double saut obligatoire.
- Le Piege des ruines constitue l'attaque la plus technique du cycle.
- Apres le Piege des ruines, le cycle reprend avec le Javelot de gres.

## Deplacement du golem valide

- Le Golem du Desert reste a la position horizontale locale `x = 1024 px` pendant tout le combat.
- Il ne marche pas et ne glisse pas vers Imran.
- Ses attaques, les degats recus et les collisions ne modifient pas cette position.
- Il ne se deplace pas pendant les recuperations de `0.30 s` ni pendant les pauses neutres de `1.80 s`.
- Au debut de chaque preparation, il se tourne sur place vers la position actuelle d'Imran.
- Cette orientation determine la direction verrouillee de l'attaque lorsque celle-ci en utilise une.
- Il ne change plus d'orientation pendant la preparation ni pendant l'execution de cette attaque.
- Le ciblage du Piege des ruines reste determine par la position d'Imran et non par l'orientation visuelle du golem.
- Il peut de nouveau se retourner au debut de la preparation suivante.
- Dans l'etat `Etourdi`, il conserve sa position et son orientation.

## Attaque 1 - Javelot de gres

> **Statut :** Validee

### Structure validee

- Le golem lance un unique javelot de gres.
- La preparation avant son lancement dure exactement `0.50 s`.
- Le javelot porte des symboles geometriques graves.
- Sa zone dangereuse mesure exactement `96 x 24 px`.
- Sa forme visuelle couvre cette zone sans creer de danger invisible.
- Sa vitesse horizontale constante est de `560 px/s`.
- Sa duree de vie maximale est de `2.00 s`.
- Sa portee maximale est donc de `1120 px`.
- Son centre se trouve a `48 px` au-dessus du sol.
- Sa zone verticale couvre donc la hauteur comprise entre `36 px` et `60 px`.
- Il se deplace horizontalement en ligne droite.
- La direction horizontale est verrouillee au debut de la preparation.
- Le projectile ne suit pas Imran apres son lancement.
- Le Bouclier de lumiere bloque automatiquement le javelot lorsqu'Imran lui fait face.
- Le javelot bloque se brise et disparait immediatement.
- Imran peut egalement franchir le javelot avec un saut normal bien place.
- La hauteur de saut normale de `89 px` conserve une marge verticale de `29 px`.
- Il retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ce projectile et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- Il disparait apres une collision valide ou a la fin de sa duree de vie.
- Il disparait toujours avant la preparation de l'attaque suivante.
- La recuperation commune de `0.30 s` commence apres sa disparition.

### Signal visuel valide

- Au debut de la preparation, le golem se tourne vers la position d'Imran et verrouille cette direction.
- Il recule le bras utilise pour le lancer.
- Du sable et de petits fragments de gres se rassemblent progressivement dans sa main.
- Les fragments se compactent et forment le javelot pendant les `0.50 s`.
- Les symboles graves produisent un bref eclat dore lorsque sa formation est terminee.
- Le golem projette alors son bras vers Imran et libere le javelot.
- Le projectile devient dangereux uniquement lorsqu'il quitte sa main.
- Le recul du bras, la formation du javelot et l'eclat final restent comprehensibles lorsque le son est coupe.

### Apparence du projectile validee

- Le javelot utilise un gres ocre correspondant au corps du golem.
- Ses deux extremites forment des pointes taillees clairement visibles.
- Des symboles geometriques dores parcourent sa surface.
- Ces symboles emettent un bref eclat au moment du lancement.
- Une courte trainee de sable suit le projectile pendant son trajet.
- La trainee reste purement visuelle et n'agrandit pas la zone dangereuse.
- Le javelot se brise en petits fragments de gres et en sable sans danger lors de sa disparition.

### Signal sonore valide

- Un bruit de sable rassemble commence au debut de la preparation.
- Un frottement de pierre accompagne la formation du javelot dans la main.
- Un claquement sec marque exactement le lancement.
- Le bruit de formation s'arrete au moment de ce claquement.
- Un leger sifflement accompagne le trajet du projectile.
- La collision avec Imran, le bouclier ou une limite solide produit un bref son de gres brise.

### Assets visuels et sonores a produire

- Animation du golem reculant son bras.
- Effet de sable et de fragments se rassemblant dans sa main.
- Formation progressive du javelot.
- Animation du bras projetant le javelot.
- Javelot en gres ocre avec pointes taillees.
- Symboles geometriques dores.
- Effet de courte trainee de sable.
- Effet de fragmentation sans danger.
- Son de sable rassemble.
- Son de frottement de pierre.
- Son de claquement sec au lancement.
- Son leger de sifflement pendant le trajet.
- Son bref de gres brise lors de la collision.

## Attaque 2 - Mur de sable

> **Statut :** Validee

### Structure validee

- Le golem cree un unique mur vertical de sable compacte.
- La preparation avant son depart dure exactement `0.75 s`.
- Le mur progresse horizontalement en restant en contact avec le sol.
- Sa vitesse horizontale constante est de `400 px/s`.
- Sa duree de vie maximale est de `3.00 s`.
- Sa portee maximale est donc de `1200 px`.
- Sa zone dangereuse mesure exactement `64 x 128 px`.
- Sa zone commence au niveau du sol et atteint une hauteur de `128 px`.
- Sa forme visuelle couvre cette zone sans creer de danger invisible.
- La direction horizontale est verrouillee au debut de la preparation.
- Le mur ne suit pas Imran apres son depart.
- La zone dangereuse ne constitue pas un obstacle solide.
- Imran ne peut ni se tenir, ni atterrir sur le mur.
- Le Bouclier de lumiere ne protege pas contre cette attaque.
- Le Dash ne rend pas Imran invulnerable au mur.
- Le saut normal seul ne permet pas de le franchir.
- La hauteur du saut normal de `89 px` reste inferieure de `39 px` au sommet du mur.
- Imran doit utiliser son Double saut pour passer entierement au-dessus.
- Un saut normal complet suivi d'un Double saut peut atteindre environ `167 px`.
- Cette combinaison conserve donc une marge verticale maximale d'environ `39 px`.
- Le mur retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche cette attaque et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- Le mur disparait lorsqu'il atteint une limite solide ou la fin de sa duree de vie.
- Il disparait toujours avant la preparation de l'attaque suivante.
- La recuperation commune de `0.30 s` commence apres sa disparition.

### Signal visuel valide

- Au debut de la preparation, le golem se tourne vers Imran et verrouille cette direction.
- Il se penche et pose simultanement ses deux mains au sol.
- Du sable converge progressivement vers l'espace situe devant ses mains.
- Une masse de sable compacte commence a monter sans etre encore dangereuse.
- Au terme des `0.75 s`, le golem releve brusquement les deux bras.
- Ce mouvement donne au mur sa hauteur complete de `128 px` et declenche son depart.
- Le mur devient dangereux uniquement lorsqu'il commence son deplacement horizontal.
- La posture basse, le rassemblement du sable et le mouvement vertical des bras restent comprehensibles lorsque le son est coupe.

### Apparence du mur validee

- Le mur utilise un sable ocre dense.
- Sa partie superieure forme une crete irreguliere clairement visible.
- Quelques fragments de gres circulent dans le sable.
- Des symboles dores apparaissent et disparaissent dans le flux.
- La base reste continuellement en contact avec le sol.
- Le sable, les fragments et les symboles visibles restent contenus dans la zone de `64 x 128 px`.
- Une courte trainee de poussiere peut suivre le mur sans agrandir sa zone dangereuse.
- Lors de sa disparition, le mur s'effondre en sable et en petits fragments sans danger.

### Signal sonore valide

- Un bruit de sable aspire commence lorsque les deux mains touchent le sol.
- Un grondement grave accompagne la montee progressive de la masse de sable.
- Une rafale seche marque exactement le mouvement vertical des bras et le depart du mur.
- Un roulement de sable accompagne le trajet horizontal.
- Le son de trajet s'arrete lorsque le mur disparait.
- Un bref effondrement de sable et de gres accompagne sa disparition.

### Assets visuels et sonores a produire

- Animation du golem posant ses deux mains au sol.
- Effet de sable convergeant vers ses mains.
- Formation progressive de la masse de sable.
- Animation des deux bras se relevant brusquement.
- Mur de sable ocre avec crete irreguliere.
- Fragments de gres et symboles dores dans le flux.
- Effet de courte trainee de poussiere.
- Effet d'effondrement sans danger.
- Son de sable aspire.
- Son de grondement grave pendant la formation.
- Son de rafale seche au depart.
- Son de roulement pendant le trajet.
- Son bref d'effondrement a la disparition.

## Attaque 3 - Piege des ruines

> **Statut :** Validee

### Structure validee

- Le Piege des ruines se deroule en deux dangers consecutifs.
- Le premier danger est une zone d'effondrement de `384 px` de largeur.
- La preparation avant l'effondrement dure exactement `0.65 s`.
- Son centre horizontal correspond a la position d'Imran au debut de la preparation.
- Cette position est verrouillee pendant toute l'attaque.
- La zone ne suit pas Imran apres le debut de la preparation.
- La zone annoncee reste sans danger jusqu'a l'impact des ruines.
- Imran doit la quitter horizontalement avec un Dash effectue au sol.
- Le Dash aerien reste impossible.
- Depuis le centre, la zone vulnerable de `32 px` d'Imran doit parcourir `208 px` pour sortir completement.
- En `0.65 s`, un deplacement normal a pleine vitesse ne peut parcourir que `156 px`.
- Le deplacement normal reste donc inferieur de `52 px` a la distance de sortie.
- Un Dash de `124 px` laisse ensuite `0.45 s` de mouvement normal.
- A la vitesse normale maximale de `240 px/s`, cette fin de preparation permet de parcourir `108 px` supplementaires.
- La sequence peut donc couvrir environ `232 px` et conserve une marge horizontale d'environ `24 px`.
- Si la zone depasse une barriere, seule sa partie situee dans l'arene reste active et visible.
- Le centre verrouille n'est jamais decale.
- Imran doit alors sortir vers l'interieur de l'arene et la distance maximale reste `208 px`.
- A l'impact, des fragments de ruines et du sable remplissent la zone annoncee.
- La zone centrale reste dangereuse pendant exactement `0.50 s` apres cet impact.
- Deux larges vagues de debris sont alors produites simultanement.
- Une vague part du bord gauche de la zone et se dirige vers la gauche.
- Une vague part du bord droit de la zone et se dirige vers la droite.
- La zone dangereuse de chaque vague mesure exactement `192 x 112 px`.
- Chaque vague reste en contact avec le sol et atteint une hauteur de `112 px`.
- La forme visuelle de chaque vague couvre cette zone sans creer de danger invisible.
- Chaque vague se deplace a une vitesse horizontale constante de `480 px/s`.
- La duree de vie maximale de chaque vague est de `2.25 s`.
- La portee maximale de chaque vague est donc de `1080 px`.
- La hauteur du saut normal de `89 px` reste inferieure de `23 px` au sommet des vagues.
- Imran doit utiliser un saut normal puis son Double saut pour rester au-dessus de la vague qui se dirige vers lui.
- Un saut normal complet suivi d'un Double saut peut atteindre environ `167 px`.
- Cette combinaison conserve donc une marge verticale maximale d'environ `55 px`.
- Le Bouclier de lumiere ne protege ni contre l'effondrement, ni contre les vagues.
- Le Dash ne rend pas Imran invulnerable a ces dangers.
- L'effondrement et chaque vague retirent `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche les differents dangers de cette attaque de retirer plusieurs coeurs pendant la meme periode.
- Aucun fragment ne devient un obstacle solide ou une plateforme.
- Les fragments de la zone centrale disparaissent entierement a la fin des `0.50 s`.
- Chaque vague disparait lorsqu'elle atteint une barriere ou la fin de sa duree de vie.
- Tous les dangers de l'attaque disparaissent avant la preparation de l'attaque suivante.
- La recuperation commune de `0.30 s` commence apres la disparition de la derniere vague.

### Signal visuel valide

- Au debut de la preparation, deux limites dorees apparaissent aux bords exacts de la zone de `384 px`.
- Ces limites restent fixes pendant les `0.65 s`.
- Des fissures lumineuses se propagent progressivement sur le sol entre les deux limites.
- Les ombres de plusieurs blocs de ruines apparaissent au-dessus de la meme zone.
- Les fissures et les ombres deviennent plus intenses jusqu'a l'impact.
- La zone reste sans danger pendant toute la preparation.
- A l'impact, les deux limites produisent un bref eclat et les fragments de ruines tombent dans la zone.
- Les deux vagues apparaissent exactement aux bords annonces et partent vers l'exterieur.
- La vague gauche et la vague droite utilisent des mouvements de particules diriges dans leurs directions respectives.
- La zone centrale, les vagues et leurs limites visibles restent suffisamment distinctes pour etre suivies simultanement.
- Aucun nuage de poussiere ne masque Imran, le golem ou les zones dangereuses.
- Les limites et les fragments centraux disparaissent a la fin des `0.50 s`.
- Les vagues conservent leur visuel jusqu'a leur collision ou a la fin de leur duree de vie.
- Le signal reste comprehensible lorsque le son est coupe.

### Animation du golem validee

- Au debut de la preparation, le golem se tourne vers Imran sans modifier le centre verrouille de la zone.
- Il leve simultanement ses deux poings au-dessus de sa tete.
- Son coeur et ses gravures emettent une lumiere doree de plus en plus intense.
- Il conserve les deux poings leves pendant la formation des limites, des fissures et des ombres.
- Au terme des `0.65 s`, il rabat brusquement les deux bras.
- Ses deux mains frappent le sol au meme instant.
- Cet impact declenche exactement la chute des ruines et le depart des deux vagues.
- Le golem ne se deplace pas horizontalement pendant cette animation.
- Cette animation reste distincte du Mur de sable, dont les mains partent du sol et se relevent.

### Apparence des dangers validee

- Les blocs de la zone centrale utilisent un gres ocre correspondant aux anciennes ruines du Desert.
- Leurs formes conservent des bords architecturaux simples et clairement lisibles.
- Certains fragments portent des symboles geometriques graves.
- De brefs eclats dores accompagnent leur impact sans agrandir la zone dangereuse.
- Les deux vagues melangent du sable ocre et de petits debris de gres.
- Les debris circulent dans la direction de chaque vague.
- La forme visible de chaque vague reste contenue dans sa zone de `192 x 112 px`.
- Une poussiere legere peut suivre les vagues sans masquer Imran ni modifier les collisions.
- Les fragments centraux se dissolvent en sable a la fin des `0.50 s`.
- Chaque vague s'effondre en sable et en petits debris sans danger lors de sa disparition.

### Signal sonore valide

- Un grondement de pierre commence au debut de la preparation.
- Son intensite augmente pendant les `0.65 s`.
- Un tintement dore accompagne l'illumination du coeur et des gravures.
- Un fort impact marque exactement le contact des deux mains avec le sol.
- Des craquements de gres accompagnent immediatement la chute des blocs.
- Deux roulements de sable commencent avec le depart des vagues.
- Leurs directions sonores correspondent aux deplacements vers la gauche et vers la droite.
- Le son des fragments centraux s'arrete a la fin des `0.50 s`.
- Chaque roulement s'arrete lorsque la vague correspondante disparait.

### Assets visuels et sonores a produire

- Animation du golem levant ses deux poings.
- Illumination progressive du coeur et des gravures.
- Animation des deux mains frappant simultanement le sol.
- Limites dorees de la zone ciblee.
- Fissures lumineuses progressives sur le sol.
- Ombres des blocs au-dessus de la zone.
- Blocs de ruines en gres ocre.
- Fragments graves et eclats dores.
- Zone centrale de sable et de debris.
- Vague de debris orientee vers la gauche.
- Vague de debris orientee vers la droite.
- Effets de poussiere legere et de disparition.
- Son de grondement de pierre progressif.
- Son de tintement dore.
- Son de fort impact des deux mains.
- Sons de chute et de craquement des blocs.
- Roulements directionnels des deux vagues.

## Arene

> **Statut :** Validee

- La zone de combat mesure `1280 px`, soit `20 grilles` de `64 px`.
- Le sol principal se trouve a `y = 896 px`.
- Le sol est unique et entierement plat.
- L'arene ne contient aucune plateforme, pente, fosse ni obstacle de deplacement.
- La camera reste fixe pendant la presentation, le combat, l'etat `Etourdi` et la defaite.
- La zone de recompense commence a la position locale `x = 1280 px`.
- Elle mesure `640 px`.
- Le centre du coffre se trouve a la position locale `x = 1824 px`.
- Les barrieres utilisent une energie doree et ambree semi-transparente.
- Des grains de sable et des fragments de gres circulent dans cette energie.
- Les positions horizontales locales sont mesurees depuis la limite interieure gauche de la zone de combat.
- Imran commence la presentation avec son centre horizontal a `x = 128 px`.
- Le Golem du Desert commence avec son centre horizontal a `x = 1024 px`.
- Le golem est tourne vers la gauche et fait face a Imran.
- La distance initiale entre leurs centres est de `896 px`.
- Il reste `256 px` entre le centre initial du golem et la limite droite de la zone de combat.
- Dans le cadre de reference, Imran apparait a `x = 448 px` dans l'ecran.
- Dans le cadre de reference, le golem apparait a `x = 1344 px` dans l'ecran.
- La portee de `1120 px` du Javelot de gres permet d'atteindre la zone initiale d'Imran.
- La portee de `1200 px` du Mur de sable permet egalement de traverser cette distance.

### Comportement du sol valide

- Le sol en gres ne modifie pas le deplacement d'Imran.
- La vitesse horizontale maximale reste `240 px/s`.
- L'acceleration au sol reste `1800 px/s2`.
- Le freinage au sol reste `2200 px/s2`.
- Le saut normal, le Double saut et le controle aerien conservent leurs valeurs communes.
- Le Dash conserve sa vitesse de `620 px/s`, sa duree de `0.20 s` et sa distance theorique de `124 px`.
- L'intervalle de `1.00 s` entre deux Dash reste inchange.
- Le sable visible ne ralentit pas Imran et ne provoque aucun enfoncement.
- Ces regles restent identiques dans la zone de combat et dans la zone de recompense.

### Direction visuelle de l'arene validee

- L'arene se trouve en plein air au milieu d'anciennes ruines du Desert.
- Le sol jouable utilise de grandes dalles de gres ocre entierement plates.
- Une facade monumentale se trouve derriere la position initiale du golem.
- Cette facade sert a sa presentation et reste en dehors des zones de collision jouables.
- Des dunes occupent l'arriere-plan le plus eloigne.
- Des colonnes brisees et des vestiges de murs apparaissent dans les plans intermediaires.
- Le ciel utilise une teinte bleu pale afin de detacher les silhouettes ocre et les signaux dores.
- La palette principale associe le gres ocre, le sable clair, l'ambre et des ombres brun rouge.
- Les contrastes conservent Imran, le golem, les projectiles et les zones annoncees clairement visibles.
- Les dunes, les colonnes et les vestiges restent purement decoratifs.
- Aucun element du decor ne cree une plateforme, une pente, une fosse ou un obstacle.
- Le meme sol en gres continue sans rupture dans la zone de recompense.
- Un vent leger transporte continuellement quelques grains de sable pendant la presentation, le combat et la sequence de recompense.
- La majorite des grains reste en arriere-plan.
- De rares particules passent au premier plan pour donner de la profondeur.
- Leur densite et leur opacite restent faibles.
- Les particules ne masquent jamais Imran, le golem, les dangers, les signaux d'attaque ou l'interface.
- Elles ne possedent aucune collision et ne modifient pas le deplacement.
- Le sable ambiant reste visuellement moins dense que celui du Mur de sable et du Piege des ruines.

## Direction visuelle du golem validee

- Le corps utilise de grands blocs de gres ocre aux formes arrondies.
- Du sable s'accumule entre certaines parties du corps.
- Des fragments d'anciennes ruines sont integres aux plaques de pierre.
- Des symboles geometriques originaux sont graves dans le gres.
- Une energie doree parcourt les fissures du corps.
- Les yeux emettent une lumiere ambree.
- Le coeur magique dore se trouve au centre du torse.
- La silhouette et les dimensions respectent les regles communes des six golems.
- Le sable, les gravures et les fragments de ruines restent decoratifs et n'agrandissent pas les zones de collision.

## Presentation du Golem du Desert

> **Statut :** Validee

### Deroulement visuel valide

- Avant le combat, le golem est integre a la facade d'une ancienne ruine.
- Le sable qui le recouvre dissimule sa silhouette.
- Il ne possede aucune zone dangereuse ou vulnerable pendant cet etat.
- La presentation commence lorsque Imran franchit le point d'entree de l'arene.
- Les commandes d'Imran sont bloquees pendant toute la presentation.
- La sequence dure exactement `3.00 s`.

| Periode | Animation |
|---|---|
| `0.00 a 1.00 s` | Le vent retire progressivement le sable qui dissimule la silhouette du golem. |
| `1.00 a 2.00 s` | Les gravures, les yeux et le coeur magique s'allument progressivement en dore et en ambre. |
| `2.00 a 3.00 s` | Le golem se detache de la facade, avance uniquement pour atteindre sa position fixe et prend sa posture de garde face a Imran. |

- Les deux barrieres dorees et ambrees montent silencieusement pendant les `0.50 s` du debut de la sequence.
- Le deplacement de liberation se termine exactement a la position locale `x = 1024 px`.
- Les fragments de gres et le sable produits par la facade restent uniquement visuels.
- Ils disparaissent avant la fin de la sequence.
- La barre de vie apparait lorsque la presentation atteint `3.00 s`.
- Le controle d'Imran revient au meme instant.
- Le golem devient vulnerable et son corps devient dangereux a cet instant.
- La preparation du Javelot de gres peut alors commencer.
- Une commande effectuee avant la fin des `3.00 s` reste ignoree.
- Une nouvelle tentative rejoue la sequence complete depuis l'etat integre a la facade.

### Signal sonore valide

- Un vent du desert commence au debut de la presentation.
- Un frottement de sable accompagne le degagement de la silhouette pendant la premiere seconde.
- Une resonance doree apparait avec l'allumage des gravures, des yeux et du coeur.
- Son intensite augmente progressivement entre `1.00 s` et `2.00 s`.
- Des craquements de gres accompagnent la liberation pendant la derniere seconde.
- Aucun cri ni aucun rugissement n'est joue.
- Les barrieres restent silencieuses.
- Tous les sons de presentation s'arretent lorsque la barre de vie apparait et que le controle revient.

### Assets visuels et sonores a produire

- Pose du golem integre a la facade et recouvert de sable.
- Animation du sable retire par le vent.
- Apparition progressive de la silhouette.
- Illumination des gravures, des yeux et du coeur.
- Animation du golem se detachant de la facade.
- Transition vers la position fixe et la posture de garde.
- Fragments de gres et sable sans danger.
- Son de vent du desert.
- Son de sable glissant sur la pierre.
- Resonance doree progressive.
- Craquements de gres pendant la liberation.

## Defaite du Golem du Desert

> **Statut :** Validee

### Deroulement visuel valide

- La sequence commence au contact du Smash Tranchant final avec le golem etourdi.
- Elle dure exactement `1.00 s`.
- La barre de vie disparait au debut de cette sequence.
- Le golem, ses fragments et ses particules ne possedent plus aucune zone dangereuse ou solide.

| Periode | Animation |
|---|---|
| `0.00 a 0.20 s` | Le coeur dore produit un dernier eclat, puis sa lumiere et celle des yeux et des gravures s'eteignent. |
| `0.20 a 0.70 s` | Le corps se desassemble en blocs de gres et en sable. |
| `0.70 a 1.00 s` | Les fragments deviennent des grains de sable et des particules dorees qui se dispersent et disparaissent. |

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

- Un bref eclat magique dore accompagne la derniere lumiere du coeur entre `0.00 s` et `0.20 s`.
- Des craquements de gres accompagnent le desassemblage entre `0.20 s` et `0.70 s`.
- Un souffle de sable accompagne la transformation des fragments en particules.
- Une resonance doree accompagne leur dispersion entre `0.70 s` et `1.00 s`.
- Le souffle et la resonance diminuent progressivement.
- Ils s'arretent avec la disparition des dernieres particules.
- Aucun son d'explosion violent n'est utilise.
- Le son d'ouverture du coffre reste distinct et commence uniquement apres une interaction valide.

### Assets visuels et sonores a produire

- Dernier eclat du coeur dore.
- Extinction du coeur, des yeux et des gravures.
- Desassemblage en blocs de gres et en sable.
- Transformation des fragments en grains de sable et particules dorees.
- Dispersion et disparition complete des particules.
- Son bref d'eclat magique dore.
- Craquements de gres pendant le desassemblage.
- Souffle de sable decroissant.
- Resonance doree decroissante.

## Recompense

> **Statut :** Validee

### Apparence du coffre validee

- Le coffre utilise une base en bois brun sombre.
- Des renforts en gres ocre et en bronze protegent ses angles, ses bords et son couvercle.
- Des symboles geometriques originaux sont graves dans les renforts.
- Une fine couche de sable repose sur le couvercle et dans certains angles.
- La serrure utilise une forme simple de cristal ambre.
- Le sable, les gravures et le cristal restent decoratifs et ne produisent aucun effet dangereux.
- Le coffre ne produit aucun rayon, aucune lumiere doree et aucun effet lumineux.
- Sa silhouette reste immediatement identifiable comme celle d'un coffre interactif.
- Son fonctionnement et son animation utilisent les regles communes des six coffres.

### Coffre, cle et transition valides

- Le coffre devient disponible a la fin de la sequence de defaite du golem.
- Imran doit se placer a `56 px` ou moins du coffre puis utiliser la commande `Interaction`.
- L'interaction lance la sequence commune de `2.00 s`.
- Le deplacement, le saut, le Dash et les attaques restent bloques pendant cette sequence.
- De `0.00 a 0.75 s`, le couvercle et son mecanisme s'ouvrent.
- De `0.75 a 1.50 s`, la quatrieme cle sort progressivement du coffre.
- De `1.50 a 2.00 s`, la cle reste visible au-dessus du coffre.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- La quatrieme cle est ajoutee automatiquement a la progression a la fin des `2.00 s`.
- Aucun nouveau pouvoir n'est debloque.
- La sauvegarde automatique commence immediatement apres l'ajout de la cle.
- Les coeurs et les vies sont restaures a `3`.
- Le niveau suivant devient le Volcan.
- Le coffre utilise le son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.
- Ce son commence avec l'interaction et accompagne toute la sequence de `2.00 s`.
- Aucun son supplementaire propre au bois, au gres, au bronze, au sable, au cristal ou a la quatrieme cle n'est ajoute.
- Le controle reste bloque apres la fin des `2.00 s`.
- Une fois la sauvegarde confirmee, un fondu au noir de `0.50 s` commence.
- La barriere gauche disparait pendant ce fondu avec le reste de l'arene.
- Le Volcan est charge pendant l'ecran noir.
- L'ecran reste noir tant que le Volcan n'est pas pret.
- Le Volcan apparait avec un fondu depuis le noir de `0.50 s`.
- Le controle revient lorsque ce niveau est entierement visible.
- Imran commence le Volcan avec `3 coeurs` et `3 vies`.

## Inventaire complementaire des assets

> **Statut :** Valide

Les assets propres a chaque attaque, a la presentation et a la defaite sont enumeres dans leurs sections respectives. Les elements complementaires suivants doivent egalement etre produits :

### Golem

- Silhouette principale du Golem du Desert.
- Pose neutre orientee vers la gauche.
- Pose neutre orientee vers la droite.
- Animation de retournement sur place.
- Animation de reaction a un impact valide sur la tete.
- Effet visuel d'impact sur la zone vulnerable.
- Animation de passage a l'etat `Etourdi`.
- Pose immobile de l'etat `Etourdi`.
- Etats eteint et allume du coeur dore, des yeux et des gravures.

### Arene

- Sol en dalles de gres raccordable sur toute la longueur de `1920 px`.
- Facade monumentale intacte, fissuree et liberee.
- Arriere-plan de dunes.
- Plan intermediaire de colonnes brisees et de vestiges.
- Ciel bleu pale.
- Systeme de grains de sable legers en arriere-plan.
- Systeme de rares particules au premier plan.
- Variante doree et ambree des deux barrieres communes.
- Particules de sable et fragments de gres pour les barrieres.
- Prolongement du decor dans la zone de recompense.

### Recompense

- Coffre du Desert ferme.
- Coffre du Desert pendant l'ouverture.
- Coffre du Desert ouvert.
- Bois brun sombre, renforts de gres ocre et de bronze, gravures et sable fin.
- Serrure en forme de cristal ambre.
- Apparition et elevation de la quatrieme cle selon l'animation commune.
- Son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.

## Criteres de validation

La fiche sera validee lorsque :

- toutes les attaques possederont des valeurs mesurables ;
- le Dash et le Double saut auront une utilite clairement definie ;
- toutes les attaques pourront etre evitees sans degat inevitable ;
- les signaux visuels resteront comprehensibles sans le son ;
- l'arene permettra d'utiliser toutes les actions requises ;
- la presentation, la defaite et la recompense seront entierement decrites ;
- les regles resteront compatibles avec les regles communes des golems.

## Sources

- [Golem du Desert du Concept Game](../../Concept-Game/08-Boss/Golem-du-Desert.md)
- [Desert oublie du Concept Game](../../Concept-Game/03-Univers/Desert-Oublie.md)
- [Regles communes des boss](Regles-Communes.md)
- [Golem du Lac gele](Golem-Lac.md)
- [Niveau 4 - Desert](../Niveaux/Niveau-4-Desert.md)
