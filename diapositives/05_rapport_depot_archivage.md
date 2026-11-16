---
marp: true
lang: fr
paginate: true
header: "LSG — Formation bio-informatique : du FASTQ au rapport"
footer: "INSP / CRPE — support pédagogique, non opposable"
---


# 5. Du résultat au rapport

Rédiger, valider, libérer, déposer, archiver

---

## Ce que contient un rapport

| Section | Contenu |
|---|---|
| Identification | identifiant de l'échantillon, du run, date, prescripteur |
| Méthode | plateforme, chimie, pipeline et sa version, bases et leurs versions |
| Résultats | ce qui a été détecté, aux seuils déclarés |
| Interprétation | ce que le résultat établit, dans les termes du domaine |
| Limites | ce que la méthode ne permet pas de conclure |
| Validation | qui a validé, quand |

La section « limites » n'est pas une précaution de style : c'est elle qui empêche le lecteur de
tirer du résultat une conclusion qu'il ne porte pas.

---

## Comment on formule

| On écrit | On n'écrit pas |
|---|---|
| « séquence du gène *bla*<sub>CTX-M</sub> détectée » | « souche résistante aux céphalosporines » |
| « co-localisation observée à moins de 5 kb » | « gène mobilisable » |
| « aucune co-localisation observée dans ces assemblages » | « gène chromosomique » |
| « non détecté au seuil de X » | « absent » |
| « lignage JN.1, base version 1.31, le 18/03/2026 » | « lignage JN.1 » |

Chaque colonne de droite est une affirmation que les données ne portent pas.

---

## Validation et libération

La validation technique porte sur la conformité du processus : critères de qualité satisfaits,
témoins conformes, versions consignées, cohérence entre les sorties.

**Un critère qualité non satisfait interdit la libération.** La décision de ne pas libérer se
trace, et le prescripteur est informé du délai et de son motif.

Une réserve orale ne laisse aucune trace et ne suit pas le rapport.

---

## Dépôt en base publique

1. **Retirer les lectures humaines, et contrôler** que le retrait a bien eu lieu.
2. Appliquer les règles de **minimisation** : date réduite si le cas est rare, granularité
   géographique maîtrisée.
3. Utiliser un **identifiant de soumission dédié**, jamais l'identifiant de laboratoire.
4. Vérifier le **format des accessions** : les accessions GenBank de série CP ne comportent pas
   de tiret bas, qui est propre à RefSeq.

Déposer des lectures non déplétées revient à publier des données génétiques humaines.

---

## Archivage et sauvegarde

- **3** copies, sur **2** supports de nature différente, dont **1** hors site.
- Un **test de restauration** à périodicité définie, avec vérification de l'empreinte du fichier
  restauré.

Un journal de sauvegarde atteste qu'une écriture s'est terminée, non que les données sont
relisibles. Une sauvegarde non restaurée est une sauvegarde non vérifiée.

---

## Rejouer dans deux ans

Trois questions, auxquelles le dossier doit répondre seul :

1. **Qui** a produit ce résultat, et était-il habilité ?
2. **Avec quelle version** du pipeline et de quelles bases ?
3. **Retrouve-t-on le même résultat**, et sinon, pourquoi ?

Si la troisième réponse diffère, ce n'est pas nécessairement une erreur — une base a pu changer.
Encore faut-il pouvoir le démontrer.

---

## Ce qu'on retient

- La section « limites » fait partie du résultat.
- La formulation engage : détecté, observé, non détecté au seuil — jamais absent, jamais résistant.
- Le dépôt public se prépare ; il ne s'improvise pas en fin de projet.
- Un résultat non rejouable n'est pas un résultat de laboratoire accrédité.
