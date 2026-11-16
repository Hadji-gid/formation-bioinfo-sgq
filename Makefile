MARP = marp
SLIDES = $(wildcard diapositives/*.md)
PDFS = $(SLIDES:.md=.pdf)

.PHONY: all slides pptx manuel propre verifier verifier-pptx

all: slides

slides: $(PDFS)

pptx:
	python3 outils/md_vers_pptx.py

diapositives/%.pdf: diapositives/%.md
	$(MARP) --pdf --allow-local-files $< -o $@

manuel:
	pandoc manuel/manuel_participant.md -o manuel/manuel_participant.pdf \
		--toc --number-sections -V lang=fr -V geometry:margin=2.2cm

verifier-pptx:
	python3 outils/verifier_pptx.py

verifier:
	@python3 outils/verifier_pptx.py
	@echo "Fichiers interdits éventuellement présents :"
	@git ls-files | grep -Ei '\.(fastq|fq|bam|vcf|fasta|fa|key|pem)(\.gz)?$$' || echo "  aucun"

propre:
	rm -f diapositives/*.pdf diapositives/*.html manuel/*.pdf
