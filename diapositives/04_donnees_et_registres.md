---
marp: true
lang: fr
paginate: true
header: "LSG — Formation SGQ, section bio-informatique"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 4. Données, vocabulaires et registres

---

## Trois niveaux de standardisation (SOP BIO-07)

| Niveau | Question | Exemple de défaut |
|---|---|---|
| **Structure** | Où est rangée la donnée, comment la relier ? | Deux tables dans une feuille |
| **Vocabulaire** | Que signifie la valeur ? | « Validé » ici, « Clôturé » là |
| **Format** | Sous quelle forme est-elle écrite ? | Dates tantôt texte, tantôt date Excel |

Il suffit qu'un seul manque pour que le jeu soit inexploitable.

---

## La règle du champ source unique

Chaque donnée possède **un seul** registre source.

Partout ailleurs, c'est une copie obtenue **par jointure**, jamais par ressaisie.

Deux registres portant la même donnée sans que l'un soit désigné comme source divergeront. C'est
une question de délai, non de probabilité.

---

## Trois règles de tenue des tableaux

1. **Une variable, une colonne** — si l'intitulé contient « et » ou « / », il y a deux colonnes.
2. **Une observation, une ligne** — jamais deux, jamais une moitié.
3. **Une valeur, une cellule** — sans commentaire accolé, sans unité collée au nombre.

---

## La valeur manquante explicite

Le tiret « - » ne dit pas laquelle des trois situations on désigne :

| | |
|---|---|
| **NR** | non renseigné — on aurait dû, on ne l'a pas fait |
| **NA** | non applicable — la question ne se pose pas ici |
| **ND** | non détecté — on a cherché, on n'a pas trouvé |

Trois situations, trois conduites différentes. Un seul tiret les confond.

---

## Une fiche n'est pas un registre

| | Fiche | Registre |
|---|---|---|
| Forme | mise en page de formulaire | tableau |
| Porte | la preuve, la signature | la donnée analysable |
| Volume | une par instance | une **ligne** par instance |

Recopier la mise en page d'une fiche dans un onglet de classeur ne produit ni l'une ni l'autre.

---

## Ce qu'on retient

- Structure, vocabulaire, format : les trois, ou rien.
- Une donnée, une source ; ailleurs, une jointure.
- NR, NA, ND — jamais « - ».
- La fiche prouve, le registre compte.
