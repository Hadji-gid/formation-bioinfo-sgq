# Programme de la formation

## Objet

Rendre chaque agent de la section bio-informatique capable d'exécuter de manière autonome les
actes relevant de son périmètre, et de **reconnaître les situations où il doit s'arrêter et
alerter**. Ce second objectif est le plus important : une erreur technique se rattrape, une
décision prise hors compétence se retrouve dans un rapport rendu.

## Objectifs pédagogiques

À l'issue de la formation, le participant est en mesure de :

1. conduire une série depuis la réception des FASTQ jusqu'au rapport, en nommant à chaque étape
   la procédure qui la régit ;
2. statuer sur la qualité d'un run et distinguer un échec de run d'un échec d'échantillon ;
3. énoncer ce qu'une détection de gène de résistance établit et ce qu'elle n'établit pas ;
4. expliquer pourquoi l'absence de co-localisation entre un gène et un élément mobile ne démontre
   pas un portage chromosomique ;
5. appliquer les vocabulaires contrôlés et la règle du champ source unique lors d'une saisie ;
6. conduire une restauration de contrôle et en consigner le résultat ;
7. préparer un dépôt en base publique conforme aux règles de minimisation ;
8. rédiger un résultat dans des termes que les données portent effectivement.

## Public et prérequis

Agents de la section bio-informatique et biologistes assurant la validation. Aucun prérequis pour
la première demi-journée. La seconde suppose un accès au serveur de calcul et la lecture préalable
des procédures BIO-02 et BIO-07.

## Durée et séquençage

Deux demi-journées, séparées d'au moins une semaine pour laisser le temps de la lecture et d'une
première mise en pratique encadrée.

### Module 0 — préalable (3 h 30, séance séparée)

| Durée | Séquence | Support |
|-------|----------|---------|
| 60 min | Flux de travail en bio-informatique : concepts, structure, outils, formats de fichiers | [`00_workflow_bioinformatique.pptx`](../diapositives/00_workflow_bioinformatique.pptx) |
| 60 min | Mise en place de l'environnement : WSL et Ubuntu, Conda, outils bioconda, gel de l'environnement | planches 9 à 12 du même module |
| 90 min | Linux, ligne de commande et scripts : se repérer, filtrer, tubes et redirections, écrire un script robuste, travaux longs | [`00b_linux_ligne_de_commande.pptx`](../diapositives/00b_linux_ligne_de_commande.pptx) |

Ce module est un préalable pour les agents qui n'ont jamais travaillé en ligne de commande. Il
peut être sauté par ceux qui exploitent déjà le pipeline, et se tient de préférence devant un
poste, chacun installant son environnement au fil des planches.

### Première demi-journée — des FASTQ aux résultats bruts (3 h 30)

| Durée | Séquence | Support |
|-------|----------|---------|
| 20 min | Accueil, objectifs, tour de table des pratiques actuelles | — |
| 35 min | Réception des données : intégrité, complétude, nomenclature, identifiant unique | [`01_reception_fastq.md`](../diapositives/01_reception_fastq.md) |
| 45 min | Contrôle qualité des lectures, déplétion humaine, critères de run et d'échantillon | [`02_controle_qualite.md`](../diapositives/02_controle_qualite.md) |
| 15 min | Pause | — |
| 50 min | Assemblage, classification taxonomique, annotation, versions de bases | [`03_assemblage_taxonomie_annotation.md`](../diapositives/03_assemblage_taxonomie_annotation.md) |
| 45 min | **Exercice 1** — statuer sur un run (jeu de données fourni) | [`exercice1_qualite_run.md`](../exercices/exercice1_qualite_run.md) |

### Seconde demi-journée — interpréter, rapporter, diffuser (3 h 30)

| Durée | Séquence | Support |
|-------|----------|---------|
| 15 min | Retour sur l'exercice 1 et sur les questions restées ouvertes | — |
| 55 min | Interpréter : gène et phénotype, co-localisation et mobilité, abondance relative, lignage | [`04_interpretation.md`](../diapositives/04_interpretation.md) |
| 15 min | Pause | — |
| 50 min | Rapport, validation, libération, dépôt public, archivage et rejouabilité | [`05_rapport_depot_archivage.md`](../diapositives/05_rapport_depot_archivage.md) |
| 45 min | **Exercices 2 à 4** selon les actes visés | [`exercices/`](../exercices/README.md) |
| 20 min | **Épreuve théorique** (45 min si passée à part) | [`epreuve_theorique.md`](../evaluation/epreuve_theorique.md) |


## Modalités d'évaluation

Conformément à la SOP RES-01, l'évaluation des acquis comporte deux volets, et **aucun des deux ne
suffit seul** :

- une **épreuve théorique** de 20 questions (26 points, seuil 21, cinq questions éliminatoires) ;
- une **mise en situation supervisée**, observée par le formateur et consignée comme preuve
  matérielle sur la fiche FM-06.

La formation est enregistrée dans **REG-FORM-001** et la feuille d'émargement est versée au
dossier. La réussite de l'épreuve ne vaut pas habilitation : l'habilitation est prononcée par le
responsable de secteur sur la fiche FM-06, acte par acte.

## Ce que la formation ne couvre pas

Les gestes de paillasse, la biosécurité et la métrologie, qui relèvent d'autres secteurs et
d'autres formations. Les procédures BIO-03, BIO-04 et BIO-06 n'étant pas encore en vigueur, les
séquences qui s'y rapportent exposent le mode opératoire effectivement appliqué et le signalent
comme tel.
