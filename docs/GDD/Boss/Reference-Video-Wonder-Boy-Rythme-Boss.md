# Reference video - rythme des attaques de boss

> **Statut :** Valide

## Source analysee

| Fichier | Resolution | Frequence | Duree |
|---|---:|---:|---:|
| `Wonder Boy The Dragon's Trap_2026.07.25-03.48.mp4` | `1920 x 1088` | Environ `60 images/s` | Environ `57.03 s` |

## Objectif

Determiner si le boss enchaine directement ses attaques ou s'il utilise une recuperation suivie d'une pause neutre.

## Methode

- Plusieurs cycles de projection de flammes ont ete examines image par image.
- La disparition de la derniere flamme produite a ete comparee au retour du boss a sa posture normale.
- Le temps passe dans cette posture a ensuite ete compare au debut de l'attaque suivante.
- Les mesures sont arrondies au dixieme de seconde.

## Sequences observees

| Sequence | Fin approximative des flammes | Attaque suivante | Intervalle visible |
|---:|---:|---:|---:|
| 1 | `35.4 s` | `37.0 s` | Environ `1.6 s` |
| 2 | `41.1 s` | `43.2 s` | Environ `2.1 s` |
| 3 | `43.9 s` | `46.5 s` | Environ `2.6 s` |

## Observations

- Le boss ne commence pas immediatement une nouvelle attaque apres la disparition de ses flammes.
- Il termine d'abord son animation offensive et revient a sa posture normale.
- Il conserve ensuite cette posture pendant une pause visible.
- La preparation de l'attaque suivante commence seulement apres cette pause.
- Les coups recus par le boss ne suppriment pas visiblement cette structure.
- Les flammes deja projetees continuent leur trajectoire pendant le retour du boss vers sa posture normale.
- Les anciennes flammes disparaissent avant la preparation visible de l'attaque suivante.
- Aucune superposition de deux vagues dangereuses n'est observee.

## Regle retenue pour Imran Adventure

Le cycle commun d'un golem utilise la structure suivante :

1. preparation ;
2. phase dangereuse ;
3. recuperation animee ;
4. pause neutre ;
5. preparation de l'attaque suivante.

- La recuperation et la pause sont deux periodes distinctes.
- Aucune nouvelle attaque ne commence pendant ces periodes.
- Le golem reste vulnerable et son corps reste dangereux.
- Recevoir un degat ne modifie pas leur duree.
- Un projectile deja lance continue jusqu'a sa collision ou a la fin de sa duree de vie.
- Tous les projectiles precedents disparaissent avant la preparation suivante.
- Deux phases dangereuses consecutives ne se superposent jamais.

## Normalisation validee

Les trois intervalles observes durent environ `1.6 s`, `2.1 s` et `2.6 s`. Leur moyenne est donc proche de `2.1 s`.

Pour les six golems, cet intervalle commun est separe ainsi :

| Periode | Duree |
|---|---:|
| Recuperation animee | `0.30 s` |
| Pause neutre | `1.80 s` |
| Intervalle total | `2.10 s` |

- La valeur totale reprend la moyenne des sequences mesurees.
- La separation entre recuperation et pause constitue une adaptation de conception.
- Les durees de preparation et de danger restent propres a chaque attaque.
- Tata Lisa possede un rythme distinct qui sera defini dans sa fiche.

## Limites

- La capture montre un boss de Wonder Boy et une seule famille d'attaque.
- Les intervalles observes ne deviennent pas des valeurs communes obligatoires pour les six golems.
- La reference valide la structure du cycle, pas les durees definitives de chaque attaque.

## Documents lies

- [Regles communes des boss](Regles-Communes.md)
- [Reference video des degats des boss](Reference-Video-Wonder-Boy-Degats-Boss.md)
- [Reference video des collisions avec le corps des boss](Reference-Video-Wonder-Boy-Collisions-Boss.md)
