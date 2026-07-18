# Reference video Wonder Boy - Reactions des ennemis

> **Statut :** Valide

## Sources

| Capture | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.18-04.03.mp4` | `1920 x 1088` | Environ `60 images/s` | `12.98 s` |
| `Wonder Boy The Dragon's Trap_2026.07.18-04.04.mp4` | `1920 x 1088` | Environ `60 images/s` | `10.50 s` |

Les captures incluent les bordures de la fenetre et la barre des taches. Ces elements ne modifient pas la mesure temporelle des reactions.

## Methode

- Les passages de combat ont ete examines image par image.
- Les impacts non fatals et les impacts fatals ont ete mesures separement.
- Pour un impact non fatal, le debut correspond a la premiere image du flash et du recul apres le contact de la lame.
- Pour un impact non fatal, la fin correspond au retour stable a l'apparence et a la pose normales.
- Pour un impact fatal, la fin correspond a la premiere image sur laquelle l'ennemi a entierement disparu.

## Mesures

| Capture | Type d'impact | Images | Duree approximative |
|---|---|---:|---:|
| `04.03` | Non fatal | `18` | `0.30 s` |
| `04.03` | Fatal, jusqu'a la disparition | Environ `40` | Environ `0.67 s` |
| `04.04` | Non fatal | `18` | `0.30 s` |
| `04.04` | Fatal, jusqu'a la disparition | Environ `40` | Environ `0.67 s` |

## Valeur retenue

Les deux reactions non fatales mesurees durent `0.30 s`, soit environ `18 images` a `60 images/s`.

Imran Adventure retient une duree legerement adaptee de `0.33 s`, soit environ `20 images` a `60 images/s`. Cette duree est utilisee pour la reaction d'un ennemi touche par l'attaque normale ou par le Smash Tranchant. Le Smash conserve ses `2 degats`, mais ne prolonge pas la reaction.

Les deux disparitions mesurees durent environ `0.67 s`. Imran Adventure retient cette meme valeur pour la duree de defaite des ennemis ordinaires.

## Observations

- La reaction combine un flash clair, un recul visible et un court blocage.
- Aucun long temps d'attente supplementaire n'apparait apres le retour a la pose normale.
- Un impact fatal prolonge le clignotement et le retour visuel avant la disparition complete.
- Les deux captures montrent des attaques normales de l'epee.
- Elles ne contiennent aucune attaque equivalente au Smash Tranchant.
- Elles ne permettent pas de verifier une interruption pendant la preparation d'une attaque ennemie.

## Limites

- Les mesures portent sur le resultat visuel de Wonder Boy et non sur son code interne.
- Une marge d'environ une ou deux images peut subsister a cause des transitions du flash.
- La valeur devra etre confirmee dans le prototype Godot avec les animations propres a Imran Adventure.
