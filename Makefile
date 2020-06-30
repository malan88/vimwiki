MARKDOWN=$(shell find . -iname "*.md")
# Form all 'html' counterparts
HTML=$(MARKDOWN:.md=.html)

.PHONY = all tar clean
all: $(HTML)

%.html: %.md style.css
	# convert md links to html and then pandoc the whole file
	sed 's/\.md)/\.html)/g' $< | \
		pandoc -s --metadata title="$*" --css "/style.css" --from markdown --to html -o $@

clean:
	rm $(HTML):w

