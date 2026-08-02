# Niveau 0 - Village des Bles

> **Statut :** Valide

La fiche detaillee du niveau 0 sera redigee pendant l'etape 12 a partir du tutoriel valide dans le Concept Game. Elle integrera des pancartes pour le Dash au sol, le Double saut et la protection automatique du Bouclier face aux projectiles, meme pendant les mouvements.

## Dimensions generales

- Le niveau utilise la resolution de reference `1920 x 1080`.
- Sa largeur horizontale de reference est fixee a `15 360 px`.
- Cette largeur correspond a environ `8 ecrans` complets.
- Le parcours reste continu, horizontal et sans embranchement.
- Cette longueur doit permettre de presenter les `7 apprentissages` sans rapprocher excessivement les exercices.

## Depart d'Imran

- Imran commence avec son centre horizontal a `x = 864 px`.
- Ses pieds reposent sur le sol dont la surface est placee a `y = 896 px`.
- Il est tourne vers la droite, dans le sens de progression.
- Il commence avec `3 coeurs`, `3 vies`, une vitesse nulle et toutes ses actions disponibles.
- La camera est placee et stabilisee avant l'apparition de l'image jouable.
- Imran apparait a `45 %` de la largeur de l'ecran, conformement au cadrage vers la droite.
- Son centre visuel se trouve approximativement a `y = 864 px`, dans la position verticale cible de la camera.
- Aucun ennemi, projectile ou autre danger ne peut atteindre la zone de depart.

## Regle de progression du tutoriel

- Aucun exercice ne declenche de porte, de barriere ou de controle invisible obligatoire.
- Le saut et le Double saut sont necessaires pour franchir naturellement la geometrie du parcours.
- Le Dash est propose sur une ligne droite sure, mais le passage reste possible sans l'utiliser.
- L'attaque normale, le Smash Tranchant et le Bouclier sont presentes dans des situations adaptees, mais leur execution ne conditionne pas la sortie.
- Le Slime bleu et le Squelette archer restent evitables.
- Aucun ennemi ordinaire ne doit etre elimine pour continuer.
- Le joueur peut poursuivre le niveau meme s'il ne realise pas un exercice facultatif.

## Decoupage horizontal

Les limites suivantes servent de reperes de conception. Elles ne provoquent aucun arret ni changement brutal de camera.

| Zone | Intervalle horizontal | Contenu principal |
|---:|---:|---|
| 1 | `x = 0 a 1 920 px` | Deplacement horizontal |
| 2 | `x = 1 920 a 3 840 px` | Saut |
| 3 | `x = 3 840 a 5 760 px` | Double saut |
| 4 | `x = 5 760 a 7 680 px` | Dash au sol |
| 5 | `x = 7 680 a 9 600 px` | Attaque normale et Slime bleu |
| 6 | `x = 9 600 a 11 520 px` | Smash Tranchant |
| 7 | `x = 11 520 a 13 440 px` | Bouclier automatique et Squelette archer |
| 8 | `x = 13 440 a 15 360 px` | Feu de camp, sortie et transition |

- Chaque zone d'apprentissage commence par sa pancarte.
- La situation de pratique se trouve apres la pancarte dans le sens de progression.
- Une courte respiration separe la pratique de la pancarte suivante.
- Le defilement de camera reste continu sur toute la largeur du niveau.

## Placement des pancartes

| Pancarte | Position horizontale |
|---|---:|
| Deplacement horizontal | `x = 1 152 px` |
| Saut | `x = 2 048 px` |
| Double saut | `x = 3 968 px` |
| Dash au sol | `x = 5 888 px` |
| Attaque normale | `x = 7 808 px` |
| Smash Tranchant | `x = 9 728 px` |
| Bouclier automatique | `x = 11 648 px` |

- La premiere pancarte est visible dans le cadrage initial.
- Chaque pancarte suivante est placee `128 px` apres le debut de sa zone.
- Toutes les pancartes sont placees avant leur exercice dans le sens de progression.
- Aucune pancarte ne modifie le point de reapparition ou la sauvegarde.

## Contenu des pancartes

Les noms entre accolades sont remplaces par la commande correspondant au dernier appareil utilise.

| Pancarte | Message de reference |
|---|---|
| Deplacement | `Utilise {GAUCHE} et {DROITE} pour deplacer Imran.` |
| Saut | `Appuie sur {SAUT} pour sauter.` |
| Double saut | `Dans les airs, appuie encore sur {SAUT} pour effectuer un Double saut.` |
| Dash | `Au sol, appuie sur {DASH} pour avancer rapidement.` |
| Attaque normale | `Appuie brievement sur {ATTAQUE}, puis relache pour donner un coup.` |
| Smash Tranchant | `Maintiens {ATTAQUE}. Quand l'epee brille, relache pour lancer le Smash Tranchant.` |
| Bouclier | `Fais face au projectile. Le Bouclier le bloque automatiquement, meme en mouvement.` |

