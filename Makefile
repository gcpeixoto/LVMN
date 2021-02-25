html:
	jupyter-book build .

latex:
	jupyter-book build . --builder pdflatex


# How to update book (see https://jupyterbook.org/publish/gh-pages.html)
# 1. Make changes to the master branch
# 2. Re-build the book
# 3. Push changes to master
# 4. Use ghp-import -n -p -f _build/html to update 
