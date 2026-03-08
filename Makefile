.PHONY: validate lint-md check-yaml check-json check-links init report help clean all

all: validate check-yaml check-json

validate:
	python3 scripts/validate_repo.py

lint-md:
	npx markdownlint-cli2 "**/*.md"

check-yaml:
	@python3 -c "\
	import yaml, glob, sys;\
	files = glob.glob('**/*.yaml', recursive=True) + glob.glob('**/*.yml', recursive=True);\
	print('Checking %d YAML file(s)...' % len(files));\
	ok = True;\
	\
	[None for f in files for ok_flag in [\
	    (lambda path: (\
	        yaml.safe_load(open(path)),\
	        print('  OK: ' + path),\
	        True\
	    )[-1])(f)\
	] if ok_flag];\
	\
	print('All YAML files valid.')\
	" 2>&1 || (echo "YAML validation failed"; exit 1)

check-json:
	@python3 -c "\
	import json, glob, sys;\
	files = glob.glob('schemas/**/*.json', recursive=True);\
	print('Checking %d JSON file(s) in schemas/...' % len(files));\
	ok = True;\
	\
	[None for f in files for ok_flag in [\
	    (lambda path: (\
	        json.load(open(path)),\
	        print('  OK: ' + path),\
	        True\
	    )[-1])(f)\
	] if ok_flag];\
	\
	print('All JSON files valid.')\
	" 2>&1 || (echo "JSON validation failed"; exit 1)

check-links:
	python3 scripts/validate_repo.py --check-links

init:
	@echo "To initialize a new product entry from templates:"
	@echo "  1. Copy templates/product-template/ to products/<your-product>/"
	@echo "  2. Update the YAML files with your product details"
	@echo "  3. Run 'make validate' to verify the structure"

report:
	@# Note: generate_report.py is a work-in-progress
	python3 scripts/generate_report.py

help:
	@echo "Available targets:"
	@echo "  all          Run validate, check-yaml, and check-json"
	@echo "  validate     Run repository structure validation"
	@echo "  lint-md      Run markdownlint-cli2 on all Markdown files"
	@echo "  check-yaml   Validate all YAML files"
	@echo "  check-json   Validate all JSON files in schemas/"
	@echo "  check-links  Run link checking via validate_repo.py"
	@echo "  init         Show instructions for initializing a new product entry"
	@echo "  report       Generate assurance report (WIP)"
	@echo "  help         Show this help message"
	@echo "  clean        Remove generated/cached files"

clean:
	rm -rf __pycache__ .pytest_cache reports/
	find . -type d -name '__pycache__' -exec rm -rf {} + 2>/dev/null || true
