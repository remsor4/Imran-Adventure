# Serpents

> **Statut :** Valide

## Objectif

Definir un ennemi terrestre rapide et previsible qui exerce une pression a proximite sans reproduire le bond du Slime ni la patrouille armee des Squelettes.

## Identite deja validee

- Le Serpent est un ennemi terrestre rapide.
- Il attaque lorsqu'Imran s'approche.
- Son deplacement utilise un glissement sec et reconnaissable.
- Sa preparation d'attaque est annoncee par la tete et le haut du corps.
- Un souffle court accompagne cette preparation.
- Sa defaite reste courte, cartoon et sans violence graphique.

## Regles communes applicables

- Une attaque ou un contact dangereux retire `1 coeur` a Imran.
- Une attaque normale de la Shadow Sword inflige `1 degat`.
- Le Smash Tranchant inflige `2 degats`.
- Une reaction non fatale dure `0.33 s`.
- Une defaite dure `0.67 s` avant la disparition.
- Un Serpent vaincu reste absent pendant la vie en cours et ne produit aucune recompense.
- Le Serpent n'est solide ni pour Imran, ni pour les autres ennemis.
- Il est bloque par le decor solide et ne tombe jamais accidentellement dans un gouffre.
- Il ne peut pas blesser les autres ennemis.
- Les emplacements d'attaque suivent la limite commune de `3 ennemis ordinaires`.

## Methode generale validee

Le Serpent utilise une patrouille rapide permanente suivie d'une attaque de proximite :

1. Il commence a patrouiller des le chargement du niveau.
2. Il se deplace continuellement au sol dans une zone horizontale predeterminee.
3. Il conserve cette patrouille lorsque Imran se trouve hors de sa detection.
4. Lorsque les conditions d'attaque sont reunies, il annonce son attaque en relevant la tete et le haut du corps.
5. Un souffle court accompagne cette preparation.
6. Il effectue ensuite une attaque terrestre rapide vers l'avant.
7. Une courte recuperation suit l'attaque.
8. Il reprend ensuite sa patrouille.

Cette methode le distingue du Slime immobile avant son activation et des Squelettes dont la patrouille produit directement leur pression principale.

## Dimensions validees

- L'enveloppe visuelle normale du Serpent mesure `64 x 32 px`.
- Pendant la preparation, la tete et le haut du corps peuvent atteindre une hauteur visuelle maximale de `48 px`.
- La collision principale avec le decor mesure `52 x 20 px`.
- La zone vulnerable mesure `48 x 24 px`.
- La zone dangereuse permanente du corps mesure `48 x 20 px`.
- Toutes les zones restent centrees sur le corps et alignees avec le sol.
- Le redressement de la tete augmente uniquement la hauteur visuelle.
- La collision principale et la zone vulnerable ne changent pas pendant la preparation.
- La zone propre a l'attaque sera definie separement.
- La longueur visuelle de `64 px` correspond a la hauteur visuelle de reference d'Imran.

## Points de vie valides

- Le Serpent possede `1 PV`.
- Une attaque normale de la Shadow Sword le vainc immediatement.
- Un Smash Tranchant le vainc egalement au premier impact.
- Sa difficulte repose sur sa vitesse, sa proximite et son rythme d'attaque.
- Il utilise directement la defaite commune de `0.67 s` sans reaction non fatale.
- Il ne produit aucune recompense lors de sa disparition.

## Vitesse de patrouille validee

- Le Serpent patrouille a une vitesse constante de `200 px/s`.
- Cette vitesse est environ `43 %` plus elevee que les `140 px/s` des Squelettes.
- Elle reste inferieure aux `240 px/s` d'Imran.
- Imran peut donc distancer le Serpent sans utiliser son Dash.
- La preparation et l'attaque possederont leurs propres regles de mouvement.

## Zone de patrouille validee

