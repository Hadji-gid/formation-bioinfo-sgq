---
marp: true
lang: fr
paginate: true
header: "LSG — Formation bio-informatique : Linux et ligne de commande"
footer: "INSP / CRPE — support pédagogique, non opposable"
---

# Linux, ligne de commande et scripts

Le poste de travail du bio-informaticien

---

## Pourquoi la ligne de commande

- **Les outils n'existent que là.** fastp, samtools, metaSPAdes, Kraken2, AMRFinderPlus : aucun n'a d'interface graphique. La ligne de commande n'est pas un choix de style.
- **La volumétrie.** Un run produit des dizaines de gigaoctets. Aucun tableur, aucun gestionnaire de fichiers ne tient à cette échelle.
- **La traçabilité.** Une commande se copie dans un registre, se rejoue à l'identique, se compare. Un clic ne laisse aucune trace.
- **La répétition.** Seize échantillons, une boucle. C'est aussi ce qui évite l'erreur de recopie, première cause d'inversion d'échantillon.

> Ce qui se fait à la souris se raconte ; ce qui se fait en ligne de commande se prouve.

---

## Se repérer dans le système de fichiers

| Commande | Ce qu'elle fait |
|---|---|
| pwd | affiche le dossier courant |
| ls -lh | liste le contenu, tailles lisibles |
| cd chemin | se déplace |
| cd .. | remonte d'un niveau |
| cd ~ | retourne au dossier personnel |
| tree -L 2 | montre l'arborescence sur deux niveaux |

Un chemin **absolu** commence par `/` et ne dépend pas d'où vous êtes : `/home/alhadji/runs/RUN-2026-03-12`. Un chemin **relatif** part du dossier courant : `../donnees/brutes`.

Sous WSL, le disque Windows est monté sous `/mnt/c/`. Travaillez dans `~/` : les accès y sont bien plus rapides.

---

## Manipuler fichiers et dossiers

| Commande | Ce qu'elle fait |
|---|---|
| mkdir -p runs/RUN-2026-03-12/brut | crée l'arborescence complète |
| cp source destination | copie |
| mv source destination | déplace ou renomme |
| rm fichier | supprime — **sans corbeille, sans retour** |
| ln -s cible lien | crée un lien symbolique |
| df -h  ·  du -sh dossier | espace disque libre · taille d'un dossier |

**La règle de prudence.** `rm -rf` ne demande rien et ne pardonne rien. Avant tout effacement, lancez la même commande avec `ls` à la place de `rm` : ce qui s'affiche est ce qui disparaîtra.

Les données brutes sont montées **en lecture seule** quand c'est possible : on ne corrige pas un FASTQ, on le remplace par une nouvelle extraction.

---

## Regarder un fichier sans l'ouvrir

| Commande | Usage |
|---|---|
| head -n 8 fichier.txt | les huit premières lignes |
| tail -n 20 journal.log | les vingt dernières |
| less fichier | parcourir — q pour quitter |
| wc -l fichier | compter les lignes |
| zcat ech.fastq.gz \| head -4 | lire un fichier compressé sans le décompresser |

Un FASTQ compte **quatre lignes par lecture** : identifiant, séquence, séparateur, scores de qualité. Le nombre de lectures est donc le nombre de lignes divisé par quatre.

```
zcat ech_R1.fastq.gz | wc -l    # puis diviser par 4
```

---

## Filtrer, extraire, compter

| Commande | Usage |
|---|---|
| grep motif fichier | les lignes contenant le motif |
| grep -c "^@" fichier | les compter |
| cut -f1,3 table.tsv | extraire les colonnes 1 et 3 |
| sort \| uniq -c | regrouper et dénombrer |
| awk '$5 > 30' table.tsv | filtrer sur la valeur d'une colonne |

Exemple — dénombrer les gènes de résistance détectés par classe :

```
cut -f11 amrfinder.tsv | sort | uniq -c | sort -rn
```

Chaque commande fait **une seule chose**. C'est leur enchaînement qui fait le travail.

---

## Tubes et redirections

