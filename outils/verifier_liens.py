#!/usr/bin/env python3
"""Vérifie que les renvois relatifs des fichiers Markdown pointent vers un fichier existant.

Les liens externes (http, https, mailto) ne sont pas suivis : une vérification réseau
échouerait de façon intermittente et ferait échouer la construction pour une mauvaise raison.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIEN = re.compile(r"\[[^\]]*\]\(([^)\s]+)")
EXTERNE = ("http://", "https://", "mailto:", "#")

erreurs = []
examines = 0

for dossier, _, fichiers in os.walk(RACINE):
    if ".git" in dossier.split(os.sep):
        continue
    for nom in fichiers:
        if not nom.endswith(".md"):
            continue
        chemin = os.path.join(dossier, nom)
        with open(chemin, encoding="utf-8") as fh:
            for numero, ligne in enumerate(fh, 1):
                for cible in LIEN.findall(ligne):
                    if cible.startswith(EXTERNE):
                        continue
                    examines += 1
                    cible = cible.split("#")[0]
                    if not cible:
                        continue
                    if not os.path.exists(os.path.join(dossier, cible)):
                        erreurs.append(
                            f"{os.path.relpath(chemin, RACINE)}:{numero} -> {cible}")

print(f"{examines} renvoi(s) interne(s) examiné(s).")
if erreurs:
    print("Renvois cassés :")
    for e in erreurs:
        print("  " + e)
    sys.exit(1)
print("Tous les renvois internes résolvent.")
