# Squelettes

> **Statut :** Valide

## Objectif

Definir deux ennemis humanoides lisibles qui partagent une base commune mais occupent des roles differents. Le Squelette epeiste exerce une pression au corps a corps, tandis que le Squelette archer oblige Imran a reagir a une attaque a distance.

## Identite deja validee

- Deux variantes de Squelettes apparaissent dans les premiers niveaux.
- Le Squelette epeiste combat au corps a corps.
- Le Squelette archer attaque a distance.
- Leurs animations utilisent des poses seches et articulees.
- Leurs mouvements produisent de legers claquements d'os stylises.
- Ils utilisent surtout leurs bruits de mouvement et aucune voix humaine.
- Leur defaite reste courte, cartoon et sans violence graphique.

## Regles communes applicables

- Une attaque ou un contact dangereux retire `1 coeur` a Imran.
- Une attaque normale de la Shadow Sword inflige `1 degat`.
- Le Smash Tranchant inflige `2 degats`.
- Une reaction non fatale dure `0.33 s`.
- Une defaite dure `0.67 s` avant la disparition.
- Un Squelette vaincu reste absent pendant la vie en cours et ne produit aucune recompense.
- Les Squelettes ne sont solides ni pour Imran, ni pour les autres ennemis.
- Ils sont bloques par le decor solide et ne tombent jamais accidentellement dans un gouffre.
- Leurs attaques ne blessent jamais les autres ennemis.
- Un maximum de `3 ennemis ordinaires` peut attaquer simultanement selon les regles communes.

## Dimensions validees

Les deux variantes de Squelettes utilisent les memes dimensions de base :

- enveloppe visuelle : `48 x 72 px` ;
- collision principale avec le decor : `36 x 60 px` ;
- zone vulnerable du corps : `32 x 56 px` ;
- zone dangereuse du corps : `32 x 56 px`.

Ces dimensions rendent les Squelettes legerement plus grands que la hauteur visuelle de reference d'Imran, fixee a `64 px`.

- L'arc et l'epee ne modifient pas la collision principale avec le decor.
- L'arc ne fait pas partie de la zone vulnerable du Squelette archer.
- L'epee possede une zone dangereuse separee qui prolonge celle du Squelette epeiste vers l'avant.
- Les dimensions exactes de cette epee seront definies avec sa portee.

## Points de vie valides

- Le Squelette epeiste possede `2 PV`.
- Le Squelette archer possede `2 PV`.
- Deux attaques normales sont necessaires pour vaincre un Squelette.
- Un seul Smash Tranchant inflige les `2 degats` necessaires et le vainc immediatement.
- Un impact non fatal declenche la reaction et la protection de `0.33 s` definies par les regles communes.

## Vitesse de patrouille validee

- Le Squelette epeiste patrouille a `140 px/s`.
- Le Squelette archer patrouille a `140 px/s`.
- Cette vitesse reste constante pendant leur marche normale.
- Elle est inferieure aux `240 px/s` d'Imran afin de permettre au joueur de les depasser.
- La preparation et le tir de l'Archer ne modifient pas cette vitesse.
- La vitesse de la fleche sera definie separement.

## Zone de patrouille validee

- Chaque Squelette possede une zone horizontale predeterminee de `800 px` de large.
- Cette zone s'etend sur `400 px` de chaque cote de sa position initiale.
- La position initiale constitue le centre fixe de la patrouille.
- L'orientation initiale est determinee par son placement dans le niveau.
- Le Squelette fait demi-tour lorsqu'il atteint une limite de sa zone.
- Un mur infranchissable ou un bord dangereux provoque egalement un demi-tour.
- Le decor peut raccourcir la distance reellement parcourue sans agrandir la zone.
- A `140 px/s`, un aller-retour complet sur la largeur maximale dure environ `11.43 s`.
- Ce rythme correspond a la duree du cycle observe dans la capture de reference de `11.62 s`.
- La patrouille reste entierement incluse dans la zone de rencontre du Squelette.

## Patrouille permanente validee

