# Makefile for ASA Project 2 2025/2026 

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -O3 -Wall -Wextra
LDFLAGS = -lm

# Targets
TARGET = deliveriesCaracol

# Source files
SRC = deliveriesCaracol.cpp

# Default target
all: $(TARGET)

# Build main program
$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $< -o $@ $(LDFLAGS)

# Run the main program
run: $(TARGET)
	./$(TARGET)

# Test target
test: $(TARGET)
	@echo "No automatic tests specified for P2."

# Clean build artifacts
clean:
	rm -f $(TARGET) *.out *.o

# Remove editor temporary files as well
distclean: clean
	rm -f *~ *.swp

# Rebuild from scratch
rebuild: clean all

.PHONY: all run test clean distclean rebuild
