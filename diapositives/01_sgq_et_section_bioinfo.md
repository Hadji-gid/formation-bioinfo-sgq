---
marp: true
lang: fr
paginate: true
header: "LSG — Formation SGQ, section bio-informatique"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 1. Le système qualité vu de la section bio-informatique

Pourquoi une procédure, quand le code est déjà versionné ?

---

## Ce qu'une procédure ajoute à un script

Un script dit **comment** une opération est faite.
Une procédure dit **qui** peut la faire, **dans quelles conditions**, **avec quelles preuves**, et
**ce qu'on fait quand elle échoue**.

Un pipeline reproductible exécuté par une personne non habilitée, sur une base de référence non
tracée, et dont l'échec n'est signalé à personne, produit un résultat reproductible et inutilisable.

---

## Trois questions auxquelles la section doit savoir répondre

1. **Qui a produit ce résultat, et était-il habilité à le faire ?**
2. **Avec quelle version du pipeline et de quelle base de référence ?**
3. **Si on refait l'analyse dans six mois, retrouve-t-on le même résultat — et sinon, pourquoi ?**

Aucune des trois n'est une question technique. Les trois se perdent si rien n'est consigné.

---

## Les procédures qui vous concernent

| Code | Objet |
|---|---|
| BIO-01 | Sauvegarde et restauration des données de séquençage |
| BIO-02 | Pipeline d'analyse et critères de qualité |
| BIO-05 | Bases de référence et versions d'outils |
| BIO-07 | Dictionnaire de données, vocabulaires, registres |
| POST-01 / POST-02 | Validation et rapport |
| POST-05 | Confidentialité et diffusion |
| RES-07 | Système d'information : accès, intégrité, hébergement |

---

## Ce que le référentiel exige

L'ISO 15189:2022 ne prescrit aucun outil bio-informatique. Elle exige que le laboratoire
démontre :

- que les personnes sont **compétentes** et autorisées (§ 6.2) ;
- que les systèmes informatiques sont **maîtrisés** (§ 7.6) ;
- que les résultats sont **traçables** jusqu'à leurs données sources.

Le choix de Kraken2 ou d'un autre classificateur vous appartient. La traçabilité de ce choix, non.

---

## Ce qu'on retient

- La procédure ne duplique pas le code : elle couvre ce que le code ne dit pas.
- Trois questions : qui, avec quelle version, et est-ce rejouable.
- Ce qui n'est pas consigné n'a pas eu lieu — du point de vue de l'audit comme de celui du
  collègue qui reprendra le dossier.