- La zone horizontale de patrouille mesure `640 px`.
- Elle s'etend sur `320 px` de chaque cote de la position initiale.
- La position initiale constitue le centre fixe de cette zone.
- L'orientation initiale est determinee par le placement du Serpent dans le niveau.
- Le Serpent fait demi-tour sans pause lorsqu'il atteint une limite.
- Il conserve sa vitesse de `200 px/s` apres le demi-tour.
- Un trajet d'une limite a l'autre dure `3.20 s`.
- Un aller-retour complet dure `6.40 s`.
- La zone reste entierement incluse dans la zone de rencontre.
- Un mur, un bord dangereux ou une surface trop courte peut reduire la distance parcourue sans agrandir la zone.

## Detection validee

- La detection est mesuree entre le centre d'Imran et le centre du Serpent.
- Imran doit se trouver a `320 px` ou moins horizontalement.
- Imran doit se trouver a `120 px` ou moins verticalement.
- Le Serpent doit etre visible a l'ecran.
- Une ligne de vue libre entre le Serpent et Imran est obligatoire.
- Les quatre conditions doivent etre reunies simultanement.
- La detection autorise uniquement la preparation d'une attaque.
- Elle ne modifie ni la vitesse, ni la direction, ni les limites de la patrouille.
- Sortir de la detection ou perdre la ligne de vue empeche le debut d'une nouvelle preparation.

## Orientation face a Imran validee

- Le Serpent peut preparer une attaque uniquement si Imran se trouve devant lui.
- Si Imran entre dans la detection par-derriere, le Serpent ne fait pas demi-tour.
- Il continue sa patrouille a `200 px/s`.
- La position d'Imran ne modifie jamais directement son orientation.
- Seules une limite de patrouille, un mur ou un bord dangereux provoquent un demi-tour.
- Apres un demi-tour normal, le Serpent peut attaquer si Imran reste detecte et se trouve maintenant devant lui.
- Cette regle interdit tout retournement instantane pendant une approche.

## Distance de declenchement validee

- Imran doit se trouver devant le Serpent.
- La distance horizontale maximale de declenchement est de `160 px`.
- La distance verticale maximale de declenchement est de `80 px`.
- Le Serpent doit toujours etre visible a l'ecran et posseder une ligne de vue libre.
- Toutes les conditions sont verifiees avant le debut de la preparation.
- Entre `160 px` et `320 px` horizontalement, le Serpent continue uniquement sa patrouille.
- Une detection ne produit donc pas automatiquement une attaque.

## Preparation de l'attaque validee

- La preparation dure `0.50 s`.
- Le Serpent interrompt sa patrouille et reste completement immobile.
- Il releve visiblement la tete et le haut du corps jusqu'a une hauteur maximale de `48 px`.
- Un souffle court et reconnaissable accompagne le redressement.
- La zone propre a l'attaque reste inactive pendant toute la preparation.
- La zone dangereuse permanente du corps reste active.
- Le Serpent occupe un emplacement d'attaque des le debut de la preparation.
- Une attaque d'Imran pendant cette duree vainc le Serpent, annule l'attaque et libere immediatement l'emplacement.

## Forme de l'attaque validee

- A la fin de la preparation, le Serpent effectue une projection horizontale vers l'avant.
- Il allonge brusquement son corps et glisse au ras du sol.
- La direction est verrouillee au debut du mouvement.
- Le Serpent ne suit pas la position d'Imran pendant l'attaque.
- Il ne peut ni se retourner, ni modifier sa trajectoire avant la fin du mouvement.
- Imran peut eviter cette attaque en sautant, en reculant ou en passant derriere le Serpent avant la projection.
- Cette attaque ne produit aucun projectile.

## Valeurs de la projection validees

- La projection parcourt une distance maximale de `128 px`.
- Cette distance est mesuree depuis le centre du Serpent au debut du mouvement.
- La phase dure `0.25 s`.
- Le Serpent se deplace a une vitesse constante de `512 px/s`.
- Le calcul utilise `128 / 0.25 = 512 px/s`.
- La direction et la vitesse ne changent jamais pendant la projection.
- La zone propre a l'attaque reste dangereuse pendant toute la duree de `0.25 s`.
- La projection est environ `2.13 fois` plus rapide que la course d'Imran a `240 px/s`.

