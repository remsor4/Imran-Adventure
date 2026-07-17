# GDD - Systemes

> **Statut :** En cours

## Objectif

Definir les regles communes de l'aventure afin que chaque echec, reprise, sauvegarde et progression produise un resultat previsible.

## Documents

| Ordre | Document | Statut initial |
|---:|---|---|
| 1 | [Coeurs et vies](Coeurs-et-Vies.md) | Valide |
| 2 | [Game Over](Game-Over.md) | Valide |
| 3 | [Checkpoints](Checkpoints.md) | A rediger |
| 4 | [Coffres et cles](Coffres-et-Cles.md) | A rediger |
| 5 | [Sauvegarde](Sauvegarde.md) | A rediger |
| 6 | [Progression](Progression.md) | A rediger |
| 7 | [Camera](Camera.md) | A rediger |

## Ordre de validation

1. Finaliser la perte et la recuperation des coeurs et des vies.
2. Relier la derniere vie au Game Over et au redemarrage du niveau.
3. Definir l'activation temporaire des checkpoints et la reapparition.
4. Definir l'ouverture des coffres, la recuperation des cles et les six verrous.
5. Definir chaque sauvegarde automatique et chaque point de reprise.
6. Confirmer la progression lineaire et l'absence de capacite a debloquer.
7. Fixer les valeurs de suivi, de cadrage et de confort de la camera.
8. Verifier tous les cas d'echec, de fermeture du jeu et de reprise.

## Criteres de validation de l'etape

L'etape 7 est validee si :

- chaque perte de coeur ou de vie possede une consequence unique ;
- chaque reapparition indique le point de retour et les valeurs restaurees ;
- les checkpoints temporaires ne sont jamais confondus avec une sauvegarde ;
- chaque coffre et chaque cle possedent une condition et un resultat ;
- chaque sauvegarde automatique possede un declencheur et un point de reprise ;
- la progression reste lineaire du niveau 0 a la liberation d'Aliyah ;
- la camera conserve Imran, les plateformes et les dangers importants dans une zone lisible.
