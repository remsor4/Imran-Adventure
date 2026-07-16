# GDD - Joueur

> **Statut :** Valide

## Objectif

Cette section definit les valeurs et les regles de mouvement d'Imran. Elle decrit le resultat attendu dans le jeu sans imposer l'architecture du code Godot.

## Documents

- [Statistiques d'Imran](Statistiques-Imran.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Deplacement](Deplacement.md)
- [Saut](Saut.md)
- [Dash](Dash.md)
- [Double saut](Double-Saut.md)
- [Reactions aux degats](Reactions-aux-Degats.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
- [Reference video du Dash Godot](Reference-Video-Dash-Godot.md)

## Principes

- Imran reste rapide, precis et facile a controler.
- La camera ne compense jamais un mouvement volontairement impraticable.
- La resolution de reference est `1920 x 1080` au format `16:9`.
- Les valeurs utilisent une grille logique de `64 px`.
- Les rapports de taille et de vitesse prennent pour reference les six premieres minutes de la video Wonder Boy validee par Rems.
- Le rapport de vitesse, la duree et l'intervalle du Dash prennent pour reference le tutoriel Godot valide par Rems.
- Le Dash est strictement terrestre : une commande recue dans les airs est ignoree.
- Les mesures du flux `640 x 360` sont normalisees dans la grille logique sans imposer une resolution interne au moteur.
- Une mise a l'echelle de l'image ne modifie jamais les distances de gameplay.
- Les valeurs validees pourront etre ajustees uniquement apres un test de prototype et une nouvelle validation.

## Sources

- [Fiche generale](../Fiche-Generale.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Controles](../Controles/README.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
- [Reference video du Dash Godot](Reference-Video-Dash-Godot.md)
- [Deplacements du Concept Game](../../Concept-Game/05-Gameplay/Deplacements.md)
- [Animation](../../Concept-Game/09-Direction-Artistique/Animation.md)
