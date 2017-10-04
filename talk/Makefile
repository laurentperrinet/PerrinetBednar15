default: pdf

SRC = perrinet11ermites_talk
SRC = perrinet11sfn_talk
SRC = perrinet12anc_talk
SRC = perrinet13cerco_talk
SRC = perrinet13gif_talk
SRC = perrinet15sis
LATEX = latexmk --pdf -pdflatex=lualatex
BIBTEX = bibtex -terse

pdf: $(SRC).pdf

$(SRC).pdf: $(SRC).tex
	$(LATEX) $(SRC)

mac_: mac_talk mac_handout
linux_: linux_talk linux_handout

mac_export_usb:
	rsync -av -u --delete --exclude .svn * /Volumes/MICKEY/TaucTalk

mac_export_dropbox:
	rsync -av -u --delete * ~/Desktop/Dropbox/SparseEdgeTalk

talk_mac: mac_talk
mac_talk: pdf
	#open -a /Applications/Adobe\ Reader.app ${SRC}.pdf  
	open ${SRC}.pdf  

edit_linux: linux_edit
linux_edit: 
	texmaker ${SRC}.tex &
	gedit Makefile &

edit_mac: mac_edit
mac_edit: 
	open ${SRC}.tex 
	mvim Makefile

talk_linux: linux_talk
linux_talk: pdf
	impressive --nologo -d 45m  -t None ${SRC}.pdf  

handout_mac: mac_handout 
mac_handout: handout bigpic
	open $(SRC)-nup.pdf  &

handout_linux: linux_handout
linux_handout: handout
	evince $(SRC)-nup.pdf &

handout: $(SRC).pdf
	pdfnup --nup 1x2  --frame true  --no-landscape $(SRC).pdf


# macros
%.pdf: %.svg
	inkscape --without-gui $< --export-pdf=$@

%.png: %.svg
	inkscape --without-gui $< --export-png=$@ -d 150

 
# cleaning macros

clean:
	rm -f *.dvi *.ps *.out *.log *.aux *.bbl *.blg *.snm *.nav  *.fdb_latexmk *.toc *.info *.synctex.gz* $(SRC).pdf $(SRC)_handout.pdf *-nup.pdf

.PHONY: clean all
