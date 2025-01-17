COMPILER = g++
OPTIONS = -Wall
PROGRAM = california
FILES = california.cpp introduction.cpp inputs.cpp inventory.cpp encounters.cpp

$(PROGRAM): $(FILES)
	$(COMPILER) $(OPTIONS) $(FILES) -o $(PROGRAM)

all: $(PROGRAM)

run: $(PROGRAM)
	./$(PROGRAM)

clean: 
	rm *$(PROGRAM)

cleanrun:
	rm *$(PROGRAM)
	$(COMPILER) $(OPTIONS) $(FILES) -o $(PROGRAM)
	./$(PROGRAM)