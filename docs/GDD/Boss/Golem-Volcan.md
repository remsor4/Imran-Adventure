# Golem du Volcan

> **Statut :** Valide

## Objectif

Definir le cinquieme gardien comme un combat exigeant une execution plus precise des capacites deja apprises. Le joueur doit enchainer le Bouclier de lumiere, le saut, le Double saut et le Dash au sol face a des attaques volcaniques clairement annoncees.

## Role du combat

- Verifier l'observation rapide des preparations visuelles et sonores.
- Reutiliser la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.
- Exiger un enchainement volontaire du saut et du Double saut.
- Exiger une sequence combinant Dash au sol, saut et Double saut.
- Augmenter la pression sans introduire une seconde phase.
- Preparer le joueur au dernier golem du Chateau.

## Capacites requises validees

- Le Bouclier de lumiere constitue la reponse principale a la premiere attaque.
- Le saut normal puis le Double saut sont obligatoires pendant la deuxieme attaque.
- La troisieme attaque exige un Dash au sol suivi d'une sequence aerienne prolongee par le Double saut.
- Le Dash aerien reste impossible.
- Le Dash ne donne aucune invulnerabilite.
- Aucune attaque ne demande une capacite indisponible depuis le niveau 0.
- Le combat reste terminable avec le deplacement normal, le saut, le Double saut, le Dash au sol, la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.

## Structure du combat validee

- Le Golem du Volcan possede une seule phase.
- Il possede `20 PV`.
- Ses points de vie ne modifient ni son comportement, ni la vitesse de ses attaques, ni l'ordre de son cycle.
- La tete constitue sa zone vulnerable pendant le combat actif.
- Une attaque normale validee sur la tete retire `1 PV`.
- Un Smash Tranchant valide sur la tete retire `2 PV`.
- Chaque attaque du golem retire `1 coeur` a Imran.
- Le contact avec son corps utilise la zone dangereuse commune de `112 x 136 px`.
- Chaque attaque se termine par la recuperation commune de `0.30 s`.
- Une pause neutre de `1.80 s` suit cette recuperation.
- A `0 PV`, le golem entre dans l'etat `Etourdi`.
- Le Smash Tranchant final peut toucher n'importe quelle partie de son corps.
- Ce Smash final declenche la sequence commune de defaite.

## Structure du cycle validee

- Le Golem du Volcan possede exactement `3 attaques`.
- Les attaques utilisent un ordre fixe et previsible.
- La premiere attaque reste identique a chaque tentative.
- Apres la troisieme attaque, le cycle reprend depuis la premiere.
- Recevoir un degat ne modifie pas l'ordre du cycle.
- Les points de vie restants ne modifient ni l'ordre, ni les valeurs, ni le rythme.
- Une perte de vie d'Imran reinitialise le cycle sur la premiere attaque.
- Le cycle utilise toujours l'ordre suivant :

| Ordre | Attaque | Fonction principale |
|---:|---|---|
| 1 | Orbe de magma frontal | Bloquer un projectile rapide avec le Bouclier de lumiere |
| 2 | Double vague de lave | Enchainer saut normal et Double saut |
| 3 | Eruption volcanique ciblee | Enchainer Dash au sol, saut et Double saut |

- L'Orbe de magma frontal constitue une entree de cycle rapide mais simple a lire.
- La Double vague de lave verifie les deux impulsions aeriennes.
- L'Eruption volcanique ciblee constitue l'attaque la plus exigeante du cycle.
- Apres l'Eruption volcanique ciblee, le cycle reprend avec l'Orbe de magma frontal.

## Deplacement du golem valide

- Le Golem du Volcan reste a la position horizontale locale `x = 1024 px` pendant tout le combat.
- Il ne marche pas vers Imran.
- Ses attaques, les degats recus et les collisions ne modifient pas cette position.
- Il ne se deplace pas pendant les recuperations de `0.30 s` ni pendant les pauses neutres de `1.80 s`.
- Au debut de chaque preparation, il se tourne sur place vers la position actuelle d'Imran.
- Cette orientation determine la direction verrouillee des attaques mobiles.
- Il ne change plus d'orientation pendant la preparation ni pendant l'execution de l'attaque.
- Le ciblage de l'Eruption volcanique ciblee depend de la position d'Imran et non de l'orientation visuelle du golem.
- Dans l'etat `Etourdi`, il conserve sa position et son orientation.

