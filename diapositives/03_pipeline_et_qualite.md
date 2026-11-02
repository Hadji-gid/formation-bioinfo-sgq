---
marp: true
lang: fr
paginate: true
header: "LSG — Formation SGQ, section bio-informatique"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 3. Qualité d'un run, et ce qu'un résultat établit

---

## Critères de run et critères d'échantillon sont indépendants

Un %Q30 global conforme **ne rattrape pas** un échantillon dont la couverture médiane est
insuffisante.

Un run peut être bon et trois échantillons mauvais. Un run peut être mauvais et tous les
échantillons individuellement passables.

---

## Comment les distinguer

| | Échec de **run** | Échec d'**échantillon** |
|---|---|---|
| Cause | commune à la série | propre à un tube |
| Indices | densité de clusters, %Q30 global, témoin de run | couverture médiane, lectures assignées, témoin interne |
| Suite | reprise de séquençage | reprise d'extraction ou nouveau prélèvement |

---

## Le piège du seuil abaissé

Abaisser un seuil pour faire passer un échantillon n'est pas une décision technique.

C'est **une modification de méthode sans validation**.

Le délai se négocie. Le critère qualité ne se négocie pas.

---

## Ce qu'une détection de gène établit

Détecter *bla*<sub>CTX-M</sub> dans un métagénome établit que **la séquence du gène est présente
dans l'échantillon**.

Cela n'établit pas :

- qu'il est **exprimé** ;
- **quel organisme** le porte ;
- que l'isolat en cause est **résistant** en clinique.

Un rapport qui franchit cet écart expose à une décision thérapeutique erronée.

---

## Ce qu'une absence de co-localisation établit

Aucun gène de résistance co-localisé avec un réplicon plasmidique sur un même contig ?

**On ne peut rien conclure sur la localisation.**

Un gène et un réplicon réellement voisins se retrouvent sur deux contigs distincts dès que
l'assemblage est fragmenté — ce qui est la règle quand le matériel bactérien est hors cible de
capture.

L'absence de preuve de mobilisation n'est pas une preuve d'absence de mobilisation.

---

## Le lignage dépend de la version de la base

Une séquence classée BA.2.86.1 il y a trois mois peut recevoir une autre attribution aujourd'hui.

Ce n'est ni une erreur d'assemblage, ni un défaut de l'outil : la nomenclature évolue par ajout et
par scission.

**Conséquence : on rapporte le lignage avec la version de la base et la date d'attribution.**

---

## Ce qu'on retient

- Run et échantillon : deux niveaux de critères, deux décisions.
- Gène détecté ≠ phénotype résistant.
- Pas de co-localisation ≠ gène chromosomique.
- Un lignage sans sa version de base n'est pas un résultat traçable.
