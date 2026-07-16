# Conventions documentaires

> **Statut :** Valide

## Format

- Tous les documents utilisent le format Markdown avec l'extension `.md`.
- Les nouveaux contenus Markdown ne contiennent aucune lettre accentuee.
- Un fichier traite un seul sujet principal.
- Les images restent dans le dossier `assets` et sont liees depuis les documents.
- Les liens internes utilisent des chemins relatifs.
- Les informations commerciales sont interdites dans le GDD.

## Nommage

- Les noms de dossiers et de fichiers utilisent uniquement des lettres ASCII, des chiffres et des tirets.
- Les espaces sont remplaces par des tirets.
- Chaque mot principal commence par une majuscule.
- Le fichier `README.md` sert de sommaire dans chaque dossier.
- Les termes officiels suivent le [glossaire du Concept Game](../../Concept-Game/01-Projet/Glossaire.md).

Exemples valides :

- `Double-Saut.md` ;
- `Coeurs-et-Vies.md` ;
- `Niveau-1-Foret.md` ;
- `Perimetre-et-Sources.md`.

## Structure minimale d'un document de regles

Un document de regles contient, lorsque le sujet le permet :

1. un titre ;
2. un statut ;
3. un objectif ;
4. les regles ;
5. les valeurs ;
6. les cas particuliers ;
7. les retours visuels et sonores ;
8. les criteres de validation ;
9. les liens vers les documents dependants.

Une section inutile peut etre omise. Une section requise ne doit pas rester vide dans un document valide.

## Statuts autorises

| Statut | Signification |
|---|---|
| `A rediger` | Le fichier est prevu mais sa redaction n'a pas commence |
| `En cours` | Le contenu est en cours de preparation ou de discussion |
| `A valider` | Le contenu est complet et attend la decision de Rems |
| `Valide` | Le contenu a ete accepte par Rems |
| `A revoir` | Une modification validee ailleurs exige une nouvelle verification |

Seul Rems peut faire passer un document de `A valider` a `Valide`.

## Regles de redaction

- Utiliser des phrases courtes et mesurables.
- Decrire le resultat attendu, pas le code utilise pour l'obtenir.
- Eviter les termes vagues comme `rapide`, `fort` ou `court` lorsqu'une valeur est necessaire.
- Employer les memes noms dans tous les documents.
- Utiliser un point pour les nombres decimaux.
- Toujours indiquer l'unite d'une valeur : secondes, pixels, degats ou pourcentage.
- Placer les valeurs regroupees dans un tableau lorsque cela facilite leur comparaison.
- Lier la definition principale au lieu de la recopier dans plusieurs fichiers.
- Ne jamais copier une mecanique provenant d'une licence existante sans l'adapter a Imran Adventure.

## Criteres de validation documentaires

Un fichier peut passer au statut `A valider` uniquement si :

- toutes ses sections necessaires sont remplies ;
- ses liens fonctionnent ;
- ses termes respectent le glossaire ;
- ses valeurs ne contredisent aucun autre document ;
- ses regles couvrent les cas d'echec importants ;
- ses criteres de validation sont observables ;
- son contenu reste dans le perimetre du GDD ;
- les nouveaux textes ne contiennent aucune lettre accentuee.
