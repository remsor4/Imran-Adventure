# Zombies

> **Statut :** Valide

## Objectif

Definir les Zombies des deux derniers niveaux comme des versions plus resistantes des Squelettes, sans creer de nouveau comportement a apprendre.

## Regle principale validee

- Les Zombies reprennent exactement toutes les regles de gameplay des Squelettes.
- Le Zombie epeiste reprend toutes les regles du Squelette epeiste.
- Le Zombie archer reprend toutes les regles du Squelette archer.
- Leur unique difference de gameplay concerne les points de vie.
- Un Squelette possede `2 PV`.
- Un Zombie possede `3 PV`.
- Aucune vitesse, dimension, detection, attaque, cadence, collision ou distance n'est augmentee.
- Leur pression supplementaire vient uniquement du coup supplementaire necessaire pour les vaincre.

La fiche [Squelettes](Squelettes.md) constitue donc la reference complete de leur comportement. Toute correction future d'une regle non liee aux points de vie doit etre appliquee de la meme maniere aux Zombies, sauf nouvelle exception explicitement validee.

## Presence dans la progression

- Les Zombies remplacent les Squelettes dans les deux derniers niveaux.
- Ils apparaissent dans le Volcan et le Chateau de Tata Lisa.
- Les deux variantes epeiste et archer restent reconnaissables avant leur premiere interaction dangereuse.
- Leur arrivee represente la montee en puissance de la magie du Chaos de Tata Lisa.
- Un Zombie n'apparait pas comme une variante aleatoire d'un Squelette dans les niveaux precedents.

## Identite visuelle et sonore

Les differences artistiques ne modifient pas le gameplay :

- le Zombie utilise une silhouette de mort-vivant cartoon et non horrifique ;
- sa marche parait plus lourde, mais conserve la vitesse de `140 px/s` ;
- ses mouvements produisent des pas lourds et un leger son de tissu use ;
- ses reactions peuvent utiliser un grognement cartoon court ;
- aucun gargarisme, son organique realiste, sang ou effet gore n'est utilise ;
- la lecture des armes, des directions et des phases d'attaque reste identique a celle des Squelettes.

## Valeurs communes heritees

| Element | Valeur |
|---|---:|
| Enveloppe visuelle | `48 x 72 px` |
| Collision avec le decor | `36 x 60 px` |
| Zone vulnerable du corps | `32 x 56 px` |
| Zone dangereuse du corps | `32 x 56 px` |
| Vitesse de patrouille | `140 px/s` |
| Largeur de patrouille | `800 px` |
| Extension autour de la position initiale | `400 px` de chaque cote |
| Degats de contact | `1 coeur` |
| Reaction non fatale | `0.33 s` |
| Protection entre deux impacts | `0.33 s` |
| Duree de defaite | `0.67 s` |

## Points de vie valides

- Le Zombie epeiste possede `3 PV`.
- Le Zombie archer possede `3 PV`.
- Une attaque normale de la Shadow Sword inflige `1 degat`.
- Trois attaques normales sont necessaires pour vaincre un Zombie.
- Un Smash Tranchant inflige `2 degats`.
- Un Smash utilise contre un Zombie a `3 PV` le laisse a `1 PV`.
- Un Smash suivi d'une attaque normale suffit a le vaincre.
- Deux Smashs peuvent egalement le vaincre.
- Chaque impact non fatal declenche la reaction et la protection de `0.33 s`.
- Aucun point de vie n'est restaure pendant la vie en cours.
- Les `3 PV` sont restaures uniquement lors de la reinitialisation des ennemis.

## Zombie epeiste

Le Zombie epeiste herite sans modification des regles de l'Epeiste :

- patrouille permanente de `800 px` a `140 px/s` ;
- aucune poursuite directe d'Imran ;
- corps dangereux sur tous les cotes pour `1 coeur` ;
- epee maintenue droite devant lui ;
- epee visuelle de `56 x 16 px` ;
- zone dangereuse de lame de `44 x 10 px` ;
- danger de contact permanent ;
- aucun emplacement d'attaque occupe.

