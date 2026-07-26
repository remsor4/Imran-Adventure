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

## Regles deja acquises

- Les sept combats de boss sont obligatoires.
- Chaque attaque de boss retire `1 coeur` par defaut.
- L'attaque normale de la Shadow Sword inflige `1 degat`.
- Le Smash Tranchant inflige `2 degats` au premier boss touche puis disparait.
- Un projectile frontal peut etre bloque automatiquement par le Bouclier de lumiere.
- Une perte de vie restaure le boss a sa vie maximale et a sa premiere phase.
- La barre de vie est centree en haut de l'ecran pendant le combat.
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
- La fermeture de l'arene reste active apres la defaite.
- Imran ne peut donc pas quitter l'arene sans recuperer la cle.
- Le coffre passe de l'etat `Protege` a l'etat `Disponible` apres la fin de la sequence de defaite.
- Aucune interaction avec le coffre n'est possible pendant cette sequence.
- Lorsque le controle revient, l'arene constitue une zone sure sans ennemi ni danger.
- Imran doit rejoindre le coffre et utiliser la commande `Interaction`.
- L'ouverture du coffre ajoute automatiquement la cle, declenche la sauvegarde et termine le niveau selon les regles deja validees.
- La victoire contre le golem seule ne termine jamais le niveau.
- Le combat final contre Tata Lisa ne possede aucun coffre et suit une conclusion distincte.

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
- Le golem produit d'abord un eclat visuel bref.
- Sa silhouette se fragmente ensuite en particules liees a son element.
- Les particules se dispersent puis disparaissent completement.
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
