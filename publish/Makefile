# Makefile to export jupyter notebooks .ipynb files to pdf through bookbook
all:
	aulas
	sessions


aulas: 
	cp ../aula-*-*.ipynb .
	python3 -m bookbook.latex --pdf --template aulas.tplx 
	mv -v combined.pdf coletanea-notebooks-metodos-numericos.pdf
	rm *.ipynb

sessions: 
	cp ../codeSession-*-*.ipynb .
	python3 -m bookbook.latex --pdf --template sessions.tplx 
	mv -v combined.pdf coletanea-code-sessions.pdf
	rm *.ipynb