- Le texte reste court et peut utiliser deux lignes au maximum.
- Une icone complete le texte sans remplacer les mots.
- Le message du Bouclier montre une fleche dirigee vers le projectile.

## Zone d'affichage des pancartes

- Chaque pancarte possede une zone d'affichage centree de `320 x 192 px`.
- Le message apparait lorsque le centre d'Imran se trouve a `160 px` ou moins horizontalement et a `96 px` ou moins verticalement.
- L'affichage est automatique et ne demande aucune commande d'interaction.
- Quitter la zone masque le message.
- Revenir dans la zone permet de relire le meme message.
- La touche ou le bouton affiche correspond toujours au dernier appareil utilise et au remappage actuel.
- La pancarte du Bouclier affiche une direction et aucune commande de blocage.
- L'affichage ne met pas le jeu en pause et ne bloque aucune commande.
- La camera et les animations continuent normalement pendant la lecture.
- Aucun ennemi, projectile ou danger ne peut entrer dans la zone d'affichage d'une pancarte.

## Chutes non punitives

- Les exercices de saut et de Double saut possedent un sol de securite sous les plateformes.
- Une chute sur ce sol ne retire aucun coeur et ne consomme aucune vie.
- Imran conserve immediatement son controle apres l'atterrissage.
- Une pente douce permet de revenir au debut de l'exercice sans saut obligatoire.
- Aucun replacement automatique, teleportation ou plateforme mobile n'est utilise.
- Le chemin inferieur ne permet pas de contourner la plateforme que le joueur doit atteindre pour continuer.

## Hauteurs des exercices de plateforme

- La surface du sol principal est placee a `y = 896 px` dans la scene de reference `1920 x 1080`.
- La plateforme de l'exercice de saut est placee `64 px` au-dessus de sa surface de depart.
- Sa surface praticable est donc placee a `y = 832 px`.
- Cette hauteur reste inferieure a la hauteur maximale visee de `89 px` du saut normal.
- La plateforme de l'exercice de Double saut est placee `128 px` au-dessus de sa surface de depart.
- Sa surface praticable est donc placee a `y = 768 px`.
- Cette seconde hauteur ne peut pas etre atteinte avec le seul saut normal.
- Elle reste accessible avec le saut normal suivi du Double saut.
- Les deux elevations utilisent des multiples de la grille logique de `64 px`.
- Chaque surface de reception mesure `512 px` de large.
- Cette largeur correspond a `8 grilles logiques`.
- Elle offre le double de la reception sure minimale de `256 px`.

## Exercice du saut

- La zone 2 utilise une seule plateforme praticable de `512 px` de large.
- Sa surface est placee a `y = 832 px`, soit `64 px` au-dessus du sol principal.
- Le joueur doit effectuer un seul saut normal pour atteindre cette surface.
- Un sol inferieur sans danger recueille Imran en cas d'echec.
- Une pente douce ramene Imran au point de depart de l'exercice.
- Aucun ennemi, projectile ou autre danger n'est present.
- La sortie de la plateforme conduit vers une reception sure avant la pancarte du Double saut.
- Le bord de depart se trouve a `x = 2 688 px`.
- Une ouverture de `128 px` separe ce bord de la plateforme.
- La plateforme occupe `x = 2 816 a 3 328 px` avec sa surface a `y = 832 px`.
- Le sol de securite de l'ouverture se trouve a `y = 960 px`.
- Une pente entre `x = 2 560 et 2 688 px` ramene Imran vers la gauche apres un echec.
- Une pente entre `x = 3 328 et 3 456 px` redescend vers le sol principal apres la reception.

## Exercice du Double saut

- La zone 3 utilise une seule plateforme praticable de `512 px` de large.
- Sa surface est placee a `y = 768 px`, soit `128 px` au-dessus du sol principal.
- Le bord de depart se trouve a `x = 4 480 px`.
- Une ouverture de `192 px` separe ce bord de la plateforme.
- La plateforme occupe `x = 4 672 a 5 184 px`.
- Le saut normal seul ne peut pas atteindre la reception.
- Le joueur doit utiliser le saut normal puis le Double saut.
- Le sol de securite de l'ouverture se trouve a `y = 960 px`.
- Une pente entre `x = 4 352 et 4 480 px` permet de recommencer apres un echec.
- Une pente entre `x = 5 184 et 5 376 px` redescend vers le sol principal.
- Aucun ennemi, projectile ou autre danger n'est present.

## Exercice du Dash

