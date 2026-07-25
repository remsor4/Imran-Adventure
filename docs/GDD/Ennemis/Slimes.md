# Slimes

> **Statut :** Valide

## Objectif

Definir le premier ennemi terrestre simple d'Imran Adventure. Le Slime apprend au joueur a reconnaitre un mouvement bondissant, une preparation visible et une attaque de proximite facile a anticiper.

## Identite deja validee

- Le Slime se deplace et attaque en bondissant.
- Son animation repose sur une compression puis un etirement du corps.
- Son deplacement utilise un son humide et un rebond doux.
- Sa defaite utilise un eclatement cartoon court, sans gore.
- Son apparence change selon l'environnement, mais son comportement general reste reconnaissable.

## Variantes visuelles disponibles

| Environnement | Variante | Utilisation actuelle |
|---|---|---|
| Village des Bles | Slime de base entierement bleu | Utilisee |
| Foret enchantee | Slime vegetal | Utilisee |
| Grotte mysterieuse | Slime rocheux ou cristallin | Reserve artistique non utilisee |
| Lac gele | Slime glace | Utilisee |
| Desert oublie | Slime de sable | Utilisee |
| Volcan | Slime de lave | Utilisee |
| Chateau de Tata Lisa | Slime sombre | Reserve artistique non utilisee |

La progression ennemie validee exclut les Slimes de la Grotte mysterieuse et du Chateau de Tata Lisa. Leurs deux variantes restent disponibles comme reserves artistiques, mais elles ne sont pas placees dans la progression actuelle.

Ces variantes sont visuelles et sonores. Une difference de statistiques ou de comportement devra etre annoncee et validee explicitement avant son ajout.

## Dimensions validees

- Au repos, le Slime occupe une enveloppe visuelle de reference de `48 x 48 px`.
- Sa hauteur visuelle correspond environ a `75 %` de celle d'Imran.
- Sa zone principale de gameplay mesure `40 x 36 px`.
- Cette zone est centree sur la masse du corps et sert au contact dangereux ainsi qu'a la reception des coups.
- Les deformations visuelles de compression et d'etirement peuvent depasser temporairement l'enveloppe de reference sans agrandir la zone de gameplay.
- Toutes les variantes visuelles conservent ces memes dimensions.

## Regles communes applicables

- Un contact dangereux ou une attaque reussie retire `1 coeur` a Imran.
- Le Slime possede `1 PV`.
- Une attaque normale de la Shadow Sword inflige `1 degat` au Slime.
- Le Smash Tranchant inflige `2 degats`.
- Une attaque normale ou un Smash Tranchant vainc donc immediatement le Slime.
- Avec `1 PV`, le Slime ne peut jamais entrer dans une reaction non fatale et passe directement a l'etat `Defaite` apres un coup recu.
- Une defaite dure `0.67 s` avant la disparition.
- Un Slime vaincu reste absent pendant la vie en cours et ne produit aucune recompense.
- Les Slimes ne sont solides ni pour Imran, ni pour les autres ennemis.
- Ils sont bloques par le decor solide et ne tombent jamais accidentellement dans un gouffre.
- Un bond peut franchir un espace uniquement si une zone d'atterrissage valide existe dans la zone de rencontre.
- Un maximum de `3 ennemis ordinaires` peut attaquer simultanement selon les regles communes.

## Methode de bond validee

- Le Slime utilise un seul type de bond pour se deplacer et attaquer.
- Il ne possede aucun grand bond offensif distinct de son mouvement normal.
- Chaque cycle commence par une compression visible au sol.
- Le corps s'etire au moment de l'impulsion, suit sa trajectoire, puis se comprime de nouveau a l'atterrissage.
- La compression et le son humide du rebond annoncent le depart du bond.
- Le meme cycle est utilise pendant la patrouille, le rapprochement et l'attaque.
- Lorsque le Slime est autorise a attaquer, il conserve le sens de deplacement impose par sa zone de patrouille.
- Le corps du Slime reste dangereux pendant le bond et le contact retire `1 coeur` si Imran n'est pas invulnerable.
- Un contact au sol avec le Slime reste un contact dangereux selon les regles communes.
- Le bond ne change ni de hauteur, ni de duree, ni d'animation uniquement parce qu'Imran est vise.
- L'atterrissage termine le bond en cours avant qu'un nouveau cycle puisse commencer.

Cette methode reprend la capture Wonder Boy validee : les deux ennemis utilisent le meme rebond pour avancer et pour toucher le joueur, sans preparation offensive separee.

## Valeurs du bond unique validees

