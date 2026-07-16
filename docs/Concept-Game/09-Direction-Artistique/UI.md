# Interface visuelle

> **Statut :** Valide

## Objectif

Definir le langage visuel commun du HUD et des menus. L'interface doit sembler appartenir au meme univers cartoon fantasy que le jeu tout en restant tres facile a comprendre pour les enfants a partir de 7 ans.

Les informations affichees et le comportement des ecrans sont decrits dans les dossiers `06-Systemes` et `11-Interface`.

## Style general

L'interface combine des panneaux simples, des contours sombres et quelques details inspires du bois, du parchemin et du metal dore.

- Les formes principales sont arrondies et accueillantes.
- Les cadres utilisent peu d'ornements et laissent respirer le contenu.
- Les fonds de panneau sont opaques ou fortement assombris pour garantir la lecture.
- Les decorations ne doivent jamais ressembler a un bouton actif.
- Le violet sombre, instable et en forme de flamme est reserve a Tata Lisa, au Chateau et aux effets de corruption.
- Le violet lavande, fin et stable, peut etre utilise pour le tranchant et les cristaux de la Shadow Sword.

## Formes

- Les boutons utilisent des rectangles arrondis ou de courtes bannieres.
- Le bouton selectionne possede un contour plus clair, une legere augmentation de taille et un marqueur de position.
- Les panneaux importants utilisent une silhouette stable dans tous les menus.
- Les fenetres de confirmation se distinguent clairement du fond de l'ecran.
- Les jauges et compteurs utilisent des formes pleines faciles a lire sans texte.

## Typographie

Deux familles maximum sont utilisees :

1. Une police de titre fantasy, ronde et lisible, pour les grands titres des ecrans.
2. Une police sans serif simple pour les boutons, les messages et les options.

Le logo utilise sa propre typographie medievale validee, avec des empattements sculptes et une lecture claire.

Regles typographiques :

- eviter les lettres trop fines ou trop ornementees ;
- conserver une taille confortable sur tous les ecrans cibles ;
- limiter les textes en majuscules aux titres courts ;
- utiliser un interligne aere ;
- ajouter un contour ou un fond lorsque le texte apparait sur le jeu ;
- tester les mots longs et les changements de langue avant validation.

## Icones

Les icones utilisent un contour commun, une silhouette simple et un detail central.

| Information | Forme principale |
|---|---|
| Coeur | Coeur rouge plein |
| Vie | Portrait simplifie d'Imran |
| Cle | Cle doree avec anneau large |
| Dash | Botte ou silhouette avec deux lignes de vitesse |
| Double saut | Deux ailes ou deux chevrons verticaux |
| Sauvegarde | Livre ferme avec petite etoile |
| Bouclier | Bouclier en bois miel avec soleil dore et halo de lumiere |
| Action | Symbole du bouton accompagne d'un verbe court |

Une icone importante ne depend jamais uniquement de sa couleur. Sa silhouette ou son symbole doit suffire a l'identifier.

## HUD

- Les coeurs et les vies occupent une zone stable dans le coin superieur gauche.
- Les cles et capacites restent groupes dans une seconde zone discrete.
- Une barre de vie rouge avec contour sombre et valeur numerique est centree en haut pendant les combats de boss.
- Le centre de l'ecran reste libre en dehors de cette barre et des messages temporaires.
- Les informations temporaires apparaissent sans masquer Imran ou un danger.
- Le HUD peut reduire son contraste lorsqu'aucune information ne change, mais il redevient visible des qu'une valeur est modifiee.

## Etats interactifs

Chaque bouton possede au minimum les etats suivants :

- normal ;
- survole ou cible ;
- selectionne ;
- active ;
- indisponible ;
- confirme.

Le changement d'etat combine au moins deux indices parmi la couleur, le contour, la taille, l'icone, le texte et l'animation.

## Couleurs et contraste

- Les menus generaux utilisent des tons creme, bleu nuit, bois chaud et or doux.
- Le rouge est reserve aux degats, aux erreurs et aux actions dangereuses.
- Le vert confirme une action positive ou une activation.
- Le violet signale la magie de Tata Lisa ou une influence hostile.
- Les textes clairs sont affiches sur un fond sombre et les textes sombres sur un fond clair.
- Aucun texte essentiel ne repose directement sur un decor sans protection visuelle.

## Accessibilite visuelle

- Associer texte et icone dans les menus importants.
- Ne jamais transmettre une information uniquement par la couleur.
- Afficher clairement le focus de navigation a la manette et au clavier.
- Eviter les clignotements rapides et les animations continues agressives.
- Permettre de reduire les secousses, flashs et effets d'ecran.
- Conserver des zones cliquables plus grandes que leur dessin visible.

## Validation d'un ecran

Un ecran est coherent si :

- l'action principale est identifiee en premier ;
- le focus de navigation est toujours visible ;
- les textes restent lisibles sur le plus petit ecran cible ;
- les icones sont comprises avec et sans couleur ;
- aucun decor ne ressemble a un controle interactif ;
- le joueur peut revenir en arriere sans ambiguite.
