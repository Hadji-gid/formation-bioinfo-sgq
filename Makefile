MARP = marp
SLIDES = $(wildcard diapositives/*.md)
PDFS = $(SLIDES:.md=.pdf)

.PHONY: all slides manuel propre verifier

all: slides

slides: $(PDFS)

diapositives/%.pdf: diapositives/%.md
	$(MARP) --pdf --allow-local-files $< -o $@

manuel:
	pandoc manuel/manuel_participant.md -o manuel/manuel_participant.pdf \
		--toc --number-sections -V lang=fr -V geometry:margin=2.2cm

verifier:
	@echo "Fichiers interdits éventuellement présents :"
	@git ls-files | grep -Ei '\.(fastq|fq|bam|vcf|fasta|fa|key|pem)(\.gz)?$$' || echo "  aucun"

propre:
	rm -f diapositives/*.pdf diapositives/*.html manuel/*.pdf
