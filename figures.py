"""Grafiken als SVG. Breite 520 = Textspalte. web: Farben ueber CSS-Variablen, print: feste Farben."""
import math
from datetime import date

PRINT = dict(ink="#1c1d21", quiet="#5d6168", grid="#e3e0d8", axis="#b1ada2", muted="#a9a59a",
             accent="#1f5fa8", navy="#183a5a", white="#ffffff")
FONT = "'Barlow Condensed', 'Arial Narrow', sans-serif"


class Pen:
    def __init__(self, mode):
        self.mode = mode

    def c(self, fill=None, stroke=None, sw=None, dash=None, op=None):
        bits = []
        if self.mode == "web":
            st = []
            if fill:
                st.append("fill:none" if fill == "none" else f"fill:var(--c-{fill})")
            if stroke:
                st.append(f"stroke:var(--c-{stroke})")
            if st:
                bits.append(f'style="{";".join(st)}"')
        else:
            if fill:
                bits.append(f'fill="{"none" if fill == "none" else PRINT[fill]}"')
            if stroke:
                bits.append(f'stroke="{PRINT[stroke]}"')
        if sw:
            bits.append(f'stroke-width="{sw}"')
        if dash:
            bits.append(f'stroke-dasharray="{dash}"')
        if op is not None:
            bits.append(f'fill-opacity="{op}"')
        return " ".join(bits)

    def t(self, x, y, s, size=12.5, col="ink", w=500, anchor="start"):
        return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{w}" '
                f'text-anchor="{anchor}" {self.c(fill=col)}>{s}</text>')


def svg_open(w, h, label):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}" font-family="{FONT}" '
            f'xmlns="http://www.w3.org/2000/svg">')


def wege(mode):
    p = Pen(mode)
    x0, cw, gap, by, bh, fy, fh = 8, 160, 12, 46, 92, 172, 62
    px = lambda i: x0 + i * (cw + gap)
    o = [svg_open(520, 246, "Drei Wege zur Information, ein gemeinsames Fundament")]
    o.append(p.t(8, 24, "Drei Wege zur Information, ein gemeinsames Fundament", 16, w=600))
    cols = [("1  Externe Suche", "Google, ChatGPT und andere", "Crawler lesen die Website", "Modell: Anbieter"),
            ("2  Auskunft auf der Website", "Suchfeld, Antwortfeld", "RAG, öffentliche Inhalte", "Modell: Stadt"),
            ("3  Interne Assistenz", "Beschäftigte fragen", "RAG, interne Dokumente", "Modell: Stadt, mit Rechten")]
    for i, (name, a, b, q) in enumerate(cols):
        x = px(i)
        o.append(f'<rect x="{x}" y="{by}" width="{cw}" height="{bh}" {p.c(fill="none", stroke="axis", sw=1.2)}/>')
        o.append(p.t(x + 10, by + 22, name, 14, w=600))
        o.append(p.t(x + 10, by + 42, a))
        o.append(p.t(x + 10, by + 58, b))
        o.append(p.t(x + 10, by + 78, q, col="quiet"))
        cx = x + cw / 2
        o.append(f'<path d="M{cx} {by + bh}V{fy - 7}" {p.c(fill="none", stroke="axis", sw=1.2)}/>')
        o.append(f'<path d="M{cx - 5} {fy - 9}L{cx} {fy - 1}L{cx + 5} {fy - 9}z" {p.c(fill="axis")}/>')
    o.append(f'<rect x="8" y="{fy}" width="504" height="{fh}" {p.c(fill="navy")}/>')
    o.append(p.t(260, fy + 27, "Fundament: gepflegte, strukturierte, aktuelle Inhalte", 16, col="white", w=600, anchor="middle"))
    o.append(p.t(260, fy + 47, "Leistungen, Satzungen, Termine, Zuständigkeiten, Ratsunterlagen", 13, col="white", anchor="middle"))
    o.append("</svg>")
    return "\n".join(o)


