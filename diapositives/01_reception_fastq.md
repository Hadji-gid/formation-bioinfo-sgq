---
marp: true
lang: fr
paginate: true
header: "LSG — Formation bio-informatique : du FASTQ au rapport"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 1. Réception des données de séquençage

Ce qui arrive au bio-informaticien, et ce qu'il vérifie avant de lancer quoi que ce soit

---

## Ce que livre le séquenceur

| Élément | Forme | Qui le produit |
|---|---|---|
| Lectures brutes | deux FASTQ par échantillon (R1, R2) | séquenceur, après démultiplexage |
| Feuille d'échantillons | fichier de correspondance index ↔ échantillon | paillasse, avant le run |
| Métriques de run | densité de clusters, %Q30 global, taux d'identification | séquenceur |
| Métadonnées cliniques | date, type de prélèvement, prescripteur | registre de réception |

La chaîne bio-informatique ne commence pas au premier outil : elle commence à la réception, et
une erreur d'appariement entre un index et un échantillon y est invisible en aval.

---

## Quatre vérifications avant toute analyse

1. **Intégrité** — l'empreinte de chaque fichier correspond à celle annoncée. Un FASTQ tronqué
   par un transfert interrompu s'analyse sans erreur et produit un résultat faux.
2. **Complétude** — autant de paires de fichiers que d'échantillons attendus, R1 et R2 présents.
3. **Nomenclature** — chaque fichier porte l'identifiant unique de laboratoire, pas un nom libre.
4. **Correspondance** — la feuille d'échantillons et les fichiers livrés désignent les mêmes
   échantillons, ni plus ni moins.

Les écarts se traitent avant de lancer l'analyse, jamais après.

---

## L'identifiant unique de laboratoire

Il relie l'échantillon, la série d'extraction, la plaque de banques, le run, le rapport et le
dépôt. C'est la clé de jointure de tout le système.

- **Un seul registre en est la source** ; partout ailleurs il est copié par jointure.
- Il ne contient **aucune donnée identifiante** : ni nom, ni date de naissance.
- Il n'est **jamais** réutilisé comme identifiant de soumission en base publique.

Un identifiant reconstitué à la main dans un tableur est la première cause de résultat attribué
au mauvais patient.

---

## Ce qu'on consigne avant de lancer

| Information | Où | Pourquoi |
|---|---|---|
| Identifiant du run et date | registre des runs | rattacher tout résultat à sa série |
| Version du pipeline | REG-PIPE-001 | rejouer l'analyse à l'identique |
| Versions des bases de référence | REG-PIPE-001 | une base change, un résultat change |
| Opérateur | registre | savoir qui a produit, et s'il était habilité |
| Empreintes des fichiers | REG-DB-001 | détecter une altération ultérieure |

---

## Qui peut lancer l'analyse

L'exécution du pipeline sur une série complète est un **acte habilité** : elle suppose le
niveau N3, c'est-à-dire la capacité à reconnaître une situation anormale et à s'arrêter.

Un agent non habilité peut l'exécuter **sous supervision**, ses productions étant relues et
contresignées. L'absence d'habilitation n'interdit pas de travailler ; elle interdit de
travailler seul.

---

## Ce qu'on retient

- L'analyse commence à la réception, pas au premier outil.
- Intégrité, complétude, nomenclature, correspondance : quatre contrôles, avant tout calcul.
- L'identifiant unique est la clé de jointure de toute la chaîne — une seule source.
- Ce qui n'est pas consigné avant le lancement ne pourra pas être reconstitué après.
