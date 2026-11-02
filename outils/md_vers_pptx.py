#!/usr/bin/env python3
"""Convertit les planches Marp en présentation PowerPoint éditable.

Pourquoi : Marp produit un PDF, qui se projette mais ne s'annote pas et ne se retouche pas
avant une séance. Ce convertisseur donne un .pptx modifiable, sans Node ni navigateur.

Usage :
    python outils/md_vers_pptx.py                  # toutes les planches
    python outils/md_vers_pptx.py diapositives/03_pipeline_et_qualite.md
"""
import glob
import os
import re
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Cm, Pt

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCENT = RGBColor(0x15, 0x60, 0x7A)
GRIS = RGBColor(0x44, 0x44, 0x44)


def planches(chemin):
    """Découpe un fichier Marp en planches, en écartant l'en-tête YAML."""
    texte = open(chemin, encoding="utf-8").read()
    if texte.startswith("---"):
        texte = texte.split("---", 2)[2]
    return [bloc.strip() for bloc in re.split(r"\n---\n", texte) if bloc.strip()]


def decouper(bloc):
    """Renvoie (titre, lignes de corps) pour une planche."""
    lignes = bloc.split("\n")
    titre = ""
    if lignes and lignes[0].lstrip().startswith("#"):
        titre = lignes[0].lstrip("# ").strip()
        lignes = lignes[1:]
    return titre, [li.rstrip() for li in lignes]


def sans_balisage(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"<sub>(.+?)</sub>", r"\1", s)
    s = re.sub(r"`(.+?)`", r"\1", s)
    return s.strip()


def segments(s):
    """Découpe une ligne en fragments (texte, gras)."""
    out = []
    for i, frag in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        if frag:
            out.append((re.sub(r"<sub>(.+?)</sub>|`", lambda m: m.group(1) or "", frag),
                        i % 2 == 1))
    return out


def tableau_de(lignes, depart):
    """Extrait un tableau Markdown à partir de l'indice `depart`."""
    corps = []
    i = depart
    while i < len(lignes) and lignes[i].strip().startswith("|"):
        cellules = [c.strip() for c in lignes[i].strip().strip("|").split("|")]
        if not all(re.fullmatch(r":?-{2,}:?", c) for c in cellules):
            corps.append([sans_balisage(c) for c in cellules])
        i += 1
    return corps, i


def ajouter_planche(prs, titre, lignes):
    diapo = prs.slides.add_slide(prs.slide_layouts[6])   # vierge
    haut = Cm(1.4)

    if titre:
        zone = diapo.shapes.add_textbox(Cm(1.6), haut, prs.slide_width - Cm(3.2), Cm(2.0))
        par = zone.text_frame.paragraphs[0]
        run = par.add_run()
        run.text = sans_balisage(titre)
        run.font.size = Pt(30)
        run.font.bold = True
        run.font.color.rgb = ACCENT
        zone.text_frame.word_wrap = True
        haut = Cm(3.4)

    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        if not ligne.strip():
            i += 1
            continue

        if ligne.strip().startswith("|"):
            corps, i = tableau_de(lignes, i)
            if not corps:
                continue
            ncol = max(len(r) for r in corps)
            hauteur = Cm(min(1.0 * len(corps) + 0.4, 10))
            forme = diapo.shapes.add_table(len(corps), ncol, Cm(1.6), haut,
                                           prs.slide_width - Cm(3.2), hauteur)
            tbl = forme.table
            for r, rang in enumerate(corps):
                for c in range(ncol):
                    cell = tbl.cell(r, c)
                    cell.text = rang[c] if c < len(rang) else ""
                    for p in cell.text_frame.paragraphs:
                        for run in p.runs:
                            run.font.size = Pt(13)
                            run.font.bold = (r == 0)
            haut = haut + hauteur + Cm(0.4)
            continue

        zone = diapo.shapes.add_textbox(Cm(1.6), haut, prs.slide_width - Cm(3.2), Cm(1.2))
        cadre = zone.text_frame
        cadre.word_wrap = True
        par = cadre.paragraphs[0]
        texte = ligne.strip()
        taille, puce = Pt(17), ""
        if texte.startswith(("- ", "* ")):
            texte, puce = texte[2:], "•  "
        elif re.match(r"^\d+\.\s", texte):
            numero, texte = texte.split(". ", 1)
            puce = numero + ".  "
        elif texte.startswith("> "):
            texte, taille = texte[2:], Pt(15)
        if puce:
            r0 = par.add_run()
            r0.text = puce
            r0.font.size = taille
            r0.font.color.rgb = ACCENT
        for frag, gras in segments(texte):
            run = par.add_run()
            run.text = frag
            run.font.size = taille
            run.font.bold = gras
            run.font.color.rgb = GRIS
        haut = haut + Cm(0.95 if len(texte) < 90 else 1.5)
        i += 1
    return diapo


def convertir(source, destination=None):
    prs = Presentation()
    prs.slide_width, prs.slide_height = Cm(33.87), Cm(19.05)   # 16:9
    for bloc in planches(source):
        titre, lignes = decouper(bloc)
        ajouter_planche(prs, titre, lignes)
    destination = destination or os.path.splitext(source)[0] + ".pptx"
    prs.save(destination)
    return destination, len(prs.slides.__iter__.__self__._sldIdLst)


if __name__ == "__main__":
    cibles = sys.argv[1:] or sorted(glob.glob(os.path.join(RACINE, "diapositives", "*.md")))
    for src in cibles:
        dst, n = convertir(src)
        print(f"{os.path.relpath(dst, RACINE)} — {n} planches")
