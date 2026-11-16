#!/usr/bin/env python3
"""Crée un diaporama au gabarit `ressources/gabarit.pptx` à partir d'un fichier Markdown.

ATTENTION : depuis le passage en source PowerPoint, les .pptx de `diapositives/` sont la
source des modules et ne sont plus régénérés. Cet outil sert à **amorcer un nouveau module**
: il refuse d'écraser un fichier existant sans --forcer.

Le gabarit est le modèle de diaporama du master, vidé de ses diapositives : il apporte le
masque, les dispositions, le thème et les polices (Caladea pour le romain, Carlito pour le
corps). Seul le logo de l'INSP figure sur la page de titre.

Usage :
    python outils/md_vers_pptx.py                       # tous les modules
    python outils/md_vers_pptx.py diapositives/03_*.md  # un seul
"""
import glob
import os
import re
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Cm, Pt

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GABARIT = os.path.join(RACINE, "ressources", "gabarit.pptx")
LOGO = os.path.join(RACINE, "ressources", "logos", "insp.png")

ROMAIN, LABEUR = "Caladea", "Carlito"
ENCRE = RGBColor(0x1A, 0x1A, 0x1A)
GRIS = RGBColor(0x53, 0x53, 0x53)
FILET = RGBColor(0xC8, 0xC8, 0xC8)
ENTETE = RGBColor(0xE7, 0xE7, 0xE6)

MARGE = Cm(2.0)
SURTITRE = "FORMATION BIO-INFORMATIQUE  ·  DU FASTQ AU RAPPORT"
BAS = "Formation bio-informatique · LSG / CRPE — INSP"
SIGNATURE = ("Laboratoire de Surveillance Génomique des Pathogènes Épidémiques",
             "Centre de Recherche pour les Pathogènes Émergents · "
             "Institut National de Santé Publique, Bamako")


# ───────────────────────────── Markdown ─────────────────────────────
def planches(chemin):
    texte = open(chemin, encoding="utf-8").read()
    if texte.startswith("---"):
        texte = texte.split("---", 2)[2]
    return [b.strip() for b in re.split(r"\n---\n", texte) if b.strip()]


def decouper(bloc):
    lignes = bloc.split("\n")
    titre = ""
    if lignes and lignes[0].lstrip().startswith("#"):
        titre = lignes[0].lstrip("# ").strip()
        lignes = lignes[1:]
    return titre, [x.rstrip() for x in lignes]


def nu(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"<sub>(.+?)</sub>", r"\1", s)
    return re.sub(r"`(.+?)`", r"\1", s).strip()


def fragments(s):
    out = []
    for i, f in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        if not f:
            continue
        f = re.sub(r"<sub>(.+?)</sub>", r"\1", f).replace("`", "")
        out.append((f, i % 2 == 1))
    return out


# ───────────────────────────── primitives ─────────────────────────────
def texte(diapo, x, y, w, h, contenu, taille, police=LABEUR, couleur=ENCRE,
          gras=False, italique=False, align=PP_ALIGN.LEFT, interligne=1.15, espacement=None):
    zone = diapo.shapes.add_textbox(x, y, w, h)
    cadre = zone.text_frame
    cadre.word_wrap = True
    cadre.margin_left = cadre.margin_right = cadre.margin_top = cadre.margin_bottom = 0
    cadre.vertical_anchor = MSO_ANCHOR.TOP
    par = cadre.paragraphs[0]
    par.alignment = align
    par.line_spacing = interligne
    for frag, g in (contenu if isinstance(contenu, list) else fragments(contenu)):
        run = par.add_run()
        run.text = frag
        run.font.size = taille
        run.font.name = police
        run.font.bold = gras or g
        run.font.italic = italique
        run.font.color.rgb = couleur
        if espacement is not None:
            run.font._rPr.set("spc", str(int(espacement * 100)))
    return zone


def filet(diapo, x, y, w, epaisseur=Pt(1), couleur=FILET):
    forme = diapo.shapes.add_shape(1, x, y, w, epaisseur)
    forme.fill.solid()
    forme.fill.fore_color.rgb = couleur
    forme.line.fill.background()
    forme.shadow.inherit = False
    return forme


