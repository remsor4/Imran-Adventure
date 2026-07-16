# Options

> **Statut :** Valide

## Objectif

Regrouper les reglages utiles sur PC dans un ecran simple, accessible depuis le menu principal et le menu Pause.

## Organisation

Les reglages sont groupes dans quatre categories :

1. Audio ;
2. Affichage ;
3. Commandes ;
4. Accessibilite.

Le nom de la categorie, le reglage selectionne et sa valeur restent visibles en meme temps.

## Audio

La Direction sonore validee impose cinq controles separes :

| Reglage | Fonction |
|---|---|
| Volume general | Modifie toutes les categories |
| Musique | Modifie uniquement les musiques |
| Effets sonores | Modifie le gameplay et l'interface |
| Ambiances | Modifie les environnements |
| Voix | Modifie les vocalises et phrases |

- Chaque categorie peut etre diminuee ou coupee.
- Une preecoute courte et douce confirme la modification.
- La preecoute ne se repete pas pendant un deplacement rapide du curseur.
- Couper une categorie ne supprime jamais une information essentielle.

## Affichage

Le menu propose :

- mode fenetre, fenetre sans bordure ou plein ecran ;
- resolution compatible avec l'ecran ;
- luminosite ;
- taille de l'interface ;
- intensite des secousses d'ecran ;
- intensite des flashs et effets plein ecran.

La liste exacte des resolutions et les valeurs par defaut seront definies dans le GDD et le TDD.

Un changement pouvant rendre l'image illisible ouvre une confirmation temporaire. Sans validation, l'ancien reglage est restaure.

## Commandes

Le menu presente les actions du clavier et de la manette.

- Les commandes peuvent etre consultees depuis le menu principal et Pause.
- Le dernier appareil utilise determine les icones affichees dans le jeu.
- Une proposition de remappage doit signaler les conflits avant validation.
- Une commande essentielle ne peut pas rester sans touche.
- Un bouton restaure les commandes par defaut apres confirmation.
- Les commandes precises et leurs valeurs seront definies dans le GDD.

La souris peut naviguer dans les menus sans devenir obligatoire pour jouer.

## Accessibilite

Le menu propose :

- sous-titres pour toute phrase enregistree ;
- taille du texte ;
- taille de l'interface ;
- reduction ou suppression des secousses ;
- reduction des flashs ;
- affichage permanent des messages de commandes importants ;
- option pour remplacer les pressions repetees par une action maintenue lorsqu'un cas le demande.

Le jeu conserve une seule difficulte. Aucun reglage d'accessibilite ne doit etre presente comme un mode facile ou difficile.

## Application des changements

- Les volumes et options de confort sont appliques immediatement.
- Les changements d'affichage sensibles demandent une confirmation.
- Les commandes sont appliquees apres resolution des conflits.
- `Retour` conserve les changements deja appliques.
- `Valeurs par defaut` demande une confirmation avant de reinitialiser une categorie.

## Persistance

Les options sont enregistrees dans une configuration locale separee de la sauvegarde de progression.

- Effacer une partie ne reinitialise pas les options.
- Une erreur de configuration restaure des valeurs sures.
- Les options chargees sont appliquees avant l'affichage du menu principal.

## Depuis le menu Pause

- Le gameplay reste suspendu.
- Le retour replace le joueur dans le menu Pause.
- Les options appliquees sont conservees si le joueur reprend ou quitte le niveau.
- Une sauvegarde de progression n'est pas creee par une modification d'option.

## Validation des Options

L'ecran est coherent si :

- chaque categorie est comprise sans explication longue ;
- les valeurs actuelles restent visibles ;
- une modification dangereuse peut etre annulee ;
- les commandes essentielles restent assignees ;
- les options persistent sans modifier la progression ;
- la navigation fonctionne au clavier et a la manette.