## Zone dangereuse et degats de l'attaque valides

- La zone dangereuse propre a l'attaque mesure `32 x 24 px`.
- Elle est placee sur la tete, devant le corps du Serpent.
- Elle devient active au debut de la projection.
- Elle reste active pendant toute la duree de `0.25 s`.
- Elle est desactivee immediatement a la fin de la projection.
- Un impact retire `1 coeur` a Imran.
- Une meme projection ne peut infliger ses degats qu'une seule fois.
- La zone dangereuse permanente du corps reste active pendant l'attaque.
- Si la tete et le corps touchent Imran sur la meme image, un seul coeur est retire.
- Le recul et les `1.30 s` d'invulnerabilite standards d'Imran sont appliques.
- L'attaque ne blesse jamais un autre ennemi.

## Recuperation validee

- La recuperation dure `0.75 s`.
- Le Serpent reste immobile pendant toute cette duree.
- La tete et le haut du corps redescendent vers la posture de patrouille.
- La zone propre a l'attaque reste desactivee.
- La zone dangereuse permanente du corps reste active.
- L'emplacement d'attaque est libere des la fin de la projection.
- Une attaque d'Imran pendant la recuperation vainc immediatement le Serpent.
- A la fin des `0.75 s`, le Serpent reprend sa patrouille.

## Position finale et chemin d'attaque valides

- Le Serpent reste a la position atteinte apres les `128 px` de projection.
- Il ne revient jamais automatiquement au point de depart de l'attaque.
- Apres la recuperation, il reprend sa patrouille dans la meme direction.
- Si la position finale correspond a une limite, il fait demi-tour avant de recommencer a avancer.
- Avant la preparation, le trajet complet de `128 px` est verifie.
- Le trajet doit rester dans la zone de patrouille.
- Il doit posseder un sol continu et ne traverser aucun mur, obstacle solide ou gouffre.
- Si le trajet n'est pas valide, la preparation ne commence pas.
- Aucun emplacement d'attaque n'est alors occupe.
- Le Serpent continue sa patrouille et applique le demi-tour normal impose par la limite ou le decor.

## Verrouillage pendant la preparation valide

- Toutes les conditions de declenchement sont verifiees au debut de la preparation.
- La direction de la projection est ensuite verrouillee.
- Le Serpent ne recalcule jamais la position d'Imran pendant les `0.50 s`.
- Si Imran saute, recule, passe derriere le Serpent ou quitte la detection, l'attaque continue.
- Si Imran quitte l'ecran apres avoir vu la preparation, l'attaque peut egalement se terminer.
- Ces mouvements constituent des esquives et non des annulations automatiques.
- Seule la defaite du Serpent ou un trajet devenu impossible annule l'attaque.
- Une annulation libere immediatement l'emplacement d'attaque.

## Cadence d'attaque validee

- Aucun delai supplementaire n'est ajoute apres la recuperation.
- Un cycle complet minimal dure `1.50 s`.
- Ce total utilise `0.50 s` de preparation, `0.25 s` de projection et `0.75 s` de recuperation.
- A la fin de la recuperation, toutes les conditions de declenchement sont de nouveau verifiees.
- Le Serpent doit obtenir un nouvel emplacement d'attaque.
- Aucune attaque suivante n'est memorisee ou declenchee automatiquement.
- Si les conditions ne sont plus reunies, il reprend sa patrouille a `200 px/s`.

## Collisions avec le decor validees

- Une plateforme traversable supporte le Serpent comme un sol.
- Le Serpent ne saute jamais et ne descend jamais volontairement d'une plateforme.
- Devant un mur, une limite de patrouille ou un gouffre, il fait demi-tour sans pause.
- Il ne tombe jamais accidentellement d'une surface.
- Si le trajet devient impossible pendant la preparation, l'attaque est annulee.
- L'emplacement d'attaque est alors libere et le Serpent reprend son comportement de patrouille.
- Si un obstacle solide est rencontre pendant la projection, le Serpent s'arrete au dernier point valide.
- La zone propre a l'attaque est desactivee immediatement.
- La projection prend fin et la recuperation de `0.75 s` commence.
- L'emplacement d'attaque est libere au moment ou la projection s'arrete.
- Une collision avec le decor ne retire aucun point de vie au Serpent.
- La zone de patrouille utilise uniquement la portion de sol praticable.

