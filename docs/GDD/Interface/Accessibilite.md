# Accessibilite

> **Statut :** En cours

## Objectif

Rendre toutes les informations utiles lisibles et comprehensibles sur PC, sans modifier la difficulte unique du jeu.

## Resolution de reference

- L'interface est concue dans un cadre de reference de `1920 x 1080`.
- Tous les elements restent ancres a leur zone fonctionnelle.
- Les coeurs et les vies restent ancres en haut a gauche.
- Les cles et les capacites restent ancrees en haut a droite.
- La barre de vie des boss reste ancree au centre superieur.
- Les messages contextuels restent ancres au centre inferieur.
- L'indicateur de sauvegarde reste ancre en bas a droite.

## Adaptation aux autres resolutions

- L'interface conserve ses proportions et ne subit aucun etirement independant sur un seul axe.
- La taille generale suit une mise a l'echelle uniforme calculee a partir de la zone d'affichage disponible.
- Les ancres replacent les elements apres un changement de resolution ou de mode de fenetre.
- Aucun texte, portrait, bouton, compteur ou icone ne peut sortir de la zone visible.
- Un format d'ecran different peut ajouter de l'espace lateral sans eloigner les informations de leur zone d'ancrage.
- Les marges de securite et les tailles reglables seront fixees dans les decisions suivantes.

## Marges de securite validees

- La marge minimale mesure `48 px` sur les quatre bords dans le cadre de reference `1920 x 1080`.
- Cette marge suit la meme mise a l'echelle uniforme que l'interface.
- Une information importante ne peut jamais entrer dans cette marge.
- Les contours decoratifs peuvent s'en approcher uniquement s'ils ne contiennent ni texte, ni icone, ni valeur utile.
- La barre de vie des boss conserve son centrage horizontal tout en respectant la marge superieure.
- Les boites de dialogue et les messages contextuels respectent la marge inferieure.

## Frontiere avec le TDD

- Le GDD fixe le resultat visuel attendu pour toutes les resolutions compatibles.
- Le choix des noeuds, des conteneurs et de la methode de mise a l'echelle sera documente dans le TDD.
