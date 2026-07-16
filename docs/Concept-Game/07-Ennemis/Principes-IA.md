# Principes d’IA

> **Statut :** Validé

## Objectif du document

Ce document définit les principes communs qui dirigent le comportement des ennemis d’**Imran Adventure**.

L’intelligence artificielle doit proposer des affrontements accessibles, compréhensibles et progressifs. Les valeurs précises, comme les vitesses, les distances de détection et les temps d’attente, seront définies dans le Game Design Document.

## Lisibilité

Le joueur doit pouvoir comprendre rapidement ce que chaque ennemi s’apprête à faire.

- Chaque attaque est précédée d’une animation ou d’un mouvement reconnaissable.
- Les ennemis terrestres, aériens, épéistes et archers possèdent des silhouettes distinctes.
- Les projectiles doivent être clairement visibles.
- Une courte animation de récupération suit les attaques importantes.
- Les réactions aux dégâts et la défaite d’un ennemi doivent être immédiatement compréhensibles.
- Les effets visuels ne doivent pas masquer Imran, les plateformes ou les dangers.

## Prévisibilité

Chaque famille d’ennemis possède un comportement simple que le joueur peut apprendre.

- Les chauves-souris attaquent en plongeant.
- Les slimes se déplacent et attaquent en bondissant.
- Les serpents progressent rapidement au sol et attaquent à proximité.
- Les épéistes cherchent le combat rapproché.
- Les archers exercent une pression à distance.
- Les zombies conservent les rôles des squelettes, mais représentent une menace plus importante.

Les variantes visuelles d’un même ennemi conservent un comportement général reconnaissable. L’apparence environnementale des slimes ne doit donc pas empêcher le joueur d’identifier leur manière de se déplacer.

Une part limitée de variation peut éviter que les combats deviennent répétitifs, mais elle ne doit jamais supprimer les signes annonçant une attaque.

## Équité

Les ennemis doivent représenter un défi sans provoquer de dégâts injustes.

- Un ennemi ne doit pas attaquer Imran avant d’être visible à l’écran.
- Le joueur doit disposer d’un temps raisonnable pour réagir.
- Les attaques doivent pouvoir être évitées, bloquées ou contournées.
- Les ennemis ne doivent pas maintenir Imran bloqué dans une succession ininterrompue d’attaques.
- Plusieurs ennemis peuvent combattre ensemble, mais leurs attaques doivent rester lisibles.
- Après avoir attaqué, un ennemi laisse une courte occasion au joueur de riposter.
- Les ennemis ne poursuivent pas Imran au-delà de leur zone prévue.

## Progression

La difficulté des rencontres augmente progressivement au cours de l’aventure.

- Les premiers niveaux présentent les ennemis dans des situations simples.
- Chaque nouveau comportement est découvert avant d’être combiné avec d’autres menaces.
- Les niveaux suivants associent progressivement les ennemis terrestres, aériens et à distance.
- Les capacités débloquées par Imran peuvent être nécessaires pour gérer certaines rencontres plus avancées.
- Dans les deux derniers niveaux, les zombies remplacent les squelettes afin de representer la montee en puissance de la magie du Chaos de Tata Lisa.
- L’augmentation de la difficulté doit venir de nouvelles combinaisons et d’une pression plus importante, sans rendre les comportements imprévisibles.

## Rôle des environnements

Les ennemis doivent être placés en fonction des caractéristiques du niveau.

- Les ennemis volants interviennent dans les espaces offrant une bonne visibilité verticale.
- Les ennemis rapides au sol sont utilisés sur des surfaces suffisamment dégagées.
- Les archers sont placés de manière à laisser au joueur une possibilité de se protéger ou de se rapprocher.
- Les groupes d’ennemis ne doivent pas masquer les pièges ou rendre les plateformes illisibles.
- L’apparence des ennemis doit rester cohérente avec l’environnement traversé.

## Accessibilité

Les comportements sont conçus pour être compris par les enfants à partir de 7 ans.

- Les animations d’attaque sont expressives et faciles à reconnaître.
- Les ennemis utilisent des comportements répétables que le joueur peut mémoriser.
- La défaite des ennemis est représentée sans violence graphique.
- Les effets sonores complètent les indications visuelles importantes.
- Les premières rencontres permettent d’apprendre par l’observation et l’expérimentation.

## Séparation avec le GDD

Le Concept Game définit uniquement l’intention générale de l’intelligence artificielle.

Les éléments suivants seront précisés dans le GDD :

- distances de détection et de poursuite ;
- vitesses de déplacement ;
- durée des animations ;
- fréquence des attaques ;
- résistance et dégâts ;
- fonctionnement détaillé des projectiles ;
- réactions aux attaques d’Imran ;
- règles précises de combinaison des ennemis.
