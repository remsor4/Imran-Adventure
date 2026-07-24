# Reference video Wonder Boy - Plongees des Chauves-souris

> **Statut :** Valide

## Source

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.24-00.01.mp4` | `1920 x 1088` | Environ `60 images/s` | `16.08 s` |

La partie de gameplay exploitable se situe principalement entre environ `6.1 s` et `13.4 s`. Le debut et la fin de la capture contiennent des menus ou des transitions.

## Methode

- La capture complete a ete examinee a `2 images/s` pour isoler la rencontre.
- La sequence de gameplay a ensuite ete examinee a `5 images/s`, puis a `10 images/s`.
- Un passage representatif a ete verifie image par image a `60 images/s`.
- Les positions hautes, les passages proches d'Imran, les impacts et les remontees ont ete compares pour les deux ennemis.

## Observations

- Les deux ennemis restent constamment en vol pendant la rencontre.
- Ils alternent une position haute, une descente en courbe, un passage pres d'Imran et une remontee.
- Leurs positions horizontales evoluent avec la zone occupee par le joueur.
- Les deux trajectoires peuvent etre differentes ou presque symetriques.
- Les ennemis convergent parfois vers Imran depuis deux directions opposees.
- Aucun projectile, aucune phase au sol et aucune teleportation ne sont visibles.
- Le contact avec Imran produit sa reaction de degat normale.
- La trajectoire de l'ennemi continue apres le contact.
- La remontee eloigne temporairement l'ennemi et separe deux passages dangereux.
- Les passages representatifs montrent une descente d'environ `1.3 a 1.5 s` et une remontee d'environ `0.7 a 0.9 s`.

## Regle retenue pour Imran Adventure

- La Chauve-souris utilise un cycle continu de plongee et de remontee apres son activation.
- Son propre corps constitue l'attaque.
- Elle passe vers la hauteur d'Imran, remonte, puis prepare un nouveau passage.
- La position d'Imran est memorisee au debut de chaque descente et la trajectoire ne se corrige plus pendant ce passage.
- La descente est normalisee a `1.40 s` et la remontee a `0.80 s`.
- Avec les `0.30 s` de preparation ajoutees pour la lisibilite, un cycle complet dure `2.50 s`.
- La vitesse moyenne est normalisee a `320 px/s` pendant la descente et a `480 px/s` pendant la remontee.
- La plongee est limitee a `320 px` horizontalement et `320 px` verticalement vers le bas.
- Le repositionnement horizontal dans la partie haute utilise une vitesse de `240 px/s`.
- Elle ne se pose pas et ne retrouve pas un point stationnaire entre deux attaques.
- Les courbes restent souples, visibles et limitees a la zone de rencontre.

## Limites

- La capture ne montre pas clairement le comportement avant la premiere activation.
- Elle ne permet pas de mesurer une distance de detection.
- La capture ne confirme pas le mode de ciblage interne ; le verrouillage au debut de la descente est une adaptation validee pour rendre l'esquive previsible.
- Elle ne montre pas une sortie complete de la zone de detection.
- Les dimensions et les points de vie sont normalises dans la fiche des Chauves-souris ; les valeurs de vitesse restent a definir.

## Sources internes

- [Chauves-souris](Chauves-Souris.md)
- [Regles communes des ennemis](Regles-Communes.md)
- [Principes d'IA](../../Concept-Game/07-Ennemis/Principes-IA.md)
