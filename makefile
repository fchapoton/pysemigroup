all: install test

install:
	sage -pip install --upgrade --no-index -v .

test:
	sage -tp --force-lib src/*py 

coverage:
	sage -coverage src/*

