# Attaque normale

> **Statut :** Valide

## Objectif

Definir l'attaque courte de la Shadow Sword et son partage de commande avec le Smash Tranchant.

## Commande partagee

- Une pression sur la commande d'attaque commence l'observation de sa duree.
- Au sol, si la commande est relachee avant `1.50 s`, l'attaque normale est declenchee au relachement.
- Au sol, si la charge complete est atteinte, l'attaque normale est remplacee par le Smash Tranchant.
- Dans les airs, le maintien ne charge jamais le Smash et le relachement declenche toujours l'attaque normale.
- Une meme pression ne peut jamais produire les deux attaques.
- Une nouvelle attaque demande une nouvelle pression apres le retour a un etat compatible.

## Nombre de coups

- Une pression courte produit exactement un seul coup d'epee.
- Il n'existe aucun enchainement automatique de plusieurs coups.
- Maintenir la commande ne repete jamais l'attaque normale.
- Un nouveau coup demande une nouvelle pression et un nouveau relachement de la commande.
- Une pression recue pendant l'animation du coup est ignoree.
- Cette pression n'est jamais memorisee pour lancer une attaque apres l'animation.
- Une nouvelle commande devient acceptable uniquement lorsque l'attaque precedente est entierement terminee.

## Retours au joueur

- Une pression courte conserve une reponse rapide et une trajectoire d'epee lisible.
- La charge commence sans jouer l'effet complet du Smash.
- Le signal brillant de charge complete appartient au Smash Tranchant.

## Duree validee

- Une attaque normale dure au total `0.35 s` a partir de son declenchement.
- Cette duree est identique pour l'attaque au sol et l'attaque aerienne.
- A `30 images/s`, elle correspond a environ 10 a 11 images et reprend le rythme observe dans la capture de reference de *Wonder Boy*.
- Au sol, le controle revient a la fin de ces `0.35 s`, sauf si l'attaque est interrompue par un degat ou un etat prioritaire.
- Dans les airs, les `0.35 s` limitent uniquement l'animation d'attaque : la trajectoire et le controle aerien continuent normalement.

## Fenetre active validee

- La collision offensive de la lame reste active pendant `0.10 s`.
- Cette fenetre commence a la premiere image ou la lame entre dans sa posture offensive.
- A `60 images/s`, elle correspond a `6 images`.
- La meme fenetre active est utilisee pour l'attaque au sol et l'attaque aerienne.
- L'effet visuel d'impact et le bref arret produit par un contact peuvent continuer apres cette fenetre sans prolonger la collision offensive.

## Portee validee

- La portee horizontale maximale de la lame est de `48 px` depuis le centre d'Imran dans la direction regardee.
- Cette distance correspond a environ trois quarts de la hauteur visuelle de reference d'Imran, fixee a `64 px`.
- Avec le collider principal de `36 px` de large, la lame atteint environ `30 px` au-dela de son bord avant.
- La zone offensive est retournee horizontalement lorsque Imran change d'orientation.
- Elle ne touche jamais une cible placee derriere Imran.

## Dimensions visuelles de la Shadow Sword

- La Shadow Sword mesure `56 px` de la pointe au pommeau pendant le gameplay.
- Sa largeur maximale est de `16 px` au niveau de la garde.
- Sa longueur represente environ `85 %` a `90 %` de la hauteur visuelle d'Imran.
- Ces proportions reprennent l'epee visible au repos dans la capture de reference de *Wonder Boy*.
- La rotation et la perspective de l'animation peuvent reduire sa longueur apparente sans modifier sa longueur de reference.
- La portee offensive reste fixee a `48 px` depuis le centre d'Imran et suit la pointe visible de la lame.
- L'illustration source conserve sa haute definition ; les dimensions indiquees correspondent a son affichage dans le gameplay.

## Degats valides

- Une attaque normale reussie inflige exactement `1 degat` a chaque cible touchee.
- Une meme cible ne peut recevoir ce degat qu'une seule fois pendant une attaque.
- Les degats sont identiques au sol et dans les airs.
- La vitesse, la distance et le moment du contact ne modifient jamais cette valeur.

## Observation de la pression au sol

