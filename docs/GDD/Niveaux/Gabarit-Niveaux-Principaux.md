# Gabarit detaille des niveaux principaux

> **Statut :** Valide

## Objectif

Fixer les coordonnees communes utilisees par les six niveaux principaux sans rendre leurs terrains, leurs rencontres ou leurs ambiances identiques.

## Dimensions generales

- La resolution de reference est `1920 x 1080`.
- Chaque niveau principal mesure `29 664 px` de large.
- Le parcours avant l'arene mesure `27 744 px`.
- L'arene et sa zone de recompense mesurent ensemble `1 920 px`.
- Le sol de reference se trouve a `y = 896 px`.
- Toutes les coordonnees utilisent une grille logique de `64 px`.
- Le parcours progresse de la gauche vers la droite et reste parcourable dans les deux sens avant l'entree de l'arene.

## Depart commun

- La limite gauche du niveau se trouve a `x = 0 px`.
- Imran apparait avec son centre a `x = 864 px` et ses pieds sur le sol a `y = 896 px`.
- Il regarde vers la droite et commence avec une vitesse nulle, `3 coeurs` et `3 vies`.
- La camera est stabilisee avant l'apparition de l'image jouable.
- La premiere source de danger ne commence jamais avant `x = 1 632 px`.
- La distance entre l'apparition et le premier danger est donc au minimum de `768 px`.

## Repartition des dix sequences

| Element | Intervalle horizontal | Fonction |
|---|---:|---|
| Entree sure | `x = 0 a 1 632 px` | Presenter le theme et rendre le controle |
| Sequence 1 | `x = 1 632 a 3 936 px` | Rappel simple |
| Sequence 2 | `x = 3 936 a 6 240 px` | Rappel simple |
| Respiration A | `x = 6 240 a 6 624 px` | Separer les sections 1 et 2 |
| Sequence 3 | `x = 6 624 a 8 928 px` | Fin de la pression simple |
| Sequence 4 | `x = 8 928 a 11 232 px` | Pression intermediaire |
| Respiration B | `x = 11 232 a 11 616 px` | Eviter trois dangers consecutifs |
| Sequence 5 | `x = 11 616 a 13 920 px` | Pression intermediaire avant checkpoint |
| Checkpoint | `x = 13 920 a 14 688 px` | Reprise temporaire |
| Sequence 6 | `x = 14 688 a 16 992 px` | Reprise intermediaire |
| Sequence 7 | `x = 16 992 a 19 296 px` | Fin de la pression intermediaire |
| Respiration C | `x = 19 296 a 19 680 px` | Separer les sections 3 et 4 |
| Sequence 8 | `x = 19 680 a 21 984 px` | Pression exigeante |
| Sequence 9 | `x = 21 984 a 24 288 px` | Pression exigeante |
| Respiration D | `x = 24 288 a 24 672 px` | Eviter trois dangers consecutifs |
| Sequence 10 | `x = 24 672 a 26 976 px` | Derniere epreuve du parcours |
| Feu de camp | `x = 26 976 a 27 744 px` | Soin volontaire et preparation |
| Arene du golem | `x = 27 744 a 29 024 px` | Combat de boss |
| Recompense | `x = 29 024 a 29 664 px` | Coffre, cle et transition |

## Sections et pression

- La section 1 contient les sequences 1 et 2.
- La section 2 contient les sequences 3 a 5.
- La section 3 contient les sequences 6 et 7.
- La section 4 contient les sequences 8 a 10.
- Les sequences 1 a 3 portent une pression simple.
- Les sequences 4 a 7 portent une pression intermediaire.
- Les sequences 8 a 10 portent une pression exigeante relative au niveau.
- La repartition atteint donc `3 sequences simples`, `4 intermediaires` et `3 exigeantes`.
- Deux sequences dangereuses au maximum se suivent sans respiration.

## Gabarit d'une sequence

- Chaque sequence dispose de `2 304 px`.
- Sa zone de rencontre ou son obstacle principal est centre dans cet intervalle.
- Les marges restantes servent a montrer le danger avant son activation et a garantir une reception sure.
- Une rencontre a `960 px` conserve `672 px` de marge de chaque cote.
- Une rencontre a `1 280 px` conserve `512 px` de marge de chaque cote.
- Une rencontre a `1 440 px` conserve `432 px` de marge de chaque cote.
- Une rencontre a `1 600 px` conserve `352 px` de marge de chaque cote.
- Une zone de reception obligatoire mesure toujours au moins `256 px`.
- Une nouvelle utilisation du terrain apparait d'abord sans ennemi actif dans sa trajectoire.

## Placement recommande des ennemis

Les positions suivantes sont mesurees par rapport au centre `C` de la sequence concernee.

| Composition | Positions initiales recommandees |
|---|---|
| Ennemi seul | `C` |
| Deux Slimes | `C - 128 px` et `C + 128 px` |
| Paire demandant `320 px` | `C - 160 px` et `C + 160 px` |
| Paire demandant `480 px` | `C - 240 px` et `C + 240 px` |
| Groupe de trois | `C - 480 px`, `C` et `C + 480 px` |

