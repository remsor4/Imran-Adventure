# Reference video - collisions avec le corps des boss

> **Statut :** Valide

## Source analysee

| Fichier | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.25-03.48.mp4` | `1920 x 1088` | Environ `60 images/s` | Environ `57.03 s` |

## Objectif

Observer plusieurs contacts entre le joueur et le corps du boss afin de determiner :

- si le corps inflige un degat ;
- si le corps agit comme un obstacle solide ;
- comment le joueur est separe du boss apres le contact ;
- si un coup porte a la tete peut etre valide en meme temps qu'un degat recu.

## Methode

- La video longue a ete examinee image par image.
- Plusieurs sequences de contact ont ete comparees, notamment autour de `25.8 s`, `29.9 s`, `34.1 s` et `42.5 s`.
- Les coeurs du joueur ont ete compares avant et apres chaque contact.
- La position du joueur a ete suivie pendant le chevauchement et le recul.
- La barre du boss a ete verifiee afin de distinguer un contact avec son corps d'un coup valide sur sa tete.
- Les projectiles visibles ont ete separes des contacts directs avec le corps.

## Observations

- Plusieurs contacts directs retirent une partie de la vie du joueur dans la reference.
- Chaque degat produit un retour visuel puis eloigne le joueur du boss.
- Les silhouettes du joueur et du boss peuvent se chevaucher pendant plusieurs images.
- Aucun arret rigide comparable a une collision avec un mur n'est observe.
- La separation visible provient principalement de la reaction et du recul apres le degat.
- Un coup valide sur la tete et un contact dangereux avec le corps peuvent se produire pendant la meme sequence.
- Dans ce cas, la barre du boss diminue tandis que le joueur subit egalement sa reaction de degat.

## Regle retenue pour Imran Adventure

- Le corps d'un boss est dangereux mais non solide pour Imran.
- Un contact valide retire `1 coeur`.
- Il applique la reaction de `0.33 s`, le recul horizontal de `220 px/s` et l'invulnerabilite de `1.30 s` deja valides.
- Pendant cette invulnerabilite, Imran peut traverser le boss sans perdre un nouveau coeur.
- Un coup porte au boss et un degat recu par Imran peuvent etre valides simultanement.
- Le corps devient inoffensif pendant la presentation, la phase de defaite et l'etat `Etourdi`.

## Adaptation

Wonder Boy utilise une reserve de vie et des portions de coeur differentes de celles d'Imran Adventure. La reference sert donc a definir le comportement du contact, tandis que la valeur est normalisee a la regle commune de `1 coeur` par degat ordinaire.

La video permet d'observer le resultat visible mais pas l'organisation interne des collisions du jeu de reference. Le GDD decrit uniquement le comportement attendu pour le joueur.

## Documents lies

- [Regles communes des boss](Regles-Communes.md)
- [Degats](../Combat/Degats.md)
- [Recul](../Combat/Recul.md)
- [Invulnerabilite](../Combat/Invulnerabilite.md)
- [Reference video des degats d'Imran](../Joueur/Reference-Video-Wonder-Boy-Degats-Imran.md)
