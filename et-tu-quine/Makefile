.PHONY: quine rm
quine: quine.c
	gcc -o $@ $?
	./quine | diff quine.c -

rm:
	rm -f quine
