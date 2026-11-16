#!/usr/bin/env python3
"""Contrôle l'intégrité des fichiers .pptx de `diapositives/`.

Deux défauts rendent une présentation « à réparer » à l'ouverture dans PowerPoint, sans que
python-pptx ne signale quoi que ce soit à l'enregistrement :

1. **Identifiants de forme en double** — deux formes d'une même planche portant le même
   `cNvPr id`. C'est ce qui arrive quand on recopie des formes d'un fichier dans un autre : les
   identifiants d'origine voyagent avec elles et entrent en collision.
2. **Relations manquantes** — une forme qui référence un `r:id` (image, lien hypertexte) absent
   du fichier de relations de la planche. Typiquement une image recopiée sans sa relation, ou un
   lien hypertexte hérité d'un autre fichier.

Usage :
    python outils/verifier_pptx.py          # contrôle, code de sortie 1 si défaut
    python outils/verifier_pptx.py --reparer  # réattribue les identifiants et retire les liens morts
"""
import collections
import glob
import os
import re
import sys
import zipfile

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = re.compile(r'r:(?:embed|id|link)="([^"]+)"')
CNVPR = re.compile(r'<(?:p|pic|a|dgm|cdr):cNvPr id="(\d+)"')


def controler(chemin):
    """Renvoie la liste des défauts : (planche, relations manquantes, identifiants en double)."""
    defauts = []
    with zipfile.ZipFile(chemin) as z:
        planches = [n for n in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)]
        for n in sorted(planches, key=lambda s: int(re.findall(r"\d+", s)[0])):
            xml = z.read(n).decode("utf-8", "ignore")
            rels = n.replace("slides/", "slides/_rels/") + ".rels"
            connus = (set(re.findall(r'Id="([^"]+)"', z.read(rels).decode("utf-8", "ignore")))
                      if rels in z.namelist() else set())
            manquantes = sorted(set(REF.findall(xml)) - connus)
            compte = collections.Counter(CNVPR.findall(xml))
            doubles = sorted(k for k, v in compte.items() if v > 1)
            if manquantes or doubles:
                defauts.append((os.path.basename(n), manquantes, doubles))
    return defauts


def reparer(chemin):
    """Réattribue des identifiants uniques et retire les liens hypertexte orphelins."""
    from pptx import Presentation
    from pptx.oxml.ns import qn

    prs = Presentation(chemin)
    renommes = liens = 0
    for diapo in prs.slides:
        connus = {r.rId for r in diapo.part.rels.values()}
        for el in list(diapo._element.iter()):
            if el.tag.endswith("}hlinkClick"):
                rid = el.get(qn("r:id"))
                if rid and rid not in connus:
                    el.getparent().remove(el)
                    liens += 1
        n = 0
        for el in list(diapo._element.iter()):
            if el.tag.endswith("}cNvPr"):
                n += 1
                el.set("id", str(n))
                if not el.get("name"):
                    el.set("name", f"Forme {n}")
        renommes += n
    prs.save(chemin)
    return renommes, liens


if __name__ == "__main__":
    fichiers = sorted(glob.glob(os.path.join(RACINE, "diapositives", "*.pptx")))
    if not fichiers:
        print("Aucune présentation à contrôler.")
        sys.exit(0)
    if "--reparer" in sys.argv:
        for f in fichiers:
            if controler(f):
                n, l = reparer(f)
                print(f"{os.path.basename(f)} — {n} identifiants réattribués, {l} lien(s) retiré(s)")
    sortie = 0
    for f in fichiers:
        defauts = controler(f)
        if defauts:
            sortie = 1
            print(f"{os.path.basename(f)} — {len(defauts)} planche(s) en défaut")
            for planche, manquantes, doubles in defauts[:10]:
                detail = []
                if manquantes:
                    detail.append("relations manquantes : " + ", ".join(manquantes))
                if doubles:
                    detail.append("identifiants en double : " + ", ".join(doubles))
                print(f"   {planche} — " + " ; ".join(detail))
        else:
            print(f"{os.path.basename(f)} — conforme")
    sys.exit(sortie)