- La pratique se deroule sur une ligne droite et plate de `768 px`.
- La surface reste placee a `y = 896 px`.
- La zone ne contient aucun vide, ennemi, projectile ou autre danger.
- Deux marques visuelles au sol sont espacees de `128 px`.
- Cet intervalle represente approximativement la distance theorique de `124 px` du Dash.
- Les marques restent indicatives et ne possedent aucune collision.
- Aucun controle ne verifie que le joueur utilise le Dash.
- Le passage reste possible en marchant.
- La piste occupe `x = 6 400 a 7 168 px`.
- Les deux marques sont centrees a `x = 6 656 px` et `x = 6 784 px`.

## Exercice de l'attaque normale

- La pancarte de l'attaque normale apparait au debut de la zone 5.
- La rencontre du Slime occupe l'intervalle `x = 8 448 a 9 408 px`.
- Cette surface plate mesure `960 px` et reste placee a `y = 896 px`.
- Le Slime de base entierement bleu commence au centre, a `x = 8 928 px`.
- Son orientation initiale est tournee vers la gauche, dans la direction d'arrivee d'Imran.
- Sa patrouille de `448 px` reste comprise entre `x = 8 704 et 9 152 px`.
- Sa detection, son bond, ses degats et son retour suivent integralement la fiche des Slimes.
- Il possede `1 PV` et une attaque normale le bat en un coup.
- Imran peut aussi sauter au-dessus du Slime et continuer sans le vaincre.
- Le Slime ne quitte jamais cette rencontre et ne peut pas atteindre les zones voisines.

## Exercice du Smash Tranchant

- La pancarte du Smash Tranchant apparait au debut de la zone 6.
- La pratique utilise un mannequin d'entrainement compose de bois et de paille.
- Le mannequin reste immobile et ne possede aucune zone dangereuse.
- Sa collision ne bloque pas le passage d'Imran.
- Il ne peut pas etre detruit et ne donne aucune recompense.
- La zone de pratique reste plate, sure et libre de tout ennemi ou projectile.
- Imran dispose du temps necessaire pour atteindre la charge complete de `1.50 s`.
- Aucun controle ne verifie que le mannequin a ete touche avant de poursuivre.
- Une attaque normale produit un petit balancement du mannequin et un impact leger.
- Un Smash Tranchant produit un mouvement plus ample, un effet d'impact plus marque et un son plus puissant.
- Les deux reactions restent visuellement et auditivement distinctes.
- Le mannequin revient automatiquement a sa position initiale apres chaque reaction.
- Une reaction en cours ne transforme jamais le mannequin en obstacle.
- Une marque de placement conseillee est affichee au sol devant le mannequin.
- La marque et le centre du mannequin sont separes de `320 px`.
- Cette distance reste inferieure de `160 px` a la portee maximale de `480 px` du projectile.
- La marque reste facultative et ne bloque pas les autres positions de tir.
- La marque conseillee est centree a `x = 10 304 px`.
- Le mannequin est centre a `x = 10 624 px` avec ses pieds sur le sol a `y = 896 px`.

## Exercice du Bouclier de lumiere

- La pancarte du Bouclier apparait au debut de la zone 7.
- Elle ne montre aucune commande de blocage et explique qu'Imran doit faire face au projectile.
- Elle precise que la protection fonctionne aussi pendant les mouvements.
- La rencontre de l'Archer occupe l'intervalle `x = 12 032 a 13 312 px`.
- Cette surface plate mesure `1 280 px` et reste placee a `y = 896 px`.
- Un seul Squelette archer est utilise.
- Il commence au centre de la rencontre, a `x = 12 672 px`.
- Son orientation initiale est tournee vers la gauche, dans la direction d'arrivee d'Imran.
- Sa patrouille de `800 px` reste comprise entre `x = 12 272 et 13 072 px`.
- Les marges entre la patrouille et les limites de la rencontre mesurent `240 px` de chaque cote.
- Sa detection, sa patrouille, sa cadence et ses fleches suivent integralement la fiche des Squelettes.
- Une fleche venant de face disparait immediatement contre le Bouclier sans retirer de coeur.
- L'Archer possede `2 PV`, mais Imran peut le depasser sans le vaincre.

## Separation avant la zone finale

- Une pile de bottes de paille occupe l'intervalle `x = 13 312 a 13 440 px`.
- Elle mesure `128 px` de large et `128 px` de haut depuis le sol place a `y = 896 px`.
- Elle constitue un decor solide pour Imran, l'Archer et les fleches.
- Une fleche qui touche les bottes disparait selon les regles normales de collision avec le decor.
- Le Squelette archer ne peut pas franchir cette separation.
- Imran utilise le Double saut deja enseigne pour passer au-dessus.
- Apres les bottes, une surface plate sure d'au moins `256 px` permet sa reception.
- Aucun ennemi ou projectile ne peut atteindre cette surface depuis la rencontre precedente.

## Feu de camp final

