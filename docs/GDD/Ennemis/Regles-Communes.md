# Regles communes des ennemis

> **Statut :** Valide

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

## Collision entre Imran et un ennemi ordinaire

- Un ennemi ordinaire vivant ne forme jamais un mur physique pour Imran.
- Imran peut traverser le volume de deplacement de l'ennemi sans etre bloque ou pousse.
- Le contact entre la zone dangereuse de l'ennemi et la zone vulnerable d'Imran retire `1 coeur` si Imran n'est pas invulnerable.
- Le recul horizontal de `220 px/s` eloigne immediatement Imran de la source du contact.
- Pendant les `1.30 s` d'invulnerabilite, Imran peut traverser l'ennemi sans recevoir un nouveau degat.
- Un ennemi ne peut ni transporter Imran, ni le coincer contre un mur, ni modifier directement son orientation.
- Imran ne peut jamais utiliser un ennemi comme plateforme.
- La zone dangereuse et les degats de contact sont desactives immediatement lorsque l'ennemi entre dans l'etat `Defaite`.
- Les attaques d'Imran utilisent leurs propres zones d'impact et ne rendent pas le corps de l'ennemi solide.
- Cette regle concerne les ennemis ordinaires. Une exception eventuelle pour un boss devra etre annoncee et validee dans sa propre fiche.

Cette regle adapte le comportement observe dans les captures Wonder Boy : le contact declenche un degat et un recul, puis l'invulnerabilite permet au joueur de ne pas rester bloque dans l'ennemi.

## Collisions entre ennemis ordinaires

- Les ennemis ordinaires ne sont jamais solides entre eux.
- Deux ennemis de la meme famille ou de familles differentes peuvent se traverser et se superposer.
- Une collision entre leurs volumes de deplacement ne modifie ni leur vitesse, ni leur direction, ni leur action en cours.
- Les ennemis ne se poussent pas, ne se bloquent pas et ne se transportent jamais entre eux.
- Un simple contact entre deux ennemis ne provoque aucun degat, aucun recul et aucune reaction.
- Chaque ennemi conserve son comportement, sa trajectoire, ses points de vie et sa zone de rencontre de maniere independante.
- Le placement des rencontres doit limiter les superpositions prolongees afin de conserver des silhouettes et des attaques lisibles.
- Cette regle ne fixe pas encore le comportement d'une attaque ou d'un projectile ennemi touchant un autre ennemi.

Cette regle reproduit le comportement observe dans la capture Wonder Boy dediee : des ennemis identiques ou differents se superposent puis se separent sans collision physique ni reaction.

## Attaques entre ennemis

- Une attaque ennemie ne peut jamais retirer de point de vie a un autre ennemi.
- Les attaques de contact et de corps a corps ignorent les zones vulnerables des autres ennemis.
- Un projectile ennemi traverse les autres ennemis sans produire d'impact, de recul ou de degat.
- Le passage a travers un autre ennemi ne ralentit pas le projectile et ne reduit pas sa portee restante.
- Un projectile ennemi disparait uniquement lorsqu'il touche Imran, son Bouclier, un element solide du decor ou lorsqu'il atteint sa limite de portee ou de duree.
- Un ennemi place entre Imran et un projectile ne peut jamais servir de protection.
- Les ennemis ne peuvent ni s'interrompre, ni se vaincre, ni modifier leurs points de vie entre eux.
- Aucun retour visuel ou sonore d'impact n'est produit lorsqu'une attaque traverse un autre ennemi.

## Collisions avec le decor

- Aucun ennemi ordinaire ne peut traverser un mur, un sol, un plafond ou un obstacle defini comme solide.
- Un ennemi terrestre repose sur les sols et est arrete par les murs solides.
- Lorsqu'un ennemi terrestre retombe sur une plateforme traversable, celle-ci le supporte comme elle supporte Imran.
- Un ennemi terrestre peut traverser une plateforme traversable pendant une montee autorisee, puis retomber dessus.
- Un ennemi volant est arrete par les murs, les plafonds, les sols et les obstacles entierement solides.
- Un ennemi volant traverse les plateformes traversables sans modifier sa trajectoire.
- Une collision avec un element solide annule uniquement la composante du mouvement dirigee vers cet element.
- Une collision avec le decor ne provoque aucun degat automatique a l'ennemi.
- Le chemin normal, l'attaque et le retour a la position initiale doivent rester compatibles avec les limites solides de la zone de rencontre.
- Si un obstacle rend la position initiale inaccessible, l'ennemi s'arrete au dernier point valide sans se teleporter et attend qu'un chemin soit de nouveau disponible.

## Bords de plateformes et gouffres

