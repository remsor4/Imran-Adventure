# Invulnerabilite

> **Statut :** Valide

## Objectif

Empecher plusieurs pertes de coeur consecutives apres un degat non bloque tout en rendant rapidement le controle au joueur.

## Valeurs validees

| Element | Valeur |
|---|---:|
| Duree totale | `1.30 s` |
| Debut | Image ou le coeur est retire |
| Duree de reaction sans controle | `0.33 s` |
| Temps restant avec controle | `0.97 s` |

## Regles

- L'invulnerabilite commence au moment exact ou un degat retire un coeur.
- Pendant `1.30 s`, toute nouvelle source ordinaire est ignoree.
- Une source ignoree ne retire aucun coeur et ne relance jamais la duree.
- Le controle revient apres les `0.33 s` de reaction si Imran possede encore au moins un coeur.
- Imran peut ensuite se deplacer, sauter, attaquer et utiliser ses capacites pendant les `0.97 s` restantes.
- Les collisions avec le decor restent actives pendant toute la duree.
- L'invulnerabilite ne permet pas de traverser un mur, un ennemi solide ou une limite de niveau.
- La mort annule immediatement l'invulnerabilite en cours.

## Retour visuel et sonore

- Le degat initial produit un flash court et un son d'impact.
- La silhouette d'Imran utilise au maximum trois pulsations lentes pendant l'invulnerabilite.
- Aucun clignotement rapide ni son en boucle n'est utilise.
- La fin de l'invulnerabilite ne bloque pas le controle et ne demande aucun effet sonore obligatoire.

## Exclusions

- Un projectile bloque par le Bouclier ne declenche pas cette invulnerabilite.
- Une attaque ennemie ignoree pendant la duree ne declenche pas de recul.
- L'invulnerabilite courte utilisee apres une reapparition est un systeme distinct qui sera fixe pendant l'etape 7.
- Un danger explicitement mortel suivra les regles validees avec les vies et les reapparitions.

## Pause et transitions

- Pause suspend le compteur sans consommer sa duree.
- Une cinematique ou un chargement suspend le compteur tant que le gameplay ne progresse pas.
- Une mort, un changement de niveau ou une reapparition termine cette invulnerabilite de degat.

## Criteres de validation

L'invulnerabilite est validee si :

- un premier degat retire un coeur et demarre `1.30 s` de protection ;
- une nouvelle attaque pendant cette duree ne retire aucun coeur ;
- une attaque ignoree ne remet pas le compteur a zero ;
- le controle revient apres `0.33 s` ;
- les collisions du decor restent normales ;
- Pause ne consomme aucune partie de la duree.

## Sources

- [Degats](Degats.md)
- [Recul](Recul.md)
- [Reactions aux degats](../Joueur/Reactions-aux-Degats.md)
- [Reference video des degats recus](../Joueur/Reference-Video-Wonder-Boy-Degats-Imran.md)
- [Statistiques d'Imran](../Joueur/Statistiques-Imran.md)