def preise(mode):
    p = Pen(mode)
    d = lambda s: date.fromisoformat(s).toordinal()
    t0, t1 = d("2021-07-01"), d("2026-01-01")
    X = lambda s: 60 + (d(s) - t0) / (t1 - t0) * 410
    Y = lambda v: 276 - (math.log10(v) + 2) / 4 * 200
    fmt = lambda v: (f"{v:,.2f}".rstrip("0").rstrip(".").replace(".", ",")) + " $"
    o = [svg_open(520, 310, "GPT-4-Leistung kostete 2025 ein Zweihundertstel des Preises von 2023")]
    o.append(p.t(8, 22, "GPT-4-Leistung kostete 2025 ein Zweihundertstel des Preises von 2023", 16, w=600))
    o.append(p.t(8, 42, "Preis pro 1 Mio. Token bei gleicher Testleistung (MMLU), logarithmische Skala", 12.5, col="quiet"))
    for v in (0.01, 0.1, 1, 10, 100):
        o.append(f'<line x1="60" x2="512" y1="{Y(v):.1f}" y2="{Y(v):.1f}" {p.c(stroke="grid")}/>')
        o.append(p.t(52, Y(v) + 4, fmt(v), col="quiet", anchor="end"))
    for yr in (2022, 2023, 2024, 2025):
        x = X(f"{yr}-01-01")
        o.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="276" y2="282" {p.c(stroke="axis")}/>')
        o.append(p.t(x, 298, str(yr), col="quiet", anchor="middle"))
    g3 = (("2021-11-01", 60, "GPT-3"), ("2024-11-01", 0.06, "Llama 3.2 3B"))
    g4 = (("2023-03-01", 37.5, "GPT-4"), ("2025-02-01", 0.18, "Gemini 2.0 Flash"))
    for (a, b), col, tcol, w in ((g3, "muted", "quiet", 500), (g4, "accent", "ink", 600)):
        xa, ya, xb, yb = X(a[0]), Y(a[1]), X(b[0]), Y(b[1])
        o.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" {p.c(stroke=col, sw=2.5)}/>')
        for x, y in ((xa, ya), (xb, yb)):
            o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" {p.c(fill=col)}/>')
        fac = f"{round(a[1] / b[1]):,}".replace(",", ".")
        # Endpunkt-Labels zweizeilig rechts vom Punkt, damit sie keine Linie kreuzen
        if col == "muted":
            o.append(p.t(xa + 8, ya - 8, f"{a[2]}: {fmt(a[1])}", col=tcol))
            o.append(p.t(xb + 9, yb + 4, b[2], col=tcol))
            o.append(p.t(xb + 9, yb + 18, fmt(b[1]), col=tcol))
            o.append(p.t((xa + xb) / 2 - 10, (ya + yb) / 2 + 30, f"GPT-3-Niveau: ÷ {fac}", col=tcol, anchor="end"))
        else:
            o.append(p.t(xa + 8, ya - 8, f"{a[2]}: {fmt(a[1])}", col=tcol, w=w))
            o.append(p.t(xb + 9, yb - 14, b[2], col=tcol, w=w))
            o.append(p.t(xb + 9, yb, fmt(b[1]), col=tcol, w=w))
            o.append(p.t((xa + xb) / 2 + 12, (ya + yb) / 2 - 8, f"GPT-4-Niveau: ÷ {fac}", col=tcol, w=w))
    o.append("</svg>")
    return "\n".join(o)


REG = [
    ("gilt", "2025-02-02", "KI-Verbote, Pflicht zur KI-Kompetenz"),
    ("gilt", "2025-08-02", "Pflichten für Basismodelle"),
    ("gilt", "2025-09-12", "Data Act: Wechsel des Cloud-Anbieters"),
    ("gilt", "2026-07-27", "KI-Omnibus: Fristen verschoben"),
    ("gilt", "2026-07-28", "KI-MIG: Aufsicht Bundesnetzagentur"),
    ("gilt", "2026-08-02", "Kennzeichnung von KI-Inhalten"),
    ("gilt", "2026-09-11", "CRA: Hersteller melden Lücken"),
    ("kommt", "2027-12-02", "Hochrisiko-KI, Anhang III"),
    ("kommt", "2027-12-11", "Cyber Resilience Act vollständig"),
    ("kommt", "2028-08-02", "Hochrisiko-KI, Anhang I"),
    ("verf", "2025-11-19", "Digital-Omnibus Daten (DSGVO)"),
    ("verf", "2026-06-03", "Cloud and AI Development Act"),
    ("verf", "2026-09-09", "EU-Vergaberecht mit Europa-Präferenz"),
]


