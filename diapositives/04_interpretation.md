---
marp: true
lang: fr
paginate: true
header: "LSG — Formation bio-informatique : du FASTQ au rapport"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 4. Interpréter

Ce qu'un résultat établit, et ce qu'il n'établit pas

---

## Détecter un gène n'est pas établir une résistance

Détecter *bla*<sub>CTX-M</sub> dans un métagénome établit que **la séquence est présente dans
l'échantillon**.

Cela n'établit pas :

- qu'elle est **exprimée** ;
- **quel organisme** la porte ;
- que l'isolat en cause est **résistant** en clinique.

Entre la présence d'un gène et la résistance d'une souche, il y a l'expression, le contexte
génétique et l'identité du porteur. Un rapport qui franchit cet écart expose à une décision
thérapeutique erronée.

---

## Co-localisation n'est pas mobilité

Un gène de résistance et un réplicon plasmidique sur un même contig, à faible distance,
constituent un **indice** de mobilisation — pondéré par cette distance.

Leur absence sur un même contig **ne conclut rien** : un gène et un réplicon réellement voisins
se retrouvent sur deux contigs distincts dès que l'assemblage est fragmenté.

> L'absence de preuve de mobilisation n'est pas une preuve d'absence de mobilisation.

C'est l'erreur d'interprétation la plus coûteuse de la chaîne, parce qu'elle produit une
conclusion rassurante et fausse.

---

## Portage et mobilisation : deux dimensions

| | Portage | Mobilisation |
|---|---|---|
| Ce qu'on mesure | présence et diversité des gènes | voisinage avec un élément mobile |
| Ce qui le limite | profondeur, catalogue | fragmentation de l'assemblage |
| Risque si confondus | surestimer le risque de transmission | conclure à tort à un portage fixe |

Rapporter le seul décompte des gènes surestime le risque de transmission.

---

## Abondance relative

Une abondance issue de données de séquençage est **compositionnelle** : elle est exprimée en
part du total. La hausse d'un taxon abaisse mécaniquement la part de tous les autres, sans
qu'aucun n'ait diminué en valeur absolue.

Conséquences pratiques : on ne compare pas deux échantillons de profondeurs très différentes
sans précaution, et on ne conclut pas à une « diminution » d'un taxon sur la seule baisse de sa
part.

---

## Lignage viral et version de base

Une séquence classée dans un lignage il y a trois mois peut en recevoir un autre aujourd'hui.
Ce n'est ni une erreur d'assemblage, ni un défaut de l'outil : la nomenclature évolue par ajout
et par scission.

**Un lignage se rapporte avec la version de la base et la date d'attribution.** Sans cela, le
résultat n'est pas interprétable un an plus tard.

---

## Les faux positifs ont des causes connues

| Observation | Cause probable | Vérification |
|---|---|---|
| Taxon partagé avec le témoin négatif | contaminant de réactif | comparer au témoin |
| Taxon attendu dans un autre échantillon du run | report d'index | examiner la plaque |
| Gène détecté sur un contig très court | correspondance fortuite | longueur et couverture du contig |
| Espèce proche d'une espèce dominante | limite de la classification | rang taxonomique supérieur |

---

## Ce qu'on retient

- Gène détecté ≠ phénotype résistant.
- Pas de co-localisation ≠ gène non mobilisable.
- Une abondance relative ne se lit pas comme une quantité.
- Un lignage sans sa version de base n'est pas un résultat traçable.