- Un ennemi terrestre ne tombe jamais accidentellement d'une plateforme ou dans un gouffre.
- Pendant une patrouille, il detecte le bord, s'arrete puis fait demi-tour selon le rythme de sa famille.
- Pendant une poursuite, il s'arrete avant le bord si Imran se trouve de l'autre cote d'un espace infranchissable.
- Il ne quitte jamais sa plateforme uniquement pour continuer une poursuite ou rejoindre la derniere position visible d'Imran.
- Pendant un retour, il utilise uniquement un chemin praticable qui reste dans sa zone de rencontre.
- Un mouvement terrestre normal ne franchit jamais un trou, meme si Imran reste visible de l'autre cote.
- Seul un mouvement volontaire propre a une famille, comme le bond d'un Slime, peut franchir un espace.
- Un tel mouvement exige une zone d'atterrissage praticable, visible et situee dans la zone de rencontre.
- Si aucune zone d'atterrissage valide n'existe, l'attaque ou le franchissement ne commence pas.
- Une charge ou une attaque terrestre incapable de franchir un vide s'arrete avant le bord.

Cette regle reprend le comportement de reference Wonder Boy valide pour le projet et empeche un ennemi de se vaincre ou de quitter sa rencontre sans action d'Imran.

## Limite des attaques simultanees

- Un maximum de `3 ennemis ordinaires` peut preparer ou executer une attaque en meme temps.
- Cette limite augmente la pression et encourage Imran a eliminer les ennemis au lieu de tous les contourner.
- Elle ne transforme pas les ennemis en condition obligatoire de fin du niveau : un passage reste possible si le joueur trouve une trajectoire sure.
- Un ennemi occupe un emplacement des le debut de la preparation visible de son attaque.
- Une attaque de corps a corps libere son emplacement a la fin de sa phase dangereuse.
- Une attaque produisant un projectile conserve son emplacement jusqu'a la disparition du projectile.
- Une attaque annulee ou un ennemi vaincu libere immediatement son emplacement.
- Lorsque les `3 emplacements` sont occupes, les autres ennemis peuvent se deplacer, poursuivre ou se repositionner, mais ils ne commencent aucune preparation d'attaque.
- Un ennemi en attente ne memorise jamais une attaque instantanee : lorsqu'un emplacement se libere, il respecte encore sa ligne de vue, sa preparation et son delai normal.
- La limite est commune a toutes les familles d'ennemis ordinaires presentes dans la meme rencontre.
- Les boss et les dangers du decor ne sont pas inclus dans cette limite et possederont leurs propres regles.

## Declenchement simultane des attaques

- Aucun intervalle minimal n'est impose entre deux preparations ennemies.
- Jusqu'a `3 ennemis` peuvent commencer leur preparation sur la meme image si les emplacements sont disponibles.
- Commencer simultanement ne supprime jamais le signe visuel et sonore propre a chaque attaque.
- Chaque attaque conserve sa preparation complete avant de devenir dangereuse.
- Les attaques declenchees sur la meme image restent independantes et peuvent se terminer a des moments differents.
- Une quatrieme attaque ne peut jamais commencer tant que les `3 emplacements` restent occupes.
- La camera et les effets doivent conserver Imran et les trois signes d'attaque suffisamment lisibles.

## Priorite d'attribution des emplacements

- Un ennemi deja en preparation ou en phase dangereuse conserve son emplacement jusqu'a sa liberation normale.
- Lorsqu'un ou plusieurs emplacements sont disponibles, seuls les ennemis respectant encore leur detection, leur ligne de vue et leur delai d'attaque peuvent les demander.
- Si plus d'ennemis sont disponibles que d'emplacements libres, les ennemis les plus proches d'Imran sont prioritaires.
- La distance est mesuree entre le centre d'Imran et le centre de chaque ennemi au moment de l'attribution.
- Si deux ennemis se trouvent a une distance equivalente, celui qui attend une autorisation d'attaque depuis le plus longtemps est prioritaire.
- Le temps d'attente commence lorsque toutes les conditions propres a l'attaque deviennent valides.
- Perdre Imran de vue, quitter la zone de detection ou devenir incapable d'attaquer annule ce temps d'attente.
- Un ennemi non selectionne continue son deplacement autorise, mais ne commence aucune preparation.
- Lorsqu'un emplacement se libere, les distances et les conditions sont de nouveau verifiees avant toute attribution.
- Une attribution ne permet jamais de supprimer ou de raccourcir la preparation visuelle et sonore de l'attaque.

## Sources

- [Principes d'IA du Concept Game](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Degats](../Combat/Degats.md)
- [Boucle de jeu](../Boucle-de-Jeu.md)
- [Coeurs et vies](../Systemes/Coeurs-et-Vies.md)
- [Checkpoints](../Systemes/Checkpoints.md)
- [Reference video des reactions ennemies](Reference-Video-Wonder-Boy-Reactions-Ennemies.md)
- [Reference video des collisions entre ennemis](Reference-Video-Wonder-Boy-Collisions-Ennemis.md)
- [Reference video des degats recus par Imran](../Joueur/Reference-Video-Wonder-Boy-Degats-Imran.md)
