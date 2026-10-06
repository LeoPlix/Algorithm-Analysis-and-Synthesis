# Makefile for ASA Project 3 2025/2026 

# Python executable
PYTHON = python3
MAIN = SnailSoft.py

# Default target
all: run_check

# Check syntax / readiness
run_check:
	@$(PYTHON) -m py_compile $(MAIN)

# Run the main program
run:
	$(PYTHON) $(MAIN)

# Test target
test:
	@echo "No automatic tests specified for P3."

# Clean build artifacts and bytecode
clean:
	rm -rf __pycache__ *.pyc *.out

# Remove editor temporary files as well
distclean: clean
	rm -f *~ *.swp

# Rebuild from scratch
rebuild: clean all

.PHONY: all run_check run test clean distclean rebuild
