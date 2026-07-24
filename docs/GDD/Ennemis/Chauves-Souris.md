# Chauves-souris

> **Statut :** Valide

## Objectif

Definir le premier ennemi volant d'Imran Adventure. La Chauve-souris apprend au joueur a surveiller l'espace aerien, reconnaitre la preparation d'une plongee et eviter une attaque venant du dessus.

## Identite deja validee

- La Chauve-souris est un ennemi volant.
- Elle attaque Imran en plongeant vers lui.
- Elle oblige le joueur a surveiller les menaces aeriennes.
- Son mouvement aerien reste souple et lisible.
- Ses sons utilisent un battement d'ailes souple et un petit cri non agressif.
- Sa defaite reste courte, cartoon et sans violence graphique.

## Regles communes applicables

- Une attaque ou un contact dangereux retire `1 coeur` a Imran.
- La Chauve-souris possede `1 PV`.
- Une attaque normale de la Shadow Sword inflige `1 degat`.
- Le Smash Tranchant inflige `2 degats`.
- Une attaque normale ou un Smash Tranchant vainc donc immediatement la Chauve-souris.
- Avec `1 PV`, elle ne peut jamais entrer dans une reaction non fatale et passe directement a l'etat `Defaite` apres un coup recu.
- Une defaite dure `0.67 s` avant la disparition.
- Une Chauve-souris vaincue reste absente pendant la vie en cours et ne produit aucune recompense.
- Elle n'est solide ni pour Imran, ni pour les autres ennemis.
- Elle est bloquee par les murs, les plafonds, les sols et les obstacles entierement solides.
- Elle traverse les plateformes traversables sans modifier sa trajectoire.
- Elle reste dans la zone de rencontre definie par le niveau.
- Un maximum de `3 ennemis ordinaires` peut attaquer simultanement selon les regles communes.

## Dimensions validees

- La Chauve-souris occupe une enveloppe visuelle de reference de `56 x 48 px`.
- Sa silhouette est plus large que haute afin de rendre les ailes immediatement reconnaissables.
- Sa zone principale de gameplay mesure `40 x 32 px`.
- Cette zone reste centree sur le corps et exclut les extremites visuelles des ailes.
- Elle sert a la reception des coups et au contact dangereux.
- Les battements d'ailes peuvent depasser temporairement l'enveloppe de reference sans agrandir la zone de gameplay.

## Attente avant activation validee

- La Chauve-souris possede un point aerien initial fixe dans la partie haute de sa zone de rencontre.
- Elle ne se deplace pas horizontalement avant son activation.
- Ses ailes utilisent une animation de battement continu.
- Son visuel oscille lentement jusqu'a `4 px` au-dessus et au-dessous du point initial.
- La boucle complete d'oscillation dure `1.20 s`.
- Cette oscillation est uniquement visuelle : la position et la zone de gameplay restent immobiles.
- Aucun cri n'est produit pendant cette attente.
- Lorsque toutes les conditions de detection sont reunies, la Chauve-souris quitte cette boucle et commence son cycle d'attaque.

## Methode de vol et d'attaque validee

- Apres son activation, la Chauve-souris enchaine des passages aeriens en courbe autour d'Imran.
- Chaque cycle commence dans la partie haute de sa zone de rencontre.
- Elle descend ensuite vers la hauteur d'Imran selon une courbe fluide.
- Son propre corps constitue l'attaque et aucun projectile n'est produit.
- Apres son passage bas, elle poursuit sa trajectoire et remonte dans la partie haute de la zone.
- La remontee cree naturellement une courte occasion de riposte avant le passage suivant.
- Elle ne se pose jamais entre deux passages et ne revient pas a un vol stationnaire apres chaque attaque.
- Un contact avec Imran ne bloque pas la Chauve-souris et n'annule pas sa trajectoire.
- Plusieurs Chauves-souris peuvent executer des courbes distinctes ou symetriques sans se bloquer entre elles.
- Les changements de direction restent progressifs et aucun deplacement instantane n'est autorise.

Cette methode reprend la capture Wonder Boy validee : les ennemis volants descendent vers le joueur, passent pres de lui, remontent, puis recommencent selon un mouvement continu et lisible.

## Preparation de la plongee validee

- Chaque plongee commence par une preparation de `0.30 s` dans la partie haute de la zone de rencontre.
- La Chauve-souris ralentit fortement sans interrompre brutalement son mouvement aerien.
- Ses ailes s'ouvrent davantage et son corps s'oriente visuellement vers Imran.
- Un petit cri unique et non agressif est joue pendant cette preparation.
- Aucun cri supplementaire n'est joue pendant la descente du meme cycle.
- La position d'Imran est memorisee uniquement a la fin des `0.30 s`, au moment ou la descente commence.
- La preparation reste complete meme si Imran change de position pendant sa duree.

## Ciblage de la plongee valide

