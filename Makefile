.PHONY: build web serve

build:
	python3 build.py

web:
	python3 build.py --web-only

serve:
	python3 -m http.server -d docs 8000
