#!/usr/bin/env python3
"""Baut docs/index.html (GitHub Page) und docs/<PDF_NAME> aus source.md.

Ablauf: pandoc -> HTML-Fragment, dann mit BeautifulSoup nachbearbeiten
(Grafiken, Icons, Fussnoten), getrennt fuer Web und Druck.
"""
import re
import subprocess
import sys
from pathlib import Path

from bs4 import BeautifulSoup

from figures import FIGS

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
ICONS = ROOT / "icons"
PDF_NAME = "kommunale-websites-im-wandel.pdf"
TITLE = "Software und KI im Wandel"
SUB = "Trends seit 2010 und Folgen für Kommunen und Behörden"
STAND = "Stand 25. Oktober 2026"

# Farben fuer den Druck (Web nutzt CSS-Variablen)
NAVY, ACCENT, ON_NAVY = "#183a5a", "#1f5fa8", "#ffffff"
PRO, CON = "#9fdcb0", "#ffb4a8"

FONTS = """
@font-face{font-family:"Raleway";src:url(fonts/raleway-latin-400-normal.woff) format("woff");font-weight:400;font-style:normal}
@font-face{font-family:"Raleway";src:url(fonts/raleway-latin-400-italic.woff) format("woff");font-weight:400;font-style:italic}
@font-face{font-family:"Raleway";src:url(fonts/raleway-latin-600-normal.woff) format("woff");font-weight:600}
@font-face{font-family:"Raleway";src:url(fonts/raleway-latin-700-normal.woff) format("woff");font-weight:700}
@font-face{font-family:"Barlow Condensed";src:url(fonts/barlow-condensed-latin-500-normal.woff) format("woff");font-weight:500}
@font-face{font-family:"Barlow Condensed";src:url(fonts/barlow-condensed-latin-600-normal.woff) format("woff");font-weight:600}
@font-face{font-family:"Barlow Condensed";src:url(fonts/barlow-condensed-latin-700-normal.woff) format("woff");font-weight:700}
"""

