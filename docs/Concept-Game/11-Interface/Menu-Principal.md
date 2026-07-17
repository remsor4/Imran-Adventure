# Menu principal

> **Statut :** Valide

## Objectif

Permettre de commencer ou reprendre l'aventure en quelques actions, avec une presentation claire et accueillante.

## Presentation

- Le logo valide de **Imran Adventure** apparait en haut de l'ecran.
- Sa taille conserve la lisibilite du titre sans masquer les boutons.
- Le fond montre une scene animee calme du royaume ou du Village des Bles.
- La musique principale commence sans transition brutale.
- Les boutons sont regroupes dans une seule colonne.
- La version du jeu peut apparaitre discretement dans un coin.

## Ordre des actions

Lorsqu'une sauvegarde existe :

1. Continuer ;
2. Nouvelle partie ;
3. Options ;
4. Quitter.

Lorsqu'aucune sauvegarde n'existe, `Nouvelle partie` recoit le focus initial. `Continuer` reste visible mais indisponible, avec un court texte indiquant qu'aucune partie n'a encore ete commencee.

## Continuer

- Charge l'unique emplacement de sauvegarde.
- Reprend au debut du dernier niveau debloque.
- Apres la sixieme cle, reprend devant la porte du donjon juste avant Tata Lisa.
- Restaure trois coeurs et trois vies.
- Conserve les cles et capacites des niveaux termines.
- Affiche le nom du niveau repris avant le chargement.

## Aventure terminee

Apres la victoire finale, la sauvegarde est marquee `Aventure terminee`.

- `Continuer` est remplace par `Revoir la fin`.
- Cette action rejoue la liberation d'Aliyah et les credits sans relancer le combat final.
- Aucune Nouvelle Partie Plus ni selection de niveau n'est ajoutee.
- Aucun niveau termine ne peut etre rejoue depuis la sauvegarde en cours.
- `Nouvelle partie` reste disponible avec une confirmation d'effacement.

## Nouvelle partie

Sans sauvegarde existante, l'aventure commence immediatement apres validation.

Si une sauvegarde existe, une fenetre explique que la progression actuelle sera effacee. Elle propose :

1. Annuler ;
2. Effacer et recommencer.

Le focus initial reste sur `Annuler`. L'effacement ne commence qu'apres une seconde validation explicite.

## Options

Ouvre l'ecran des reglages sans modifier la progression. Le retour replace le focus sur `Options`.

## Quitter

- Ouvre une confirmation avant de fermer le jeu.
- Le focus initial reste sur `Annuler`.
- La fermeture attend la fin d'une sauvegarde eventuelle.
- Le bouton ferme uniquement l'application PC.

## Navigation

- Le premier bouton disponible recoit le focus a l'ouverture.
- Le clavier, la manette et la souris utilisent le meme ordre visuel.
- Le focus ne peut pas quitter la liste des boutons.
- Une action indisponible produit un retour court sans ouvrir un nouvel ecran.
- Le dernier appareil utilise determine les icones de commandes.

## Retour d'un sous-menu

Quand le joueur revient des Options ou d'une confirmation :

- le meme fond et la meme musique sont conserves ;
- le focus revient sur l'action precedente ;
- aucune nouvelle sauvegarde n'est chargee ;
- les changements d'options deja appliques restent actifs.

## Validation du menu

Le menu principal est coherent si :

- la premiere action utile est selectionnee ;
- l'etat de `Continuer` est compris immediatement ;
- aucune sauvegarde ne peut etre effacee par une seule pression ;
- le titre reste lisible sur le fond anime ;
- la navigation fonctionne sans souris ;
- le joueur peut quitter ou revenir sans ambiguite.
