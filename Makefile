# (C) 2020 Nathaniel D'Rozario
# See LICENSE file for license details

.PHONY: clean

CXX = g++
PY = python3

build-test-program:
	$(CXX) test.cpp -o test.exe

test: build-test-program
	$(PY) ioverify.py test test.zip

clean:
	rm -rf test.exe
	rm -rf *.in
	rm -rf *.out