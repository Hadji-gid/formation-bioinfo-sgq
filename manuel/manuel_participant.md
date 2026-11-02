# Manuel du participant

*Support pédagogique — ne remplace aucune procédure. En cas de divergence, la version en vigueur
de la SOP fait foi.*

## 1. À quoi sert ce manuel

À retrouver, après la séance, les règles qui engagent un résultat. Il est organisé par **acte** :
pour chacun, ce que l'acte produit, les deux ou trois règles qui le gouvernent, et l'erreur
caractéristique à ne pas commettre.

Les erreurs décrites ne sont pas théoriques : chacune correspond à une défaillance observée ou
plausible dans un laboratoire de surveillance génomique, et c'est sur elles que porte l'évaluation.

## 2. Les douze actes


### A1 — Exécuter le pipeline d'analyse primaire

*BIO-02 — niveau N3*

Ce que l'acte produit : des lectures nettoyées, un alignement, un jeu de variants ou un assemblage,
et un journal d'exécution.

Règles : l'exécution se fait sur une version déclarée du pipeline ; le journal est conservé ; une
étape en échec est identifiée avant toute relance, et non relancée à l'aveugle.

Erreur caractéristique : relancer jusqu'à ce que ça passe. Si une étape échoue deux fois pour la
même raison, la cause est dans les données ou dans la configuration, pas dans la malchance.

### A2 — Statuer sur la qualité d'un run

*BIO-02 — niveau N3*

Règles : les critères de run et les critères d'échantillon sont indépendants et s'appliquent tous
les deux ; un seuil ne s'abaisse pas pour faire passer un échantillon.

Erreur caractéristique : valider seize échantillons parce que le %Q30 global est conforme, alors
que trois d'entre eux sont sous le seuil de couverture.

Pour distinguer un échec de run d'un échec d'échantillon : si les indicateurs globaux sont
conformes et qu'un seul tube s'écarte, l'échec est au tube — la suite est une reprise
d'extraction, pas une reprise de séquençage.

### A3 — Attribuer un lignage et un clade

*BIO-05 — niveau N3*

Règles : la version de la base de lignages est vérifiée avant attribution et **consignée avec le
résultat** ; une réattribution après mise à jour est un comportement attendu, pas une anomalie.

Erreur caractéristique : rapporter un lignage sans sa version, puis ne pas pouvoir expliquer, trois
mois plus tard, pourquoi la même séquence est classée autrement.

### A4 — Mettre à jour les bases de référence et les outils

*BIO-05 — niveau N4*

Règles : jamais en cours de série ; version, date et motif consignés ; un jeu de contrôle est
rejoué après mise à jour et les résultats comparés avant / après, avec conclusion écrite.

Erreur caractéristique : mettre à jour parce qu'une nouvelle version est parue. Une mise à jour
non rejouée est un changement non maîtrisé, même si elle améliore l'outil.

Point d'attention propre à la surveillance virale : certains outils conservent leur numéro de
version pendant que leur base de données change chaque semaine. Le numéro de version de l'outil ne
suffit donc pas à décrire ce qui a tourné.

### A5 — Classification taxonomique métagénomique

*BIO-03 (à rédiger) — niveau N3*

Règles : le témoin négatif se lit **avant** les échantillons ; un taxon présent dans le témoin est
réputé apporté par les réactifs ou l'environnement ; aucun taxon n'est rapporté sous le seuil
d'abondance fixé.

Erreur caractéristique : rapporter comme positifs six échantillons porteurs, à faible abondance,
d'un taxon également présent dans le témoin négatif.

### A6 — Gènes de résistance et facteurs de virulence

*BIO-04 (à rédiger) — niveau N3*

Règles : on rapporte une **détection de séquence**, pas un phénotype. L'organisme porteur n'est pas
établi par la seule détection dans un métagénome.

Erreur caractéristique : écrire « souche résistante aux céphalosporines de troisième génération »
à partir de la détection de *bla*<sub>CTX-M</sub>.

### A7 — Potentiel de mobilisation

*BIO-04 (à rédiger) — niveau N3*

Règles : la co-localisation d'un gène et d'un réplicon sur un même contig est un **indice** de
mobilisation, pondéré par la distance. Son absence ne conclut rien.

Erreur caractéristique : conclure au portage chromosomique faute de co-localisation. Un gène et un
réplicon voisins se retrouvent sur deux contigs distincts dès que l'assemblage est fragmenté — ce
qui est la règle quand le matériel bactérien est hors cible de capture.

### A8 — Sauvegarde et restauration

*BIO-01 — niveau N3*

Règles : 3 copies, 2 supports de nature différente, 1 hors site ; test de restauration à
périodicité définie, avec vérification de l'empreinte du fichier restauré.

Erreur caractéristique : considérer six mois de journaux « réussis » comme une preuve. Le journal
atteste une écriture, pas une relecture.

### A9 — Dépôt en base publique

*POST-05, BIO-06 (à rédiger) — niveau N3*

Règles : retrait des lectures humaines **et contrôle** de ce retrait ; règles de minimisation
appliquées ; identifiant de soumission dédié, distinct de l'identifiant de laboratoire.

Erreur caractéristique : réutiliser l'identifiant interne comme identifiant public, créant une clé
de rapprochement durable entre une donnée publiée et un dossier nominatif.

### A10 — Dictionnaire de données et registres

*BIO-07 — niveau N3*

Règles : vocabulaires contrôlés ; champ source unique ; NR / NA / ND au lieu du tiret ; dates en
AAAA-MM-JJ ; unité dans l'intitulé de colonne, jamais dans la valeur.

Erreur caractéristique : corriger la copie au lieu de la source. L'écart réapparaîtra.

### A11 — Validation et libération d'un rapport

*POST-01, POST-02 — niveau N4*

Règles : un critère qualité non satisfait interdit la libération ; la décision de ne pas libérer
se trace ; une réserve orale n'est pas une trace.

Erreur caractéristique : libérer sous pression de délai en prévenant verbalement le prescripteur.

### A12 — Administration du système d'information

*RES-07 — niveau N3*

Règles : moindre privilège ; révocation le jour du départ ; aucune validation de résultat par
l'administrateur ; secrets hors des dépôts de code et des registres.

Erreur caractéristique : laisser actif le compte d'un agent parti, parce que personne n'a signalé
le départ au responsable du système d'information.

## 3. Mémento des seuils et formats

| Objet | Règle |
|---|---|
| Date | AAAA-MM-JJ (ISO 8601) |
| Booléen | OUI / NON seuls ; tout commentaire en colonne dédiée |
| Valeur manquante | NR (non renseigné), NA (non applicable), ND (non détecté) |
| Décimale | point décimal |
| Unité | dans l'intitulé de colonne |
| Version | nombre nu, sans préfixe « v » |
| Accession GenBank | sans tiret bas (CP123456) — le tiret bas est propre à RefSeq (NZ_CP…) |

## 4. Où trouver quoi

| Besoin | Document |
|---|---|
| Que dois-je être capable de faire ? | FM-06, annexe 1 |
| Quels critères pour accepter un run ? | BIO-02 |
| Comment nommer un champ, quelle valeur admise ? | BIO-07, annexes 1 et 2 |
| Combien de temps garder quoi ? | QMS-01, annexe 2 |
| Que faire d'une anomalie ? | QMS-02 |
| Puis-je déposer ce fichier là ? | RES-07, tableau des supports autorisés |
