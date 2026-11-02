# Épreuve théorique — section bio-informatique

**14 questions à choix unique (1 point) et 6 questions à réponse courte (2 points) — 26 points — 45 minutes.**

Seuil de réussite : **21/26**, et aucune erreur sur les questions signalées ÉLIMINATOIRE (3, 6, 7, 8, 9).

Les procédures du laboratoire sont autorisées. L'accès à Internet et l'aide d'un tiers ne le sont pas.

> L'épreuve théorique ne suffit pas à prononcer une habilitation : elle complète une preuve matérielle recueillie au titre de la fiche FM-06.

## Première partie — questions à choix unique

**1.** Un adaptateur de séquençage n'a pas été retiré avant alignement. Quel en est l'effet sur l'appel de variants ?  `A1`

- [ ] a) Aucun : l'aligneur écarte les séquences d'adaptateur.
- [ ] b) Une perte de profondeur, sans effet sur les variants.
- [ ] c) Des mésappariements en extrémité de lecture, susceptibles de produire de faux variants.
- [ ] d) Une erreur d'exécution du pipeline.

**2.** Un run présente un %Q30 global conforme, mais trois échantillons sur seize ont une couverture médiane sous le seuil. Quelle décision ?  `A2`

- [ ] a) Valider le run et rejeter les trois échantillons concernés.
- [ ] b) Rejeter le run entier.
- [ ] c) Valider les seize échantillons, le critère global étant satisfait.
- [ ] d) Relancer l'analyse de ces trois échantillons avec un seuil abaissé.

**3.** Une séquence classée BA.2.86.1 il y a trois mois reçoit une attribution différente après mise à jour de la base de lignages. Quelle conclusion ?  *(ÉLIMINATOIRE)*  `A3`

- [ ] a) L'assemblage de cette séquence était défectueux.
- [ ] b) L'outil de classification présente une anomalie à signaler à l'éditeur.
- [ ] c) La nouvelle attribution invalide rétroactivement l'analyse initiale.
- [ ] d) L'attribution dépend de la version de la base : le lignage se rapporte avec la version utilisée et la date d'attribution.

**4.** À quel moment une base de référence ou une version d'outil peut-elle être actualisée ?  `A4`

- [ ] a) Dès sa publication, pour disposer de la version la plus récente.
- [ ] b) Hors série en cours, avec rejeu d'un jeu de contrôle et comparaison avant/après.
- [ ] c) À chaque run, pour garantir l'homogénéité.
- [ ] d) Une fois par an, à date fixe.

**5.** Un témoin négatif d'extraction fait apparaître un taxon également détecté, à faible abondance, dans six échantillons. Quelle interprétation ?  `A5`

- [ ] a) Contamination probable de réactif : le taxon est écarté de ces échantillons ou rapporté avec réserve explicite.
- [ ] b) Les six échantillons sont positifs pour ce taxon.
- [ ] c) Le témoin a été contaminé par les échantillons, sans incidence sur les résultats.
- [ ] d) Le seuil d'abondance doit être abaissé pour mieux détecter ce taxon.

**6.** La détection du gène blaCTX-M dans un échantillon permet-elle de conclure à une résistance aux céphalosporines de troisième génération ?  *(ÉLIMINATOIRE)*  `A6`

- [ ] a) Oui, il s'agit d'un déterminant de résistance acquise.
- [ ] b) Oui, si la couverture du gène dépasse 90 %.
- [ ] c) Non : la détection du gène ne préjuge ni de son expression, ni de l'espèce qui le porte, ni du phénotype de l'isolat en cause.
- [ ] d) Oui, à condition que l'identité nucléotidique dépasse 98 %.

**7.** Dans un échantillon, aucun gène de résistance n'est co-localisé avec un réplicon plasmidique sur un même contig. Que peut-on en conclure ?  *(ÉLIMINATOIRE)*  `A7`

- [ ] a) Les gènes détectés sont chromosomiques.
- [ ] b) Rien sur leur localisation : l'absence de co-localisation dépend aussi de la fragmentation de l'assemblage et de la chimie de banque.
- [ ] c) Les gènes détectés ne sont pas mobilisables.
- [ ] d) L'échantillon doit être réanalysé avec un autre assembleur.

