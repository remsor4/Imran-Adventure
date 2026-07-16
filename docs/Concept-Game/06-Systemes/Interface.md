# Interface

> **Statut :** À valider

## Objectif du document

Définir les principes généraux de l'interface d'Imran Adventure.

L'interface doit transmettre les informations essentielles sans surcharger l'écran. Elle doit être claire, lisible et compréhensible par les enfants à partir de 7 ans.

Les écrans particuliers sont détaillés séparément dans le dossier `11-Interface`.

## Principes généraux

L'interface doit respecter les règles suivantes :

- utiliser des icônes simples et facilement reconnaissables ;
- afficher peu de texte pendant l'action ;
- employer une taille de texte confortable ;
- conserver un contraste suffisant entre les informations et le décor ;
- ne pas dépendre uniquement des couleurs pour transmettre une information ;
- afficher les messages importants pendant une durée suffisante ;
- utiliser la même organisation visuelle dans tous les niveaux.

L'interface doit rester cohérente avec la direction artistique en dessin animé du jeu.

## Informations affichées pendant le jeu

Le HUD doit présenter uniquement les informations utiles à la progression immédiate.

Il doit permettre au joueur de connaître :

- le nombre de cœurs restants ;
- le nombre de vies restantes ;
- le nombre de clés récupérées ;
- les capacités débloquées ;
- la vie restante du boss pendant chaque affrontement.

Les cœurs et les vies doivent rester visibles pendant l'exploration et les combats.

Le compteur de clés peut être affiché de manière discrète, puisqu'une seule clé est obtenue à la fin de chaque niveau.

Les icônes du Dash et du Double saut doivent apparaître après leur déblocage afin de rappeler au joueur qu'elles sont disponibles.

Pendant un combat de boss, une barre de vie horizontale est centree en haut de l'ecran. Elle affiche aussi la valeur numerique actuelle afin de rester comprehensible sans dependre uniquement de la couleur.

## Messages contextuels

Des messages courts peuvent apparaître lorsque le joueur doit effectuer une action particulière.

Exemples :

- ouvrir un coffre ;
- activer une pancarte de contrôle ;
- confirmer une nouvelle partie ;
- utiliser une nouvelle capacité pour la première fois ;
- reprendre après une sauvegarde.

Les messages doivent indiquer clairement la touche ou le bouton correspondant à l'appareil utilisé.

Ils disparaissent automatiquement lorsqu'ils ne sont plus nécessaires.

## Retours visuels

L'interface doit confirmer immédiatement les actions importantes.

Le joueur doit recevoir un retour clair lorsqu'il :

- perd un cœur ;
- perd une vie ;
- bloque une attaque avec le Bouclier de lumière ;
- active une pancarte ;
- récupère une clé ;
- débloque le Dash ;
- débloque le Double saut ;
- déclenche une sauvegarde automatique ;
- vainc un boss.

Les retours peuvent combiner une animation, une icône, un court texte et un effet sonore.

## Sauvegarde automatique

Lorsqu'une sauvegarde automatique est effectuée, une petite icône ou un message apparaît brièvement.

Cette indication ne doit pas bloquer le jeu.

Le joueur ne doit pas quitter le jeu pendant que l'indicateur de sauvegarde est visible.

## Menus

Les menus doivent utiliser une navigation simple et cohérente.

Le menu principal doit proposer au minimum :

- Continuer ;
- Nouvelle partie ;
- Options ;
- Quitter.

Le menu Pause doit proposer au minimum :

- Reprendre ;
- Options ;
- Recommencer le niveau ;
- Quitter vers le menu principal.

Toute action pouvant effacer une progression ou faire quitter un niveau doit demander une confirmation.

## Accessibilité et lisibilité

L'interface doit être adaptée aux jeunes joueurs.

Elle doit privilégier :

- des phrases courtes ;
- des mots simples ;
- des boutons suffisamment grands ;
- une sélection clairement visible ;
- des icônes accompagnées de texte dans les menus importants ;
- une distinction claire entre une option disponible et une option indisponible.

Les informations importantes ne doivent jamais être indiquées uniquement par une différence de couleur.

## Séparation avec les documents détaillés

Ce fichier définit les principes communs de l'interface.

Les écrans et éléments suivants sont détaillés dans le dossier `11-Interface` :

- HUD ;
- menu principal ;
- menu Pause ;
- écran Game Over ;
- écran de victoire ;
- options.