CSS_WEB = FONTS + """
:root{--bg:#fbfaf6;--ink:#1c1d21;--quiet:#5d6168;--rule:#dedbd2;--tint:#efece4;--accent:#1f5fa8;--navy:#183a5a;--sand:#ece3cc;
--pro:#9fdcb0;--con:#ffb4a8;
--c-ink:#1c1d21;--c-quiet:#5d6168;--c-grid:#e3e0d8;--c-axis:#b1ada2;--c-muted:#a9a59a;--c-accent:#1f5fa8;--c-navy:#183a5a;--c-white:#ffffff}
@media (prefers-color-scheme:dark){:root{--bg:#16171a;--ink:#e9e7e1;--quiet:#a6a39b;--rule:#34363b;--tint:#202226;--accent:#7eaae8;--navy:#23507c;--sand:#2e2a21;
--c-ink:#e9e7e1;--c-quiet:#a6a39b;--c-grid:#34363b;--c-axis:#5d5f64;--c-muted:#75736c;--c-accent:#7eaae8;--c-navy:#23507c;--c-white:#ffffff}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.7 Raleway,system-ui,sans-serif;font-variant-numeric:lining-nums}
.wrap{max-width:1100px;margin:0 auto;padding:56px 16px 96px}
.col{max-width:680px}
h1,h2,h3,dt,th,.k-head,nav#TOC::before{font-family:"Barlow Condensed","Arial Narrow",sans-serif}
header.top h1{font-weight:700;font-size:3.3rem;line-height:1;letter-spacing:-.005em;margin:0 0 .6rem}
header.top .sub{font-size:1.1rem;line-height:1.45;color:var(--quiet);margin:0 0 1rem}
header.top .meta{font-size:.85rem;color:var(--quiet);display:flex;gap:1.2rem;align-items:center;flex-wrap:wrap}
header.top .meta a{display:inline-flex;gap:.35rem;align-items:center;color:var(--accent);font-weight:600;text-decoration:none}
header.top .meta svg{width:1.1em;height:1.1em}
h2{font-weight:700;font-size:2.05rem;line-height:1.1;margin:3.6rem 0 1rem;padding-top:.9rem;border-top:3px solid var(--ink)}
h3{font-weight:600;font-size:1.35rem;margin:2.2rem 0 .5rem}
p{margin:0 0 1.05rem}
a{color:var(--accent);text-decoration-thickness:1px;text-underline-offset:2px}
nav#TOC{margin:2.4rem 0 2.8rem;padding:1.2rem 1.4rem;background:var(--tint);font-size:.92rem}
nav#TOC::before{content:"Inhalt";display:block;font-weight:600;font-size:1.15rem;text-transform:uppercase;letter-spacing:.04em;margin-bottom:.5rem}
nav#TOC ul{list-style:none;margin:0;padding:0;columns:2;column-gap:2rem}
nav#TOC ul ul{display:none}
nav#TOC li{margin:0;padding:.14rem 0;break-inside:avoid}
nav#TOC a{text-decoration:none;color:var(--ink)}
nav#TOC a:hover{color:var(--accent)}
.k-head{display:flex;align-items:center;gap:.45rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.k-head svg{width:1.25em;height:1.25em;flex:none}
.beiuns{background:var(--sand);padding:.85rem 1rem .95rem;margin:1rem 0 1.3rem;font-size:.86rem;line-height:1.55}
.beiuns .k-head{font-size:.9rem;color:var(--navy);margin-bottom:.3rem}
@media (prefers-color-scheme:dark){.beiuns .k-head{color:var(--accent)}}
.beiuns p{margin:0}
.folgen{background:var(--navy);color:#fff;padding:1.15rem 1.35rem 1.2rem;margin:1.6rem 0 .8rem;font-size:.95rem;line-height:1.55}
.folgen .k-head{font-size:1.05rem;margin-bottom:.55rem}
.folgen a{color:#fff}
.folgen ul{list-style:none;margin:0;padding:0}
.folgen li{position:relative;padding-left:1.75rem;margin:.4rem 0}
.folgen li p{margin:0}
.mk{position:absolute;left:0;top:.2em;width:1.1em;height:1.1em;display:inline-flex}
.mk svg{width:100%;height:100%}
.mk.pro{color:var(--pro)}.mk.con{color:var(--con)}.mk.rec{color:#fff}
.inl{display:inline-flex;width:1em;height:1em;vertical-align:-.12em;margin-right:.15em}
.inl svg{width:100%;height:100%}
.inl.pro{color:#2f7d4f}.inl.con{color:#b4483c}.inl.rec{color:var(--accent)}
.table-wrap{overflow-x:auto;margin:1.3rem 0 1.5rem}
table{border-collapse:collapse;font:500 .98rem/1.35 "Barlow Condensed","Arial Narrow",sans-serif;width:100%}
th,td{text-align:left;vertical-align:top;padding:.45rem .55rem;border-bottom:1px solid var(--rule)}
th{font-weight:600;text-transform:uppercase;letter-spacing:.04em;font-size:.85rem;color:var(--quiet);border-bottom:2px solid var(--ink)}
td[style*="center"],th[style*="center"]{text-align:center}
td .ok{display:inline-flex;width:1.1em;height:1.1em;color:var(--navy)}
@media (prefers-color-scheme:dark){td .ok{color:var(--accent)}}
td .ok svg{width:100%;height:100%}
figure{margin:1.8rem 0 2rem}
figure svg{width:100%;height:auto;display:block}
figcaption{font-size:.78rem;color:var(--quiet);margin-top:.5rem}
ol,ul{padding-left:1.4rem}
li{margin:.3rem 0}
.checklist ul{list-style:none;padding-left:0}
.checklist li{padding-left:1.7rem;position:relative}
.checklist li::before{content:"";position:absolute;left:.1rem;top:.42em;width:.85em;height:.85em;border:2px solid var(--ink)}
dl{margin:0}
dt{font-weight:600;font-size:1.2rem;margin-top:1.2rem}
dd{margin:.1rem 0 0}
dt:target{color:var(--accent)}
.gl{position:relative}
.gl-tip{display:none;position:absolute;left:0;top:calc(100% + 6px);z-index:5;width:max-content;max-width:min(19rem,80vw);
  padding:.55rem .7rem;background:var(--ink);color:var(--bg);font:400 .82rem/1.45 Raleway,system-ui,sans-serif;text-align:left;text-transform:none;letter-spacing:0}
.gl-tip::before{content:"";position:absolute;left:0;right:0;top:-6px;height:6px}
@media (hover:hover){.gl:hover .gl-tip{display:block}}
.gl a:focus-visible+.gl-tip{display:block}
.gl.off .gl-tip{display:none}
.footnote-ref{text-decoration:none}
.footnote-ref sup{font:600 .78em "Barlow Condensed",sans-serif;color:var(--accent);padding-left:1px}
.footnotes{margin-top:4rem;font-size:.8rem;line-height:1.5;color:var(--quiet)}
.footnotes hr{display:none}
.footnotes h2{font-size:1.5rem;color:var(--ink)}
.footnotes li:target{background:var(--tint)}
.footnote-back{text-decoration:none}
footer{margin-top:3rem;font-size:.8rem;color:var(--quiet)}
@media (min-width:1060px){
  .col{margin-right:380px}
  .beiuns{float:right;clear:right;width:300px;margin:.35rem -380px 1rem 0}
}
@media (max-width:640px){body{font-size:16px}nav#TOC ul{columns:1}header.top h1{font-size:2.5rem}h2{font-size:1.7rem}}
"""