- Le feu de camp est centre a `x = 14 400 px` dans la zone 8.
- Sa zone sure s'etend de `x = 14 016 a 14 784 px`.
- Elle mesure `768 px`, soit `384 px` de chaque cote du feu.
- Le sol reste plat a `y = 896 px` sur toute cette zone.
- Aucun ennemi, projectile, piege ou autre danger ne peut y entrer.
- Imran doit utiliser la commande `Interaction` pour profiter du feu de camp.
- L'interaction reste volontaire et restaure uniquement ses coeurs jusqu'au maximum de `3`.
- Le nombre de vies ne change pas.
- Ignorer le feu de camp ne bloque pas la sortie.

## Sortie vers la Foret enchantee

- Le parcours progresse de la gauche vers la droite.
- Un portail ouvert du Village occupe l'intervalle `x = 15 104 a 15 232 px`.
- La Foret enchantee reste visible au-dela du portail dans le decor.
- La zone de transition occupe l'intervalle `x = 15 232 a 15 360 px`.
- Entrer dans cette zone ne demande aucune commande d'interaction.
- La progression est sauvegardee avant le debut de la transition visuelle.
- La sauvegarde marque le niveau 0 comme termine et debloque la Foret enchantee.
- Le niveau 0 ne peut plus etre rejoue apres cette sauvegarde.
- Un fondu au noir de `0.50 s` commence uniquement apres la fin de la sauvegarde.
- La Foret enchantee est chargee pendant l'ecran noir.
- Un fondu depuis le noir de `0.50 s` revele ensuite le niveau 1.
- Imran commence le niveau 1 avec `3 coeurs` et `3 vies`.

## Perte de vie et Game Over

- Le niveau 0 ne contient aucun checkpoint.
- Perdre une vie replace Imran a `x = 864 px` avec `3 coeurs` et une vie en moins.
- Le Slime, l'Archer, leurs projectiles et le mannequin reviennent a leur etat initial.
- Les pancartes restent relisibles et ne conservent aucun etat de progression.
- Un Game Over recommence le niveau 0 a `x = 864 px` avec `3 coeurs` et `3 vies`.
- Quitter avant la sortie reprend aussi au debut du niveau 0.

## Camera et lisibilite

- La camera suit Imran sans coupure sur les `15 360 px`.
- Elle respecte le cadrage vers la droite et la gauche deja valide.
- Elle ne descend pas vers les sols de securite si Imran reste dans sa zone verticale de confort.
- Chaque pancarte, obstacle, ennemi et reception est visible avant son activation.
- Le portail final et la Foret apparaissent progressivement pendant l'approche.

## Direction visuelle

- Le premier plan utilise des chemins de terre, des bottes de paille, du bois clair et des maisons rurales.
- Les champs de ble, les moulins et les toits du Village restent dans les plans de decor sans cacher le gameplay.
- Les couleurs restent chaudes et rassurantes.
- Les zones de saut utilisent du bois et de la terre afin de rester distinctes des ennemis.
- Le portail final associe visuellement le Village aux premieres plantes de la Foret enchantee.
- Aucun element decoratif ne masque une pancarte, un bord, un ennemi ou le feu de camp.

## Criteres de validation

- le parcours mesure `15 360 px` et contient huit zones continues ;
- les sept pancartes apparaissent dans l'ordre valide ;
- chaque message utilise la commande active et reste relisible ;
- le saut normal et le Double saut possedent des exercices obligatoires sans perte de coeur ou de vie ;
- le Dash, l'attaque, le Smash et le Bouclier peuvent etre pratiques sans bloquer la sortie ;
- le Slime bleu et le Squelette archer restent seuls dans leur rencontre et peuvent etre evites ;
- aucun checkpoint, golem, coffre ou cle n'apparait ;
- le feu de camp restaure volontairement les coeurs sans restaurer les vies ;
- la sortie sauvegarde la fin du tutoriel avant la transition ;
- un joueur novice peut viser une duree totale de `8 a 12 min` sans perdre de vie.

## Sources

- [Tutoriel du niveau 0](../../Concept-Game/05-Gameplay/Tutoriel-Niveau-0.md)
- [Village des Bles](../../Concept-Game/03-Univers/Village-des-Bles.md)
- [Structure commune](Structure-Commune.md)
- [Saut](../Joueur/Saut.md)
- [Double saut](../Joueur/Double-Saut.md)
- [Dash](../Joueur/Dash.md)
- [Attaque normale](../Combat/Attaque-Normale.md)
- [Smash Tranchant](../Combat/Smash-Tranchant.md)
- [Blocage automatique](../Combat/Blocage.md)
- [Slimes](../Ennemis/Slimes.md)
- [Squelettes](../Ennemis/Squelettes.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Sauvegarde](../Systemes/Sauvegarde.md)