- La compression de preparation avant le depart dure `0.10 s`.
- La phase aerienne du bond dure `0.72 s`.
- Le Slime ne marque aucune pause supplementaire au sol entre deux bonds.
- La compression d'atterrissage devient directement la preparation du bond suivant et dure `0.10 s`.
- Un cycle continu complet dure donc `0.82 s` : `0.10 s` au sol puis `0.72 s` en l'air.
- Le sommet de la trajectoire atteint une hauteur maximale de `144 px` par rapport au point de depart.
- Un bond complet parcourt une distance horizontale de reference de `112 px`.
- Ces valeurs restent identiques pour un bond de deplacement, d'attaque ou de retour.
- La trajectoire ne peut pas etre corrigee apres le depart du sol.

Ces proportions reprennent le rythme mesure dans la capture Wonder Boy, puis sont adaptees aux dimensions validees du Slime.

## Contact dangereux valide

- La zone principale de `40 x 36 px` constitue aussi la zone dangereuse du corps du Slime.
- Cette zone reste dangereuse pendant l'attente, la compression, le bond, l'atterrissage et le retour a la position initiale.
- Un chevauchement avec la zone vulnerable d'Imran retire `1 coeur` si Imran n'est pas invulnerable.
- Le recul et les `1.30 s` d'invulnerabilite d'Imran s'appliquent selon les regles communes.
- Un contact continu peut infliger un nouveau degat uniquement apres la fin de cette invulnerabilite.
- Le contact ne bloque pas le Slime, ne modifie pas sa trajectoire et ne change pas sa direction.
- Le Bouclier de lumiere ne protege pas contre ce contact, car il bloque uniquement les projectiles venant de face.
- La zone dangereuse est desactivee immediatement lorsque le Slime entre dans l'etat `Defaite`.

## Gestion des emplacements d'attaque validee

- Chaque bond actif demande un emplacement d'attaque, y compris les bonds qui suivent le premier bond d'une activation.
- L'emplacement est occupe des le debut des `0.10 s` de compression.
- Il est libere au moment de l'atterrissage qui termine la phase aerienne.
- La dangerosite permanente du corps ne prolonge pas l'occupation de cet emplacement apres l'atterrissage.
- Si aucun emplacement n'est disponible, le Slime reste au sol dans sa boucle d'attente, sans compression et sans son de preparation.
- Lorsqu'un emplacement se libere, le Slime verifie de nouveau la detection, la visibilite et la ligne de vue avant de commencer sa compression.
- L'absence de pause supplementaire entre deux bonds s'applique uniquement lorsqu'un emplacement est immediatement disponible.
- Les bonds de retour vers la position initiale restent des deplacements et n'occupent aucun emplacement d'attaque.

## Zone de patrouille et direction validees

- Chaque Slime possede une zone horizontale predeterminee a l'interieur de sa zone de rencontre.
- Cette zone mesure `448 px` de large, soit la distance de quatre bonds complets de `112 px`.
- Elle s'etend sur `224 px` de chaque cote de la position initiale du Slime.
- La position initiale du Slime constitue donc le centre fixe de sa zone de patrouille.
- Son orientation d'attente initiale est fixee par son placement dans le niveau.
- La direction de son premier bond actif est choisie vers Imran au moment de l'activation.
- Il enchaine ses bonds dans ce meme sens tant qu'il n'atteint pas une limite de sa zone.
- Il ne recalcule jamais sa direction pour viser ou suivre directement Imran.
- La direction reste totalement fixe pendant chaque trajectoire aerienne.
- Si le prochain bond normal depassait une limite, le Slime termine son mouvement au dernier point d'atterrissage valide situe dans la zone.
- Apres cet atterrissage, il inverse sa direction avant de commencer le bond suivant.
- Apres le premier bond actif, Imran place derriere le Slime ne provoque aucun demi-tour immediat.
- Le Slime ne peut quitter sa zone ni pendant un deplacement, ni pendant une attaque, ni pendant une reaction aux degats.
- Une limite de zone produit le meme changement de sens qu'un obstacle infranchissable ou un bord dangereux.
- La zone de patrouille reste incluse dans la zone de rencontre definie par le niveau.

Le Slime represente donc un danger mobile et previsible. Imran doit observer son rythme et sa trajectoire plutot que provoquer une poursuite directe.

## Activation du mouvement validee

