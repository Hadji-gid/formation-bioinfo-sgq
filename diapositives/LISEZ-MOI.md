# Les diaporamas : le `.pptx` est la source

Depuis novembre 2026, **le fichier `.pptx` de chaque module est la source**. On le modifie dans
PowerPoint, on l'enregistre, on le verse à Git. Il n'est plus régénéré.

## Pourquoi ce choix

Les modules étaient produits à partir des fichiers Markdown de ce dossier. Deux sources
coexistaient donc pour un même module, et toute retouche faite dans PowerPoint était écrasée à
la génération suivante. Une seule source vaut mieux qu'une source théorique et une source
réelle.

## Ce que deviennent les fichiers `.md`

Ils restent dans le dépôt comme **trace du contenu rédigé**, et parce qu'ils se lisent et se
comparent ligne à ligne sur GitHub, ce qu'un `.pptx` ne permet pas. Ils ne sont plus
contraignants : en cas de divergence avec le `.pptx`, **c'est le `.pptx` qui fait foi**.

Si vous modifiez une planche en profondeur, reportez la correction dans le `.md` correspondant
— non par obligation, mais pour que l'historique Git garde une trace lisible de ce qui a changé.

## Modifier un module

```bash
cd formation-bioinfo-sgq
# ouvrir diapositives/0X_….pptx dans PowerPoint, modifier, enregistrer
make verifier-pptx          # identifiants de forme et relations
git add diapositives/0X_….pptx
git commit -m "diapositives: ..."
git push
```

Le contrôle d'intégrité n'est pas une formalité : une planche recopiée d'un autre diaporama
emporte les identifiants de ses formes, et PowerPoint refuse alors d'ouvrir le fichier sans le
réparer.

## Créer un nouveau module

Le convertisseur `outils/md_vers_pptx.py` sert à **amorcer** un module : il produit un `.pptx`
au gabarit à partir d'un `.md`. Il refuse d'écraser un fichier existant ; `--forcer` lève ce
garde-fou, à n'utiliser qu'en connaissance de cause.

```bash
# écrire diapositives/06_mon_module.md, puis
python3 outils/md_vers_pptx.py diapositives/06_mon_module.md
```

## Poids du dépôt

Chaque version d'un `.pptx` est stockée en entier : six modules représentent environ 3,5 Mo par
tour de modifications. C'est tenable pour un support de formation ; si le dépôt devenait lourd,
Git LFS serait la réponse — à ne mettre en place qu'au moment où le besoin se fait sentir.