## Attaque 1 - Orbe de magma frontal

> **Statut :** Validee

### Structure validee

- Le golem lance une unique orbe de magma.
- La preparation avant le lancement dure exactement `0.50 s`.
- Sa zone dangereuse mesure exactement `64 x 64 px`.
- Sa vitesse horizontale constante est de `600 px/s`.
- Son centre se trouve a `48 px` au-dessus du sol.
- Sa zone verticale couvre donc la hauteur comprise entre `16 px` et `80 px`.
- Le saut normal de `89 px` conserve une marge verticale de `9 px`.
- Sa duree de vie maximale est de `1.90 s`.
- Sa portee maximale est donc de `1140 px`.
- La forme visuelle couvre la zone dangereuse sans creer de danger invisible.
- L'orbe se deplace horizontalement en ligne droite.
- La direction est verrouillee au debut de la preparation.
- Le projectile ne suit pas Imran apres son lancement.
- Le Bouclier de lumiere bloque automatiquement l'orbe lorsqu'Imran lui fait face.
- L'orbe bloquee se brise et disparait immediatement.
- Imran peut egalement la franchir avec un saut normal bien place.
- L'orbe retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ce projectile et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- Le projectile disparait apres une collision valide ou a la fin de sa duree de vie.
- La recuperation commune de `0.30 s` commence apres sa disparition.

### Signal visuel valide

- Au debut de la preparation, le golem se tourne vers Imran et verrouille cette direction.
- Il rapproche une main de son coeur incandescent.
- Une energie rouge-orange se propage du coeur jusque dans sa paume.
- Du magma et de petits fragments de basalte se condensent dans sa main.
- L'orbe atteint sa taille complete pendant les `0.50 s`.
- Le bras recule legerement avant le lancer.
- Un bref eclat orange marque la fin de la preparation.
- Le golem projette alors son bras vers Imran.
- L'orbe devient dangereuse uniquement lorsqu'elle quitte sa main.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence du projectile validee

- L'orbe utilise une coque irreguliere de basalte noir.
- Des fissures rouge-orange revelent le magma incandescent contenu a l'interieur.
- Un coeur lumineux facilite la lecture de sa rotation.
- Une courte trainee de braises et de fumee legere suit son trajet.
- La trainee reste purement visuelle et n'agrandit pas la zone dangereuse.
- Lors de sa disparition, l'orbe se brise en fragments de roche refroidie et en braises sans danger.

### Signal sonore valide

- Un bouillonnement de magma commence au debut de la preparation.
- Des craquements de roche accompagnent la formation de la coque.
- Un claquement volcanique sec marque exactement le lancement.
- Un leger sifflement chaud accompagne le trajet.
- La collision avec Imran, le bouclier ou une limite produit un bref melange de roche brisee et de magma eteint.

### Assets visuels et sonores a produire

- Animation de la main rapprochee du coeur.
- Propagation de l'energie du coeur vers la paume.
- Formation progressive de l'orbe.
- Animation du bras recule puis du lancer.
- Orbe en basalte fissuree par le magma.
- Effet de trainee de braises et de fumee.
- Effet de fragmentation sans danger.
- Son de bouillonnement de magma.
- Son de craquements pendant la formation.
- Son de claquement au lancement.
- Son de sifflement pendant le trajet.
- Son bref de collision et de refroidissement.

## Attaque 2 - Double vague de lave

> **Statut :** Validee

### Structure validee