| Symbole | Effet |
|---|---|
| commande1 \| commande2 | la sortie de l'une alimente l'autre |
| commande > fichier | écrit dans le fichier, **en l'écrasant** |
| commande >> fichier | ajoute à la fin |
| commande 2> erreurs.log | détourne les messages d'erreur |
| commande \| tee journal.txt | affiche **et** enregistre |

Le piège du chevron simple : `>` écrase sans prévenir. Un `>` à la place d'un `>>` a effacé plus d'un journal d'exécution.

Conservez toujours la sortie : `fastp … 2> journal_fastp.txt` — c'est elle qui expliquera, dans six mois, pourquoi un échantillon a été écarté.

---

## Permissions et exécution

| Commande | Usage |
|---|---|
| ls -l | affiche les droits (rwx) |
| chmod +x script.sh | rend un script exécutable |
| ./script.sh | exécute un script du dossier courant |
| which samtools | où se trouve l'outil réellement appelé |
| samtools --version | quelle version tourne |

`which` et `--version` ne sont pas des commandes de curiosité : ce sont elles qui remplissent le registre des versions, et elles disent souvent qu'un autre environnement que celui qu'on croyait est actif.

---

## Écrire un script

Un script est une suite de commandes dans un fichier. Il se relit, se corrige, se verse à Git.

```
#!/usr/bin/env bash
set -euo pipefail

RUN="RUN-2026-03-12"
ENTREE="$HOME/runs/$RUN/brut"
SORTIE="$HOME/runs/$RUN/nettoye"
mkdir -p "$SORTIE"

for R1 in "$ENTREE"/*_R1.fastq.gz; do
    ECH=$(basename "$R1" _R1.fastq.gz)
    fastp -i "$R1" -I "$ENTREE/${ECH}_R2.fastq.gz" \
          -o "$SORTIE/${ECH}_R1.fastq.gz" -O "$SORTIE/${ECH}_R2.fastq.gz" \
          --json "$SORTIE/${ECH}.json" 2> "$SORTIE/${ECH}.log"
done
```

---

## Ce que chaque ligne du script apporte

- **#!/usr/bin/env bash** — indique quel interpréteur exécute le fichier.
- **set -euo pipefail** — arrête le script à la première erreur, refuse les variables non définies, et propage l'échec à travers les tubes. Sans cette ligne, un script continue allègrement après un échec et produit des sorties incomplètes qui passent inaperçues.
- **Les chemins en variables** — un seul endroit à modifier pour changer de run.
- **Les guillemets autour des variables** — sans eux, un nom de fichier contenant un espace casse la commande.
- **Un journal par échantillon** — la preuve de ce qui s'est passé, échantillon par échantillon.

---

## Rendre un script réutilisable

Passer le run en argument plutôt que l'écrire en dur :

```
RUN="${1:?Usage : ./nettoyer.sh RUN-AAAA-MM-JJ}"

./nettoyer.sh RUN-2026-03-12
```

Trois garde-fous qui coûtent trois lignes :

- vérifier que le dossier d'entrée existe avant de commencer ;
- refuser d'écrire dans un dossier de sortie déjà rempli, plutôt que d'écraser ;
- afficher la version des outils en tête de journal.

Le script va dans le dépôt Git du laboratoire. **Les données n'y vont jamais.**

---

## Travaux longs et travail à distance

| Commande | Usage |
|---|---|
| ssh utilisateur@serveur | se connecter au serveur de calcul |
| tmux new -s analyse | ouvrir une session qui survit à la déconnexion |
| tmux attach -t analyse | y revenir plus tard |
| htop | voir la charge et la mémoire |
| nproc  ·  free -h | nombre de cœurs · mémoire disponible |

Un assemblage dure des heures. Lancé sans `tmux`, il meurt avec la connexion — une coupure de réseau suffit. Lancé dans une session nommée, il continue, et vous le retrouvez le lendemain.

---

## Ce qu'on retient

- Une commande fait une chose ; c'est l'enchaînement qui fait le travail.
- `>` écrase, `>>` ajoute, `tee` fait les deux — et le journal se conserve.
- `set -euo pipefail` en tête de tout script : un échec doit arrêter le traitement, pas le laisser produire des sorties partielles.
- Les scripts se versionnent, les données jamais.
- `which` et `--version` avant de croire savoir quel outil tourne.
