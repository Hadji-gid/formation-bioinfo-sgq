---
marp: true
lang: fr
paginate: true
header: "LSG — Formation SGQ, section bio-informatique"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 5. Sauvegarde, accès et diffusion

---

## Une sauvegarde journalisée n'est pas une sauvegarde vérifiée

Le journal atteste qu'une **écriture** s'est terminée.

Il n'atteste pas que les données sont **relisibles**.

Seule une **restauration de contrôle**, avec vérification de l'empreinte du fichier restauré,
en apporte la preuve — et c'est le seul moment où l'on découvre une archive illisible *avant* d'en
avoir besoin.

---

## Règle 3-2-1

- **3** copies des données
- sur **2** supports de nature différente
- dont **1** hors site

Et un test de restauration à périodicité définie, consigné.

---

## Hébergement externe : ce n'est pas une commodité

Déposer sur un service de stockage en ligne un fichier contenant un élément identifiant constitue
un **transfert de données à caractère personnel** (loi n° 2013-015 du 21 mai 2013).

Hors du territoire national : niveau de protection adéquat **et** autorisation préalable de l'APDP.

Un compte gratuit n'offre aucune garantie sur le lieu d'hébergement, la rétention, ni les accès du
prestataire.

---

## Git : le code, jamais les données

Ne doivent **jamais** entrer dans un dépôt de code :

- données nominatives ou pseudonymisées, et la table de correspondance ;
- fichiers de séquences ;
- jetons, mots de passe, clés ;
- rapports nominatifs.

Un élément supprimé dans un commit ultérieur **reste dans l'historique**. Un dépôt accidentel
impose la **révocation du secret**, pas une suppression.

---

## Avant tout dépôt en base publique

1. Retirer les lectures humaines — et **contrôler** que le retrait a bien eu lieu.
2. Appliquer les règles de minimisation : date réduite si le cas est rare, granularité
   géographique maîtrisée.
3. Utiliser un **identifiant de soumission dédié** : jamais l'identifiant unique de laboratoire.

Déposer des lectures non déplétées revient à publier des données génétiques humaines.

---

## Ce qu'on retient

- Sauvegarde non restaurée = sauvegarde non vérifiée.
- Le cloud grand public n'est pas un support pour de la donnée identifiante.
- Git versionne le code ; les données vivent ailleurs.
- Le dépôt public se prépare, il ne s'improvise pas en fin de projet.