- Les deux variantes commencent leur patrouille des le chargement du niveau.
- Elles ne possedent aucun etat d'attente immobile pendant leur comportement normal.
- Elles continuent leur patrouille meme si Imran se trouve hors de leur detection ou hors de l'ecran.
- Leur orientation initiale est choisie lors de leur placement dans le niveau.
- L'Epeiste ne change jamais de comportement selon la position d'Imran.
- L'Archer cesse uniquement de preparer de nouveaux tirs lorsque ses conditions de detection ne sont plus reunies.
- La marche utilise des poses seches et articulees accompagnees de legers claquements d'os stylises.
- Une reaction aux degats, une defaite ou une interruption imposee par une collision peut temporairement arreter cette patrouille.

## Sortie de la rencontre et reinitialisation validees

- Les Squelettes ne quittent jamais leur zone de patrouille pour suivre Imran.
- Lorsque Imran quitte leur detection ou leur zone de rencontre, ils ne retournent pas au centre.
- Ils continuent leur patrouille depuis leur position courante.
- Revenir dans la zone ne provoque aucune teleportation et ne modifie pas leur orientation.
- Les degats deja recus restent conserves pendant la vie en cours.
- Une perte de vie, un Game Over, un abandon ou un rechargement du niveau replace chaque Squelette a sa position initiale.
- Cette reinitialisation restaure son orientation initiale, ses `2 PV` et son cycle de patrouille.

## Collisions avec le decor validees

- Un mur ou un obstacle infranchissable provoque un demi-tour immediat.
- Un bord de plateforme ou un gouffre provoque un demi-tour avant la chute.
- Une plateforme traversable supporte les Squelettes comme un sol.
- Les Squelettes ne sautent jamais et ne descendent jamais volontairement d'une plateforme.
- Ils ne peuvent pas utiliser une plateforme traversable pour atteindre un autre etage.
- Si le decor raccourcit la patrouille, ils utilisent uniquement la portion praticable comprise dans leur zone.
- L'epee ne modifie pas la collision principale du Squelette epeiste.
- Une partie de la lame placee derriere un mur ou un obstacle solide ne peut pas blesser Imran.
- Aucun degat d'epee ne traverse un element solide du decor.
- Une fleche disparait des son premier contact avec un decor solide.
- Une collision avec le decor ne provoque aucun degat au Squelette.

## Emplacements d'attaque valides

- Le Squelette epeiste n'occupe jamais un emplacement d'attaque.
- Son corps et son epee utilisent des dangers de contact permanents.
- Le Squelette archer demande un emplacement avant de commencer sa preparation de `0.50 s`.
- Si aucun emplacement n'est disponible, il continue sa patrouille sans tendre son arc.
- Il ne memorise aucun tir a lancer immediatement.
- Lorsqu'un emplacement se libere, toutes les conditions de tir sont de nouveau verifiees.
- L'Archer conserve son emplacement pendant la preparation et pendant toute la trajectoire de la fleche.
- Une preparation annulee, une defaite avant le lancement ou la disparition de la fleche libere immediatement l'emplacement.
- La recuperation visuelle de `0.25 s` et le delai de `2 s` n'occupent aucun emplacement apres la disparition de la fleche.
- La limite commune de `3 ennemis ordinaires` capables d'attaquer simultanement reste applicable.

## Detection validee

### Squelette epeiste

- L'Epeiste ne possede aucune action active declenchee par une detection.
- Il conserve sa patrouille, sa zone dangereuse corporelle et sa lame dangereuse tant qu'il est vivant.
- Son danger de contact permanent ne constitue pas une attaque et ne demande aucun emplacement d'attaque.

### Squelette archer

- La detection est mesuree entre le centre d'Imran et le centre de l'Archer.
- Imran doit se trouver a `800 px` ou moins horizontalement.
- Imran doit se trouver a `480 px` ou moins verticalement.
- L'Archer doit etre visible a l'ecran.
- Une ligne de vue libre entre l'Archer et Imran est obligatoire.
- Les quatre conditions doivent etre reunies simultanement pour autoriser un nouveau tir.
- La detection autorise le tir mais ne modifie ni la vitesse, ni la direction, ni les limites de la patrouille.
- Si l'Archer regarde dans la mauvaise direction, il continue sa patrouille sans se retourner immediatement.
- Sortir de la detection ou perdre la ligne de vue empeche uniquement le debut d'un nouveau tir.
- Une fleche deja lancee continue selon les regles de son projectile.
- La distance verticale permet a l'Archer de detecter Imran sur une plateforme sans lui permettre de viser vers le haut.