- La position d'Imran est memorisee au moment exact ou la descente commence.
- La courbe de plongee vise cette position memorisee et non les mouvements suivants d'Imran.
- La Chauve-souris ne corrige jamais sa trajectoire pendant la descente ou le passage bas.
- Un saut, un Dash ou un changement de direction effectue apres le debut de la descente peut donc permettre d'eviter l'attaque.
- La remontee conserve elle aussi sa trajectoire sans chercher a rejoindre immediatement Imran.
- Une nouvelle position d'Imran peut etre memorisee uniquement au debut du cycle d'attaque suivant.

## Durees du cycle d'attaque validees

- La descente en courbe vers la position memorisee dure `1.40 s`.
- Le passage bas ne contient aucun arret ni temps d'attente distinct.
- La remontee vers la partie haute de la zone dure `0.80 s`.
- La trajectoire complete apres la preparation dure donc `2.20 s`.
- Un cycle comprenant les `0.30 s` de preparation dure `2.50 s`.
- Ces durees restent identiques apres un passage reussi ou evite.
- Un contact avec Imran ne relance, ne raccourcit et n'interrompt aucun de ces compteurs.

## Vitesses du cycle validees

- La descente utilise une vitesse moyenne de reference de `320 px/s`.
- La remontee utilise une vitesse moyenne de reference de `480 px/s`.
- La vitesse instantanee peut varier progressivement le long de la courbe sans produire de changement brutal.
- La descente reste volontairement plus lente afin de laisser le temps de lire et d'eviter la trajectoire.
- La remontee plus rapide eloigne la Chauve-souris apres son passage et prepare le cycle suivant.
- Ces valeurs correspondent a une trajectoire de reference proche de la portee maximale.
- Les durees restent fixes sur une trajectoire plus courte ; sa vitesse moyenne reelle est donc reduite sans modifier le rythme du cycle.

## Portee de la plongee validee

- Une plongee peut parcourir au maximum `320 px` horizontalement depuis son point de depart.
- Elle peut descendre au maximum de `320 px` verticalement.
- La position visee doit se trouver sous la Chauve-souris afin que le mouvement reste une plongee.
- Si Imran est detecte mais se trouve hors de cette portee, la Chauve-souris reste dans la partie haute de la zone et se repositionne avant de commencer sa preparation.
- La portee est verifiee une premiere fois avant la preparation de `0.30 s`.
- Elle est verifiee de nouveau a la fin de la preparation, juste avant le verrouillage de la cible.
- Si Imran n'est plus dans la portee a cette seconde verification, la plongee ne commence pas et la Chauve-souris reprend son repositionnement aerien.
- La trajectoire ne peut jamais etre allongee pour depasser ces limites.

## Repositionnement aerien valide

- Lorsque la detection est valide mais que la plongee ne peut pas commencer, la Chauve-souris reste a la hauteur de son point initial.
- Elle suit uniquement la position horizontale actuelle d'Imran.
- Sa vitesse de repositionnement est de `240 px/s`.
- Aucun mouvement vertical n'est ajoute pendant cette phase.
- Ce repositionnement ne constitue pas une attaque et n'occupe aucun emplacement d'attaque.
- Il ne produit ni cri, ni animation de preparation.
- La position horizontale d'Imran peut etre suivie en continu uniquement pendant ce repositionnement.
- Des que les portees horizontale et verticale deviennent valides, la Chauve-souris quitte ce suivi et commence sa preparation de `0.30 s`.
- Si la portee verticale reste invalide, elle termine son alignement horizontal puis attend a cette hauteur.
- Le repositionnement reste limite par les obstacles solides et les limites de la zone de rencontre.

## Contact dangereux valide

- La zone principale de `40 x 32 px` constitue aussi la zone dangereuse du corps de la Chauve-souris.
- Cette zone reste dangereuse pendant l'attente, le repositionnement, la preparation, la descente, la remontee et le retour au point initial.
- Un chevauchement avec la zone vulnerable d'Imran retire `1 coeur` si Imran n'est pas invulnerable.
- Le recul et les `1.30 s` d'invulnerabilite d'Imran s'appliquent selon les regles communes.
- Un contact continu peut infliger un nouveau degat uniquement apres la fin de cette invulnerabilite.
- Le contact ne bloque pas la Chauve-souris, ne modifie pas sa courbe et ne change pas son compteur de cycle.
- Le Bouclier de lumiere ne protege pas contre ce contact, car il bloque uniquement les projectiles venant de face.
- La zone dangereuse est desactivee immediatement lorsque la Chauve-souris entre dans l'etat `Defaite`.

## Recuperation apres la plongee validee

- Les `0.80 s` de remontee constituent toute la phase de recuperation.
- La Chauve-souris ne peut commencer aucune nouvelle plongee pendant cette remontee.
- Elle ne suit pas Imran et ne modifie pas sa trajectoire de retour vers la partie haute.
- Elle reste vulnerable aux attaques normales et au Smash Tranchant pendant toute cette phase.
- Son corps reste dangereux selon la regle de contact validee.
- Une nouvelle preparation peut commencer uniquement lorsque la remontee est terminee.
- Aucun temps d'attente supplementaire n'est ajoute si la detection, la portee et les autres conditions d'attaque restent valides.

## Gestion des emplacements d'attaque validee

