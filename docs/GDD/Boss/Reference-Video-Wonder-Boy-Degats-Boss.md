# Reference video Wonder Boy - Degats des boss

> **Statut :** Valide

## Sources

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.25-03.48.mp4` | `1920 x 1088` | Environ `60 images/s` | `57.03 s` |
| `Wonder Boy The Dragon's Trap_2026.07.25-03.46.mp4` | `1920 x 1088` | Environ `60 images/s` | `21.57 s` |

## Methode

- Les captures completes ont ete examinees a `1 image/s` pour localiser les combats et les impacts.
- Les sequences de combat ont ensuite ete examinees a `5 images/s`.
- Deux impacts representatifs ont ete verifies a `20 images/s`.
- La position de la lame, le flash du boss et la valeur de la barre ont ete compares image par image.

## Observations

- La barre de vie apparait apres la presentation du boss.
- Les coups valides touchent la tete du boss.
- Un contact valide produit un flash clair du boss et une baisse immediate de la barre.
- Dans la capture `03.48`, un coup a la tete fait notamment passer la barre de `100` a `88`.
- Un autre impact a la tete fait passer la barre de `88` a `80`.
- Les contacts et attaques qui ne chevauchent pas la tete ne produisent aucune baisse de la barre.
- Un coup peut infliger des degats pendant une action offensive du boss.
- Le boss conserve donc une zone vulnerable pendant le combat actif et pas seulement pendant une recuperation.
- La phase de defaite commence lorsque la barre atteint `0`.

Les valeurs de degats visibles appartiennent a Wonder Boy. Elles ne remplacent pas les degats deja valides pour Imran Adventure.

## Regle retenue pour Imran Adventure

- Les six golems et Tata Lisa peuvent recevoir des degats pendant tout le combat actif.
- La preparation, l'execution et la recuperation d'une attaque ne ferment pas automatiquement leur vulnerabilite.
- Seule la zone de la tete peut recevoir une attaque normale ou un Smash Tranchant.
- Un impact sur le corps, les bras, les jambes, une arme ou un autre element du boss ne retire aucun point de vie.
- La presentation, une transition de phase et la phase de defaite rendent le boss invulnerable.
- Un impact valide ne ralentit, ne repousse et n'interrompt pas l'action du boss.
- Un flash et une protection contre un nouvel impact durent `0.33 s`.
- Les degats restent ceux du GDD : `1 degat` pour une attaque normale et `2 degats` pour le Smash Tranchant.
- Un Smash qui atteint reellement la tete pendant le combat actif conserve ses `2 degats` et ne subit aucune penalite.
- Lorsque la barre atteint `0`, le boss entre dans un etat `Etourdi` propre a Imran Adventure.
- Un Smash Tranchant touchant ensuite n'importe quelle partie de son corps declenche sa defaite cinematographique sans infliger de degat supplementaire.

## Limites

- Les captures ne montrent pas de transition de phase identifiable.
- L'invulnerabilite pendant les transitions de phase est une regle propre a Imran Adventure validee par Rems.
- Les captures ne permettent pas de fixer les dimensions de la zone vulnerable de la tete.
- La capture montre un flash proche de `0.35 s` ; la valeur de `0.33 s` est une normalisation validee pour Imran Adventure.
- La finition obligatoire au Smash Tranchant est une regle propre a Imran Adventure et non une mesure tiree des captures.

## Sources internes

- [Regles communes des boss](Regles-Communes.md)
- [Degats](../Combat/Degats.md)
- [Attaque normale](../Combat/Attaque-Normale.md)
- [Smash Tranchant](../Combat/Smash-Tranchant.md)
