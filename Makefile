
CHAPTERS := 000_header.md \
			Introduction_to_computation.md \
			Introducing_Python.md \
			Loops_and_sequences.md \
			Conditional_statements.md \
			List_comprehension.md \
			Tables.md \
			Functions.md


SOURCE_CHAPTERS := $(foreach chapter,$(CHAPTERS),chapters/$(chapter))

PANDOC := pandoc

PANDOC_OPTS_ALL :=  --standalone --toc \
					-f markdown+smart \
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

book.pdf: $(SOURCE_CHAPTERS) Makefile templates/latex-template.tex
	cat $(SOURCE_CHAPTERS) | sed 's/.png){#fig:/){#fig:/' | $(PANDOC) $(PANDOC_PDF_OPTS) -o $@

book.epub: $(SOURCE_CHAPTERS) Makefile
	cat $(SOURCE_CHAPTERS) | sed 's/.png){#fig:/){#fig:/' | $(PANDOC) $(PANDOC_EPUB_OPTS) -o $@ $(SOURCE_CHAPTERS)

wc: $(SOURCE_CHAPTERS)
	wc -w $(SOURCE_CHAPTERS)

chapters/%.md: chapters/%.ipynb
	jupyter nbconvert $< --to Markdown

clean:
	rm book.pdf book.epub