Sa resistance de `3 PV` constitue sa seule difference de gameplay avec le Squelette epeiste.

## Zombie archer

Le Zombie archer herite sans modification des regles de l'Archer :

- patrouille permanente de `800 px` a `140 px/s` ;
- aucune poursuite directe d'Imran ;
- detection horizontale de `800 px` ;
- detection verticale de `480 px` ;
- visibilite et ligne de vue obligatoires ;
- tir uniquement dans la direction regardee ;
- preparation de `0.50 s` sans arret de la patrouille ;
- delai minimal de `2 s` entre deux lancements ;
- recuperation visuelle de `0.25 s` ;
- fleche visuelle de `48 x 12 px` ;
- zone dangereuse de fleche de `40 x 8 px` ;
- vitesse de fleche de `600 px/s` ;
- portee maximale de `960 px` ;
- duree maximale de `1.60 s` ;
- degats de fleche de `1 coeur` ;
- blocage automatique par le Bouclier de lumiere lorsque la fleche arrive de face ;
- disparition de la fleche selon toutes les regles du Squelette archer.

Sa resistance de `3 PV` constitue sa seule difference de gameplay avec le Squelette archer.

## Reactions, collisions et persistance

- Un impact non fatal arrete le Zombie pendant `0.33 s`.
- Son orientation est conservee pendant cette reaction.
- Une preparation de tir est annulee par un impact.
- Une fleche deja lancee continue normalement.
- Les dangers de contact restent actifs pendant une reaction non fatale.
- Toutes les collisions avec Imran, les ennemis et le decor suivent les regles des Squelettes.
- Les Zombies ne quittent jamais leur zone de patrouille pour poursuivre Imran.
- Ils conservent leurs points de vie et leur position pendant la vie en cours.
- Une perte de vie, un Game Over, un abandon ou un rechargement restaure leur position initiale, leur orientation initiale et leurs `3 PV`.
- Un Zombie vaincu reste absent pendant le reste de la vie en cours.
- Aucun Zombie ne produit de coeur, de vie, de cle ou de recompense.

## Emplacements d'attaque

- Le Zombie epeiste n'occupe jamais un emplacement d'attaque.
- Le Zombie archer suit exactement les regles d'emplacement du Squelette archer.
- Il occupe un emplacement depuis le debut de sa preparation jusqu'a la disparition de sa fleche.
- Une annulation ou une defaite libere immediatement cet emplacement.
- La limite commune de `3 ennemis ordinaires` reste applicable.

## Absence d'autres augmentations

Les Zombies ne possedent aucune augmentation cachee :

- pas de vitesse de patrouille supplementaire ;
- pas de zone de detection plus grande ;
- pas de preparation plus courte ;
- pas de cadence de tir plus elevee ;
- pas de fleche plus rapide ou plus grande ;
- pas de degats supplementaires ;
- pas de nouvelle attaque ;
- pas de poursuite plus agressive.

Le terme `plus agressif` du Concept Game est traduit dans le GDD uniquement par la pression produite par le point de vie supplementaire.

## Criteres de validation

La fiche des Zombies sera validee si :

- les deux variantes correspondent exactement aux variantes des Squelettes ;
- chaque variante possede `3 PV` ;
- toutes les autres valeurs restent identiques ;
- leur apparence et leurs sons restent cartoon et non horrifiques ;
- le joueur peut reutiliser les comportements appris contre les Squelettes ;
- aucune nouvelle decision de gameplay n'est necessaire dans le prototype.

## Sources

- [Zombies du Concept Game](../../Concept-Game/07-Ennemis/Zombies.md)
- [Squelettes du GDD](Squelettes.md)
- [Principes d'IA](../../Concept-Game/07-Ennemis/Principes-IA.md)
- [Animation](../../Concept-Game/09-Direction-Artistique/Animation.md)
- [Effets sonores](../../Concept-Game/10-Direction-Sonore/Effets-Sonores.md)
- [Voix](../../Concept-Game/10-Direction-Sonore/Voix.md)
- [Regles communes des ennemis](Regles-Communes.md)