- La Chauve-souris demande un emplacement d'attaque avant de commencer sa preparation.
- L'emplacement est occupe des le debut des `0.30 s` de preparation.
- Il reste occupe pendant les `1.40 s` de descente et le passage bas.
- Il est libere au moment ou commencent les `0.80 s` de remontee.
- La dangerosite permanente du corps ne prolonge pas l'occupation de cet emplacement.
- La remontee et le repositionnement aerien n'occupent aucun emplacement d'attaque.
- Une preparation annulee libere immediatement l'emplacement.
- La defaite de la Chauve-souris libere immediatement l'emplacement.
- Si les `3 emplacements` sont occupes, la Chauve-souris peut continuer son repositionnement dans la partie haute mais ne commence aucune preparation.
- Lorsqu'un emplacement se libere, la detection, la ligne de vue et la portee sont de nouveau verifiees avant toute preparation.

## Zone de detection validee

- La detection est mesuree entre le centre d'Imran et le centre de la Chauve-souris.
- Imran doit se trouver a `800 px` ou moins horizontalement.
- Imran doit se trouver a `480 px` ou moins verticalement.
- Ces valeurs correspondent aux distances maximales dans chaque axe et non a la largeur totale de la zone.
- La Chauve-souris doit egalement etre visible a l'ecran et posseder une ligne de vue libre vers Imran.
- Les conditions horizontale, verticale, de visibilite et de ligne de vue doivent etre reunies simultanement.
- La distance verticale est plus grande que celle du Slime afin de permettre une activation depuis une position aerienne lisible.
- Ces distances sont des valeurs de conception propres a Imran Adventure, car la capture commence apres l'activation des ennemis.

## Sortie de detection et retour valides

- Quitter la zone de detection, perdre la visibilite ou perdre la ligne de vue declenche les memes regles de sortie.
- Si cette perte se produit pendant l'attente active ou le repositionnement, la Chauve-souris commence immediatement son retour.
- Si elle se produit pendant la preparation, la plongee est annulee et l'emplacement d'attaque est libere immediatement.
- Si elle se produit pendant la descente, la Chauve-souris termine la descente en cours sans corriger sa trajectoire.
- L'emplacement d'attaque est alors libere au debut normal de la remontee.
- Si la perte se produit pendant la remontee, celle-ci se termine normalement.
- Apres la remontee, la Chauve-souris retourne vers son point aerien initial a `240 px/s`.
- Ce retour utilise un mouvement aerien souple et n'occupe aucun emplacement d'attaque.
- La Chauve-souris ne suit plus Imran et ne memorise aucune cible pendant le retour.
- Son corps reste dangereux pendant le retour selon la regle de contact validee.
- Si Imran redevient detectable pendant le retour, la Chauve-souris termine quand meme son trajet jusqu'au point initial.
- Une nouvelle activation peut commencer uniquement apres le retour complet et une nouvelle verification de toutes les conditions.
- Au point initial, la Chauve-souris reprend sa boucle d'attente de `1.20 s`.

## Collisions avec le decor validees

- La Chauve-souris traverse les plateformes traversables sans modifier sa trajectoire.
- Avant chaque preparation, une premiere courbe basee sur la position actuelle d'Imran est verifiee.
- Apres le verrouillage final de la cible, la courbe definitive est verifiee une seconde fois.
- Si un mur, un sol, un plafond ou un obstacle entierement solide coupe l'une de ces courbes, la plongee ne commence pas.
- Une annulation apres la preparation libere immediatement l'emplacement d'attaque.
- La Chauve-souris poursuit alors son repositionnement dans la partie haute sans occuper d'emplacement d'attaque.
- Si une collision inattendue avec un element solide se produit pendant la descente, la plongee est annulee.
- L'emplacement d'attaque est libere immediatement et la remontee commence depuis le dernier point valide.
- Une collision avec le decor ne retire aucun point de vie et ne declenche aucune reaction aux degats.
- Les zones contenant des Chauves-souris doivent offrir un passage aerien libre entre leur position haute et les positions d'attaque autorisees.
- Le retour au point initial doit lui aussi posseder un trajet libre prevu par le niveau.

## Criteres de validation

La fiche des Chauves-souris est validee car :

- la position d'attente est mesurable et reconnaissable ;
- la zone de detection possede des distances precises ;
- la plongee commence par une preparation visuelle et sonore ;
- la trajectoire et la vitesse permettent au joueur de reagir ;
- la phase dangereuse et la condition d'impact sont sans ambiguite ;
- la recuperation offre une occasion de riposte ;
- les points de vie et les dimensions sont fixes ;
- les collisions avec le decor possedent un resultat unique ;
- la Chauve-souris ne quitte jamais sa zone de rencontre ;
- chaque valeur peut etre testee dans le prototype sans decision de gameplay manquante.

## Sources

- [Chauves-souris du Concept Game](../../Concept-Game/07-Ennemis/Chauves-Souris.md)
- [Principes d'IA](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Animation](../../Concept-Game/09-Direction-Artistique/Animation.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
- [Regles communes des ennemis](Regles-Communes.md)
- [Reference video des plongees](Reference-Video-Wonder-Boy-Plongees-Chauves-Souris.md)