CSS_PRINT = FONTS + """
@page{size:A4;margin:18mm 15mm 20mm 20mm;
  @bottom-left{content:"Software und KI im Wandel";font:500 8pt "Barlow Condensed";color:#5d6168;letter-spacing:.03em}
  @bottom-right{content:counter(page);font:600 8.5pt "Barlow Condensed";color:#5d6168}
  @footnote{border-top:.5pt solid #b1ada2;padding-top:1.6mm;margin-top:3mm}}
@page :first{@bottom-left{content:none}@bottom-right{content:none}}
html{font:400 8.9pt/1.5 Raleway,"DejaVu Sans",sans-serif;color:#1c1d21;font-variant-numeric:lining-nums}
body{margin:0}
.col{padding-right:57mm}
a{color:inherit;text-decoration:none}
a[href^="#"]{color:#1f5fa8}
h1,h2,h3,dt,th,.k-head,nav#TOC::before{font-family:"Barlow Condensed","DejaVu Sans",sans-serif}
header.top{margin:18mm 0 10mm}
header.top h1{font-weight:700;font-size:34pt;line-height:1;margin:0 0 3mm}
header.top .sub{font-size:11pt;line-height:1.4;color:#5d6168;margin:0 0 4mm}
header.top .meta{font-size:8.5pt;color:#5d6168}
header.top .meta a{display:none}
nav#TOC{margin:8mm 0 0;page-break-after:always;font-size:9pt}
nav#TOC::before{content:"INHALT";display:block;font-weight:600;font-size:12pt;letter-spacing:.05em;margin-bottom:3mm}
nav#TOC ul{list-style:none;margin:0;padding:0}
nav#TOC ul ul{display:none}
nav#TOC li{margin:1.1mm 0}
nav#TOC a{color:#1c1d21}
nav#TOC a::after{content:leader(".") target-counter(attr(href),page);color:#5d6168}
h2{font-weight:700;font-size:19pt;line-height:1.05;margin:9mm 0 3mm;padding-top:2mm;border-top:1.6pt solid #1c1d21;break-after:avoid}
h3{font-weight:600;font-size:12.5pt;margin:5mm 0 1.5mm;break-after:avoid}
p{margin:0 0 2.4mm;orphans:3;widows:3}
.k-head{font-weight:600;text-transform:uppercase;letter-spacing:.05em}
.k-head svg{width:3.4mm;height:3.4mm;vertical-align:-.7mm;margin-right:1.2mm}
.beiuns{float:right;clear:right;width:49mm;margin:.5mm -57mm 2mm 0;background:#ece3cc;padding:2.4mm 2.8mm 2.6mm;font-size:7.3pt;line-height:1.42}
.beiuns .k-head{font-size:8.2pt;color:#183a5a;margin-bottom:1mm}
.beiuns p{margin:0}
.bu-in{display:inline-block;width:100%}
.folgen{background:#183a5a;color:#fff;padding:3.4mm 4mm 3.6mm;margin:4mm 0 2mm;font-size:8.2pt;line-height:1.45;break-inside:avoid}
.folgen .k-head{font-size:9.6pt;margin-bottom:1.6mm}
.folgen a{color:#fff}
.folgen ul{list-style:none;margin:0;padding:0}
.folgen li{position:relative;padding-left:5mm;margin:1.2mm 0}
.folgen li p{margin:0}
.mk{position:absolute;left:0;top:.5mm;width:3.2mm;height:3.2mm}
.mk svg{width:3.2mm;height:3.2mm}
.inl svg{width:2.8mm;height:2.8mm;vertical-align:-.4mm}
table{border-collapse:collapse;font:500 8.6pt/1.3 "Barlow Condensed","DejaVu Sans",sans-serif;width:100%;margin:3mm 0 4mm;clear:right}
th,td{text-align:left;vertical-align:top;padding:1.2mm 1.5mm;border-bottom:.4pt solid #d8d4ca}
th{font-weight:600;text-transform:uppercase;letter-spacing:.04em;font-size:7.6pt;color:#5d6168;border-bottom:1pt solid #1c1d21}
td[style*="center"],th[style*="center"]{text-align:center}
td .ok svg{width:3mm;height:3mm}
tr{break-inside:avoid}
figure{margin:4mm 0 4mm;clear:right;break-inside:avoid}
figure svg{width:100%;height:auto}
figcaption{font-size:6.8pt;color:#5d6168;margin-top:1.2mm}
ol,ul{padding-left:5mm;margin:0 0 2.4mm}
li{margin:.8mm 0}
.checklist{break-inside:avoid}
.checklist ul{list-style:none;padding-left:0}
.checklist li{padding-left:5mm;position:relative}
.checklist li::before{content:"";position:absolute;left:.3mm;top:1mm;width:2.4mm;height:2.4mm;border:.9pt solid #1c1d21}
dl{margin:0}
dt{font-weight:600;font-size:11pt;margin-top:3mm;break-after:avoid}
dd{margin:.4mm 0 0}
.fn{float:footnote;font-size:6.7pt;line-height:1.35;color:#3c4043;text-align:left}
.fn a{color:#1f5fa8}
::footnote-call{content:counter(footnote);vertical-align:super;font:600 6.4pt/0 "Barlow Condensed";color:#1f5fa8;padding-left:.3pt}
::footnote-marker{content:counter(footnote) "  ";font:600 7pt "Barlow Condensed"}
"""


