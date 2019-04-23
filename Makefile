

PANDOC := pandoc

# --filter ulysses-figure-labels \

PANDOC_OPTS :=      --standalone --toc -f markdown+smart \
                    --top-level-division=chapter \
										--filter py2-ulysses-figure-labels \
										--filter pandoc-crossref \
                    --filter pandoc-citeproc \
                    --default-image-extension=pdf \
                    --highlight-style monochrome \
                    --variable links-as-notes \
                    --variable secnumdepth=section \
                    --toc-depth=2 \
                    --template=templates/7x10.tex \
										--resource-path=book

all: book.pdf

#test.md: book/index.md 000_header.yml Makefile templates/7x10.tex
#	$(PANDOC) --filter ulysses-figure-labels 000_header.yml book/index.md -o $@

#book1.pdf: test.md 000_header.yml Makefile templates/7x10.tex
#		$(PANDOC) $(PANDOC_OPTS) 000_header.yml test.md -o $@

book.pdf: book/index.md 000_header.yml Makefile templates/7x10.tex
	$(PANDOC) $(PANDOC_OPTS) 000_header.yml book/index.md -o $@


refs: book/index.md
	grep -ho '{#.*:.*}' book/index.md
	egrep -ho '\[@.*:*?\]' book/index.md

clean:
	rm book.pdf
