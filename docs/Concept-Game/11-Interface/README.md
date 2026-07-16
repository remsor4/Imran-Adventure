# 11 - Interface

Ce dossier definit les ecrans visibles par le joueur et leur comportement general. L'interface doit rester simple, stable et comprehensible par les enfants a partir de 7 ans.

## Documents

- [HUD](HUD.md)
- [Menu principal](Menu-Principal.md)
- [Menu Pause](Pause.md)
- [Game Over](Game-Over.md)
- [Victoire](Victoire.md)
- [Options](Options.md)

## Principes communs

- Une seule action principale est mise en avant a la fois.
- Le focus de navigation reste toujours visible.
- Les menus fonctionnent au clavier, a la manette et a la souris.
- Les indications de touche s'adaptent au dernier appareil utilise.
- Chaque action importante combine texte, icone et son lorsque cela est utile.
- Une information essentielle ne depend jamais uniquement d'une couleur ou d'un son.
- Les phrases restent courtes et les boutons suffisamment grands.
- La position des elements communs reste stable entre les ecrans.
- Le bouton de retour ramene toujours a l'ecran precedent sans modifier la progression.

## Confirmations obligatoires

Une confirmation est demandee avant de :

- effacer une sauvegarde avec une nouvelle partie ;
- recommencer le niveau en cours ;
- quitter un niveau vers le menu principal ;
- quitter le jeu depuis le menu principal ;
- abandonner une modification de commandes non enregistree.

La fenetre de confirmation place l'action sans risque en premier. L'action destructive utilise un texte explicite et ne repose pas uniquement sur la couleur rouge.