def icon(name, cls="", color=None):
    """Phosphor-Icon (bold) inline. Im Druck feste Farbe statt currentColor."""
    svg = (ICONS / f"{name}.svg").read_text().strip()
    svg = svg.replace("<svg ", f'<svg aria-hidden="true" class="{cls}" ', 1)
    if color:
        svg = svg.replace('fill="currentColor"', f'fill="{color}"')
    return svg


def pandoc():
    tpl = ROOT / ".frag.tpl"
    tpl.write_text('<nav id="TOC">$table-of-contents$</nav>\n$body$\n')
    res = subprocess.run(["pandoc", str(ROOT / "source.md"), "-f", "markdown", "-t", "html5",
                          "--toc", "--toc-depth=2", "--wrap=none", "--template", str(tpl)],
                         capture_output=True, text=True, check=True)
    tpl.unlink()
    if res.stderr:
        print(res.stderr, file=sys.stderr)
    return res.stdout


def frag(html):
    return BeautifulSoup(html, "html.parser")


def dress(soup, mode):
    """Grafiken, Kasten-Koepfe, Marker und Haken einsetzen."""
    pr = mode == "print"
    for p in soup.find_all("p"):
        m = re.fullmatch(r"FIGURE:(\w+)", p.get_text(strip=True))
        if m:
            fn, cap = FIGS[m.group(1)]
            p.replace_with(frag(f'<figure id="abb-{m.group(1)}">{fn(mode)}<figcaption>{cap}</figcaption></figure>'))
    for box in soup.select("div.folgen"):
        label = box.get("title") or box.get("data-title") or "Folgen für kleine Kommunen"  # ::: {.folgen title="..."}
        for k in ("title", "data-title"):
            if k in box.attrs:
                del box[k]
        box.insert(0, frag(f'<div class="k-head">{icon("info", color=ON_NAVY if pr else None)}'
                           f'<span>{label}</span></div>'))
    for box in soup.select("div.beiuns"):
        inner = soup.new_tag("div", attrs={"class": "bu-in"})  # inline-block: im PDF nicht ueber Seiten teilbar
        for child in list(box.contents):
            inner.append(child.extract())
        box.append(inner)
        box = inner
        box.insert(0, frag(f'<div class="k-head">{icon("map-pin", color=NAVY if pr else None)}'
                           f'<span>Bei uns</span></div>'))
    names = {"pro": "plus", "con": "minus", "rec": "arrow-right"}
    for kind, name in names.items():
        for sp in soup.select(f"span.{kind}"):
            in_box = sp.find_parent("div", class_="folgen") is not None
            if pr:
                col = {"pro": PRO, "con": CON, "rec": ON_NAVY} if in_box else {"pro": "#2f7d4f", "con": "#b4483c", "rec": ACCENT}
                svg = icon(name, color=col[kind])
            else:
                svg = icon(name)
            sp.clear()
            sp.append(frag(svg))
            sp["class"] = ["mk" if in_box else "inl", kind]
            sp["aria-label"] = {"pro": "Vorteil", "con": "Nachteil", "rec": "Empfehlung"}[kind]
    for td in soup.find_all("td"):
        if td.get_text(strip=True) == "✓":
            td.clear()
            td.append(frag(f'<span class="ok" aria-label="ja">{icon("check", color=NAVY if pr else None)}</span>'))


