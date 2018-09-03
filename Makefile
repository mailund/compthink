

# Full
CHAPTERS := 000_header.yml \
		      Introduction_to_computation.txt \
		      Introducing_Python.txt \
              Introduction_to_algorithms.txt \
              Algorithmic_complexity.txt \
              Searching_and_sorting.txt \
              Functions.txt \
              Recursion.txt \
              Parsers_and_languages.txt \
              Divide_and_conquer.txt \
              Return_to_functions.txt \
              Return_to_sorting.txt \
              Stacks.txt \
              Set_sequences_maps.txt \
              Trees_and_graphs.txt \
              Pythons_data_model.txt \
              Testing.txt \
              Python-vm.txt \
              Conclusions.txt \
              Solutions.txt


#CHAPTERS := 000_header.yml \
#              Recursion.txt \


SOURCE_CHAPTERS := $(foreach chapter,$(CHAPTERS),chapters/$(chapter))

PANDOC := pandoc

PANDOC_OPTS_ALL :=  --standalone --toc -f markdown+smart \
                    --top-level-division=chapter \
                    --filter pandoc-crossref \
                    --filter pandoc-citeproc

PANDOC_PDF_OPTS := $(PANDOC_OPTS_ALL) \
                    --default-image-extension=pdf \
                    --variable links-as-notes \
                    --variable secnumdepth=section \
                    --toc-depth=2 \
                    --template=templates/latex-template.tex

all: book.pdf wc

book.pdf: $(SOURCE_CHAPTERS) Makefile templates/latex-template.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) $(SOURCE_CHAPTERS) -o $@

wc: $(SOURCE_CHAPTERS)
	wc -w $(SOURCE_CHAPTERS)

refs: $(SOURCE_CHAPTERS)
	grep -ho '{#.*:.*}' chapters/*.txt
	egrep -ho '\[@.*:*?\]' chapters/*.txt

clean:
	rm book.pdf book.epub