- Le golem produit deux vagues de lave successives dans la meme direction.
- La preparation avant le depart de la premiere vague dure exactement `0.70 s`.
- La direction horizontale est verrouillee au debut de cette preparation.
- Les vagues ne suivent pas Imran apres leur depart.
- La premiere vague part au terme des `0.70 s`.
- La seconde part exactement `0.35 s` apres la premiere.
- Les deux vagues restent en contact avec le sol.
- La premiere vague possede une zone dangereuse de `128 x 56 px`.
- Le saut normal de `89 px` conserve `33 px` de marge au-dessus de cette premiere vague.
- La seconde vague possede une zone dangereuse de `160 x 112 px`.
- Le saut normal reste inferieur de `23 px` au sommet de la seconde vague.
- Un saut normal complet suivi d'un Double saut peut atteindre environ `167 px`.
- Cette combinaison conserve donc une marge verticale maximale d'environ `55 px`.
- Chaque vague se deplace a une vitesse horizontale constante de `520 px/s`.
- La duree de vie maximale de chaque vague est de `2.20 s`.
- La portee maximale de chaque vague est donc de `1144 px`.
- La forme visible de chaque vague couvre sa zone sans creer de danger invisible.
- Le Bouclier de lumiere ne protege pas contre les vagues.
- Le Dash ne rend pas Imran invulnerable a leur contact.
- Imran utilise le saut normal pour la premiere vague.
- Il utilise ensuite son Double saut pour franchir la seconde vague plus haute.
- Chaque vague retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche les deux vagues de retirer plusieurs coeurs pendant la meme periode.
- Chaque vague disparait lorsqu'elle atteint une barriere ou la fin de sa duree de vie.
- La recuperation commune de `0.30 s` commence apres la disparition de la derniere vague.

### Signal visuel valide

- Au debut de la preparation, le golem se tourne vers Imran et verrouille cette direction.
- Il abaisse ses deux poings de chaque cote de son corps.
- Le premier poing se couvre de magma orange.
- Le second accumule davantage de magma et produit une lumiere plus intense.
- Au terme des `0.70 s`, le premier poing frappe le sol et produit la vague basse.
- Le second poing reste leve et continue de briller.
- Apres `0.35 s`, le second poing frappe le sol et produit la vague haute.
- La difference de taille et de lumiere entre les deux poings annonce clairement la hauteur des vagues.
- Chaque vague devient dangereuse uniquement lorsqu'elle quitte le point d'impact.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence des vagues validee

- La premiere vague forme une crete de lave orange entouree de petits morceaux de basalte.
- La seconde vague utilise une crete plus haute et une masse de magma plus importante.
- Des fissures jaunes et orange parcourent les fragments de roche.
- Une courte trainee de braises suit chaque vague.
- La fumee reste legere et ne masque jamais les zones dangereuses.
- Les braises et la fumee n'agrandissent pas les collisions.
- Chaque vague se refroidit en fragments de basalte puis disparait sans danger.

### Signal sonore valide

- Un grondement de magma commence lorsque les deux poings s'abaissent.
- Deux intensites sonores distinctes accompagnent leur charge.
- Un premier impact grave marque le depart de la vague basse.
- Un second impact plus puissant retentit `0.35 s` plus tard.
- Un roulement de lave accompagne chaque trajet.
- Le roulement le plus grave correspond a la seconde vague.
- Chaque disparition produit un bref son de basalte refroidi et brise.

### Assets visuels et sonores a produire

- Animation des deux poings abaisses.
- Charge de magma differente sur chaque poing.
- Animation du premier poing frappant le sol.
- Animation du second poing frappant le sol.
- Vague basse de `128 x 56 px`.
- Vague haute de `160 x 112 px`.
- Fragments de basalte fissures.
- Trainees de braises et de fumee legere.
- Effets de refroidissement et de disparition.
- Son de grondement pendant la charge.
- Premier impact grave.
- Second impact plus puissant.
- Roulements distincts des deux vagues.
- Sons brefs de refroidissement et de fragmentation.

## Attaque 3 - Eruption volcanique ciblee

> **Statut :** Validee

### Structure validee