def glossary_tips(soup):
    """Web: Glossar-Links zeigen die Definition beim Zeigen oder Fokussieren."""
    defs = {}
    for dt in soup.select("dl dt"):
        anchor, dd = dt.find(id=re.compile(r"^g-")), dt.find_next_sibling("dd")
        if anchor and dd:
            defs[anchor["id"]] = dd.get_text(" ", strip=True)
    for i, a in enumerate(soup.select('a[href^="#g-"]')):
        text = defs.get(a["href"][1:])
        if not text:
            continue
        a.wrap(soup.new_tag("span", attrs={"class": "gl"}))
        tip = soup.new_tag("span", attrs={"class": "gl-tip", "role": "tooltip", "id": f"tip-{i}"})
        tip.string = text
        a.insert_after(tip)
        a["aria-describedby"] = tip["id"]


# Tooltip nach links schieben, wenn er rechts aus dem Fenster oder dem scrollbaren
# Tabellen-Container ragt (der wuerde ihn abschneiden).
# Escape blendet ihn aus, ohne Maus oder Fokus zu bewegen (WCAG 1.4.13).
TIP_JS = """<script>
const glOf=e=>e.target.closest&&e.target.closest('.gl');
const place=g=>{const t=g.querySelector('.gl-tip'),w=g.closest('.table-wrap'),b=w?w.getBoundingClientRect():{left:0,right:document.documentElement.clientWidth};t.style.left='0';t.style.display='block';const r=t.getBoundingClientRect(),over=r.right-b.right+8;if(over>0)t.style.left=-Math.min(over,r.left-b.left-8)+'px';t.style.display=''};
for(const ev of ['mouseover','focusin'])document.addEventListener(ev,e=>{const g=glOf(e);if(g)place(g)});
document.addEventListener('keydown',e=>{if(e.key==='Escape')document.querySelectorAll('.gl:hover,.gl:focus-within').forEach(g=>g.classList.add('off'))});
const reset=e=>{const g=glOf(e);if(g&&(e.type==='focusout'||e.target===g))g.classList.remove('off')};
document.addEventListener('mouseleave',reset,true);document.addEventListener('focusout',reset);
</script>"""


def header(web):
    link = (f'<a href="{PDF_NAME}">{icon("download-simple")}PDF herunterladen</a>' if web else "")
    return (f'<header class="top"><h1>{TITLE}</h1><p class="sub">{SUB}</p>'
            f'<div class="meta"><span>{STAND}</span>{link}</div></header>')


def head(css):
    return (f'<!doctype html>\n<html lang="de"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{TITLE}</title><meta name="description" content="{SUB}">'
            f'<style>{css}</style></head>')


def build_web(html):
    soup = frag(html)
    dress(soup, "web")
    glossary_tips(soup)
    for t in soup.find_all("table"):
        t.wrap(soup.new_tag("div", attrs={"class": "table-wrap"}))
    notes = soup.find(["section", "aside"], class_="footnotes")
    if notes:
        h = soup.new_tag("h2", id="belege")
        h.string = "Anmerkungen und Belege"
        notes.insert(0, h)
        for ref in soup.find_all("a", class_="footnote-ref"):
            li = notes.find("li", id=ref["href"][1:])
            if li:
                ref["title"] = li.get_text(" ", strip=True).replace("↩︎", "").strip()
    nav = soup.find("nav", id="TOC").extract()
    page = (head(CSS_WEB) + '<body><div class="wrap">' + header(True) + str(nav)
            + '<article class="col">' + str(soup) + "</article>"
            + f'<footer class="col">{TITLE} · {STAND}</footer></div>{TIP_JS}</body></html>')
    (OUT / "index.html").write_text(page)


def build_print(html):
    soup = frag(html)
    dress(soup, "print")
    notes = soup.find(["section", "aside"], class_="footnotes")
    for ref in soup.find_all("a", class_="footnote-ref"):
        li = notes.find("li", id=ref["href"][1:])
        for back in li.find_all("a", class_="footnote-back"):
            back.decompose()
        inner = "".join(str(c) for p in li.find_all("p") for c in p.contents).strip()
        ref.replace_with(frag(f'<span class="fn">{inner}</span>'))
    notes.decompose()
    nav = soup.find("nav", id="TOC").extract()
    page = head(CSS_PRINT) + '<body><div class="col">' + header(False) + str(nav) + str(soup) + "</div></body></html>"
    from weasyprint import HTML
    HTML(string=page, base_url=str(OUT)).write_pdf(OUT / PDF_NAME)
    if "--keep-print-html" in sys.argv:
        (OUT / "print.html").write_text(page)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    h = pandoc()
    build_web(h)
    if "--web-only" not in sys.argv:
        build_print(h)
    print("ok:", OUT / "index.html", "|", OUT / PDF_NAME)
