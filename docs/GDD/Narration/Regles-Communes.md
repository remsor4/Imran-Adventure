# Regles communes des cinematiques

> **Statut :** Valide

## Format de production valide

- Toutes les cinematiques sont realisees directement dans Godot.
- Elles utilisent les scenes, personnages, decors, animations, cameras et dialogues du jeu.
- Elles ne sont pas integrees sous la forme de fichiers video prerendus.
- Cette methode permet de modifier le cadrage, les durees, les animations et les dialogues sans refaire une video complete.
- Les sequences restent compatibles avec la resolution cible de `1920 x 1080`.

## Integration

- Une cinematique charge uniquement les ressources necessaires a la scene concernee.
- Le controle du joueur et le HUD suivent les regles qui seront validees dans cette fiche.
- Chaque scene precise son declencheur, ses personnages, son deroulement, ses informations affichees et le moment exact ou le controle revient.

## Dialogues et voix

- Tous les dialogues narratifs sont affiches sous forme de texte.
- Une boite de dialogue est placee dans la partie basse de l'ecran.
- La boite affiche le portrait, le nom et le texte du personnage qui parle.
- Sa taille et ses marges sont concues pour la resolution `1920 x 1080`.
- Elle ne masque pas le visage du personnage actif ni une action narrative importante.
- Les personnages utilisent de courtes vocalises pour accompagner leurs reactions et leurs prises de parole.
- Les vocalises ne reproduisent pas la phrase complete.
- Les phrases completes de Tata Lisa deja validees conservent leur voix enregistree et leur sous-titre.
- Couper le volume des voix ne masque jamais le texte d'un dialogue ou un sous-titre.

## Avancement des dialogues

- Chaque phrase reste affichee jusqu'a une pression sur la commande `Interaction`.
- Une pression valide uniquement la phrase actuellement affichee.
- Les actions cinematographiques sans dialogue avancent automatiquement selon leur duree.
- Une action necessaire a la comprehension attend la fermeture de la boite de dialogue avant de commencer.
- Le texte ne disparait jamais automatiquement pendant que le joueur le lit.

## Controle, HUD et commandes

- Le HUD est masque pendant toute cinematique.
- Le deplacement, le saut, le Double saut, le Dash et les attaques sont bloques.
- Une pression sur `Interaction` avance uniquement le dialogue courant.
- La commande `Retour` sert uniquement a passer la cinematique lorsqu'elle est maintenue.
- Le menu Pause ne peut pas etre ouvert pendant une cinematique.
- Le controle revient uniquement au point de reprise indique dans la fiche de la scene.

## Passage des cinematiques valide

- Maintenir la commande `Retour` pendant `1.50 s` passe la cinematique.
- Sur clavier, cette commande utilise `Echap`.
- Sur manette, elle utilise le bouton droit `B` ou `Rond` selon l'appareil.
- Un indicateur de progression apparait en bas a droite pendant le maintien.
- Relacher la commande avant `1.50 s` masque l'indicateur et annule le passage.
- La fonction reste disponible des la premiere lecture de la scene.
- Passer l'introduction place Imran au debut jouable du niveau 0 avec son etat initial complet.
- Passer un evenement entre deux niveaux place Imran dans la zone d'entree sure du niveau suivant.
- Passer la conclusion attend ou termine la sauvegarde finale avant d'afficher l'ecran de victoire.
- Passer une scene applique toujours son etat final : personnages, portes, effets, progression et camera.
- Une cle, une recompense ou une sauvegarde ne peut jamais etre perdue par cette action.

## Durees cibles validees

Les plages suivantes incluent une lecture normale des dialogues. Un joueur peut les prolonger puisque chaque phrase attend sa confirmation.

| Sequence | Duree cible |
|---|---:|
| Introduction complete | `50 a 70 s` |
| Apres la Foret enchantee | `15 a 22 s` |
| Apres la Grotte mysterieuse | `8 a 12 s` |
| Apres le Lac gele | `15 a 22 s` |
| Apres le Desert oublie | `8 a 12 s` |
| Apres le Volcan | `18 a 25 s` |
| Liberation et reunion familiale | `40 a 55 s` |

- Les animations sans dialogue utilisent des durees fixes a l'interieur de ces plages.
- Une scene attend aussi longtemps que necessaire pendant l'affichage d'un dialogue.
- La presentation de Tata Lisa, sa defaite et l'ouverture des six verrous conservent leurs durees exactes deja validees.

## Criteres techniques communs

- Une scene ne rend jamais le controle pendant un chargement ou un fondu noir.
- La camera est stabilisee avant le retour du controle.
- Les zones dangereuses et les ennemis sont desactives pendant une cinematique narrative.
- La boite de dialogue et l'indicateur de passage utilisent le dernier appareil actif.
- Toute phrase entierement enregistree conserve un sous-titre visible lorsque le volume des voix est coupe.
- Chaque fin de sequence appelle un unique point de sortie afin d'obtenir le meme resultat apres lecture complete ou passage.