- L'attaque combine une zone centrale ciblee et une impulsion dangereuse sur tout le sol.
- La zone centrale mesure exactement `416 px` de largeur.
- La preparation avant l'activation dure exactement `0.70 s`.
- Son centre horizontal correspond a la position d'Imran au debut de la preparation.
- Cette position est verrouillee pendant toute l'attaque.
- La zone ne suit pas Imran apres le debut de la preparation.
- La zone centrale reste sans danger pendant toute la preparation.
- Depuis le centre, la zone vulnerable de `32 px` d'Imran doit parcourir `224 px` pour sortir completement.
- En `0.70 s`, un deplacement normal a pleine vitesse ne peut parcourir que `168 px`.
- Le deplacement normal reste donc inferieur de `56 px` a la distance de sortie.
- Un Dash de `124 px` laisse ensuite `0.50 s` de mouvement.
- A `240 px/s`, ce mouvement permet de parcourir `120 px` supplementaires.
- La sequence peut donc couvrir environ `244 px` et conserve une marge horizontale d'environ `20 px`.
- Le Dash doit commencer au sol et sa direction reste verrouillee.
- Si la zone depasse une barriere, seule sa partie situee dans l'arene reste active et visible.
- Le centre verrouille n'est jamais decale.
- Imran doit alors sortir vers l'interieur de l'arene et la distance maximale reste `224 px`.
- Au terme des `0.70 s`, une eruption verticale remplit toute la hauteur jouable de la zone centrale.
- Cette eruption reste dangereuse pendant exactement `0.50 s`.
- Au meme instant, une impulsion volcanique rend tout le sol de l'arene dangereux sur une hauteur de `48 px`.
- Cette impulsion reste active pendant exactement `0.80 s`.
- La duree totale du saut normal est d'environ `0.71 s`.
- Le saut normal seul ne permet donc pas de rester en l'air pendant toute l'impulsion.
- Imran doit sauter apres son Dash puis utiliser son Double saut pour prolonger sa periode aerienne.
- Le Bouclier de lumiere ne protege ni contre l'eruption, ni contre l'impulsion du sol.
- Le Dash ne rend pas Imran invulnerable a ces dangers.
- L'eruption centrale et l'impulsion du sol retirent `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ces deux dangers de retirer plusieurs coeurs pendant la meme periode.
- Aucun danger ne constitue un obstacle solide ou une plateforme.
- L'eruption centrale disparait a la fin des `0.50 s`.
- Le sol redevient entierement sur a la fin des `0.80 s`.
- Aucun magma dangereux ne persiste apres cette disparition.
- La recuperation commune de `0.30 s` commence lorsque l'impulsion du sol disparait.

### Signal visuel valide

- Deux limites rouge-orange apparaissent aux bords exacts de la zone centrale.
- Des fissures de magma se propagent dans le sol entre ces limites pendant les `0.70 s`.
- Une lueur rouge discrete parcourt egalement tout le sol de l'arene.
- Cette lueur annonce l'impulsion globale mais reste sans danger pendant la preparation.
- La zone centrale et la lueur du sol deviennent progressivement plus intenses.
- A l'activation, les deux limites produisent un bref eclat.
- Une colonne de magma et de fragments de basalte remplit la zone centrale.
- Une onde lumineuse se propage instantanement sur toute la surface du sol.
- Pendant les `0.80 s`, les fissures du sol brillent fortement et produisent de petites flammes contenues sous `48 px`.
- La colonne centrale reste suffisamment transparente pour conserver les limites visibles.
- Les flammes, les braises et la chaleur visible ne masquent jamais Imran.
- La colonne disparait a `0.50 s`.
- Les fissures refroidissent et s'eteignent completement a `0.80 s`.
- Le signal reste comprehensible lorsque le son est coupe.

### Animation du golem validee

- Au debut de la preparation, le golem se tourne vers Imran.
- Il rapproche ses deux mains de son coeur incandescent.
- La lumiere du coeur et des fissures augmente progressivement.
- Il ecarte lentement les deux bras pendant que les signaux apparaissent au sol.
- Au terme des `0.70 s`, il ouvre brusquement les bras a leur extension maximale.
- Ce mouvement declenche exactement la colonne centrale et l'impulsion du sol.
- Le golem ne se deplace pas horizontalement pendant cette animation.
- Cette posture reste distincte des deux frappes au sol de la Double vague de lave.

### Apparence des dangers validee

- La colonne centrale melange magma rouge-orange, fragments de basalte noir et braises.
- Les fragments restent contenus dans la zone de `416 px`.
- L'impulsion du sol utilise des fissures orange et jaunes sur les dalles de basalte.
- De petites flammes rouges restent contenues sous la hauteur dangereuse de `48 px`.
- Une chaleur visible deforme legerement l'air sans masquer les silhouettes.
- Les braises, la fumee et la chaleur restent purement visuelles.
- Aucune fissure ni aucun fragment ne modifie la collision du sol.
- Tous les effets refroidissent en roche sombre avant de disparaitre.

### Signal sonore valide

- Une pression de magma grave commence au debut de la preparation.
- Un battement incandescent accompagne la lumiere du coeur.
- Des craquements parcourent progressivement le sol.
- Un puissant souffle volcanique marque l'ouverture brusque des bras.
- Un grondement vertical accompagne la colonne centrale pendant `0.50 s`.
- Un crepitement grave accompagne l'impulsion du sol pendant `0.80 s`.
- Le grondement de la colonne s'arrete avec sa disparition.
- Le crepitement diminue puis s'arrete lorsque le sol redevient sur.

### Assets visuels et sonores a produire

- Animation des mains rapprochees du coeur.
- Illumination progressive du coeur et des fissures.
- Animation des bras qui s'ecartent lentement puis brusquement.
- Limites rouge-orange de la zone centrale.
- Fissures de magma progressives dans la zone.
- Lueur d'avertissement sur tout le sol.
- Colonne de magma et fragments de basalte.
- Onde lumineuse d'activation.
- Fissures et petites flammes de l'impulsion du sol.
- Effets de braises, de fumee et de chaleur.
- Refroidissement complet du sol.
- Son de pression de magma.
- Battement incandescent du coeur.
- Craquements progressifs du sol.
- Souffle volcanique d'activation.
- Grondement de la colonne.
- Crepitement de l'impulsion du sol.

## Arene

> **Statut :** Validee

### Structure validee

- La zone de combat mesure exactement `1280 px`, soit `20 grilles` de `64 px`.
- Le sol principal se trouve a `y = 896 px`.
- Le sol est unique et entierement plat.
- L'arene ne contient aucune plateforme, pente, fosse ni obstacle de deplacement.
- La camera reste fixe pendant la presentation, le combat, l'etat `Etourdi` et la defaite.
- La zone de recompense commence a la position locale `x = 1280 px`.
- Elle mesure exactement `640 px`.
- La longueur totale accessible atteint `1920 px`.
- Le centre du coffre se trouve a la position locale `x = 1824 px`.
- Les barrieres utilisent une energie rouge-orange semi-transparente.
- Des braises et des fragments de basalte circulent dans cette energie.
- Les positions horizontales locales sont mesurees depuis la limite interieure gauche de la zone de combat.
- Imran commence la presentation avec son centre horizontal a `x = 128 px`.
- Le Golem du Volcan commence avec son centre horizontal a `x = 1024 px`.
- Le golem est tourne vers la gauche et fait face a Imran.
- La distance initiale entre leurs centres est de `896 px`.
- Il reste `256 px` entre le centre initial du golem et la limite droite de la zone de combat.
- Dans le cadre de reference, Imran apparait a `x = 448 px` dans l'ecran.
- Dans le cadre de reference, le golem apparait a `x = 1344 px` dans l'ecran.
- Les portees des attaques mobiles permettent d'atteindre la zone initiale d'Imran.

### Comportement du sol valide

- Le sol en basalte ne modifie pas le deplacement d'Imran lorsqu'aucune attaque ne l'affecte.
- La vitesse horizontale maximale reste `240 px/s`.
- L'acceleration au sol reste `1800 px/s2`.
- Le freinage au sol reste `2200 px/s2`.
- Le saut normal, le Double saut et le controle aerien conservent leurs valeurs communes.
- Le Dash conserve sa vitesse de `620 px/s`, sa duree de `0.20 s` et sa distance theorique de `124 px`.
- L'intervalle de `1.00 s` entre deux Dash reste inchange.
- La chaleur ambiante ne ralentit pas Imran et ne retire aucun coeur.
- Ces regles restent identiques dans la zone de combat et dans la zone de recompense.

### Direction visuelle de l'arene validee

- L'arene se trouve en plein air dans une ancienne caldeira volcanique.
- Le sol jouable utilise de grandes dalles de basalte noir entierement plates.
- Une paroi de lave refroidie se trouve derriere la position initiale du golem.
- Cette paroi sert a sa presentation et reste hors des collisions jouables.
- Des coulees de lave apparaissent dans l'arriere-plan sans rejoindre la surface jouable.
- Des formations d'obsidienne et des rochers volcaniques occupent les plans intermediaires.
- Un ciel rouge sombre et un panache de fumee completent l'arriere-plan.
- La palette associe le noir du basalte, le gris de la cendre, le rouge-orange du magma et quelques jaunes incandescents.
- Les contours clairs et les variations de luminosite conservent Imran et les signaux dangereux lisibles.
- Les coulees, l'obsidienne, les rochers et la fumee restent purement decoratifs.
- Aucun element du decor ne cree une plateforme, une pente, une fosse ou un obstacle.
- Le meme sol en basalte continue sans rupture dans la zone de recompense.
- Quelques braises circulent continuellement en arriere-plan.
- De rares braises passent au premier plan avec une faible opacite.
- Elles ne masquent jamais Imran, le golem, les dangers ou l'interface.
- Elles ne possedent aucune collision et restent moins denses que les effets des attaques.

## Direction visuelle du golem validee

- Le corps utilise de grands blocs de basalte noir aux formes arrondies.
- Quelques plaques d'obsidienne brillantes renforcent les epaules, les avant-bras et le dos.
- Des fissures remplies de magma incandescent parcourent le corps.
- Les yeux emettent une lumiere rouge-orange.
- Le coeur magique incandescent reste entoure de roche refroidie au centre du torse.
- Une legere chaleur visible deforme l'air autour de certaines parties du corps.
- Le golem ne produit aucune flamme excessive pendant sa pose neutre.
- La silhouette et les dimensions respectent les regles communes des six golems.
- Les plaques, les fissures, les braises et la chaleur restent decoratives et n'agrandissent pas les zones de collision.

## Presentation du Golem du Volcan

> **Statut :** Validee

### Deroulement visuel valide

- Avant le combat, le golem est confondu avec une ancienne coulee de lave refroidie contre la paroi.
- Il ne possede aucune zone dangereuse ou vulnerable pendant cet etat.
- La presentation commence lorsque Imran franchit le point d'entree de l'arene.
- Les commandes d'Imran sont bloquees pendant toute la presentation.
- La sequence dure exactement `3.00 s`.

| Periode | Animation |
|---|---|
| `0.00 a 1.00 s` | Le coeur commence a briller comme une braise et la roche refroidie autour de lui tremble. |
| `1.00 a 2.00 s` | Les fissures et les yeux s'allument, tandis que de petits fragments de basalte se detachent. |
| `2.00 a 3.00 s` | Le golem se libere de la paroi, atteint sa position fixe et prend sa posture de garde face a Imran. |

- Les deux barrieres rouge-orange montent silencieusement pendant les `0.50 s` du debut de la sequence.
- Le deplacement de liberation se termine exactement a la position locale `x = 1024 px`.
- Les fragments et les braises de la paroi restent uniquement visuels.
- Ils disparaissent avant la fin de la sequence.
- La barre de vie apparait lorsque la presentation atteint `3.00 s`.
- Le controle d'Imran revient au meme instant.
- Le golem devient vulnerable et son corps devient dangereux a cet instant.
- La preparation de l'Orbe de magma frontal peut alors commencer.
- Une commande effectuee avant la fin des `3.00 s` reste ignoree.
- Une nouvelle tentative rejoue la sequence complete depuis l'etat integre a la paroi.

### Signal sonore valide

- Un grondement volcanique profond commence au debut de la presentation.
- Un bouillonnement discret accompagne l'allumage du coeur.
- Le grondement et le bouillonnement augmentent pendant l'allumage des fissures et des yeux.
- Des craquements de basalte accompagnent la liberation pendant la derniere seconde.
- Aucun cri ni aucun rugissement n'est joue.
- Les barrieres restent silencieuses.
- Tous les sons de presentation s'arretent lorsque la barre de vie apparait et que le controle revient.

### Assets visuels et sonores a produire

- Pose du golem integre a la coulee refroidie.
- Animation du coeur qui s'allume comme une braise.
- Tremblement de la roche refroidie.
- Illumination progressive des fissures et des yeux.
- Detachement de petits fragments de basalte.
- Animation du golem se liberant de la paroi.
- Transition vers la position fixe et la posture de garde.
- Son de grondement volcanique.
- Son de bouillonnement progressif.
- Craquements de basalte pendant la liberation.

## Defaite du Golem du Volcan

> **Statut :** Validee

### Deroulement visuel valide

- La sequence commence au contact du Smash Tranchant final avec le golem etourdi.
- Elle dure exactement `1.00 s`.
- La barre de vie disparait au debut de cette sequence.
- Le golem, ses fragments et ses particules ne possedent plus aucune zone dangereuse ou solide.

| Periode | Animation |
|---|---|
| `0.00 a 0.20 s` | Le coeur produit un dernier eclat, puis le magma des yeux et des fissures s'eteint. |
| `0.20 a 0.70 s` | Le corps refroidit et se desassemble en blocs de basalte et en morceaux d'obsidienne. |
| `0.70 a 1.00 s` | Les fragments deviennent des braises sombres et des particules de cendre qui se dispersent et disparaissent. |

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

- Un bref eclat incandescent accompagne la derniere lumiere du coeur entre `0.00 s` et `0.20 s`.
- Un souffle de refroidissement accompagne l'extinction du magma.
- Des craquements de basalte et d'obsidienne accompagnent le desassemblage entre `0.20 s` et `0.70 s`.
- Un crepitement de braises accompagne la transformation en particules.
- Un souffle de cendre accompagne leur dispersion entre `0.70 s` et `1.00 s`.
- Le crepitement et le souffle diminuent progressivement.
- Ils s'arretent avec les dernieres particules.
- Aucun son d'explosion violent n'est utilise.

### Assets visuels et sonores a produire

- Dernier eclat du coeur incandescent.
- Extinction du coeur, des yeux et des fissures.
- Refroidissement visible du corps.
- Desassemblage en blocs de basalte et morceaux d'obsidienne.
- Transformation en braises sombres et particules de cendre.
- Dispersion et disparition complete des particules.
- Son bref d'eclat incandescent.
- Son de refroidissement du magma.
- Craquements de basalte et d'obsidienne.
- Crepitement de braises decroissant.
- Souffle de cendre decroissant.

## Recompense

> **Statut :** Validee

### Apparence du coffre validee

- Le coffre utilise une base en bois noirci.
- Des renforts en basalte et en metal sombre protegent ses angles, ses bords et son couvercle.
- De petits fragments d'obsidienne decorent les quatre angles.
- Des fissures rouge-orange peintes ou gravees rappellent le magma sans emettre de lumiere.
- Une fine couche de cendre repose sur le couvercle.
- La serrure utilise une forme simple de cristal rouge-orange.
- Les fissures, l'obsidienne, la cendre et le cristal restent decoratifs.
- Le coffre ne produit aucun rayon, aucune lumiere doree et aucun effet lumineux.
- Sa silhouette reste immediatement identifiable comme celle d'un coffre interactif.
- Son fonctionnement et son animation utilisent les regles communes des six coffres.

### Coffre, cle et transition valides

- Le coffre devient disponible a la fin de la sequence de defaite du golem.
- Imran doit se placer a `56 px` ou moins du coffre puis utiliser la commande `Interaction`.
- L'interaction lance la sequence commune de `2.00 s`.
- Le deplacement, le saut, le Dash et les attaques restent bloques pendant cette sequence.
- De `0.00 a 0.75 s`, le couvercle et son mecanisme s'ouvrent.
- De `0.75 a 1.50 s`, la cinquieme cle sort progressivement du coffre.
- De `1.50 a 2.00 s`, la cle reste visible au-dessus du coffre.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- La cinquieme cle est ajoutee automatiquement a la progression a la fin des `2.00 s`.
- Aucun nouveau pouvoir n'est debloque.
- La sauvegarde automatique commence immediatement apres l'ajout de la cle.
- Les coeurs et les vies sont restaures a `3`.
- Le niveau suivant devient le Chateau de Tata Lisa.
- Le coffre utilise le son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.
- Ce son commence avec l'interaction et accompagne toute la sequence de `2.00 s`.
- Aucun son supplementaire propre au bois, au basalte, au metal, a l'obsidienne, a la cendre, au cristal ou a la cinquieme cle n'est ajoute.
- Le controle reste bloque apres la fin des `2.00 s`.
- Une fois la sauvegarde confirmee, un fondu au noir de `0.50 s` commence.
- La barriere gauche disparait pendant ce fondu avec le reste de l'arene.
- Le Chateau de Tata Lisa est charge pendant l'ecran noir.
- L'ecran reste noir tant que le Chateau de Tata Lisa n'est pas pret.
- Le Chateau de Tata Lisa apparait avec un fondu depuis le noir de `0.50 s`.
- Le controle revient lorsque ce niveau est entierement visible.
- Imran commence le Chateau de Tata Lisa avec `3 coeurs` et `3 vies`.

## Inventaire complementaire des assets

> **Statut :** Valide

Les assets propres a chaque attaque, a la presentation et a la defaite sont enumeres dans leurs sections respectives. Les elements complementaires suivants doivent egalement etre produits :

### Golem

- Silhouette principale du Golem du Volcan.
- Pose neutre orientee vers la gauche.
- Pose neutre orientee vers la droite.
- Animation de retournement sur place.
- Animation de reaction a un impact valide sur la tete.
- Effet visuel d'impact sur la zone vulnerable.
- Animation de passage a l'etat `Etourdi`.
- Pose immobile de l'etat `Etourdi`.
- Etats eteint et allume du coeur, des yeux et des fissures.

### Arene

- Sol en dalles de basalte raccordable sur toute la longueur de `1920 px`.
- Paroi de lave refroidie intacte, fissuree et liberee.
- Arriere-plan de coulees de lave et de caldeira.
- Formations d'obsidienne et rochers volcaniques.
- Ciel rouge sombre et panache de fumee.
- Systeme de braises legeres en arriere-plan.
- Systeme de rares braises au premier plan.
- Variante rouge-orange des deux barrieres communes.
- Particules de braises et fragments de basalte pour les barrieres.
- Prolongement du decor dans la zone de recompense.

### Recompense

- Coffre du Volcan ferme.
- Coffre du Volcan pendant l'ouverture.
- Coffre du Volcan ouvert.
- Bois noirci, renforts de basalte et de metal sombre, obsidienne et cendre.
- Fissures gravees sans lumiere et serrure en cristal rouge-orange.
- Apparition et elevation de la cinquieme cle selon l'animation commune.
- Son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.

## Criteres de validation

La fiche sera validee lorsque :

- les trois attaques possederont des valeurs mesurables et compatibles ;
- les signaux visuels resteront comprehensibles sans le son ;
- l'Orbe de magma pourra etre bloquee ou evitee ;
- la Double vague exigera le saut puis le Double saut ;
- l'Eruption ciblee exigera le Dash au sol puis le Double saut ;
- aucune attaque ne produira de degat inevitable ;
- l'arene restera plate, lisible et sans danger permanent ;
- la presentation, la defaite et la recompense respecteront les regles communes ;
- tous les assets necessaires seront identifies.

## Sources

- [Golem du Volcan du Concept Game](../../Concept-Game/08-Boss/Golem-du-Volcan.md)
- [Volcan du Concept Game](../../Concept-Game/03-Univers/Volcan.md)
- [Regles communes des boss](Regles-Communes.md)
- [Golem du Desert](Golem-Desert.md)
- [Niveau 5 - Volcan](../Niveaux/Niveau-5-Volcan.md)
