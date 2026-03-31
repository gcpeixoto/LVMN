start: 
	jupyter-book start

html:
	jupyter-book build --html

pdf:
	jupyter-book build --pdf

clean:
	jupyter-book clean --all