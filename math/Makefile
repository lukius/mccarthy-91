SRC_FILE=mccarthy.tex
BIN_DIR=..
RM=rm -rf
PDFLATEX=pdflatex


all: $(SRC_FILE)
	$(PDFLATEX) -output-directory $(BIN_DIR) $<
	$(PDFLATEX) -output-directory $(BIN_DIR) $<

clean:
	$(RM) $(BIN_DIR)/*.dvi $(BIN_DIR)/*.aux $(BIN_DIR)/*.log $(BIN_DIR)/*.pdf