## Sortie de la rencontre et reinitialisation validees

- Quitter la detection ou la zone de rencontre ne renvoie pas le Serpent au centre de sa patrouille.
- Il continue sa patrouille depuis sa position courante.
- Une attaque dont la preparation a deja commence peut se terminer normalement.
- Aucun nouveau cycle d'attaque ne commence si les conditions de detection ne sont plus reunies.
- Revenir dans la zone ne provoque aucune teleportation et ne modifie pas son orientation.
- Une perte de vie, un Game Over, un abandon ou un rechargement du niveau replace le Serpent a sa position initiale.
- Cette reinitialisation restaure son orientation initiale, son `1 PV` et son cycle de patrouille.

## Emplacements d'attaque valides

- Le Serpent demande un emplacement avant de commencer sa preparation.
- Si aucun emplacement n'est disponible, il continue sa patrouille a `200 px/s`.
- Il ne se redresse pas et ne produit aucun souffle de preparation pendant cette attente.
- Aucune attaque n'est memorisee.
- Lorsqu'un emplacement se libere, toutes les conditions sont de nouveau verifiees.
- L'emplacement reste occupe pendant les `0.50 s` de preparation et les `0.25 s` de projection.
- Il est libere des le debut de la recuperation de `0.75 s`.
- Une annulation ou la defaite du Serpent libere immediatement l'emplacement.
- La limite commune de `3 ennemis ordinaires` reste applicable.

## Contact dangereux permanent valide

- La zone dangereuse corporelle mesure `48 x 20 px`.
- Elle reste active en permanence tant que le Serpent est vivant.
- Un contact avec le corps retire `1 coeur` a Imran, quel que soit le cote touche.
- Cette regle reste active pendant la patrouille, la preparation, la projection et la recuperation.
- Le recul et les `1.30 s` d'invulnerabilite standards d'Imran sont appliques.
- Si la zone corporelle et la zone de tete touchent Imran pendant la meme attaque, un seul coeur est retire.
- La zone dangereuse corporelle et la zone d'attaque sont desactivees immediatement lorsque le Serpent entre dans l'etat `Defaite`.

## Interruption et defaite validees

- Le Serpent possede `1 PV` et ne peut donc jamais subir une reaction non fatale.
- Une attaque normale ou un Smash Tranchant le vainc immediatement.
- Un impact pendant la patrouille, la preparation, la projection ou la recuperation interrompt son action.
- Son mouvement et toutes ses zones dangereuses sont desactives immediatement.
- Un emplacement d'attaque eventuellement occupe est libere.
- Sa defaite cartoon dure `0.67 s` avant sa disparition.
- Il reste absent pendant le reste de la vie en cours et ne produit aucune recompense.

## Criteres de validation

La fiche des Serpents sera validee si :

- ses dimensions, ses points de vie et sa vitesse sont fixes ;
- son deplacement rapide reste different de celui des Slimes et des Squelettes ;
- sa detection et sa distance d'attaque sont mesurables ;
- sa preparation visuelle et sonore laisse un temps de reaction clair ;
- son attaque possede une portee, une vitesse, une duree et des degats ;
- sa recuperation produit une occasion de riposte ;
- ses collisions et ses limites de patrouille sont previsibles ;
- aucune valeur de gameplay ne reste a decider pendant le prototype.

## Sources

- [Serpents du Concept Game](../../Concept-Game/07-Ennemis/Serpents.md)
- [Principes d'IA](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Animation](../../Concept-Game/09-Direction-Artistique/Animation.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
- [Regles communes des ennemis](Regles-Communes.md)
