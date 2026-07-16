# Reference video du Dash Godot

> **Statut :** Valide

## Source

- Video : [Creer un dash en 2D : Godot - Debutant](https://www.youtube.com/watch?v=Au3OqStGrjo)
- Duree analysee : de `0:00` a `10:23`
- Moteur visible : Godot 4
- Resolution du flux utilise pour verifier le code : `1920 x 1080`

Cette video est un tutoriel d'implementation. Elle fournit des valeurs de depart coherentes, mais ne definit pas des standards universels pour tous les jeux de plateforme.

## Chapitres observes

| Plage approximative | Contenu | Utilisation |
|---|---|---|
| `0:00 - 0:46` | Presentation du Dash | Intention generale |
| `0:47 - 1:27` | Projet de base | Valeurs de deplacement servant au rapport |
| `1:28 - 7:00` | Creation du Dash | Vitesse, duree et logique horizontale |
| `7:01 - 9:59` | Limitation du Dash | Delai avant reutilisation |
| `10:00 - 10:23` | Conclusion | Verification du comportement final |

## Valeurs finales visibles dans le tutoriel

| Element | Valeur du tutoriel |
|---|---:|
| Vitesse horizontale normale du personnage dans l'inspecteur | `350 px/s` |
| Vitesse cible finale du Dash | `900 px/s` |
| Rapport Dash sur deplacement normal | Environ `2.57` |
| Duree du Dash avec `DashTimer` | `0.20 s` |
| Intervalle de reutilisation avec `DashAgainTimer` | `1.00 s` depuis le debut du Dash |
| Facteur d'interpolation horizontal | `0.20` par mise a jour physique |

Le tutoriel fait varier uniquement la composante horizontale avec une interpolation vers la vitesse cible. Le minuteur de reutilisation commence au meme moment que le minuteur du Dash.

## Normalisation pour Imran Adventure

La vitesse normale d'Imran est `240 px/s`. Le rapport du tutoriel donne `240 x 900 / 350`, soit environ `617 px/s`. La cible est arrondie a `620 px/s` pour rester lisible et simple a regler.

| Element | Cible pour Imran Adventure |
|---|---:|
| Vitesse du Dash | `620 px/s` |
| Duree du Dash | `0.20 s` |
| Distance theorique sans obstacle | Environ `124 px` |
| Intervalle entre deux declenchements | `1.00 s` depuis le debut du Dash |
| Delai restant apres la fin du Dash | `0.80 s` |

La distance theorique utilise une vitesse constante afin que le resultat soit previsible. L'implementation exacte de l'acceleration et des transitions sera detaillee dans le TDD.

## Comportements confirmes par la video

- Le Dash ne modifie que le mouvement horizontal.
- La commande peut etre recue sans condition de contact avec le sol.
- La gravite continue de modifier la vitesse verticale dans le tutoriel.
- Le Dash ne fournit aucune invulnerabilite.
- Les collisions normales du `CharacterBody2D` restent actives.
- Sans direction horizontale maintenue, la cible du tutoriel devient nulle.

## Adaptations propres a Imran Adventure

Le GDD conserve volontairement les regles suivantes, absentes ou differentes du tutoriel :

- le Dash peut etre declenche uniquement lorsque Imran touche une surface praticable ;
- une commande recue dans les airs est ignoree et n'est pas memorisee ;
- la direction utilise l'orientation d'Imran si aucune direction n'est maintenue ;
- la vitesse horizontale du Dash est appliquee de facon previsible ;
- quitter une surface d'appui interrompt immediatement le Dash et declenche la chute normale ;
- toucher un mur solide interrompt le Dash ;
- le Dash reste indisponible pendant les etats incompatibles ;
- les effets visuels et sonores rendent son debut et sa fin lisibles.

Ces adaptations preservent les intentions deja definies pour Imran Adventure sans copier toutes les simplifications du tutoriel.

## Valeurs a verifier dans le prototype

- La distance de `124 px` doit rester compatible avec une grille logique de `64 px`.
- Le delai restant de `0.80 s` ne doit pas rendre le deplacement lent ou frustrant.
- La reprise du controle horizontal ne doit pas provoquer de changement brutal.
- Une commande aerienne doit etre ignoree sans etre memorisee jusqu'a la reception.
- La sortie d'une plateforme doit interrompre proprement le Dash.
- Un obstacle doit arreter le Dash sans vibration ni traversee.

## Criteres de validation

La reference est correctement appliquee si :

- la vitesse du Dash reste proche de `2.57` fois la vitesse normale ;
- le Dash dure `0.20 s` ;
- un nouveau Dash ne peut pas commencer avant `1.00 s` depuis le precedent ;
- le Dash ne peut etre declenche que lorsque Imran touche le sol ;
- les adaptations propres au projet restent distinguees des comportements visibles dans le tutoriel ;
- les valeurs sont confirmees ou ajustees apres un prototype jouable.

## Sources internes

- [Dash](Dash.md)
- [Statistiques d'Imran](Statistiques-Imran.md)
- [Deplacement](Deplacement.md)
- [Etats du joueur](Etats-du-Joueur.md)
- [Reference video Wonder Boy](Reference-Video-Wonder-Boy.md)
