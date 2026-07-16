# Processus de validation

> **Statut :** Valide

## Responsabilites

| Personne | Responsabilites |
|---|---|
| Rems | Donne les intentions, choisit entre les propositions et valide les decisions finales |
| Codex | Analyse les documents, propose des solutions, redige, controle la coherence et applique les corrections validees |

Le projet ne prevoit aucun autre membre d'equipe.

## Cycle de redaction

1. Codex relit les sources validees.
2. Codex identifie les informations deja connues et les decisions manquantes.
3. Rems choisit les elements qui changent l'experience ou l'identite du jeu.
4. Codex redige les documents concernes.
5. Codex verifie les liens, les valeurs, les termes et les contradictions.
6. Le document passe au statut `A valider`.
7. Rems valide le contenu ou demande une correction.
8. Apres validation explicite, le document passe au statut `Valide`.

Une etape du plan commence uniquement lorsque l'etape precedente est validee.

## Audit croise toutes les deux etapes

Apres chaque etape paire validee, Codex audite les deux etapes qui viennent d'etre terminees avant de commencer l'etape suivante.

L'audit controle :

- la coherence entre les deux etapes ;
- la conformite avec le Concept Game ;
- la conformite avec le cadre du GDD ;
- les statuts autorises ;
- les liens internes ;
- les termes et les valeurs ;
- l'absence de contenu manquant ;
- l'absence de lettres accentuees dans les nouveaux contenus.

Codex presente les problemes trouves a Rems. Les corrections confirmees sont appliquees dans un commit de maintenance separe avant le debut de l'etape suivante.

## Modification d'une decision validee

Lorsqu'une decision validee change :

1. identifier son document principal ;
2. passer ce document au statut `A revoir` ;
3. rechercher tous les documents dependants ;
4. appliquer la nouvelle decision dans le document principal ;
5. corriger les documents dependants ;
6. verifier les liens et les contradictions ;
7. demander une nouvelle validation a Rems.

Une modification du TDD ne peut pas changer silencieusement une regle du GDD. Une limite technique doit etre expliquee, puis la modification du GDD doit etre validee avant son implementation.

## Controle avant validation

Codex verifie :

- le statut du document ;
- l'absence de section vide ;
- l'absence de valeur contradictoire ;
- l'absence de lien casse ;
- la conformite avec le Concept Game ;
- la frontiere entre GDD et TDD ;
- la coherence avec le public cible ;
- la presence de criteres de validation ;
- l'absence de lettres accentuees dans les nouveaux contenus.

## Decision finale

Une absence de reponse ne vaut jamais validation. La validation doit etre exprimee clairement par Rems.

## Commit de fin d'etape

Apres chaque validation explicite d'une etape, Codex cree automatiquement un commit au format suivant :

`docs(gdd): valider etape N - sujet`

Le message utilise uniquement des caracteres ASCII et indique le numero ainsi que le sujet de l'etape.

Le commit contient uniquement les fichiers lies a l'etape validee. Les modifications sans rapport restent hors du commit. Apres la creation, Codex communique le message et l'identifiant court du commit a Rems.
