---
marp: true
lang: fr
paginate: true
header: "LSG — Formation bio-informatique : du FASTQ au rapport"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 2. Contrôle qualité des lectures

Décider si les données méritent d'être analysées

---

## Les métriques qui décident

| Métrique | Ce qu'elle mesure | Effet d'une valeur basse |
|---|---|---|
| %Q30 | proportion de bases à moins d'une erreur sur mille | faux variants, assemblage bruité |
| Paires de lectures | profondeur disponible | assemblage fragmenté, taxons manqués |
| Taux d'adaptateur | résidus de la préparation | mésappariements en extrémité |
| Duplicats | redondance de PCR | abondance surestimée |
| Lectures humaines | part de l'hôte | profondeur microbienne effective réduite |

---

## Le nettoyage, et ses limites

**fastp** retire les adaptateurs, élague les extrémités de mauvaise qualité et écarte les
lectures trop courtes. Paramètres employés : longueur minimale 50 pb, qualité Phred 20,
détection automatique des adaptateurs en mode apparié.

Ce qu'il **ne fait pas** : il ne rattrape pas une profondeur insuffisante, ne corrige pas une
erreur de préparation de banque, et ne compense pas un échantillon dégradé. Un nettoyage qui
retire la moitié des lectures signale un problème en amont — il ne le résout pas.

---

## Déplétion des lectures humaines

Alignement sur l'assemblage de référence humain, puis retrait des paires dont les deux lectures
s'alignent.

- **Raison scientifique** : la fraction humaine mobilise la profondeur sans informer.
- **Raison réglementaire** : une lecture humaine déposée en base publique est une donnée
  génétique identifiante.

Le retrait se **contrôle** et se consigne : la proportion retirée est une métrique du run, pas
un détail d'exécution.

---

## Deux niveaux de critères, deux décisions

| | Échec de **run** | Échec d'**échantillon** |
|---|---|---|
| Cause | commune à la série | propre à un tube |
| Indices | densité de clusters, %Q30 global, témoin de run | couverture médiane, lectures assignées, témoin interne |
| Suite | reprise de séquençage | reprise d'extraction ou nouveau prélèvement |

Un %Q30 global conforme ne rattrape pas un échantillon sous le seuil de couverture.

---

## Le piège du seuil abaissé

Abaisser un seuil pour faire passer un échantillon n'est pas une décision technique : c'est une
**modification de méthode sans validation**.

Le délai se négocie avec le prescripteur. Le critère qualité ne se négocie pas.

Si un seuil paraît systématiquement trop strict, la voie est une demande de modification du
document qui le fixe — pas un ajustement au cas par cas.

---

## Les témoins se lisent en premier

- **Témoin négatif d'extraction** — un taxon qui y figure est réputé apporté par les réactifs ou
  l'environnement, jusqu'à preuve du contraire.
- **Témoin positif de run** — sa non-conformité invalide la série, quels que soient les
  échantillons.
- **Témoin interne d'extraction** — non détecté, il signale une inhibition : l'échantillon est
  invalidé, même si ses autres métriques sont bonnes.

Sans témoin interne, une inhibition produit un résultat négatif indiscernable d'un vrai négatif.

---

## Ce qu'on retient

- Le nettoyage améliore des données exploitables ; il ne sauve pas des données insuffisantes.
- La déplétion humaine est une obligation réglementaire autant qu'une mesure d'efficacité.
- Run et échantillon : deux jeux de critères, deux décisions, deux suites.
- Les témoins se lisent avant les échantillons.