## Preparation du tir de l'Archer validee

- Un tir commence par une preparation de `0.50 s`.
- L'Archer continue sa patrouille a `140 px/s` pendant cette preparation.
- Il leve son arc et tend visiblement sa corde.
- Un leger son de tension accompagne cette animation.
- La preparation occupe un emplacement d'attaque selon les regles communes.
- Une attaque d'Imran recue pendant cette duree annule le tir.
- L'emplacement d'attaque est libere immediatement si la preparation est annulee.
- Si la preparation se termine normalement, une seule fleche est lancee.

## Cadence de tir de l'Archer validee

- Deux lancements de fleche sont separes par un minimum de `2 s`.
- Ce delai commence au moment ou la fleche quitte l'arc.
- L'Archer continue sa patrouille a `140 px/s` pendant ce delai.
- Il ne peut commencer aucune nouvelle preparation de tir avant la fin des `2 s`.
- La fin du delai n'impose pas un tir immediat.
- La detection, la visibilite, la ligne de vue, l'orientation et la disponibilite d'un emplacement d'attaque sont de nouveau verifiees.
- Une preparation annulee avant le lancement ne compte pas comme un lancement de fleche.

## Vitesse de la fleche validee

- La fleche se deplace a une vitesse constante de `600 px/s`.
- Sa trajectoire reste strictement horizontale.
- Elle conserve sa direction et sa vitesse jusqu'a sa disparition.
- Elle ne possede aucune acceleration, aucune gravite et aucun guidage vers Imran.
- La vitesse de la fleche ne depend pas du deplacement de l'Archer.
- Le recul, un changement de direction ou la defaite de l'Archer apres le lancement ne modifient pas la fleche deja presente.

## Dimensions de la fleche validees

- La fleche possede une taille visuelle de `48 x 12 px`.
- Sa zone dangereuse mesure `40 x 8 px`.
- La zone dangereuse est centree sur la partie visible de la fleche.
- La reduction de `4 px` sur chaque extremite evite un impact invisible devant la pointe ou derriere l'empennage.
- La reduction de `2 px` en haut et en bas evite un impact lorsque la silhouette visible ne touche pas clairement Imran.
- Ces dimensions sont normalisees pour les proportions d'Imran Adventure et ne correspondent pas aux dimensions internes du jeu de reference.

## Portee et duree de la fleche validees

- La fleche possede une portee maximale de `960 px`.
- Cette distance correspond a la moitie de la largeur de reference de `1920 px`.
- Elle possede une duree de vie maximale de `1.60 s`.
- A `600 px/s`, la fleche parcourt exactement `960 px` en `1.60 s`.
- Elle disparait des que la portee ou la duree maximale est atteinte.
- Sa portee couvre la detection horizontale de `800 px` et conserve une marge de `160 px` pour le mouvement d'Imran apres le lancement.
- La distance est mesuree depuis le point ou la fleche quitte l'arc.

## Impacts et disparition de la fleche valides

- Une fleche qui touche la zone vulnerable d'Imran retire `1 coeur`, puis disparait.
- Le recul et l'invulnerabilite standards d'Imran sont appliques.
- Le Bouclier de lumiere bloque automatiquement une fleche arrivant de face.
- Ce blocage fonctionne lorsque Imran est immobile ou en mouvement.
- Une fleche bloquee ne retire aucun coeur et disparait immediatement.
- Une fleche arrivant par-derriere n'est pas bloquee par le Bouclier.
- Une fleche qui touche un mur, un sol, un plafond ou un autre decor solide disparait.
- Une fleche traverse tous les autres ennemis sans degat, recul, impact ou ralentissement.
- Une fleche disparait lorsqu'elle atteint `960 px` ou `1.60 s`.
- Sortir de l'ecran ne suffit pas a la faire disparaitre avant une autre condition de disparition.
- L'emplacement d'attaque de l'Archer reste occupe depuis le debut de la preparation jusqu'a la disparition de la fleche.
- La disparition de la fleche libere immediatement cet emplacement.
- La duree maximale de `1.60 s` reste inferieure a la cadence de `2 s` : un meme Archer ne peut donc jamais avoir deux fleches actives simultanement.

## Recuperation visuelle de l'Archer validee

