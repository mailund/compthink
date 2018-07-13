


CHAPTERS := 000_header.yml \
		          Introduction_to_computation.txt \
              Introduction_to_algorithms.txt \
              Algorithmic_complexity.txt \
              Searching_and_sorting.txt \
              Recursion.txt \
              Divide_and_conquer.txt \
              Conclusions.txt \
              Solutions.txt

#CHAPTERS := 000_header.yml \
#              Solutions.txt

CHAPTERS := 000_header.yml \
              Introducing_Python.txt \
              Recursion.txt \
              Divide_and_conquer.txt \



SOURCE_CHAPTERS := $(foreach chapter,$(CHAPTERS),chapters/$(chapter))

PANDOC := pandoc

PANDOC_OPTS_ALL :=  --standalone --toc -f markdown+smart \
                    --top-level-division=chapter \
                    --filter pandoc-crossref \
                    --filter pandoc-citeproc

PANDOC_PDF_OPTS := $(PANDOC_OPTS_ALL) \
                    --default-image-extension=pdf \
                    --variable links-as-notes \
                    --template=templates/latex-template.tex

PANDOC_EPUB_OPTS := $(PANDOC_OPTS_ALL) \
                    --default-image-extension=png \
                    -t epub3 --toc-depth=1 \
                    --epub-cover-image=cover.png

all: book.pdf wc

book.pdf: $(SOURCE_CHAPTERS) Makefile templates/latex-template.tex
	$(PANDOC) $(PANDOC_PDF_OPTS) $(SOURCE_CHAPTERS) -o $@

wc: $(SOURCE_CHAPTERS)
	wc -w $(SOURCE_CHAPTERS)

refs: $(SOURCE_CHAPTERS)
	grep -ho '{#.*:.*}' chapters/*.txt

clean:
	rm book.pdf book.epub
