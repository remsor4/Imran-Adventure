# Golem du Chateau

> **Statut :** Valide

## Objectif

Definir le sixieme et dernier golem comme l'epreuve finale des capacites d'Imran avant Tata Lisa. Le combat doit verifier le Bouclier de lumiere, le saut, le Double saut et le Dash au sol sans introduire de nouvelle mecanique difficile a reutiliser.

## Role du combat

- Conclure la progression des six golems.
- Verifier une derniere fois la lecture des preparations visuelles et sonores.
- Reutiliser la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.
- Exiger le saut normal puis le Double saut dans une meme attaque.
- Exiger un Dash au sol suivi d'un saut et d'un Double saut.
- Donner a la grande epee une place centrale dans les trois attaques.
- Preparer le joueur au combat final contre Tata Lisa.

## Capacites requises validees

- Le Bouclier de lumiere constitue la reponse principale a la premiere attaque.
- Le Double saut constitue l'alternative au bouclier pour cette premiere attaque.
- Le saut normal puis le Double saut sont obligatoires pendant la deuxieme attaque.
- La troisieme attaque exige un Dash au sol suivi d'une sequence aerienne prolongee par le Double saut.
- Le Dash aerien reste impossible.
- Le Dash ne donne aucune invulnerabilite.
- Aucune attaque ne demande une capacite indisponible depuis le niveau 0.
- Le combat reste terminable avec le deplacement normal, le saut, le Double saut, le Dash au sol, la Shadow Sword, le Smash Tranchant et le Bouclier de lumiere.

## Structure du combat validee

- Le Golem du Chateau possede une seule phase.
- Il possede `22 PV`.
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

- Le Golem du Chateau possede exactement `3 attaques`.
- Les attaques utilisent un ordre fixe et previsible.
- La premiere attaque reste identique a chaque tentative.
- Apres la troisieme attaque, le cycle reprend depuis la premiere.
- Recevoir un degat ne modifie pas l'ordre du cycle.
- Les points de vie restants ne modifient ni l'ordre, ni les valeurs, ni le rythme.
- Une perte de vie d'Imran reinitialise le cycle sur la premiere attaque.
- Le cycle utilise toujours l'ordre suivant :

| Ordre | Attaque | Fonction principale |
|---:|---|---|
| 1 | Croissant violet | Bloquer un projectile avec le Bouclier de lumiere ou utiliser le Double saut |
| 2 | Double entaille au sol | Enchainer saut normal et Double saut |
| 3 | Sceau de la lame | Enchainer Dash au sol, saut et Double saut |

- Le Croissant violet constitue une entree de cycle directe et simple a lire.
- La Double entaille au sol verifie les deux impulsions aeriennes.
- Le Sceau de la lame constitue l'attaque la plus exigeante du cycle.
- Apres le Sceau de la lame, le cycle reprend avec le Croissant violet.

## Deplacement du golem valide

- Le Golem du Chateau reste a la position horizontale locale `x = 1024 px` pendant tout le combat.
- Il ne marche pas vers Imran.
- Ses attaques, les degats recus et les collisions ne modifient pas cette position.
- Il ne se deplace pas pendant les recuperations de `0.30 s` ni pendant les pauses neutres de `1.80 s`.
- Au debut de chaque preparation, il se tourne sur place vers la position actuelle d'Imran.
- Cette orientation determine la direction verrouillee des attaques mobiles.
- Il ne change plus d'orientation pendant la preparation ni pendant l'execution de l'attaque.
- Le ciblage du Sceau de la lame depend de la position d'Imran et non de l'orientation visuelle du golem.
- Dans l'etat `Etourdi`, il conserve sa position et son orientation.

## Attaque 1 - Croissant violet

> **Statut :** Validee

### Structure validee

