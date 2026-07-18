# Regles communes des ennemis

> **Statut :** En cours

## Objectif

Definir le cadre partage par tous les ennemis ordinaires avant de fixer les valeurs et les exceptions propres a chaque famille.

## Regles deja validees

- Les ennemis ordinaires peuvent etre evites et ne sont jamais une condition generale de fin du niveau.
- Un ennemi n'attaque pas Imran avant d'etre visible a l'ecran.
- Chaque ennemi reste dans la zone de rencontre prevue par le niveau.
- Chaque attaque commence par un signe visuel et sonore reconnaissable.
- Une courte recuperation apres une attaque permet a Imran de riposter.
- Une attaque ennemie ordinaire ou un contact dangereux retire `1 coeur` a Imran.
- Une attaque normale de la Shadow Sword inflige `1 degat`.
- Le Smash Tranchant inflige `2 degats` au premier ennemi touche puis disparait.
- Un projectile ennemi venant de face peut etre bloque automatiquement par le Bouclier de lumiere.
- Aucun ennemi ordinaire ne donne de coeur, de vie, de cle ou de capacite.
- Tous les ennemis reviennent a leur etat initial apres la perte d'une vie.
- Une defaite reste lisible, courte et sans violence graphique.

## Persistance pendant une vie

- Un ennemi vaincu reste absent pendant toute la vie en cours.
- Quitter sa zone puis y revenir ne le fait pas reapparaitre.
- La perte d'une vie recharge tous les ennemis du niveau, y compris ceux deja vaincus.
- Un Game Over, un abandon, une fermeture du jeu ou un nouveau chargement du niveau recharge aussi tous les ennemis.
- Aucun ennemi ordinaire ne reapparait selon un temps d'attente pendant une meme vie.

## Limite de poursuite

- Chaque ennemi possede une zone de rencontre definie par le niveau.
- Un ennemi vivant ne poursuit jamais Imran au-dela de cette zone.
- Lorsque Imran quitte la zone, l'ennemi interrompt sa poursuite et son attaque en cours.
- Il retourne ensuite a sa position initiale sans se teleporter.
- Pendant ce retour, il ne commence aucune nouvelle attaque.
- Une fois revenu, il reprend son comportement d'attente ou de patrouille propre a sa famille.

## Perte de la ligne de vue

- Lorsqu'un ennemi actif perd Imran de vue, il memorise sa derniere position visible.
- Il rejoint cette position uniquement si elle reste dans sa zone de rencontre.
- Il ne peut commencer aucune attaque tant que la ligne de vue reste bloquee.
- Arrive a la derniere position visible, il attend `0.75 s`.
- Si Imran redevient visible pendant cette attente, la poursuite reprend.
- Si Imran reste invisible apres `0.75 s`, l'ennemi retourne a sa position initiale selon les regles de limite de poursuite.

## Comportement hors de l'ecran

- Une attaque dont la preparation a ete clairement visible peut se terminer si l'ennemi sort ensuite de l'ecran.
- Un projectile deja lance continue selon les regles de sa famille.
- Aucune nouvelle attaque ne peut commencer tant que l'ennemi reste hors de l'ecran.
- Aucune commande d'attaque n'est mise en attente pour etre lancee instantanement au retour a l'ecran.
- Lorsque l'ennemi redevient visible, il doit encore respecter sa detection, sa ligne de vue et son delai normal entre deux attaques.

## Interruption par une attaque d'Imran

- Un coup recu pendant la preparation d'une attaque ennemie annule cette attaque.
- L'ennemi entre alors dans une reaction aux degats de `0.33 s` avant de pouvoir agir de nouveau.
- Une fois la phase dangereuse commencee, les degats d'Imran sont appliques mais l'attaque ennemie continue jusqu'a sa fin normale.
- Le retour visuel de l'impact commence immediatement et dure `0.33 s`.
- Si la phase dangereuse continue pendant ce retour, l'ennemi ne commence aucune nouvelle action avant la fin de la phase et de la duree de `0.33 s` calculee depuis l'impact.
- Une attaque normale ou un Smash Tranchant ne peut infliger ses degats qu'une seule fois au meme ennemi.
- L'attaque normale et le Smash Tranchant utilisent la meme duree de reaction de `0.33 s`.
- Le Smash se distingue par ses `2 degats`, pas par un blocage plus long.

## Protection entre deux impacts

- Des le premier degat recu, l'ennemi est protege contre un nouveau degat pendant `0.33 s`.
- Cette protection se termine en meme temps que la reaction aux degats.
- Une autre attaque d'Imran touchant pendant cette duree ne retire aucun point de vie et ne relance pas la reaction.
- La protection empeche les impacts doubles d'une meme attaque et limite le blocage continu d'un ennemi.
- Elle ne restaure aucun point de vie et ne modifie pas la zone de rencontre.

## Defaite et disparition

- Un ennemi entre dans l'etat `Defaite` des que ses points de vie atteignent `0`.
- Son deplacement, sa poursuite, ses attaques et ses degats de contact sont desactives immediatement.
- Il ne peut plus recevoir de nouvel impact.
- Le retour visuel et sonore de defaite dure `0.67 s`, soit environ `40 images` a `60 images/s`.
- L'ennemi disparait entierement a la fin de cette duree.
- La disparition reste courte, lisible et sans violence graphique.
- Aucun coeur, aucune vie, aucune cle et aucune autre recompense ne sont produits.
- L'ennemi reste absent pendant le reste de la vie en cours selon les regles de persistance.

## Activation initiale

- Un ennemi devient agressif uniquement lorsque deux conditions sont reunies : il est visible a l'ecran et Imran entre dans sa zone de detection.
- Une ligne de vue libre entre l'ennemi et Imran est egalement obligatoire.
- Un mur ou un obstacle solide place entre eux bloque la detection.
- Entrer dans la zone de detection ne suffit pas si un obstacle solide coupe la ligne de vue.
- Un ennemi ne commence jamais une attaque a travers un mur ou un obstacle solide.
- La taille et la forme de la zone de detection sont definies dans la fiche de chaque famille.
- Etre visible sans avoir detecte Imran ne declenche aucune attaque.
- Detecter une position hors de l'ecran ne declenche aucune attaque.
- Avant son activation, l'ennemi reste en attente ou suit sa patrouille locale sans poursuivre Imran.
- Une activation ne modifie pas les limites de la zone de rencontre.

## Points de vie apres une poursuite

- Un ennemi conserve tous les degats deja recus pendant la vie en cours.
- Quitter sa zone de rencontre ne restaure aucun point de vie.
- Revenir a sa position initiale ne restaure aucun point de vie.
- Si Imran retourne dans la zone, le combat reprend avec les points de vie restants de l'ennemi.
- Les points de vie sont entierement restaures uniquement lors du rechargement des ennemis apres une perte de vie, un Game Over, un abandon, une fermeture du jeu ou un nouveau chargement du niveau.

## Points a definir ensemble

- collisions entre Imran, les ennemis et le decor ;
- nombre maximal d'attaques simultanees ;

## Sources

- [Principes d'IA du Concept Game](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Degats](../Combat/Degats.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Checkpoints](../Systemes/Checkpoints.md)
- [Reference video des reactions ennemies](Reference-Video-Wonder-Boy-Reactions-Ennemies.md)
