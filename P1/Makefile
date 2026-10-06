# Makefile for ASA Project 1 2025/2026 

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -O3 -Wall -Wextra
LDFLAGS = -lm

# Targets (English names)
TARGET = protein_chain

# Source files (English names)
SRC = protein_chain.cpp

# Default target
all: $(TARGET)

# Build main program
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

# Run the main program
run: $(TARGET)
	./$(TARGET)

# Test with the examples from the statement
test: $(TARGET)
	@echo "=== Example Test 1 ==="
	@printf "3\n10 5 12\nABA\n" | ./$(TARGET)
	@echo "\n=== Example Test 2 ==="
	@printf "9\n4 2 7 3 5 1 2 8 3\nANBPAPBNA\n" | ./$(TARGET)

# Clean build artifacts
clean:
	rm -f $(TARGET) *.out *.o

# Remove editor temporary files as well
distclean: clean
	rm -f *~ *.swp

# Rebuild from scratch
rebuild: clean all

.PHONY: all run test clean distclean rebuild