- Apres le lancement, l'Archer utilise une recuperation visuelle de `0.25 s`.
- Il rabaisse son arc pendant cette animation.
- Il continue sa patrouille a `140 px/s`.
- La recuperation ne ralentit ni l'Archer, ni la fleche deja lancee.
- Elle se deroule pendant le delai minimal de `2 s` entre deux lancements.
- L'Archer ne peut commencer aucune nouvelle preparation pendant cette recuperation.
- Une attaque d'Imran recue pendant cette animation applique normalement les degats et la reaction de `0.33 s`.

## Changement de direction pendant la preparation valide

- L'Archer continue de respecter les limites de sa patrouille pendant les `0.50 s` de preparation.
- S'il atteint une limite, un mur ou un bord dangereux, il fait demi-tour normalement.
- Imran peut egalement passer derriere l'Archer pendant cette duree.
- Juste avant le lancement, la detection, la visibilite, la ligne de vue et l'orientation sont verifiees une seconde fois.
- Si l'Archer ne regarde plus dans la direction d'Imran, le tir est annule.
- Une annulation ne produit aucune fleche et ne declenche pas le delai de `2 s`.
- L'emplacement d'attaque est libere immediatement.
- L'Archer poursuit sa patrouille sans pause ni retournement supplementaire.

## Origine des valeurs de l'Archer

- La capture determine directement la patrouille horizontale, le demi-tour aux limites, le maintien du deplacement pendant le tir, la trajectoire droite et l'absence de visee verticale.
- La zone de `800 px` et la vitesse de `140 px/s` produisent un aller-retour de `11.43 s`, proche des `11.62 s` de la capture complete.
- La vitesse de fleche de `600 px/s` adapte le passage rapide visible dans la capture a la vitesse d'Imran de `240 px/s`.
- La fleche se deplace donc a `2.5 fois` la vitesse de course d'Imran.
- La preparation de `0.50 s` et la cadence de `2 s` sont des valeurs de lisibilite et d'equilibrage pour le public cible.
- La taille visuelle de `48 x 12 px` est adaptee au Squelette de `72 px` de haut et a la hauteur visuelle d'Imran de `64 px`.
- La zone dangereuse de `40 x 8 px` est volontairement plus petite que l'image afin de rendre la collision juste.
- Les valeurs qui ne peuvent pas etre mesurees directement dans la capture devront etre verifiees dans le prototype Godot.

## Roles a differencier

### Squelette epeiste

- patrouille horizontale dans une zone predeterminee ;
- aucune poursuite directe d'Imran ;
- epee maintenue droite devant lui pendant son deplacement ;
- danger frontal produit par son epee.

### Squelette archer

- patrouille horizontale dans une zone predeterminee ;
- preparation visible avant le tir ;
- projectile frontal pouvant etre bloque par le Bouclier de lumiere ;
- courte recuperation apres le tir.

## Methode de comportement validee pour l'Archer

La methode generale est basee sur la capture de reference :

1. Le Squelette archer patrouille continuellement dans une zone horizontale predeterminee.
2. Il fait demi-tour a chaque limite de cette zone ou devant un obstacle infranchissable.
3. Il ne quitte jamais sa patrouille pour poursuivre Imran.
4. Il conserve son deplacement pendant la preparation et le declenchement du tir.
5. Il peut tirer uniquement lorsqu'il regarde dans la direction d'Imran et que les autres conditions de tir sont reunies.
6. Il ne se retourne pas instantanement uniquement pour tirer.
7. Sa fleche part dans la direction regardee et suit une trajectoire droite et horizontale.
8. Il ne vise ni vers le haut ni vers le bas.
9. Si Imran se trouve en hauteur, la fleche peut passer sous lui.
10. La fleche ne corrige jamais sa trajectoire apres son lancement.

## Methode de comportement validee pour l'Epeiste

Le Squelette epeiste reprend la meme logique de patrouille que le Squelette archer :

