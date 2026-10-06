# Root Makefile for ASA Projects (P1, P2, P3)

SUBDIRS = P1 P2 P3

all:
	@for dir in $(SUBDIRS); do \
		if [ -d $$dir ]; then \
			echo "=== Building $$dir ==="; \
			$(MAKE) -C $$dir all || exit 1; \
		fi \
	done

clean:
	@for dir in $(SUBDIRS); do \
		if [ -d $$dir ]; then \
			echo "=== Cleaning $$dir ==="; \
			$(MAKE) -C $$dir clean || exit 1; \
		fi \
	done

distclean:
	@for dir in $(SUBDIRS); do \
		if [ -d $$dir ]; then \
			echo "=== Distcleaning $$dir ==="; \
			$(MAKE) -C $$dir distclean || exit 1; \
		fi \
	done

rebuild:
	@for dir in $(SUBDIRS); do \
		if [ -d $$dir ]; then \
			echo "=== Rebuilding $$dir ==="; \
			$(MAKE) -C $$dir rebuild || exit 1; \
		fi \
	done

test:
	@for dir in $(SUBDIRS); do \
		if [ -d $$dir ]; then \
			echo "=== Testing $$dir ==="; \
			$(MAKE) -C $$dir test || exit 1; \
		fi \
	done

.PHONY: all clean distclean rebuild test $(SUBDIRS)
