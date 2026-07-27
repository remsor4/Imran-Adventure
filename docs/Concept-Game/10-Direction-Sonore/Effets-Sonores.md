# Effets sonores

> **Statut :** Valide

## Objectif

Definir les grandes familles d'effets sonores et leur fonction. Un son de gameplay doit confirmer une action, annoncer un danger ou signaler un changement d'etat.

## Langage sonore

| Famille | Identite | Sens |
|---|---|---|
| Imran | Sons nets, courts et reactifs | Controle et mouvement |
| Shadow Sword | Metal sombre, souffle et reflet aigu | Attaque et energie noire maitrisee |
| Bouclier de lumiere | Impact rond, verre doux et accord chaud | Protection et reussite |
| Chaos | Texture instable, souffle inverse et grave magique | Tata Lisa et corruption |
| Golems | Pierre, materiau du biome et impact lourd | Masse et puissance |
| Recompense | Cloche claire, harpe et accord ascendant | Progression et victoire |
| Interface | Clic doux, bois et petite note | Navigation et confirmation |

Les sons importants utilisent une attaque claire et une duree courte. Les sons decoratifs restent plus doux et moins contrastes.

Les cristaux naturels de la Grotte utilisent des tintements purs, froids et reguliers. La magie du Chaos utilise des souffles inverses, des hauteurs instables et une resonance plus sombre. Ces deux familles ne doivent jamais partager exactement la meme signature.

## Deplacements d'Imran

| Action | Son attendu |
|---|---|
| Pas | Variation selon herbe, bois, pierre, sable, glace et metal |
| Saut | Impulsion courte et legere |
| Reception | Impact adapte au materiau et a la hauteur |
| Demi-tour | Frottement tres court |
| Dash | Souffle rapide avec direction nette |
| Double saut | Seconde impulsion plus aerienne et lumineuse |
| Glissade | Frottement continu leger, surtout sur la glace |
| Reapparition | Accord court de retour, sans son punitif |

Les pas utilisent plusieurs variations pour eviter une repetition mecanique. Ils deviennent plus discrets lorsque la musique ou un combat demande de l'espace.

## Combat d'Imran

### Shadow Sword

- sortie et rangement de la lame ;
- plusieurs variations de mouvement pour l'attaque normale ;
- impact different sur ennemi, pierre, metal et bouclier ;
- montee progressive pendant la charge ;
- depart puissant et trajectoire audible du Smash Tranchant ;
- disparition claire du projectile ou impact final.

Le Smash Tranchant conserve un element aigu afin de rester audible dans le Chateau et les combats charges.

### Bouclier de lumiere

- apparition courte de la protection ;
- impact rond et lumineux lors d'une protection automatique reussie ;
- variation plus lourde contre une attaque de boss ;
- disparition courte du projectile bloque, sans son de renvoi ;
- disparition discrete de la lumiere apres l'impact.

Une protection automatique reussie doit etre immediatement reconnaissable sans regarder l'interface.

## Ennemis

Chaque type possede une signature simple :

- **Chauve-souris :** battement d'ailes souple et petit cri non agressif ;
- **Slime :** mouvement humide, rebond doux et eclatement cartoon ;
- **Serpent :** glissement sec et souffle court avant l'attaque ;
- **Squelette :** claquement leger d'os stylises et mouvement articule ;
- **Zombie :** pas lourd, tissu use et grognement cartoon non horrifique.

Le son de preparation d'une attaque reste different du son d'attente. La disparition d'un ennemi est courte, non violente et sans effet organique realiste.

## Degats, coeurs et vies

- Imran produit un son d'impact, un court signal d'alerte et une reaction vocale.
- La perte d'un coeur est plus legere que la perte d'une vie.
- La perte d'une vie utilise une descente musicale courte, sans son brutal.
- La recuperation des coeurs et des vies utilise un accord ascendant et chaleureux.
- L'invulnerabilite temporaire ne produit pas de boucle sonore fatigante.

Le joueur doit distinguer un degat subi, un projectile bloque automatiquement et une attaque infligee.

## Coffres, cles et progression

| Evenement | Son attendu |
|---|---|
| Coffre disponible | Petit reflet sonore discret |
| Ouverture du coffre et revelation de la cle | Son commun de `2.00 s` combinant mecanisme, montee magique et tintement final |
| Cle recuperee | Aucun son supplementaire avant le signal distinct de sauvegarde |
| Pancarte du Dash comprise | Impulsion rapide suivie d'un accord positif |
| Pancarte du Double saut comprise | Deux notes ascendantes et effet aerien |
| Six verrous ouverts | Six reactions courtes puis accord final |

Les six coffres utilisent le meme asset original : `assets/audio/sfx/ouverture-coffre-commune.wav`. Aucun son de matiere propre au niveau et aucun second tintement de cle ne sont ajoutes.

La musique de recompense peut remplacer une partie des autres effets pour eviter une accumulation excessive.

## Points de controle et sauvegarde

- Une pancarte activee utilise un son de bois leger suivi d'une confirmation breve, douce et clairement reconnaissable.
- Le son d'activation est joue une seule fois pendant la tentative, meme si Imran retraverse la zone.
- Une reapparition a la pancarte utilise le meme motif sous une forme plus douce.
- La sauvegarde automatique utilise un signal court, calme et distinct de la recuperation d'un objet.
- La fin de sauvegarde confirme clairement que le joueur peut continuer.

## Boss

Tous les golems partagent une base sonore commune :

- coeur magique qui s'allume ;
- roche qui se deplace ;
- impact lourd des pieds et des poings ;
- charge annoncee par une montee grave ;
- coeur qui faiblit ;
- desassemblage final non violent.

Chaque golem ajoute son materiau :

| Golem | Matiere sonore |
|---|---|
| Foret | Pierre, racines, feuilles |
| Grotte | Roche, minerais, cristaux |
| Lac | Glace, neige, fissures froides |
| Desert | Gres, sable, blocs anciens |
| Volcan | Basalte, magma, vapeur |
| Chateau | Pierre noire, armure, metal et magie |

Tata Lisa utilise des sons plus rapides et moins reguliers. Ses attaques partent de sa voix, de ses gestes ou de la Pierre du Chaos avant de devenir dangereuses.

## Interface

- deplacement du focus ;
- validation ;
- retour ;
- erreur ou action indisponible ;
- ouverture et fermeture d'un menu ;
- modification d'une option ;
- confirmation d'une action importante ;
- apparition et fin du Game Over ;
- ecran de victoire.

Les sons d'interface restent courts, doux et coherents. Une erreur doit etre claire sans etre agressive.

## Variations et repetition

- Les pas, coups et impacts utilisent plusieurs variations proches.
- La hauteur et le volume peuvent varier legerement sans changer la fonction du son.
- Les sons frequents sont plus courts et moins brillants que les sons rares.
- Un meme effet ne doit pas etre relance de facon a augmenter brutalement le volume.
- Les sons aleatoires ne doivent jamais ressembler a un signal de danger.

## Priorite et confort

- Les attaques dangereuses passent avant les impacts decoratifs.
- Les sons repetes sont limites pendant les combats charges.
- Les basses des golems laissent de la place a la musique et aux alertes.
- Les sons aigus du Dash, des cles et de l'interface restent doux.
- Le joueur peut regler les effets sonores separement de la musique et des ambiances.

## Validation d'un effet

Un effet est coherent si :

- sa fonction est comprise sans image ;
- il reste distinct des sons proches ;
- son volume correspond a son importance ;
- il supporte la repetition ;
- il correspond au materiau visible ;
- il reste confortable pour un jeune public ;
- il ne masque pas une alerte plus importante.