# ───────────────────────────── planches ─────────────────────────────
def page_de_titre(prs, titre, sous_titre, module):
    diapo = prs.slides.add_slide(prs.slide_layouts[0])
    if os.path.exists(LOGO):
        diapo.shapes.add_picture(LOGO, MARGE, Cm(0.9), height=Cm(2.9))
    texte(diapo, Cm(2.3), Cm(5.8), Cm(27.3), Cm(0.7),
          SURTITRE + (f"  ·  MODULE {module}" if module else ""),
          Pt(13), LABEUR, GRIS, espacement=1.8)
    texte(diapo, Cm(2.3), Cm(7.0), Cm(27.3), Cm(2.4), nu(titre),
          Pt(44), ROMAIN, ENCRE, gras=True, interligne=1.0)
    if sous_titre:
        texte(diapo, Cm(2.3), Cm(10.2), Cm(25.4), Cm(1.7), nu(sous_titre),
              Pt(17), LABEUR, GRIS, interligne=1.25)
    filet(diapo, Cm(2.3), Cm(12.4), Cm(8.1), Pt(1.5), RGBColor(0x8C, 0x8C, 0x8C))
    texte(diapo, Cm(2.3), Cm(12.9), Cm(27.3), Cm(1.0), SIGNATURE[0], Pt(18), LABEUR, ENCRE)
    texte(diapo, Cm(2.3), Cm(13.9), Cm(27.3), Cm(0.8), SIGNATURE[1], Pt(14), LABEUR, GRIS)
    return diapo


def entete(diapo, titre, numero):
    try:
        ph = diapo.shapes.title
    except (KeyError, AttributeError):
        ph = None
    if ph is not None:
        ph.left, ph.top, ph.width, ph.height = MARGE, Cm(1.5), Cm(29.8), Cm(1.2)
        par = ph.text_frame.paragraphs[0]
        for frag, g in fragments(titre):
            run = par.add_run()
            run.text = frag
            run.font.size = Pt(30)
            run.font.name = ROMAIN
            run.font.bold = True
            run.font.color.rgb = ENCRE
    else:
        texte(diapo, MARGE, Cm(1.5), Cm(29.8), Cm(1.2), titre, Pt(30), ROMAIN, ENCRE, gras=True)
    filet(diapo, MARGE, Cm(3.0), Cm(29.8), Pt(1.2))
    texte(diapo, MARGE, Cm(17.5), Cm(20), Cm(0.7), BAS, Pt(12), LABEUR, GRIS)
    texte(diapo, Cm(29.0), Cm(17.5), Cm(2.9), Cm(0.7), str(numero),
          Pt(12), LABEUR, GRIS, align=PP_ALIGN.RIGHT)
    return Cm(4.2)


def tableau(diapo, corps, y, largeur):
    ncol = max(len(r) for r in corps)
    hl = Cm(0.95)
    tbl = diapo.shapes.add_table(len(corps), ncol, MARGE, y, largeur, hl * len(corps)).table
    for r, rang in enumerate(corps):
        tbl.rows[r].height = hl
        for c in range(ncol):
            cell = tbl.cell(r, c)
            cell.text = ""
            cell.margin_left = cell.margin_right = Cm(0.25)
            cell.margin_top = cell.margin_bottom = Cm(0.08)
            cell.fill.solid()
            cell.fill.fore_color.rgb = ENTETE if r == 0 else RGBColor(0xFE, 0xFE, 0xFD)
            par = cell.text_frame.paragraphs[0]
            for frag, g in fragments(rang[c] if c < len(rang) else ""):
                run = par.add_run()
                run.text = frag
                run.font.size = Pt(13)
                run.font.name = ROMAIN if r == 0 else LABEUR
                run.font.bold = (r == 0) or g
                run.font.color.rgb = ENCRE if r == 0 else GRIS
    return y + hl * len(corps) + Cm(0.5)


