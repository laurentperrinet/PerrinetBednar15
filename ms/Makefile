default: srep supplementary

SRC = PerrinetBednar14

srep: $(SRC)srep.pdf
report: $(SRC)report.pdf
full: $(SRC)full.pdf
poster: $(SRC)poster.pdf
supplementary: $(SRC)supplementary.pdf

#LATEXMK = latexmk -pdf
LATEXMK = latexmk --pdf  -pdflatex=lualatex

$(SRC)full.pdf: $(SRC)full.tex #../bib/$(SRC).bib
	$(LATEXMK) $(SRC)full.tex

$(SRC)poster.pdf: $(SRC)poster.tex #../bib/$(SRC).bib
	$(LATEXMK) $(SRC)poster.tex

$(SRC)supplementary.pdf: $(SRC)supplementary.tex #../bib/$(SRC).bib
	$(LATEXMK) $(SRC)supplementary.tex

$(SRC)srep.pdf: $(SRC)srep.tex #../bib/$(SRC).bib
	$(LATEXMK) $(SRC)srep.tex

$(SRC)report.pdf: $(SRC)report.tex #../bib/$(SRC).bib
	$(LATEXMK) $(SRC)report.tex

edit_linux: linux_edit
linux_edit:
	texmaker ${SRC}.tex &
	gedit Makefile &

edit_mac: mac_edit
mac_edit:
	open *.tex
	mvim Makefile
	open -a /Applications/BibDesk.app/  ../bib/${SRC}.bib

../bib/$(SRC).bib: bib
bib: bib_citeulike
bib_citeulike:
	wget "http://www.citeulike.org/bibtex/user/LaurentPerrinet/tag/assofield?fieldmap=posted-at:date-added&do_username_prefix=0&key_type=4" -O ../bib/${SRC}.bib

# cleaning macros
touch:
	touch *.tex

clean_luatex_cache:
	rm -fr ~/Library/texlive
	luaotfload-tool --update --force -vv
clean:
	rm -f *.bcf *idx  *.md5 *.out  *.auxlock  *.run.xml *.dvi *.ps *.out *.log *.aux *.bbl *.blg *.snm *.fls *.nav *.toc *.fff *.synctex.gz* *.fdb_latexmk

.PHONY:  all clean
