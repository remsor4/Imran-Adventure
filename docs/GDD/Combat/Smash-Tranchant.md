# Smash Tranchant

> **Statut :** Valide

## Objectif

Definir l'attaque chargee de la Shadow Sword qui libere un croissant d'energie noir brillant en ligne droite.

## Sequence de commande

1. Le joueur maintient la commande de l'attaque normale.
2. Tant que les `1.50 s` de charge ne sont pas atteintes, un relachement declenche l'attaque normale.
3. Apres `1.50 s` de maintien, une animation brillante apparait autour de la Shadow Sword.
4. La lueur indique que le Smash Tranchant est pret.
5. Entre `1.50 s` et `3.00 s`, le joueur peut relacher la commande pour liberer le Smash Tranchant.
6. Si la commande est encore maintenue a `3.00 s`, le Smash Tranchant est libere automatiquement.

Une meme pression ne peut pas declencher une attaque normale puis un Smash Tranchant.

## Signal de charge complete

- La charge complete demande `1.50 s` de maintien continu.
- La lueur apparait autour de l'epee sans masquer Imran.
- Elle utilise le noir brillant et le violet clair de la Shadow Sword.
- Une impulsion sonore courte confirme que la charge est prete.
- Le signal reste visible entre `1.50 s` et le lancement manuel ou automatique.
- Le croissant d'energie apparait uniquement au lancement manuel ou automatique.

## Limite de maintien

- La duree maximale totale est de `3.00 s` depuis la pression initiale.
- La fenetre de lancement manuel dure donc `1.50 s` apres la charge complete.
- A `3.00 s`, le croissant d'energie part automatiquement dans l'orientation verrouillee.
- Apres un lancement automatique, la commande doit etre relachee avant de pouvoir commencer une nouvelle attaque.
- Le lancement automatique utilise les memes valeurs et les memes effets qu'un lancement manuel.

## Interruption connue

- Recevoir un degat annule immediatement la charge.
- Une mort ou un etat verrouille annule la charge.
- Une charge annulee par un degat, une mort ou un etat verrouille ne produit ni attaque normale, ni projectile.

## Disponibilite

- La charge du Smash Tranchant peut commencer uniquement lorsque Imran touche une surface praticable.
- Le Smash Tranchant ne peut pas etre charge ni libere pendant un saut ou une chute.
- Perdre le contact avec le sol annule la charge et fait disparaitre la lueur.
- Si la commande reste maintenue apres cette perte de contact, son relachement produit une attaque normale aerienne.
- Un maintien commence dans les airs ne remplit jamais la charge et ne produit aucune lueur.
- Son relachement produit une attaque normale, quelle que soit sa duree.

## Immobilisation pendant la charge

- Imran reste immobile des le debut du maintien au sol.
- Sa vitesse horizontale volontaire est ramenee a zero.
- Les commandes gauche et droite sont ignorees pendant toute la charge.
- Le saut, le Double saut et le Dash ne peuvent pas commencer pendant la charge.
- Le Bouclier est inactif des le debut du maintien au sol et pendant toute la charge.
- L'orientation choisie au debut de la charge est conservee jusqu'au lancement ou a l'annulation.
- Le mouvement impose par une plateforme mobile ne compte pas comme un deplacement volontaire.
- Recevoir un degat peut toujours interrompre la charge et appliquer le recul valide.

## Lancement et reprise valides

- Le projectile apparait immediatement au relachement valide ou au lancement automatique a `3.00 s`.
- Imran joue ensuite une animation de lancement de `0.35 s`.
- Il reste immobile pendant toute cette animation.
- Sa vitesse horizontale volontaire reste a zero et son orientation reste verrouillee.
- Les commandes gauche, droite, saut, Double saut, Dash, attaque et interaction sont ignorees pendant les `0.35 s`.
- Une plateforme mobile peut continuer a transporter Imran.
- La charge est terminee des que le projectile est cree ; le Bouclier redevient donc actif pendant l'animation de lancement.
- Recevoir un degat interrompt l'animation et applique le recul, sans supprimer un projectile deja cree.
- Le controle revient apres les `0.35 s` si aucun degat, aucune mort et aucun etat verrouille ne l'a interrompu.

## Projectile valide

- Le lancement cree un unique croissant d'energie qui avance horizontalement dans l'orientation verrouillee d'Imran.
- Le projectile conserve la meme taille et la meme vitesse pendant tout son trajet.
- Il ne subit ni gravite, ni acceleration, ni changement de direction.
- Sa longueur horizontale visible est de `64 px`, soit la hauteur visuelle de reference d'Imran.
- Sa hauteur visuelle et sa hauteur de collision sont de `32 px`.
- Sa vitesse constante est de `600 px/s`.
- Sa portee maximale est de `480 px`, soit `25 %` de la largeur de reference de `1920 px`.
- Sans collision, sa duree de vie maximale est de `0.80 s`.
- Lance depuis le centre de l'ecran, il parcourt ainsi la moitie de la distance entre Imran et la bordure correspondante.
- Il disparait des que sa portee maximale est atteinte.

## Degats et impacts valides

- Le projectile inflige exactement `2 degats`.
- Il disparait au premier ennemi ou boss touche.
- Il disparait au premier mur ou obstacle solide touche.
- Il ne traverse jamais plusieurs ennemis.
- Une cible ne peut recevoir les degats qu'une seule fois par projectile.
- Un impact declenche les effets visuels et sonores correspondants sans prolonger la collision offensive.

## Criteres de validation

Le Smash Tranchant est valide si :

- la charge complete demande `1.50 s` et le lancement automatique arrive a `3.00 s` ;
- Imran reste immobile et sans protection automatique pendant la preparation et la charge ;
- aucun Smash ne peut etre charge ou lance dans les airs ;
- le projectile apparait immediatement puis Imran reste immobile pendant `0.35 s` ;
- le projectile mesure `64 x 32 px`, avance a `600 px/s` et parcourt au maximum `480 px` en `0.80 s` ;
- le premier ennemi, boss, mur ou obstacle touche arrete le projectile ;
- un impact valide inflige `2 degats` une seule fois ;
- un projectile deja cree continue son trajet si Imran recoit ensuite un degat.

## Sources

- [Attaque normale](Attaque-Normale.md)
- [Priorites des actions](../Controles/Priorites-des-Actions.md)
- [Smash Tranchant du Concept Game](../../Concept-Game/05-Gameplay/Smash-Tranchant.md)
- [Shadow Sword](../../Concept-Game/05-Gameplay/Shadow-Sword.md)
- [Effets visuels](../../Concept-Game/09-Direction-Artistique/Effets-Visuels.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
