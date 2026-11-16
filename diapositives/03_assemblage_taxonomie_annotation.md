---
marp: true
lang: fr
paginate: true
header: "LSG — Formation bio-informatique : du FASTQ au rapport"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 3. De la lecture au résultat

Assemblage, classification taxonomique, annotation

---

## La chaîne

Lectures nettoyées → **assemblage** (contigs) → **classification taxonomique** (qui est là, en
quelle proportion) → **annotation** (gènes de résistance, facteurs de virulence, réplicons
plasmidiques) → interprétation.

Chaque étape produit une sortie **et** un journal. Les deux se conservent : le journal est ce
qui permettra d'expliquer un résultat surprenant trois mois plus tard.

---

## Assemblage

**metaSPAdes** en mode métagénomique, longueurs de k-mers 21, 33, 55 et 77. Les assemblages
sont évalués sans référence (nombre de contigs, N50, longueur totale).

La **fragmentation** n'est pas un détail de qualité : elle détermine ce que l'on pourra
observer. Deux éléments réellement voisins sur le génome se retrouvent sur deux contigs
distincts dès que la couverture est faible ou inégale — et tout critère fondé sur leur
voisinage devient alors indisponible.

Un échantillon dont la profondeur microbienne est trop faible **ne s'assemble pas**. Il sort de
l'analyse, et sa sortie se consigne.

---

## Classification taxonomique

**Kraken2** attribue chaque lecture à un taxon par comparaison de k-mers ; **Bracken**
ré-estime ensuite les abondances au rang choisi.

| Point de vigilance | Conduite |
|---|---|
| Lectures non classées | en rapporter la proportion : elle qualifie la base, pas l'échantillon |
| Taxon à très faible abondance | sous le seuil fixé, il ne se rapporte pas |
| Taxon présent dans le témoin négatif | réputé contaminant de réactif |
| Abondance relative | compositionnelle : la hausse d'un taxon abaisse mécaniquement les autres |

---

## Annotation

| Outil | Objet | Critères |
|---|---|---|
| AMRFinderPlus | gènes de résistance | catalogue de référence NCBI, identité et couverture minimales |
| ABRicate / VFDB | facteurs de virulence | seuils d'identité et de couverture déclarés |
| ABRicate / PlasmidFinder | réplicons plasmidiques | idem |

Une annotation est une **correspondance de séquence** dans un catalogue, à des seuils déclarés.
Changer les seuils change le résultat : ils font partie de la méthode et se consignent.

---

## Les versions sont des paramètres

Un outil peut conserver son numéro de version pendant que sa base de données change chaque
semaine. Le numéro de version de l'outil ne décrit donc pas ce qui a tourné.

Règles de mise à jour :

1. **Jamais en cours de série** — les échantillons d'une même série doivent rester comparables.
2. Version, date et motif **consignés** dans REG-PIPE-001.
3. Un **jeu de contrôle rejoué** après mise à jour, et les résultats comparés avant / après,
   avec conclusion écrite.

Une mise à jour non rejouée est un changement non maîtrisé, même si elle améliore l'outil.

---

## Ce qui sort, et où cela va

| Sortie | Destination | Conservation |
|---|---|---|
| FASTQ nettoyés, déplétés | stockage de travail, puis archive | règle 3-2-1 |
| Contigs et métriques d'assemblage | dossier d'analyse | durée fixée par QMS-01 |
| Tables d'annotation | dossier d'analyse et registre | durée fixée par QMS-01 |
| Journaux d'exécution | dossier d'analyse | aussi longtemps que le résultat |

---

## Ce qu'on retient

- La fragmentation de l'assemblage conditionne ce qu'on pourra observer ensuite.
- Une classification dépend de sa base ; une annotation dépend de ses seuils.
- Les versions d'outils et de bases sont des paramètres de méthode, pas des détails techniques.
- Le journal se conserve aussi longtemps que le résultat qu'il explique.
