# Kommunale Websites im Wandel

Trends seit 2010 und Folgen für Städte mit 15.000 bis 40.000 Einwohner:innen.

- Text: `source.md` (pandoc-Markdown)
- Ausgabe: `docs/index.html` (GitHub Page) und `docs/kommunale-websites-im-wandel.pdf`, beide nicht eingecheckt

## Bauen

Voraussetzungen: Python 3.10+, pandoc 3, Pakete aus `requirements.txt`.

```
pip install -r requirements.txt
python3 build.py
```

Vorschau: `make serve`, dann http://localhost:8000 öffnen.

## Veröffentlichen

Jeder Push auf `main` baut Seite und PDF neu und veröffentlicht `docs/` auf GitHub Pages
(`.github/workflows/pages.yml`, Einstellung Pages → Source: GitHub Actions).

## Lizenzen

Schriften: Raleway und Barlow Condensed (SIL Open Font License, über Fontsource). Icons: Phosphor Icons (MIT).