**8.** Le journal indique depuis six mois des sauvegardes « réussies ». La sauvegarde est-elle vérifiée ?  *(ÉLIMINATOIRE)*  `A8`

- [ ] a) Oui : le journal en fait foi.
- [ ] b) Oui, si la taille de l'archive est conforme à l'attendu.
- [ ] c) Oui, si aucune alerte n'a été émise.
- [ ] d) Non : seule une restauration de contrôle, avec vérification de l'empreinte du fichier restauré, en apporte la preuve.

**9.** Avant dépôt en base publique de lectures issues d'un prélèvement humain, quelle opération est impérative ?  *(ÉLIMINATOIRE)*  `A9`

- [ ] a) Retirer les lectures d'origine humaine et contrôler l'effectivité de ce retrait.
- [ ] b) Compresser les fichiers au format attendu par la plateforme.
- [ ] c) Renommer les fichiers selon l'identifiant unique de laboratoire.
- [ ] d) Déposer les contigs assemblés plutôt que les lectures brutes.

**10.** L'identifiant de soumission en base publique peut-il être l'identifiant unique de laboratoire ?  `A9`

- [ ] a) Oui : cela facilite la traçabilité entre le dépôt et le dossier d'analyse.
- [ ] b) Non : un identifiant de soumission dédié est utilisé, la table de correspondance restant hors diffusion.
- [ ] c) Oui, si l'identifiant ne contient ni nom ni date de naissance.
- [ ] d) Indifférent, le choix relevant du déposant.

**11.** Un registre porte l'accession « CP_123456 ». Que signale ce format ?  `A10`

- [ ] a) Rien d'anormal : c'est une accession GenBank valide.
- [ ] b) Une accession de séquence protéique.
- [ ] c) Une accession provisoire, valable jusqu'à publication.
- [ ] d) Un format erroné : les accessions GenBank de série CP ne comportent pas de tiret bas, qui est propre aux accessions RefSeq.

**12.** Une même donnée figure dans deux registres avec des valeurs divergentes. Quelle conduite ?  `A10`

- [ ] a) Corriger la valeur dans le registre où l'on a constaté l'écart.
- [ ] b) Conserver les deux valeurs et signaler l'écart en commentaire.
- [ ] c) Corriger le registre désigné comme source et répercuter par jointure, sans ressaisie.
- [ ] d) Retenir la valeur la plus récente des deux.

**13.** Un rapport est attendu le jour même, mais un critère qualité n'est pas satisfait. Quelle conduite ?  `A11`

- [ ] a) Libérer le rapport en formulant une réserve orale au prescripteur.
- [ ] b) Ne pas libérer, tracer la décision et informer le prescripteur du délai et de son motif.
- [ ] c) Libérer un rapport partiel portant les seuls résultats conformes.
- [ ] d) Libérer le rapport, la responsabilité revenant au prescripteur.

**14.** Que recouvre le principe du moindre privilège ?  `A12`

- [ ] a) N'accorder à chacun que les droits strictement nécessaires aux actes pour lesquels il est habilité.
- [ ] b) Limiter le nombre de comptes ouverts sur le système.
- [ ] c) Réserver les droits d'administration au chef de laboratoire.
- [ ] d) Imposer un renouvellement fréquent des mots de passe.

## Seconde partie — questions à réponse courte

**15.** Citer deux éléments du journal d'exécution qui permettent d'identifier l'étape en échec, et indiquer ce que chacun apporte.  `A1` — 2 points

> 

**16.** Énoncer la différence entre un échec de run et un échec d'échantillon, et donner pour chacun un indicateur distinctif.  `A2` — 2 points

> 

**17.** Décrire en trois étapes la conduite à tenir après la mise à jour d'une base de référence.  `A4` — 2 points

> 

**18.** Expliquer en quelques lignes pourquoi une chimie de capture ciblée limite la mise en évidence d'une co-localisation entre un gène de résistance et un élément génétique mobile.  `A7` — 2 points

> 

**19.** Énumérer trois éléments qui ne doivent en aucun cas figurer dans un dépôt de code.  `A12` — 2 points

> 

**20.** Un agent quitte le laboratoire. Citer les actions à mener sur ses accès et le délai applicable.  `A12` — 2 points

> 