def regulierung(mode, stand="2026-10-25"):
    p = Pen(mode)
    d = lambda s: date.fromisoformat(s).toordinal()
    lo, hi = d("2025-01-01"), d("2028-10-01")
    L, R = 206, 512
    X = lambda s: L + (d(s) - lo) / (hi - lo) * (R - L)
    gi = {"gilt": 0, "kommt": 1, "verf": 2}
    Y = lambda i, g: 104 + 23 * i + 30 * gi[g]
    mo = lambda s: f"{s[5:7]}/{s[2:4]}"
    xn = X(stand)
    o = [svg_open(520, 480, "Die KI-Regeln gelten, Fristen und Gesetze sind noch in Bewegung")]
    o.append(p.t(8, 22, "Die KI-Regeln gelten, Fristen und Gesetze sind noch in Bewegung", 16, w=600))
    o.append(p.t(8, 42, "EU- und Bundesregeln mit Bezug zu kommunaler KI und Websites", 12.5, col="quiet"))
    for yr in (2025, 2026, 2027, 2028):
        x = X(f"{yr}-01-01")
        o.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="72" y2="448" {p.c(stroke="grid")}/>')
        o.append(p.t(x + 3, 66, str(yr), col="quiet"))
    o.append(f'<line x1="{L}" x2="{R}" y1="72" y2="72" {p.c(stroke="axis", sw=1.2)}/>')
    heads = {"gilt": "Gilt bereits", "kommt": "Kommt", "verf": "Im Verfahren"}
    seen = set()
    for i, (g, dt, name) in enumerate(REG):
        y = Y(i, g)
        if g not in seen:
            seen.add(g)
            o.append(p.t(8, y - 20, heads[g].upper(), 11.5, col="quiet", w=600))
        o.append(p.t(8, y + 4, name, 13))
        x = X(dt)
        if g == "verf":
            o.append(f'<rect x="{x:.1f}" y="{y - 7}" width="{R - x:.1f}" height="14" '
                     f'{p.c(fill="muted", stroke="muted", dash="3 3", op=0.22)}/>')
            o.append(p.t(R - 6, y + 4, f"vorgeschlagen {mo(dt)}", 11.5, anchor="end"))
            continue
        o.append(f'<line x1="{L}" x2="{x:.1f}" y1="{y}" y2="{y}" {p.c(stroke="grid")}/>')
        fill = "muted" if g == "gilt" else "none"
        o.append(f'<path d="M{x:.1f} {y - 5.5}l5.5 5.5l-5.5 5.5l-5.5 -5.5z" {p.c(fill=fill, stroke="muted", sw=1.4)}/>')
        left = x > R - 34 or (g == "gilt" and 0 < xn - x < 40)
        o.append(p.t(x - 9 if left else x + 9, y + 4, mo(dt), 11.5, col="quiet", anchor="end" if left else "start"))
    o.append(f'<line x1="{xn:.1f}" x2="{xn:.1f}" y1="72" y2="448" {p.c(stroke="accent", sw=1.5, dash="4 3")}/>')
    o.append(p.t(xn, 466, "Stand " + f"{stand[8:10]}.{stand[5:7]}.{stand[0:4]}", 12, col="accent", w=600, anchor="middle"))
    o.append("</svg>")
    return "\n".join(o)


FIGS = {
    "wege": (wege, "Eigene Darstellung."),
    "preise": (preise, "Quellen: a16z, LLMflation (GPT-3-Niveau); Epoch AI (GPT-4-Niveau). Listenpreise pro 1 Mio. Token."),
    "regulierung": (regulierung, "Quellen: Amtsblatt der EU, EU-Kommission, BGBl. 2026 I Nr. 223. Stand 25.10.2026."),
}