- Avant son activation, le Slime reste immobile a sa position initiale.
- Son animation d'attente forme une boucle de `1.20 s`.
- Cette boucle utilise uniquement un leger balancement du corps, sans compression ni etirement de bond.
- Elle ne produit aucun son et ne modifie jamais la position ou la zone de gameplay du Slime.
- Cette difference visuelle empeche de confondre l'attente avec la preparation active d'un bond.
- Il commence son cycle de bonds uniquement lorsque Imran entre dans sa zone de detection.
- Comme pour les autres ennemis, le Slime doit aussi etre visible a l'ecran et posseder une ligne de vue libre vers Imran.
- Si Imran se trouve devant lui, le Slime conserve son orientation pour le premier bond.
- Si Imran entre dans la zone de detection derriere lui, le Slime se retourne au sol avant de bondir vers Imran.
- Ce retournement ne cree aucune attaque distincte et ne modifie pas les valeurs du bond unique.
- La compression complete et le son de preparation restent obligatoires avant le premier bond.
- Le Slime ne peut pas commencer ce premier bond si les `3 emplacements` d'attaque sont deja occupes.
- Il reste alors immobile jusqu'a ce qu'un emplacement se libere et que toutes les conditions d'activation soient encore valides.
- Une fois le premier bond commence, les changements de direction suivent uniquement les limites de la zone de patrouille.

## Zone de detection validee

- La detection est mesuree entre le centre d'Imran et le centre du Slime.
- Imran doit se trouver a `800 px` ou moins horizontalement du Slime.
- Imran doit se trouver a `240 px` ou moins verticalement du Slime.
- Ces valeurs correspondent aux distances maximales dans chaque axe et non a la largeur totale de la zone.
- Le Slime doit egalement etre visible a l'ecran et posseder une ligne de vue libre vers Imran.
- Les conditions horizontale, verticale, de visibilite et de ligne de vue doivent etre reunies simultanement.
- La distance horizontale de `800 px` reprend la mesure de la capture Wonder Boy validee.
- La distance verticale de `240 px` est une valeur de conception adaptee au jeu, car la capture ne presente aucun test entre deux plateformes.

## Sortie de la zone de detection validee

- Lorsque Imran quitte la zone de detection, le Slime termine le bond deja commence sans modifier sa trajectoire.
- L'emplacement d'attaque occupe par ce bond est libere a l'atterrissage.
- Apres cet atterrissage, le Slime revient vers sa position initiale en utilisant le meme cycle de bonds.
- Les bonds de retour servent uniquement au deplacement et n'occupent aucun emplacement d'attaque.
- Le contact avec le corps du Slime reste dangereux pendant le retour.
- Le Slime ne commence aucune nouvelle attaque et ne se dirige pas vers Imran pendant cette phase.
- Si Imran entre de nouveau dans la zone de detection pendant le retour, le Slime termine quand meme son trajet jusqu'a sa position initiale.
- Le retour respecte les murs, les bords, les zones d'atterrissage et les limites de la zone de rencontre.
- Arrive a sa position initiale, le Slime termine son dernier bond, retrouve son orientation d'attente et redevient immobile.
- Une nouvelle activation peut commencer uniquement apres ce retour complet et une nouvelle verification de la visibilite, de la ligne de vue et de la zone de detection.

## Collisions avec les murs et les plafonds validees

- Si le Slime touche un mur pendant un bond, son mouvement horizontal s'arrete immediatement.
- Il termine ensuite sa chute verticalement jusqu'au dernier point d'atterrissage valide.
- Il change de direction uniquement apres cet atterrissage et jamais pendant la trajectoire aerienne.
- Si le Slime touche un plafond pendant sa montee, son mouvement vertical ascendant s'arrete immediatement.
- Il commence alors sa descente tout en conservant son mouvement horizontal si aucun mur ne le bloque.
- Une collision avec un mur ou un plafond ne retire aucun point de vie et ne declenche aucune reaction aux degats.
- Les limites de la zone de patrouille et la verification d'une zone d'atterrissage valide restent prioritaires avant le depart d'un bond.

## Criteres de validation

La fiche des Slimes est validee car :

- un seul cycle de bond sert clairement au deplacement et a l'attaque ;
- le Slime reste dans sa zone et change de sens uniquement a une limite validee ;
- le premier bond commence uniquement apres la detection et part vers Imran ;
- quitter la detection provoque un retour complet a la position initiale avant une nouvelle activation ;
- la zone de detection possede une distance mesurable ;
- la compression, le bond et la duree au sol possedent une duree ;
- le joueur peut identifier une attaque avant de recevoir un degat ;
- les points de vie et les dimensions sont fixes ;
- le comportement reste identique pour toutes les variantes visuelles ;
- chaque valeur peut etre testee dans le prototype sans decision de gameplay manquante.

## Sources

- [Slimes du Concept Game](../../Concept-Game/07-Ennemis/Slimes.md)
- [Principes d'IA](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Animation](../../Concept-Game/09-Direction-Artistique/Animation.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
- [Regles communes des ennemis](Regles-Communes.md)
- [Reference video des collisions entre ennemis](Reference-Video-Wonder-Boy-Collisions-Ennemis.md)
- [Reference video du bond unique](Reference-Video-Wonder-Boy-Bonds-Slimes.md)
- [Reference video de la detection horizontale](Reference-Video-Wonder-Boy-Detection-Slimes.md)
