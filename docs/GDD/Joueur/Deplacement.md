# Deplacement

> **Statut :** Valide

## Objectif

Definir le mouvement horizontal d'Imran au sol et dans les airs.

## Regles au sol

- Imran se deplace uniquement vers la gauche ou la droite.
- Une direction maintenue rapproche progressivement sa vitesse de `240 px/s`.
- Il n'existe aucune commande de course.
- Relacher la direction applique le freinage jusqu'a l'arret.
- Une direction opposee commence par freiner, puis accelere dans le nouveau sens.
- Gauche et droite maintenues ensemble produisent une direction neutre.
- L'orientation suit la derniere direction valide sauf pendant une action qui la verrouille.

## Valeurs au sol

| Element | Valeur |
|---|---:|
| Vitesse maximale | `240 px/s` |
| Acceleration | `1800 px/s2` |
| Freinage | `2200 px/s2` |
| Temps theorique pour atteindre la vitesse maximale | Environ `0.13 s` |
| Temps theorique pour s'arreter | Environ `0.11 s` |

## Controle aerien

- Une direction peut modifier la trajectoire horizontale pendant le saut et la chute.
- Le controle aerien reste plus doux que le controle au sol.
- Relacher la direction en l'air reduit progressivement la vitesse horizontale sans l'annuler instantanement.
- Changer de direction en l'air est possible mais demande plus de temps qu'au sol.
- La vitesse horizontale normale ne depasse pas `240 px/s` hors Dash ou recul.

## Valeurs en l'air

| Element | Valeur |
|---|---:|
| Acceleration horizontale | `1200 px/s2` |
| Freinage horizontal | `600 px/s2` |
| Vitesse horizontale maximale normale | `240 px/s` |

## Pentes et plateformes

- Imran peut marcher sur une pente allant jusqu'a `45 degres`.
- Une pente plus forte est traitee comme un mur.
- Une plateforme traversable peut etre franchie par dessous puis supporte Imran lorsqu'il retombe dessus.
- Aucune commande de descente a travers une plateforme n'est prevue.
- Les petites irregularites du sol ne doivent pas provoquer un saut ou une chute involontaire.

## Collisions horizontales

- Un mur arrete le mouvement horizontal normal.
- Une pression continuee contre un mur ne produit ni tremblement ni accumulation de vitesse.
- Imran ne peut pas traverser un mur, un ennemi solide ou une limite de niveau.
- La collision ne change pas automatiquement son orientation.
- Aucun saut mural ni glissade murale n'est prevu.

## Cas particuliers

- Le mouvement est ignore pendant les etats verrouilles.
- Une reapparition remet la vitesse horizontale a zero.
- Une plateforme mobile transporte Imran sans modifier sa vitesse volontaire. Son comportement detaille sera precise dans les fiches de niveaux si elle est utilisee.
- Un Dash ou un recul peut depasser la vitesse normale mais conserve ses propres regles de collision.

## Criteres de validation

Le deplacement est valide si :

- la vitesse maximale est identique au clavier, a la croix et au stick ;
- le demarrage et l'arret restent rapides sans etre instantanes ;
- Imran peut corriger un saut sans changer brutalement de direction ;
- les directions opposees produisent une vitesse cible neutre ;
- un mur arrete Imran sans vibration visible ;
- aucune commande de course, saut mural ou descente de plateforme n'est introduite.

## Sources

- [Statistiques d'Imran](Statistiques-Imran.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Mapping clavier](../Controles/Mapping-Clavier.md)
- [Mapping manette](../Controles/Mapping-Manette.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
- [Deplacements du Concept Game](../../Concept-Game/05-Gameplay/Deplacements.md)
