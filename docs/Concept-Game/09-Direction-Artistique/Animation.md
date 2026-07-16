# Animation

> **Statut :** A valider

## Objectif

Definir les principes d'animation qui donnent au jeu un mouvement fluide, expressif et facile a lire. L'animation soutient le gameplay avant de rechercher le spectacle.

## Principes communs

- Chaque action importante possede une preparation, une action et un retour au repos.
- La preparation annonce clairement les attaques et les dangers.
- Les poses principales restent lisibles sans les images intermediaires.
- Le squash and stretch renforce les impacts sans deformer durablement les personnages.
- Les mouvements secondaires ajoutent de la vie sans cacher l'action principale.
- Les animations ne doivent jamais retarder une commande essentielle du joueur.
- Les boucles evitent les mouvements mecaniques parfaitement synchrones.

## Rythme par famille

| Famille | Rythme | Sensation recherchee |
|---|---|---|
| Imran | Rapide et precis | Courage, agilite, reactivite |
| Allies | Souple et calme | Chaleur, securite |
| Ennemis communs | Simple et annonce | Comprehension immediate |
| Golems | Lent et puissant | Masse, poids, force |
| Tata Lisa | Theatral et contraste | Controle, magie, autorite |
| Decors | Discret et decale | Monde vivant sans distraction |

## Imran

Le corps d'Imran s'incline legerement dans la direction du mouvement. Sa tete et son regard anticipent l'action pour renforcer son caractere volontaire.

Animations principales :

- attente avec respiration et regard actif ;
- demarrage, course, freinage et demi-tour ;
- montee, sommet du saut, chute et reception ;
- Double saut avec pose distincte ;
- Dash avec silhouette et direction tres claires ;
- attaque normale, charge et Smash Tranchant ;
- sortie et rangement du Bouclier de lumiere ;
- blocage reussi et recul sous un impact ;
- degat, perte d'une vie et retour au point de controle ;
- interaction avec un coffre, une cle ou une pancarte ;
- victoire et liberation d'Aliyah.

Les attaques a l'epee doivent conserver une trajectoire visible. Les anticipations d'Imran restent courtes afin de ne pas rendre les commandes lourdes.

## Ennemis

Chaque type d'ennemi possede :

- une boucle d'attente qui montre sa personnalite ;
- un deplacement reconnaissable ;
- une preparation d'attaque impossible a confondre avec son attente ;
- une reaction aux degats ;
- une disparition courte, non violente et sans gore.

La chauve-souris utilise un mouvement aerien souple. Le slime se comprime et s'etire. Le squelette utilise des poses seches et articulees. Le zombie avance avec un poids lent. Le serpent annonce son attaque par la tete et le haut du corps.

## Golems

Les golems donnent une forte sensation de masse.

- Les pieds restent ancres au sol avant une attaque lourde.
- Les bras et les epaules entrainent le reste du corps.
- Les impacts produisent un court temps d'arret visuel.
- Les fissures et le coeur magique reagissent aux changements de phase.
- Les attaques puissantes utilisent une anticipation longue et evidente.
- La defaite montre la fin de la magie de controle plutot qu'une destruction violente.

Le materiau modifie les mouvements secondaires : feuilles et racines pour la Foret, poussiere pour le Desert, eclats de glace pour le Lac, magma pour le Volcan.

## Tata Lisa

Tata Lisa utilise des gestes amples des bras et des mains. Son voile, ses manches et ses bijoux prolongent ses mouvements avec un leger retard.

- Ses poses d'attente montrent son impatience et son autorite.
- Ses sourcils, ses yeux et sa bouche portent une grande partie de son jeu d'actrice.
- Ses sorts commencent par une pose claire dirigee vers leur cible.
- Sa magie violette suit ses mains avant de former une attaque.
- Ses reactions restent expressives et theatrales sans devenir effrayantes.

## Decors

Les animations de decor restent lentes et peu contrastees :

- ble et tissus agites par le vent au Village ;
- feuilles, fleurs et particules naturelles dans la Foret ;
- lueurs de cristaux et gouttes d'eau dans la Grotte ;
- neige, vapeur froide et reflets au Lac ;
- sable, tissus uses et poussiere dans le Desert ;
- fumee, braises et chaleur dans le Volcan ;
- flammes violettes, rideaux et magie flottante dans le Chateau.

Les mouvements de l'arriere-plan ne doivent jamais ressembler a une plateforme, un ennemi ou un projectile.

## Transitions et interface

- Les menus utilisent des transitions courtes et douces.
- Une selection reagit immediatement par une variation de taille, de lumiere ou de position.
- Les icones importantes peuvent utiliser une petite impulsion pour attirer l'attention.
- Les transitions longues restent reservees aux changements de niveau et aux scenes narratives.

## Validation d'une animation

Une animation est valide si :

- l'action est comprise sans effet visuel ni son ;
- la pose principale reste lisible a la taille d'affichage du jeu ;
- le danger est annonce assez tot ;
- le mouvement correspond au poids du personnage ;
- la boucle ne provoque pas de saut visible ;
- l'animation ne masque pas une commande ou un obstacle.