- Tous les ennemis commencent devant Imran dans le sens d'entree.
- Dans une paire avec Archer, l'Archer occupe la position la plus a droite et soutient l'autre ennemi.
- Dans un groupe avec Epeiste, Serpent et Archer, l'ordre gauche vers droite est `Epeiste, Serpent, Archer`.
- Une Chauve-souris utilise son point aerien au-dessus de sa position horizontale recommandee.
- Les separations minimales et les conditions de terrain de la fiche des combinaisons restent prioritaires.
- Les limites de rencontre bloquent toute poursuite et tout projectile vers une zone sure.

## Obstacles et fosses

- Les plateformes obligatoires sont statiques, visibles et alignees sur la grille de `64 px`.
- Un saut normal obligatoire utilise au maximum une elevation de `64 px` ou une fosse de `128 px` de large.
- Un Double saut obligatoire utilise une elevation de `128 px` ou une fosse de `192 px` de large.
- Une action combinee conserve une surface stable entre le Dash, le saut et le Double saut.
- Une fosse declaree mortelle retire une vie et provoque la reapparition normale.
- Aucune fosse ne commence dans une zone sure ou une zone de reception.
- Aucun ennemi ne couvre la premiere reception d'un obstacle nouvellement introduit.
- Une plateforme au-dessus d'une fosse mesure au moins `256 px` de large.
- Une porte de pratique du Dash place sa dalle a `192 px` du passage et reste ouverte pendant `0.70 s`.
- La marche normale parcourt `168 px` pendant ce temps et ne suffit pas a franchir la porte.
- Le Dash suivi du mouvement normal parcourt environ `244 px` et conserve une marge de `52 px`.
- Une porte ne se referme jamais tant que la zone du passage est occupee par Imran.
- Elle ne retire aucun coeur et ne peut pas coincer Imran dans le decor.
- Apres son premier franchissement, une approche depuis la droite la maintient ouverte afin de permettre le retour en arriere.

## Checkpoint commun

- La pancarte de controle est centree a `x = 14 304 px`.
- Sa zone sure s'etend de `x = 13 920 a 14 688 px`.
- L'activation est automatique et ne bloque pas le controle.
- Le sol est plat, stable et sans danger sur toute la zone.
- Aucun projectile ou ennemi des sequences 5 et 6 ne peut atteindre cette zone.
- Apres activation, une perte de vie replace Imran au centre de la pancarte avec `3 coeurs` et une vie en moins.

## Feu de camp commun

- Le feu de camp est centre a `x = 27 360 px`.
- Sa zone sure s'etend de `x = 26 976 a 27 744 px`.
- Imran utilise volontairement la commande `Interaction` pour restaurer ses coeurs a `3`.
- Le feu ne restaure aucune vie.
- Ignorer le feu ne bloque pas l'entree de l'arene.
- Aucun ennemi, projectile, piege ou fosse ne peut atteindre cette zone.

## Arene et recompense

- L'arene commence a la coordonnee globale `x = 27 744 px`.
- Les coordonnees internes des fiches de boss utilisent cette position comme origine locale.
- La zone de combat locale mesure `1 280 px` et se termine a la coordonnee globale `x = 29 024 px`.
- La zone de recompense locale mesure `640 px` et se termine a `x = 29 664 px`.
- Le coffre se trouve a la coordonnee locale `x = 1 824 px`, soit la coordonnee globale `x = 29 568 px`.
- La victoire contre le golem ouvre la zone de recompense mais ne termine pas le niveau.
- Imran doit ouvrir le coffre avec `Interaction` a `56 px` ou moins.
- La cle est ajoutee, puis la sauvegarde est terminee avant la transition.
- Le niveau termine ne peut plus etre rejoue.

## Duree cible

- Chaque niveau principal vise `20 a 25 min` de gameplay.
- La largeur commune produit environ `2 min` de marche continue sans combat, obstacle, attente ou retour.
- Les dix sequences, les lectures, le checkpoint, le feu de camp et le golem portent la duree totale dans la plage cible.
- Une duree hors cible se corrige d'abord par le placement, l'espace et le rythme, sans modifier les valeurs du joueur ou des ennemis.

## Criteres de validation

- les six niveaux utilisent les memes limites mesurables sans partager le meme contenu ;
- chaque niveau contient exactement dix sequences reparties `3, 4, 3` ;
- le checkpoint et le feu de camp possedent leurs zones sures completes ;
- le premier danger reste a `768 px` ou plus du point d'apparition ;
- deux dangers au maximum se suivent sans respiration ;
- chaque rencontre respecte sa largeur et ses separations minimales ;
- l'arene et la recompense conservent leurs coordonnees locales validees ;
- le parcours peut etre transforme en plan puis en scene Godot.

## Sources

- [Structure commune](Structure-Commune.md)
- [Courbe de difficulte](../Equilibrage/Courbe-de-Difficulte.md)
- [Combinaisons et progression](../Ennemis/Combinaisons-et-Progression.md)
- [Camera](../Systemes/Camera.md)
- [Checkpoints](../Systemes/Checkpoints.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Regles communes des boss](../Boss/Regles-Communes.md)