- Des que la commande est maintenue au sol, Imran s'arrete pour preparer une possible charge.
- Sa vitesse horizontale volontaire revient a zero.
- Le deplacement horizontal, le saut et le Dash sont bloques jusqu'au relachement de la commande.
- Le Bouclier est inactif pendant tout le maintien au sol, meme avant que les `1.50 s` de charge soient atteintes.
- Un relachement avant `1.50 s` produit l'attaque normale puis rend le controle selon la duree de cette attaque.
- Cette immobilisation ne s'applique pas lorsque la commande commence pendant un saut ou une chute.

## Immobilisation pendant le coup au sol

- Imran reste immobile pendant toute l'animation de l'attaque normale au sol.
- Sa vitesse horizontale volontaire reste a zero.
- Les commandes gauche, droite, saut, Double saut et Dash sont ignorees jusqu'a la fin de l'animation.
- L'orientation choisie au declenchement du coup reste verrouillee pendant l'animation.
- Une plateforme mobile peut transporter Imran sans annuler son attaque.
- Recevoir un degat peut interrompre l'attaque et appliquer le recul valide.
- Le controle revient uniquement lorsque l'animation est entierement terminee.

## Disponibilite

- L'attaque normale peut etre declenchee au sol.
- Elle peut aussi etre declenchee pendant un saut ou une chute.
- Le joueur peut appuyer sur Saut et Attaque au meme instant lorsqu'Imran est au sol.
- Dans ce cas, le saut commence en premier et le coup est traite comme une attaque aerienne.
- Cette combinaison ne declenche pas l'immobilisation propre a l'attaque au sol.
- Pendant un saut ou une chute, sa disponibilite ne depend pas de la duree de maintien de la commande.
- Une attaque aerienne ne suspend ni la gravite, ni la vitesse verticale.
- La vitesse horizontale deja en cours est conservee pendant toute l'animation aerienne.
- Les commandes gauche et droite restent actives avec le controle horizontal normal du saut.
- L'attaque ne fige, ne raccourcit et ne prolonge jamais la trajectoire du saut ou de la chute.
- Elle ne restaure pas le Double saut et ne modifie pas sa disponibilite.
- Elle reste impossible pendant un Dash, un degat, une interaction, une mort ou un etat verrouille.
- Apres le relachement, le Bouclier peut bloquer un projectile frontal pendant l'attaque normale, meme si Imran est en mouvement.

## Reference de gameplay

Les captures de *Wonder Boy* fournies par Rems le 17 juillet 2026 confirment le comportement recherche :

- au sol, le personnage arrete son deplacement pendant toute l'animation du coup ;
- en l'air, le coup d'epee se joue sans interrompre la trajectoire horizontale ou verticale du saut ;
- le personnage continue sa montee ou sa chute jusqu'a la reception normale.
- dans la capture a `60 images/s`, le premier impact visible arrive entre `0.067 s` et `0.083 s` apres le debut offensif du coup, ce qui justifie une fenetre active de `0.10 s`.
- la distance entre le centre du personnage et la pointe de la lame represente environ trois quarts de sa hauteur visuelle, ce qui donne une portee normalisee de `48 px` pour Imran.
- au repos, la longueur totale de l'epee represente environ `85 %` a `90 %` de la hauteur du personnage, ce qui donne `56 px` pour Imran.

## Criteres de validation

L'attaque normale est validee si :

- une pression courte produit un seul coup et aucun enchainement automatique ;
- une nouvelle commande recue pendant le coup est ignoree ;
- l'animation dure `0.35 s` et la collision reste active pendant `0.10 s` ;
- la lame atteint `48 px` depuis le centre d'Imran et inflige `1 degat` ;
- Imran reste immobile pendant un coup au sol ;
- une attaque aerienne conserve la trajectoire et le controle horizontal du saut ou de la chute ;
- la Shadow Sword reste lisible avec une longueur de `56 px` ;
- le Bouclier peut proteger Imran pendant l'attaque apres le relachement de la commande.

## Sources

- [Smash Tranchant](Smash-Tranchant.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Shadow Sword](../../Concept-Game/05-Gameplay/Shadow-Sword.md)
- [Combat du Concept Game](../../Concept-Game/05-Gameplay/Combat.md)
- [Reference video du combat Wonder Boy](Reference-Video-Wonder-Boy-Combat.md)
