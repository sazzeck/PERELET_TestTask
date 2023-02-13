TEST_DIR := tests/
PYTHON := python3 -m

.PHONY: tests
tests:
	$(PYTHON) unittest $(TEST_DIR)matrix_test.py

run:
	$(PYTHON) src