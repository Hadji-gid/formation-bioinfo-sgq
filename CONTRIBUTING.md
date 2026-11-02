# Proposer une modification

## Règle de préséance

Ce dépôt est un support pédagogique. **Il ne crée aucune exigence.** Si une planche ou une page du
manuel contredit une procédure en vigueur, c'est la procédure qui s'applique, et la divergence est
signalée comme une anomalie du support.

## Deux cas à distinguer

**1. Le support est faux ou obsolète, la procédure est juste.**
Ouvrir une issue, ou proposer directement une modification. La correction est relue par le
responsable de la section bio-informatique. Aucun formulaire qualité n'est requis.

**2. La procédure elle-même doit changer.**
Le dépôt n'est pas le lieu de cette discussion. Remplir une demande de modification de document
(formulaire **FDM-001**) et suivre la procédure de maîtrise des documents **PM1-SM-01**. Le support
n'est mis à jour qu'**après** entrée en vigueur de la nouvelle version du document.

## Ce qui ne doit jamais entrer dans ce dépôt

- Donnée nominative ou pseudonymisée, et toute table de correspondance identifiant / identité
- Fichier de séquences, même déplété
- Jeton d'accès, mot de passe, clé, chaîne de connexion
- Rapport d'analyse réel, même anonymisé en apparence

Un élément supprimé dans un commit ultérieur **reste accessible dans l'historique** : un dépôt
accidentel impose la révocation du secret concerné, et non une simple suppression.

## Convention de commit

Un commit, un objet. Messages en français, à l'impératif, préfixés par le dossier concerné :

```
diapositives: corriger le seuil de couverture de la planche 12
manuel: ajouter le cas du témoin négatif contaminé
exercices: nouveau jeu de données pour l'exercice 2
```

## Avant de proposer

- Les diapositives se construisent sans erreur (`make slides`)
- Aucun chiffre n'est modifié sans référence à la procédure qui le fixe
- Les renvois aux SOP mentionnent le code et, si possible, le paragraphe