- Le golem projette un unique croissant d'energie avec son epee.
- La preparation avant le lancement dure exactement `0.50 s`.
- Sa zone dangereuse mesure exactement `80 x 96 px`.
- Sa vitesse horizontale constante est de `620 px/s`.
- Son centre se trouve a `64 px` au-dessus du sol.
- Sa zone verticale couvre donc la hauteur comprise entre `16 px` et `112 px`.
- Le saut normal de `89 px` reste inferieur de `23 px` au sommet du croissant.
- Un saut normal complet suivi d'un Double saut peut atteindre environ `167 px`.
- Cette combinaison conserve donc une marge verticale maximale d'environ `55 px`.
- Sa duree de vie maximale est de `1.85 s`.
- Sa portee maximale est donc de `1147 px`.
- La forme visuelle couvre la zone dangereuse sans creer de danger invisible.
- Le croissant se deplace horizontalement en ligne droite.
- La direction est verrouillee au debut de la preparation.
- Le projectile ne suit pas Imran apres son lancement.
- Le Bouclier de lumiere bloque automatiquement le croissant lorsqu'Imran lui fait face.
- Le croissant bloque se fragmente et disparait immediatement.
- Imran peut egalement le franchir avec un Double saut.
- Un saut normal seul ne permet pas de passer au-dessus.
- Le croissant retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ce projectile et un autre danger de retirer plusieurs coeurs pendant la meme periode.
- Le projectile disparait apres une collision valide ou a la fin de sa duree de vie.
- La recuperation commune de `0.30 s` commence apres sa disparition.

### Signal visuel valide

- Au debut de la preparation, le golem se tourne vers Imran et verrouille cette direction.
- Il place son epee au-dessus de son epaule opposee.
- La ligne violette de la lame s'allume progressivement.
- Son coeur produit une impulsion qui se propage jusque dans l'epee.
- Une forme de croissant se dessine le long du tranchant.
- La lueur atteint sa pleine intensite pendant les `0.50 s`.
- Un bref eclat violet marque la fin de la preparation.
- Le golem effectue alors une entaille horizontale vers Imran.
- Le croissant devient dangereux uniquement lorsqu'il quitte la lame.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence du projectile validee

- Le croissant utilise une energie violette entouree d'un contour clair.
- De petits fragments d'obsidienne tournent autour de sa partie centrale.
- Une courte trainee violette suit son trajet.
- Quelques etincelles metalliques rappellent la grande epee.
- La trainee, les fragments et les etincelles restent purement visuels.
- Aucun effet ne depasse la zone dangereuse de `80 x 96 px`.
- Lors de sa disparition, le croissant se brise en fragments violets et noirs sans danger.

### Signal sonore valide

- Une resonance magique sombre commence au debut de la preparation.
- Un frottement de metal et d'obsidienne accompagne la montee de l'epee.
- Un son de lame rapide marque exactement le lancement.
- Un leger bourdonnement violet accompagne le trajet.
- La collision avec Imran, le bouclier ou une limite produit un bref son cristallin de fragmentation.

### Assets visuels et sonores a produire

- Animation de l'epee placee au-dessus de l'epaule.
- Illumination progressive de la ligne violette de la lame.
- Propagation de l'impulsion du coeur vers l'epee.
- Formation du croissant sur le tranchant.
- Animation de l'entaille horizontale.
- Croissant violet de `80 x 96 px`.
- Fragments d'obsidienne et etincelles metalliques.
- Courte trainee violette.
- Effet de fragmentation sans danger.
- Son de resonance magique pendant la preparation.
- Son de frottement du metal et de l'obsidienne.
- Son de lame au lancement.
- Bourdonnement leger pendant le trajet.
- Son cristallin de fragmentation.

## Attaque 2 - Double entaille au sol

> **Statut :** Validee

### Structure validee

