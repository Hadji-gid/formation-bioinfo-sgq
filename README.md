# Formation — Section bio-informatique du système de management de la qualité

Support de formation interne du **Laboratoire de Surveillance Génomique des Pathogènes
Épidémiques** (LSG), Centre de Recherche pour les Pathogènes Émergents, Institut National de
Santé Publique, Bamako.

Cette formation répond à l'étape 4 de la procédure **RES-01** (gestion des compétences, de la
formation et des habilitations), qui impose, pour toute formation interne, un exposé, une mise en
situation supervisée et une évaluation des acquis. Les trois sont dans ce dépôt.

## À qui elle s'adresse

Tout agent appelé à réaliser un acte de la section bio-informatique : bio-informaticien,
biologiste assurant la validation, technicien exécutant le pipeline, étudiant ou stagiaire placé
sous supervision. Aucun prérequis en ligne de commande n'est exigé pour la première demi-journée.

## Ce qu'elle couvre

Les **douze actes** de la section, tels que définis par la fiche d'habilitation FM-06 :

| N° | Acte | Procédure | Niveau requis |
|----|------|-----------|---------------|
| A1 | Exécuter le pipeline d'analyse primaire sur une série complète | BIO-02 | N3 |
| A2 | Statuer sur la qualité d'un run et décider de la reprise ou du rejet | BIO-02 | N3 |
| A3 | Attribuer un lignage et un clade viral | BIO-05 | N3 |
| A4 | Mettre à jour les bases de référence et les versions d'outils | BIO-05 | N4 |
| A5 | Produire et interpréter une classification taxonomique métagénomique | BIO-03 | N3 |
| A6 | Rechercher les gènes de résistance et les facteurs de virulence | BIO-04 | N3 |
| A7 | Évaluer le potentiel de mobilisation des gènes de résistance | BIO-04 | N3 |
| A8 | Sauvegarder les données et exécuter une restauration de contrôle | BIO-01 | N3 |
| A9 | Retirer les lectures humaines et déposer en base publique | POST-05 | N3 |
| A10 | Tenir le dictionnaire de données et les registres | BIO-07 | N3 |
| A11 | Valider techniquement et libérer un rapport bio-informatique | POST-01/02 | N4 |
| A12 | Administrer le système d'information | RES-07 | N3 |

## Comment utiliser ce dépôt

| Dossier | Contenu | Pour qui |
|---|---|---|
| [`programme/`](programme/programme.md) | Objectifs, séquençage, fiche de séance | Animateur |
| [`diapositives/`](diapositives/01_sgq_et_section_bioinfo.md) | Cinq jeux de planches au format Marp | Animateur |
| [`manuel/`](manuel/manuel_participant.md) | Manuel remis aux participants | Participants |
| [`exercices/`](exercices/README.md) | Quatre mises en situation et leurs jeux de données | Participants |
| [`evaluation/`](evaluation/README.md) | Épreuve théorique et grille de correction | Évaluateur |
| [`emargement/`](emargement/feuille_emargement.md) | Feuille de présence à verser au registre REG-FORM-001 | Responsable Qualité |

## Construire les diapositives

Les planches sont écrites en Markdown, lisibles telles quelles sur GitHub et projetables sans
outil. Pour produire un PDF :

```bash
npm install -g @marp-team/marp-cli   # une seule fois
make slides                          # produit diapositives/*.pdf
```

## Articulation avec le système documentaire

Ce dépôt est un **support pédagogique**, non un document opposable. Il ne remplace aucune
procédure : en cas de divergence, la version en vigueur de la SOP fait foi. Toute correction de
fond passe par une demande de modification (formulaire FDM-001) sur le document source, puis par
une mise à jour de ce dépôt — voir [`CONTRIBUTING.md`](CONTRIBUTING.md).

Aucune donnée réelle de patient ne figure ici et aucune ne doit y être ajoutée : les jeux de
données d'exercice sont synthétiques (voir [`exercices/donnees/README.md`](exercices/donnees/README.md)).

## Licence

Contenu pédagogique sous licence Creative Commons Attribution 4.0 International (CC BY 4.0) —
voir [`LICENSE`](LICENSE). Réutilisation encouragée par les laboratoires de la sous-région, sous réserve de
citer la source et d'adapter les références documentaires à leur propre système qualité.