1. Il patrouille continuellement dans une zone horizontale predeterminee.
2. Il fait demi-tour a chaque limite de cette zone ou devant un obstacle infranchissable.
3. Il ne quitte jamais sa patrouille pour poursuivre Imran.
4. Il maintient son epee droite devant lui pendant son deplacement.
5. La pointe de l'epee reste dirigee vers son sens de deplacement.
6. Lorsqu'il fait demi-tour, le Squelette et son epee changent ensemble de direction.
7. La zone dangereuse de la lame reste active en permanence tant que le Squelette est vivant.
8. Un contact entre la lame et la zone vulnerable d'Imran retire `1 coeur`.
9. Ce contact applique le recul et l'invulnerabilite standards d'Imran.
10. La lame permanente est un danger de contact et non une attaque separee.
11. Elle ne possede donc aucune preparation, aucune recuperation et n'occupe aucun emplacement d'attaque.
12. La zone dangereuse de la lame est desactivee immediatement lorsque le Squelette entre dans l'etat `Defaite`.
13. Le corps du Squelette reste egalement dangereux sur tous ses cotes.
14. Un contact avec son corps, y compris par-derriere, retire `1 coeur` a Imran.
15. L'epee prolonge uniquement la zone dangereuse du Squelette vers l'avant.

## Dimensions et position de l'epee validees

- L'epee possede une taille visuelle de `56 x 16 px`.
- Sa zone dangereuse de lame mesure `44 x 10 px`.
- La poignee occupe les `12 px` restants et ne provoque aucun degat.
- L'epee est maintenue horizontalement depuis la main placee devant le Squelette.
- La zone dangereuse commence apres la poignee et se termine a la pointe visible.
- Elle reste centree verticalement sur la lame.
- L'epee change horizontalement de cote en meme temps que le Squelette fait demi-tour.
- Elle ne modifie jamais la collision principale de `36 x 60 px` utilisee contre le decor.
- Ces dimensions correspondent a celles de la Shadow Sword d'Imran afin de conserver une proportion commune entre les armes.

## Contact dangereux de l'Archer valide

- La zone dangereuse corporelle du Squelette archer mesure `32 x 56 px`.
- Un contact avec son corps retire `1 coeur` a Imran, quel que soit le cote touche.
- Le recul et les `1.30 s` d'invulnerabilite standards d'Imran sont appliques.
- L'arc ne possede aucune zone dangereuse.
- Toucher uniquement l'arc ne provoque aucun degat.
- La fleche est la seule attaque a distance de l'Archer.
- La zone dangereuse corporelle est desactivee immediatement lorsque l'Archer entre dans l'etat `Defaite`.

## Reaction non fatale validee

- Lorsqu'un Squelette survit a un impact, sa reaction dure `0.33 s`.
- Il interrompt immediatement sa marche et reste sur place pendant cette duree.
- Il conserve son orientation.
- Sa zone dangereuse corporelle reste active.
- L'epee du Squelette epeiste reste egalement dangereuse.
- Une preparation de tir de l'Archer est annulee selon les regles communes.
- Une fleche deja lancee conserve sa trajectoire et ses proprietes.
- La recuperation visuelle ou le delai de tir de l'Archer ne sont pas relances par la reaction.
- A la fin des `0.33 s`, le Squelette reprend sa patrouille dans la meme direction.
- Si un obstacle, un mur ou un bord dangereux empeche cette reprise, il fait demi-tour avant de repartir.

## Criteres de validation

La fiche des Squelettes sera validee si :

- les deux roles sont reconnaissables avant leur premiere interaction dangereuse ;
- chaque variante possede des points de vie et des dimensions ;
- chaque detection et chaque distance d'action sont mesurables ;
- chaque attaque active possede une preparation, une phase dangereuse et une recuperation ;
- les dangers de contact permanents sont clairement distingues des attaques actives ;
- le projectile de l'Archer possede toutes ses valeurs ;
- le Bouclier bloque clairement un projectile venant de face ;
- chaque variante respecte la limite de la zone de rencontre ;
- les comportements restent previsibles pour le public cible ;
- chaque valeur peut etre testee dans le prototype sans decision de gameplay manquante.

## Sources

- [Squelettes du Concept Game](../../Concept-Game/07-Ennemis/Squelettes.md)
- [Principes d'IA](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Animation](../../Concept-Game/09-Direction-Artistique/Animation.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
- [Voix](../../Concept-Game/10-Direction-Sonore/Voix.md)
- [Regles communes des ennemis](Regles-Communes.md)
- [Blocage automatique](../Combat/Blocage.md)
- [Reference video de la patrouille et du tir de l'Archer](Reference-Video-Patrouille-Squelette-Archer.md)
