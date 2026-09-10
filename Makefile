PYTHON ?= python
.PHONY: check check-full test test-full format lint build
check:
	$(PYTHON) scripts/check.py
check-full:
	$(PYTHON) scripts/check.py --full
test:
	$(PYTHON) scripts/run_tests.py
test-full:
	$(PYTHON) scripts/run_tests.py --full
format:
	$(PYTHON) -m ruff format .
lint:
	$(PYTHON) -m ruff check .
build:
	$(PYTHON) scripts/build_release.py --candidate
