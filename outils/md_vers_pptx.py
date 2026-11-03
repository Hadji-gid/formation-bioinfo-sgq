#!/usr/bin/env python3
"""Convertit les planches Marp en présentation PowerPoint, au gabarit institutionnel.

Le gabarit reprend celui des exposés du master : page de titre à deux logos, surtitre espacé,
titre en romain, filet gris, bas de page discret, tableaux à en-tête grisé. Tout est produit
depuis le Markdown de `diapositives/`, qui reste la source unique.

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
from pptx.enum.text import PP_ALIGN
from pptx.util import Cm, Emu, Pt

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGOS = os.path.join(RACINE, "ressources", "logos")

SERIF, SANS = "Georgia", "Calibri"
ENCRE = RGBColor(0x1A, 0x1A, 0x1A)
GRIS = RGBColor(0x6B, 0x6B, 0x6B)
FILET = RGBColor(0xC8, 0xC8, 0xC8)
ENTETE = RGBColor(0xEF, 0xEF, 0xEF)

LARGEUR, HAUTEUR = Cm(33.87), Cm(19.05)
MARGE = Cm(2.2)
UTILE = LARGEUR - 2 * MARGE

SURTITRE = "FORMATION SGQ  ·  SECTION BIO-INFORMATIQUE"
BAS_DE_PAGE = "Formation SGQ · Section bio-informatique · LSG / CRPE — INSP"
SIGNATURE = ("Laboratoire de Surveillance Génomique des Pathogènes Épidémiques\n"
             "Centre de Recherche pour les Pathogènes Émergents — Institut National de "
             "Santé Publique, Bamako")


# ───────────────────────────── lecture du Markdown ─────────────────────────────
def planches(chemin):
    texte = open(chemin, encoding="utf-8").read()
    if texte.startswith("---"):
        texte = texte.split("---", 2)[2]
    return [b.strip() for b in re.split(r"\n---\n", texte) if b.strip()]


def decouper(bloc):
    lignes = bloc.split("\n")
    titre, niveau = "", 0
    if lignes and lignes[0].lstrip().startswith("#"):
        niveau = len(lignes[0]) - len(lignes[0].lstrip("#"))
        titre = lignes[0].lstrip("# ").strip()
        lignes = lignes[1:]
    return titre, niveau, [x.rstrip() for x in lignes]


def nu(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"<sub>(.+?)</sub>", r"\1", s)
    return re.sub(r"`(.+?)`", r"\1", s).strip()


def fragments(s):
    """Découpe une ligne en (texte, gras), en retirant le balisage résiduel."""
    out = []
    for i, f in enumerate(re.split(r"\*\*(.+?)\*\*", s)):
        if not f:
            continue
        f = re.sub(r"<sub>(.+?)</sub>", r"\1", f).replace("`", "")
        out.append((f, i % 2 == 1))
    return out


# ───────────────────────────── primitives de mise en page ─────────────────────────────
def texte(diapo, x, y, w, h, contenu, taille=16, police=SANS, couleur=ENCRE,
          gras=False, italique=False, align=PP_ALIGN.LEFT, interligne=1.15, espacement=None):
    zone = diapo.shapes.add_textbox(x, y, w, h)
    cadre = zone.text_frame
    cadre.word_wrap = True
    cadre.margin_left = cadre.margin_right = cadre.margin_top = cadre.margin_bottom = 0
    par = cadre.paragraphs[0]
    par.alignment = align
    par.line_spacing = interligne
    morceaux = contenu if isinstance(contenu, list) else fragments(contenu)
    for frag, g in morceaux:
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
    forme = diapo.shapes.add_shape(1, x, y, w, epaisseur)     # rectangle
    forme.fill.solid()
    forme.fill.fore_color.rgb = couleur
    forme.line.fill.background()
    forme.shadow.inherit = False
    return forme


def logo(diapo, nom, x, y, hauteur):
    chemin = os.path.join(LOGOS, nom)
    if os.path.exists(chemin):
        return diapo.shapes.add_picture(chemin, x, y, height=hauteur)
    return None


# ───────────────────────────── planches ─────────────────────────────
def page_de_titre(prs, titre, sous_titre, module):
    diapo = prs.slides.add_slide(prs.slide_layouts[6])
    img = logo(diapo, "insp.png", Cm(0), Cm(1.6), Cm(2.8))
    if img is not None:
        img.left = int((LARGEUR - img.width) / 2)
    texte(diapo, MARGE, Cm(5.6), UTILE, Cm(0.8),
          SURTITRE + (f"  ·  MODULE N° {module}" if module else ""),
          taille=Pt(11), police=SANS, couleur=GRIS, align=PP_ALIGN.CENTER, espacement=2.2)
    texte(diapo, MARGE, Cm(6.9), UTILE, Cm(3.2), nu(titre),
          taille=Pt(40), police=SERIF, couleur=ENCRE, gras=True,
          align=PP_ALIGN.CENTER, interligne=1.05)
    if sous_titre:
        texte(diapo, MARGE, Cm(10.4), UTILE, Cm(1.4), nu(sous_titre),
              taille=Pt(17), police=SANS, couleur=GRIS, align=PP_ALIGN.CENTER)
    filet(diapo, Cm(14.4), Cm(12.6), Cm(5.0), Pt(1.6), GRIS)
    texte(diapo, MARGE, Cm(13.6), UTILE, Cm(2.2), SIGNATURE,
          taille=Pt(12), police=SANS, couleur=GRIS, align=PP_ALIGN.CENTER, interligne=1.3)
    return diapo


def entete(diapo, titre, numero):
    texte(diapo, MARGE, Cm(1.5), UTILE, Cm(1.6), nu(titre),
          taille=Pt(26), police=SERIF, couleur=ENCRE, gras=True)
    filet(diapo, MARGE, Cm(3.1), UTILE, Pt(1.4))
    texte(diapo, MARGE, HAUTEUR - Cm(1.5), UTILE - Cm(2), Cm(0.7), BAS_DE_PAGE,
          taille=Pt(9), police=SANS, couleur=GRIS)
    texte(diapo, LARGEUR - MARGE - Cm(2), HAUTEUR - Cm(1.5), Cm(2), Cm(0.7), str(numero),
          taille=Pt(9), police=SANS, couleur=GRIS, align=PP_ALIGN.RIGHT)
    return Cm(3.9)


def tableau(diapo, corps, y, largeur):
    ncol = max(len(r) for r in corps)
    hl = Cm(0.95)
    forme = diapo.shapes.add_table(len(corps), ncol, MARGE, y, largeur, hl * len(corps))
    tbl = forme.table
    tbl.first_row = True
    for r, rang in enumerate(corps):
        tbl.rows[r].height = hl
        for c in range(ncol):
            cell = tbl.cell(r, c)
            cell.text = ""
            cell.margin_left = cell.margin_right = Cm(0.25)
            cell.margin_top = cell.margin_bottom = Cm(0.1)
            cell.fill.solid()
            cell.fill.fore_color.rgb = ENTETE if r == 0 else RGBColor(0xFF, 0xFF, 0xFF)
            par = cell.text_frame.paragraphs[0]
            for frag, g in fragments(rang[c] if c < len(rang) else ""):
                run = par.add_run()
                run.text = frag
                run.font.size = Pt(13)
                run.font.name = SERIF if r == 0 else SANS
                run.font.bold = (r == 0) or g
                run.font.color.rgb = ENCRE if r == 0 else GRIS
    return y + hl * len(corps) + Cm(0.5)


def item_terme(diapo, marqueur, terme, suite, y, largeur):
    texte(diapo, MARGE, y, Cm(1.2), Cm(0.9), marqueur,
          taille=Pt(15), police=SERIF, couleur=GRIS, gras=True)
    hauteur = Cm(0.95)
    texte(diapo, MARGE + Cm(1.3), y, largeur - Cm(1.3), Cm(0.9), terme,
          taille=Pt(16), police=SERIF, couleur=ENCRE, gras=True)
    if suite:
        lignes = max(1, round(len(suite) / 105 + 0.4))
        texte(diapo, MARGE + Cm(1.3), y + Cm(0.75), largeur - Cm(1.3), Cm(0.8 * lignes), suite,
              taille=Pt(14), police=SANS, couleur=GRIS, interligne=1.2)
        hauteur += Cm(0.72 * lignes)
    filet(diapo, MARGE, y + hauteur + Cm(0.12), largeur, Pt(0.75))
    return y + hauteur + Cm(0.55)


def corps(diapo, lignes, y, numero_planche):
    largeur = UTILE
    i, compteur = 0, 0
    while i < len(lignes):
        ligne = lignes[i]
        if not ligne.strip():
            i += 1
            continue

        if ligne.strip().startswith("|"):
            table_corps = []
            while i < len(lignes) and lignes[i].strip().startswith("|"):
                cellules = [c.strip() for c in lignes[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cellules):
                    table_corps.append(cellules)
                i += 1
            if table_corps:
                y = tableau(diapo, table_corps, y, largeur)
            continue

        brut = ligne.strip()
        marqueur = ""
        if re.match(r"^\d+\.\s", brut):
            marqueur, brut = brut.split(". ", 1)
            marqueur += "."
        elif brut.startswith(("- ", "* ")):
            compteur += 1
            marqueur, brut = chr(96 + compteur) + ")", brut[2:]

        if marqueur:
            m = re.match(r"^\*\*(.+?)\*\*[.:]?\s*(.*)$", brut)
            if m and m.group(2):
                y = item_terme(diapo, marqueur, m.group(1), m.group(2), y, largeur)
            else:
                y = item_terme(diapo, marqueur, brut, "", y, largeur)
            i += 1
            continue

        if brut.startswith("> "):
            texte(diapo, MARGE + Cm(0.6), y, largeur - Cm(0.6), Cm(1.0), brut[2:],
                  taille=Pt(14), police=SANS, couleur=GRIS, italique=True)
            y += Cm(1.1)
            i += 1
            continue

        nlignes = max(1, round(len(nu(brut)) / 95 + 0.45))
        texte(diapo, MARGE, y, largeur, Cm(0.9 * nlignes), brut,
              taille=Pt(16), police=SANS, couleur=ENCRE, interligne=1.25)
        y += Cm(0.82 * nlignes + 0.3)
        i += 1
    return y


def convertir(source, destination=None):
    prs = Presentation()
    prs.slide_width, prs.slide_height = LARGEUR, HAUTEUR
    blocs = planches(source)
    module = re.match(r"(\d+)", os.path.basename(source))
    module = module.group(1).lstrip("0") if module else ""

    titre, _niveau, lignes = decouper(blocs[0])
    sous = next((x.strip() for x in lignes if x.strip()), "")
    page_de_titre(prs, titre, sous, module)

    for n, bloc in enumerate(blocs[1:], start=2):
        t, _niv, corps_lignes = decouper(bloc)
        diapo = prs.slides.add_slide(prs.slide_layouts[6])
        y = entete(diapo, t or " ", n)
        corps(diapo, corps_lignes, y, n)

    destination = destination or os.path.splitext(source)[0] + ".pptx"
    prs.save(destination)
    return destination, len(blocs)


if __name__ == "__main__":
    cibles = sys.argv[1:] or sorted(glob.glob(os.path.join(RACINE, "diapositives", "*.md")))
    for src in cibles:
        dst, n = convertir(src)
        print(f"{os.path.relpath(dst, RACINE)} — {n} planches")