- Le golem produit deux entailles d'energie successives dans la meme direction.
- La preparation avant le depart de la premiere entaille dure exactement `0.65 s`.
- La direction horizontale est verrouillee au debut de cette preparation.
- Les entailles ne suivent pas Imran apres leur depart.
- La premiere entaille part au terme des `0.65 s`.
- La seconde part exactement `0.30 s` apres la premiere.
- Les deux entailles restent en contact avec le sol.
- La premiere entaille possede une zone dangereuse de `144 x 64 px`.
- Le saut normal de `89 px` conserve `25 px` de marge au-dessus de cette premiere entaille.
- La seconde entaille possede une zone dangereuse de `176 x 120 px`.
- Le saut normal reste inferieur de `31 px` au sommet de la seconde entaille.
- Un saut normal complet suivi d'un Double saut peut atteindre environ `167 px`.
- Cette combinaison conserve donc une marge verticale maximale d'environ `47 px`.
- Chaque entaille se deplace a une vitesse horizontale constante de `540 px/s`.
- La duree de vie maximale de chaque entaille est de `2.10 s`.
- La portee maximale de chaque entaille est donc de `1134 px`.
- La forme visible de chaque entaille couvre sa zone sans creer de danger invisible.
- Le Bouclier de lumiere ne protege pas contre les entailles.
- Le Dash ne rend pas Imran invulnerable a leur contact.
- Imran utilise le saut normal pour la premiere entaille.
- Il utilise ensuite son Double saut pour franchir la seconde entaille plus haute.
- Chaque entaille retire `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche les deux entailles de retirer plusieurs coeurs pendant la meme periode.
- Chaque entaille disparait lorsqu'elle atteint une barriere ou la fin de sa duree de vie.
- La recuperation commune de `0.30 s` commence apres la disparition de la derniere entaille.

### Signal visuel valide

- Au debut de la preparation, le golem se tourne vers Imran et verrouille cette direction.
- Il abaisse la pointe de son epee pres du sol.
- Une premiere ligne violette courte apparait sur la partie basse de la lame.
- Une seconde ligne plus haute et plus intense apparait ensuite sur toute sa longueur.
- Au terme des `0.65 s`, le golem effectue une premiere entaille basse et produit la petite vague.
- Il conserve son epee en mouvement et la lumiere restante augmente.
- Apres `0.30 s`, il effectue une seconde entaille plus ample et produit la grande vague.
- La difference de taille, de posture et de lumiere annonce clairement la hauteur des deux dangers.
- Chaque entaille devient dangereuse uniquement lorsqu'elle quitte le point de contact avec le sol.
- Le signal reste comprehensible lorsque le son est coupe.

### Apparence des entailles validee

- La premiere entaille forme une vague violette basse bordee de fragments d'obsidienne.
- La seconde entaille utilise une vague plus haute, plus claire et plus large.
- Des morceaux de dalle et de petites etincelles metalliques accompagnent leur depart.
- Une courte trainee de runes violettes suit chaque entaille.
- La trainee, les fragments et les etincelles restent purement visuels.
- Aucun effet n'agrandit les zones dangereuses.
- Chaque entaille se fragmente en energie violette et en poussiere sombre avant de disparaitre.

### Signal sonore valide

- Une resonance metallique grave commence lorsque la pointe de l'epee s'abaisse.
- Deux intensites de vibration distinctes accompagnent la charge.
- Un premier impact sec marque le depart de l'entaille basse.
- Un second impact plus puissant retentit `0.30 s` plus tard.
- Un son de lame sur la pierre accompagne chaque trajet.
- Le son le plus grave correspond a la seconde entaille.
- Chaque disparition produit un bref son de rune eteinte et de pierre brisee.

### Assets visuels et sonores a produire

- Animation de la pointe de l'epee abaissee vers le sol.
- Deux niveaux d'illumination de la lame.
- Animation de la premiere entaille basse.
- Animation de la seconde entaille plus ample.
- Entaille basse de `144 x 64 px`.
- Entaille haute de `176 x 120 px`.
- Fragments d'obsidienne et morceaux de dalle.
- Etincelles metalliques et courtes trainees de runes.
- Effets de fragmentation et de disparition.
- Son de resonance metallique pendant la preparation.
- Premier impact sec.
- Second impact plus puissant.
- Sons distincts des deux trajets.
- Sons brefs de pierre et de runes lors de la disparition.

## Attaque 3 - Sceau de la lame

> **Statut :** Validee

### Structure validee

- L'attaque combine une zone centrale ciblee et une impulsion dangereuse sur tout le sol.
- La zone centrale mesure exactement `432 px` de largeur.
- La preparation avant l'activation dure exactement `0.75 s`.
- Son centre horizontal correspond a la position d'Imran au debut de la preparation.
- Cette position est verrouillee pendant toute l'attaque.
- La zone ne suit pas Imran apres le debut de la preparation.
- La zone centrale reste sans danger pendant toute la preparation.
- Depuis le centre, la zone vulnerable de `32 px` d'Imran doit parcourir `232 px` pour sortir completement.
- En `0.75 s`, un deplacement normal a pleine vitesse ne peut parcourir que `180 px`.
- Le deplacement normal reste donc inferieur de `52 px` a la distance de sortie.
- Un Dash de `124 px` laisse ensuite `0.55 s` de mouvement.
- A `240 px/s`, ce mouvement permet de parcourir `132 px` supplementaires.
- La sequence peut donc couvrir environ `256 px` et conserve une marge horizontale d'environ `24 px`.
- Le Dash doit commencer au sol et sa direction reste verrouillee.
- Si la zone depasse une barriere, seule sa partie situee dans l'arene reste active et visible.
- Le centre verrouille n'est jamais decale.
- Imran doit alors sortir vers l'interieur de l'arene et la distance maximale reste `232 px`.
- Au terme des `0.75 s`, une colonne de lames violettes remplit toute la hauteur jouable de la zone centrale.
- Cette colonne reste dangereuse pendant exactement `0.50 s`.
- Au meme instant, une impulsion runique rend tout le sol de l'arene dangereux sur une hauteur de `56 px`.
- Cette impulsion reste active pendant exactement `0.80 s`.
- La duree totale du saut normal est d'environ `0.71 s`.
- Le saut normal seul ne permet donc pas de rester en l'air pendant toute l'impulsion.
- Imran doit sauter apres son Dash puis utiliser son Double saut pour prolonger sa periode aerienne.
- Le Bouclier de lumiere ne protege ni contre la colonne, ni contre l'impulsion du sol.
- Le Dash ne rend pas Imran invulnerable a ces dangers.
- La colonne et l'impulsion retirent `1 coeur` en cas de contact valide.
- L'invulnerabilite standard empeche ces deux dangers de retirer plusieurs coeurs pendant la meme periode.
- Aucun danger ne constitue un obstacle solide ou une plateforme.
- La colonne disparait a la fin des `0.50 s`.
- Le sol redevient entierement sur a la fin des `0.80 s`.
- Aucune rune dangereuse ne persiste apres cette disparition.
- La recuperation commune de `0.30 s` commence lorsque l'impulsion du sol disparait.

### Signal visuel valide

- Deux limites violettes verticales apparaissent aux bords exacts de la zone centrale.
- Des runes geometriques se dessinent au sol entre ces limites pendant les `0.75 s`.
- Une ligne violette discrete parcourt egalement tout le sol de l'arene.
- Cette ligne annonce l'impulsion globale mais reste sans danger pendant la preparation.
- La zone centrale, la ligne du sol et la lame deviennent progressivement plus intenses.
- A l'activation, les deux limites produisent un bref eclat.
- Une colonne d'energie et de lames spectrales remplit la zone centrale.
- Une onde runique se propage instantanement sur toute la surface du sol.
- Pendant les `0.80 s`, les runes du sol brillent fortement sous la hauteur de `56 px`.
- La colonne reste suffisamment transparente pour conserver les limites visibles.
- Les fragments, les lames et les runes ne masquent jamais Imran.
- La colonne disparait a `0.50 s`.
- Les runes s'eteignent completement a `0.80 s`.
- Le signal reste comprehensible lorsque le son est coupe.

### Animation du golem validee

- Au debut de la preparation, le golem se tourne vers Imran.
- Il place son epee verticalement devant son coeur.
- La lumiere du coeur se propage dans toute la longueur de la lame.
- Il leve lentement l'epee pendant que les signaux apparaissent au sol.
- Au terme des `0.75 s`, il plante brusquement l'epee dans le sol.
- Ce mouvement declenche exactement la colonne centrale et l'impulsion runique.
- Le golem ne se deplace pas horizontalement pendant cette animation.
- Cette posture reste distincte des deux entailles laterales de la deuxieme attaque.

### Apparence des dangers validee

- La colonne centrale melange energie violette, lames spectrales, fragments d'obsidienne et morceaux de metal sombre.
- Les fragments restent contenus dans la zone de `432 px`.
- L'impulsion du sol utilise des runes violettes geometriques sur les dalles.
- De petites pointes d'energie restent contenues sous la hauteur dangereuse de `56 px`.
- Une faible brume violette accompagne l'attaque sans masquer les silhouettes.
- Les fragments, les etincelles et la brume restent purement visuels.
- Aucune rune ni aucun fragment ne modifie la collision du sol.
- Tous les effets s'eteignent ou se desassemblent avant de disparaitre.

### Signal sonore valide

- Une resonance magique et metallique grave commence au debut de la preparation.
- Un battement cristallin accompagne la lumiere du coeur.
- Des crepitements runiques parcourent progressivement le sol.
- Un impact de lame puissant marque le moment ou l'epee touche le sol.
- Un bourdonnement vertical accompagne la colonne pendant `0.50 s`.
- Une vibration grave accompagne l'impulsion du sol pendant `0.80 s`.
- Le bourdonnement de la colonne s'arrete avec sa disparition.
- La vibration diminue puis s'arrete lorsque le sol redevient sur.

### Assets visuels et sonores a produire

- Animation de l'epee placee devant le coeur.
- Propagation de la lumiere du coeur dans la lame.
- Animation de l'epee levee puis plantee dans le sol.
- Limites violettes de la zone centrale.
- Runes geometriques progressives dans la zone.
- Ligne d'avertissement sur tout le sol.
- Colonne d'energie et lames spectrales.
- Onde runique d'activation.
- Runes et pointes de l'impulsion du sol.
- Fragments d'obsidienne, morceaux de metal et brume legere.
- Extinction complete des runes.
- Son de resonance magique et metallique.
- Battement cristallin du coeur.
- Crepitements runiques progressifs.
- Impact puissant de l'epee.
- Bourdonnement de la colonne.
- Vibration de l'impulsion du sol.

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
- Les barrieres utilisent une energie violette sombre semi-transparente.
- Des fragments d'obsidienne et des eclats de metal sombre circulent dans cette energie.
- Les positions horizontales locales sont mesurees depuis la limite interieure gauche de la zone de combat.
- Imran commence la presentation avec son centre horizontal a `x = 128 px`.
- Le Golem du Chateau termine sa presentation avec son centre horizontal a `x = 1024 px`.
- Le golem est tourne vers la gauche et fait face a Imran.
- La distance initiale entre leurs centres est de `896 px`.
- Il reste `256 px` entre le centre initial du golem et la limite droite de la zone de combat.
- Dans le cadre de reference, Imran apparait a `x = 448 px` dans l'ecran.
- Dans le cadre de reference, le golem apparait a `x = 1344 px` dans l'ecran.
- Les portees des attaques mobiles permettent d'atteindre la zone initiale d'Imran.

### Comportement du sol valide

- Le sol en pierre anthracite ne modifie pas le deplacement d'Imran lorsqu'aucune attaque ne l'affecte.
- La vitesse horizontale maximale reste `240 px/s`.
- L'acceleration au sol reste `1800 px/s2`.
- Le freinage au sol reste `2200 px/s2`.
- Le saut normal, le Double saut et le controle aerien conservent leurs valeurs communes.
- Le Dash conserve sa vitesse de `620 px/s`, sa duree de `0.20 s` et sa distance theorique de `124 px`.
- L'intervalle de `1.00 s` entre deux Dash reste inchange.
- L'ambiance magique du chateau ne ralentit pas Imran et ne retire aucun coeur.
- Ces regles restent identiques dans la zone de combat et dans la zone de recompense.

### Direction visuelle de l'arene validee

- L'arene se trouve dans une grande salle interieure du Chateau de Tata Lisa.
- Le sol jouable utilise de grandes dalles de pierre gris anthracite entierement plates.
- Un socle de statue se trouve derriere la position finale du golem.
- Ce socle sert a sa presentation et reste hors des collisions jouables.
- Des murs en pierre sombre, des piliers et de grandes arches occupent l'arriere-plan.
- Des bannieres violettes et des vitraux sombres rappellent l'autorite de Tata Lisa.
- Des armures decoratives et des symboles geometriques occupent les plans intermediaires.
- La palette associe le gris anthracite, le noir de l'obsidienne, le violet sombre et quelques reflets argent.
- Les contours clairs et les variations de luminosite conservent Imran et les signaux dangereux lisibles.
- Les piliers, les bannieres, les vitraux et les armures restent purement decoratifs.
- Aucun element du decor ne cree une plateforme, une pente, une fosse ou un obstacle.
- Le meme sol en pierre continue sans rupture dans la zone de recompense.
- De faibles poussieres et quelques particules magiques violettes circulent en arriere-plan.
- De rares particules passent au premier plan avec une faible opacite.
- Elles ne masquent jamais Imran, le golem, les dangers ou l'interface.
- Elles ne possedent aucune collision et restent moins denses que les effets des attaques.

## Direction visuelle du golem validee

- Le corps utilise de grands blocs de pierre gris anthracite et d'obsidienne.
- Une armure de chevalier sombre, massive et symetrique couvre sa silhouette.
- De larges epaulieres renforcent le haut de son corps.
- Un casque integre possede une visiere relevee.
- Les deux grands yeux emettent une lumiere violette.
- Des fissures d'energie violette parcourent la pierre et l'armure.
- Un coeur magique en forme de cristal violet se trouve au centre du torse.
- La grande epee utilise du metal sombre, de l'obsidienne et une ligne d'energie violette.
- La silhouette mesure environ deux fois et demie la taille d'Imran.
- Le style reste cartoon, lisible et adapte aux enfants a partir de 7 ans.
- L'armure, les epaulieres, le casque et l'epee n'agrandissent pas les zones de collision communes.

## Presentation du Golem du Chateau

> **Statut :** Validee

### Deroulement visuel valide

- Avant le combat, le golem ressemble a une grande statue de chevalier placee devant le passage.
- Son epee est plantee dans le sol et toutes ses lumieres sont eteintes.
- Il ne possede aucune zone dangereuse ou vulnerable pendant cet etat.
- La presentation commence lorsque Imran franchit le point d'entree de l'arene.
- Les commandes d'Imran sont bloquees pendant toute la presentation.
- La sequence dure exactement `3.00 s`.

| Periode | Animation |
|---|---|
| `0.00 a 1.00 s` | Les gravures de l'epee s'allument, le socle tremble et une poussiere legere tombe de l'armure. |
| `1.00 a 2.00 s` | Le coeur, les yeux et les fissures s'allument progressivement en violet. |
| `2.00 a 3.00 s` | Le golem retire son epee du sol, descend du socle, atteint sa position fixe et prend sa garde face a Imran. |

- Les deux barrieres violettes montent silencieusement pendant les `0.50 s` du debut de la sequence.
- Le deplacement depuis le socle se termine exactement a la position locale `x = 1024 px`.
- La poussiere et les fragments du socle restent uniquement visuels.
- Ils disparaissent avant la fin de la sequence.
- La barre de vie apparait lorsque la presentation atteint `3.00 s`.
- Le controle d'Imran revient au meme instant.
- Le golem devient vulnerable et son corps devient dangereux a cet instant.
- La preparation du Croissant violet peut alors commencer.
- Une commande effectuee avant la fin des `3.00 s` reste ignoree.
- Une nouvelle tentative rejoue la sequence complete depuis l'etat de statue.

### Signal sonore valide

- Une resonance basse de pierre et de metal commence au debut de la presentation.
- Un bourdonnement magique violet accompagne l'allumage de l'epee.
- Un battement cristallin accompagne l'allumage du coeur et des yeux.
- Un frottement de pierre et un raclement de lame accompagnent le retrait de l'epee.
- Des pas lourds accompagnent la descente du socle.
- Aucun cri ni aucun rugissement n'est joue.
- Les barrieres restent silencieuses.
- Tous les sons de presentation s'arretent lorsque la barre de vie apparait et que le controle revient.

### Assets visuels et sonores a produire

- Pose de statue avec l'epee plantee dans le sol.
- Etats eteint et allume des gravures de l'epee.
- Tremblement du socle et chute de poussiere.
- Illumination progressive du coeur, des yeux et des fissures.
- Animation de retrait de l'epee.
- Animation de descente du socle.
- Transition vers la position fixe et la posture de garde.
- Son de resonance de pierre et de metal.
- Bourdonnement magique progressif.
- Battement cristallin.
- Raclement de l'epee retiree du sol.
- Pas lourds sur les dalles.

## Defaite du Golem du Chateau

> **Statut :** Validee

### Deroulement visuel valide

- La sequence commence au contact du Smash Tranchant final avec le golem etourdi.
- Elle dure exactement `1.00 s`.
- La barre de vie disparait au debut de cette sequence.
- Le golem, son epee, ses fragments et ses particules ne possedent plus aucune zone dangereuse ou solide.

| Periode | Animation |
|---|---|
| `0.00 a 0.20 s` | Le coeur et l'epee produisent un dernier eclat, puis les yeux et toutes les fissures s'eteignent. |
| `0.20 a 0.70 s` | Le golem pose brievement un genou au sol, puis son armure, son corps et son epee se desassemblent. |
| `0.70 a 1.00 s` | Les fragments deviennent des particules violettes et de faibles etincelles metalliques qui disparaissent. |

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

- Un bref accord magique accompagne le dernier eclat du coeur et de l'epee.
- Un son d'energie eteinte accompagne la disparition des lumieres violettes.
- Une resonance d'armure accompagne le genou pose au sol.
- Des sons de pierre, d'obsidienne et de metal accompagnent le desassemblage.
- Un tintement leger accompagne les dernieres etincelles.
- Tous les sons diminuent progressivement et s'arretent avec les dernieres particules.
- Aucun son d'explosion violent n'est utilise.

### Assets visuels et sonores a produire

- Dernier eclat du coeur et de l'epee.
- Extinction du coeur, des yeux, des fissures et de la lame.
- Animation du genou pose au sol.
- Desassemblage de l'armure, du corps et de l'epee.
- Fragments de pierre anthracite, d'obsidienne et de metal sombre.
- Transformation en particules violettes et etincelles metalliques.
- Disparition complete des particules.
- Son du dernier accord magique.
- Son d'extinction de l'energie.
- Resonance de l'armure.
- Sons de desassemblage de pierre, d'obsidienne et de metal.
- Tintement leger des dernieres etincelles.

## Recompense

> **Statut :** Validee

### Apparence du coffre validee

- Le coffre utilise une base en bois noir et en pierre gris anthracite.
- Des renforts en metal sombre protegent ses angles, ses bords et son couvercle.
- De petits fragments d'obsidienne decorent les quatre angles.
- Des motifs geometriques de chevalier sont graves dans les plaques metalliques.
- Une serrure en forme de cristal violet se trouve au centre.
- Les motifs, les fragments et le cristal restent decoratifs.
- Le coffre ne produit aucun rayon, aucune lumiere doree et aucun effet lumineux.
- Sa silhouette reste immediatement identifiable comme celle d'un coffre interactif.
- Son fonctionnement et son animation utilisent les regles communes des six coffres.

### Coffre, cle et transition valides

- Le coffre devient disponible a la fin de la sequence de defaite du golem.
- Imran doit se placer a `56 px` ou moins du coffre puis utiliser la commande `Interaction`.
- L'interaction lance la sequence commune de `2.00 s`.
- Le deplacement, le saut, le Dash et les attaques restent bloques pendant cette sequence.
- De `0.00 a 0.75 s`, le couvercle et son mecanisme s'ouvrent.
- De `0.75 a 1.50 s`, la sixieme cle sort progressivement du coffre.
- De `1.50 a 2.00 s`, la cle reste visible au-dessus du coffre.
- Aucune seconde interaction et aucune collision de ramassage ne sont necessaires.
- La sixieme cle est ajoutee automatiquement a la progression a la fin des `2.00 s`.
- Aucun nouveau pouvoir n'est debloque.
- La sauvegarde automatique commence immediatement apres l'ajout de la cle.
- Les coeurs et les vies sont restaures a `3`.
- Le prochain objectif devient le combat contre Tata Lisa devant la porte du donjon.
- Le coffre utilise le son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.
- Ce son commence avec l'interaction et accompagne toute la sequence de `2.00 s`.
- Aucun son supplementaire propre au bois, a la pierre, au metal, a l'obsidienne, au cristal ou a la sixieme cle n'est ajoute.
- Le controle reste bloque apres la fin des `2.00 s`.
- Une fois la sauvegarde confirmee, un fondu au noir de `0.50 s` commence.
- La barriere gauche disparait pendant ce fondu avec le reste de l'arene.
- La zone precedant le combat contre Tata Lisa est chargee pendant l'ecran noir.
- L'ecran reste noir tant que cette zone n'est pas prete.
- La nouvelle zone apparait avec un fondu depuis le noir de `0.50 s`.
- Le controle revient lorsque la zone est entierement visible.
- Imran commence cette sequence avec `3 coeurs`, `3 vies` et les `6 cles`.
- L'ouverture des six verrous reste impossible avant la victoire contre Tata Lisa.
- Le donjon reste uniquement le decor de la scene finale et ne devient pas un niveau jouable.

## Inventaire complementaire des assets

> **Statut :** Valide

Les assets propres a chaque attaque, a la presentation et a la defaite sont enumeres dans leurs sections respectives. Les elements complementaires suivants doivent egalement etre produits :

### Golem

- Silhouette principale du Golem du Chateau.
- Pose neutre orientee vers la gauche.
- Pose neutre orientee vers la droite.
- Animation de retournement sur place.
- Animation de reaction a un impact valide sur la tete.
- Effet visuel d'impact sur la zone vulnerable.
- Animation de passage a l'etat `Etourdi`.
- Pose immobile de l'etat `Etourdi`.
- Etats eteint et allume du coeur, des yeux, des fissures et de la lame.
- Grande epee en metal sombre et obsidienne.

### Arene

- Sol en dalles de pierre anthracite raccordable sur toute la longueur de `1920 px`.
- Socle de statue intact et libere.
- Murs en pierre sombre, piliers et grandes arches.
- Bannieres violettes et vitraux sombres.
- Armures decoratives et motifs geometriques.
- Systeme de poussiere legere en arriere-plan.
- Systeme de rares particules violettes au premier plan.
- Variante violette sombre des deux barrieres communes.
- Fragments d'obsidienne et eclats de metal pour les barrieres.
- Prolongement du decor dans la zone de recompense.

### Recompense

- Coffre du Chateau ferme.
- Coffre du Chateau pendant l'ouverture.
- Coffre du Chateau ouvert.
- Bois noir, pierre anthracite, renforts de metal sombre et obsidienne.
- Motifs de chevalier et serrure en cristal violet.
- Apparition et elevation de la sixieme cle selon l'animation commune.
- Son commun `assets/audio/sfx/ouverture-coffre-commune.wav`.

## Justification des choix valides

- Une seule phase conserve une difficulte lisible et limite la charge de programmation.
- Les trois attaques reutilisent des systemes deja definis pour les autres golems.
- Les valeurs de vitesse, de duree et de taille restent proches des combats precedents tout en demandant une execution plus precise.
- L'epee donne au golem une identite propre sans ajouter une mecanique reservee a un seul combat.
- Le cycle verifie successivement la defense, les deux sauts puis l'enchainement du Dash et des sauts.
- L'ordre fixe permet au joueur de comprendre ses erreurs et de progresser a chaque tentative.
- Les signaux violets, les runes et les mouvements de la lame distinguent clairement les trois attaques.
- L'arene plate evite qu'un obstacle transforme une attaque lisible en degat inevitable.
- La transition apres la sixieme cle respecte la progression deja validee vers Tata Lisa.

## Criteres de validation

La fiche sera validee lorsque :

- les trois attaques possederont des valeurs mesurables et compatibles ;
- les signaux visuels resteront comprehensibles sans le son ;
- le Croissant violet pourra etre bloque ou evite avec le Double saut ;
- la Double entaille exigera le saut puis le Double saut ;
- le Sceau de la lame exigera le Dash au sol puis le Double saut ;
- aucune attaque ne produira de degat inevitable ;
- l'epee restera au centre de l'identite visuelle et mecanique du combat ;
- l'arene restera plate, lisible et sans danger permanent ;
- la presentation, la defaite et la recompense respecteront les regles communes ;
- la sixieme cle conduira au combat contre Tata Lisa sans ouvrir immediatement le donjon ;
- tous les assets necessaires seront identifies.

## Sources

- [Golem du Chateau du Concept Game](../../Concept-Game/08-Boss/Golem-du-Chateau.md)
- [Chateau de Tata Lisa du Concept Game](../../Concept-Game/03-Univers/Chateau-de-Tata-Lisa.md)
- [Regles communes des boss](Regles-Communes.md)
- [Golem du Volcan](Golem-Volcan.md)
- [Progression du GDD](../Systemes/Progression.md)
- [Niveau 6 - Chateau](../Niveaux/Niveau-6-Chateau.md)