def item(diapo, marqueur, terme, suite, y, largeur):
    texte(diapo, MARGE, y, Cm(1.1), Cm(1.1), marqueur, Pt(20), ROMAIN, GRIS, gras=True)
    texte(diapo, MARGE + Cm(1.5), y + Cm(0.05), largeur - Cm(1.5), Cm(0.9), terme,
          Pt(17), ROMAIN, ENCRE, gras=True)
    h = Cm(1.0)
    if suite:
        n = max(1, round(len(nu(suite)) / 110 + 0.45))
        texte(diapo, MARGE + Cm(1.5), y + Cm(0.95), largeur - Cm(1.5), Cm(0.8 * n), suite,
              Pt(14), LABEUR, GRIS, interligne=1.2)
        h += Cm(0.62 * n)
    filet(diapo, MARGE, y + h + Cm(0.15), largeur, Pt(0.75))
    return y + h + Cm(0.6)


def corps(diapo, lignes, y):
    largeur = Cm(29.8)
    i, compteur = 0, 0
    while i < len(lignes):
        ligne = lignes[i].strip()
        if not ligne:
            i += 1
            continue

        if ligne.startswith("|"):
            table = []
            while i < len(lignes) and lignes[i].strip().startswith("|"):
                cellules = [c.strip() for c in lignes[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cellules):
                    table.append(cellules)
                i += 1
            if table:
                y = tableau(diapo, table, y, largeur)
            continue

        marqueur = ""
        if re.match(r"^\d+\.\s", ligne):
            marqueur, ligne = ligne.split(". ", 1)
            marqueur += "."
        elif ligne.startswith(("- ", "* ")):
            compteur += 1
            marqueur, ligne = chr(96 + compteur) + ".", ligne[2:]

        if marqueur:
            m = re.match(r"^\*\*(.+?)\*\*[.:]?\s*(.*)$", ligne)
            if m and m.group(2):
                y = item(diapo, marqueur, m.group(1), m.group(2), y, largeur)
            else:
                y = item(diapo, marqueur, ligne, "", y, largeur)
            i += 1
            continue

        if ligne.startswith("> "):
            texte(diapo, MARGE + Cm(0.8), y, largeur - Cm(0.8), Cm(1.0), ligne[2:],
                  Pt(16), ROMAIN, ENCRE, italique=True, interligne=1.2)
            y += Cm(1.3)
            i += 1
            continue

        n = max(1, round(len(nu(ligne)) / 100 + 0.45))
        texte(diapo, MARGE, y, largeur, Cm(0.9 * n), ligne, Pt(16), LABEUR, ENCRE, interligne=1.3)
        y += Cm(0.78 * n + 0.35)
        i += 1
    return y


def convertir(source, destination=None):
    prs = Presentation(GABARIT)
    blocs = planches(source)
    mod = re.match(r"(\d+)", os.path.basename(source))
    mod = mod.group(1).lstrip("0") if mod else ""

    titre, lignes = decouper(blocs[0])
    page_de_titre(prs, titre, next((x.strip() for x in lignes if x.strip()), ""), mod)

    for n, bloc in enumerate(blocs[1:], start=2):
        t, lg = decouper(bloc)
        diapo = prs.slides.add_slide(prs.slide_layouts[1])
        for forme in list(diapo.placeholders):
            if forme.placeholder_format.idx != 0:
                forme._element.getparent().remove(forme._element)
        y = entete(diapo, t or " ", n)
        corps(diapo, lg, y)

    destination = destination or os.path.splitext(source)[0] + ".pptx"
    prs.save(destination)
    return destination, len(blocs)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    forcer = "--forcer" in sys.argv
    cibles = args or sorted(glob.glob(os.path.join(RACINE, "diapositives", "*.md")))
    for src in cibles:
        attendu = os.path.splitext(src)[0] + ".pptx"
        if os.path.exists(attendu) and not forcer:
            print(f"{os.path.relpath(attendu, RACINE)} — existe déjà, non régénéré "
                  "(le .pptx est la source ; --forcer pour écraser)")
            continue
        dst, n = convertir(src)
        print(f"{os.path.relpath(dst, RACINE)} — {n} planches")
