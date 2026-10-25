---
title: Internet im Wandel
subtitle: Trends seit 2010 und Folgen für Kommunen und Behörden
date: Stand 25. Oktober 2026
lang: de
---

## Einleitung {#einleitung}

Das Papier beschreibt, wie sich die Nutzung von Websites und die Entwicklung von Software seit etwa 2010 verändert haben und was daraus für Städte mit 15.000 bis 40.000 Einwohnern in Bayern folgt. Jedes Kapitel stellt einen Trend dar und endet mit einem Kasten zu den Folgen für kleine Kommunen ([+]{.pro} Vorteil, [−]{.con} Nachteil, [→]{.rec} Empfehlung). Randnotizen übertragen einzelne Punkte auf Moosburg. Fachbegriffe erklärt das [Glossar](#glossar).

::: {.folgen title="Auf einen Blick"}
- [→]{.rec} Informationen werden häufiger über Suchmaschinen und KI-Antworten gefunden als direkt auf Websites. Wirksam ist, was dort gefunden wird: gepflegte, strukturierte Inhalte.
- [→]{.rec} Der Preis für KI-Leistung fällt um ein Vielfaches pro Jahr, und Softwarehersteller bauen ihre Preismodelle um. Verträge sollten sinkende Preise weitergeben können.
- [→]{.rec} Für Auskunft und Entwürfe reichen offene Modelle und Bausteine, die andere Verwaltungen bereits einsetzen. Sie lassen sich nachnutzen und selbst betreiben.
- [→]{.rec} Die Regeln für KI, Cloud und Beschaffung ändern sich bis 2028 mehrfach.
- [→]{.rec} Aufbereitete Daten nützen jeder späteren KI-Lösung, ob gekauft oder selbst gebaut.
:::

### Drei Wege zur Information {#drei-wege}

In Debatten über KI werden drei Wege vermischt, auf denen Menschen an Informationen kommen. Technisch hängen sie kaum voneinander ab, alle drei brauchen aber dieselbe Datengrundlage.

FIGURE:wege

1. **Externe Suche und [KI-Suche](#g-kisuche).** Menschen fragen Google, ChatGPT oder Perplexity. Deren [Crawler](#g-crawler) lesen öffentliche Websites. Ob der Betreiber einer Website selbst ein [Sprachmodell](#g-llm) einsetzt, spielt dafür keine Rolle. Er beeinflusst Inhalt, Struktur und Aktualität seiner Seiten.
2. **Auskunft auf der eigenen Website.** Ein Such- oder Antwortfeld auf der Website. Modell und Betrieb wählt der Betreiber. Datenbasis sind dieselben öffentlichen Inhalte wie bei Weg 1.
3. **Interne Assistenz.** Beschäftigte durchsuchen Dienstanweisungen, Satzungen, Ratsunterlagen und Akten oder lassen Entwürfe vorbereiten. Dazu kommen Zugriffsrechte, personenbezogene Daten und Protokollierung.

Für Weg 1 braucht eine Organisation kein eigenes Modell. Bei Weg 2 und 3 lässt sich das Modell austauschen, die aufbereiteten Daten bleiben.

### Anwendungsfälle {#anwendungsfaelle}

| Anwendungsfall | Beispiel | Datenbasis | Hauptrisiko |
|----------|----------------|--------------|------------|
| Auskunft für Bürger | „Wann ist Sperrmüll in der Altstadt?“ | Website, Leistungsbeschreibungen, Abfallkalender | Falsche oder veraltete Auskunft |
| Auskunft intern | „Welche Wertgrenze gilt für Direktaufträge?“ | Dienstanweisungen, Satzungen, Beschlüsse | Zugriff ohne Berechtigung |
| Dokumente befüllen | Bescheid-Entwurf, Sitzungsvorlage, Antwort auf Bürgeranfrage | Vorlagen und Fallakte | Personenbezogene Daten, ungeprüfte Übernahme |
| Zusammenfassen, übersetzen | Protokoll, Leichte Sprache, mehrsprachige Hinweise | Vorhandener Text | Sinnverschiebung |

Auskunft ist im Kern eine Suche, das Modell formuliert nur das Ergebnis. Beim Befüllen von Dokumenten schreibt das Modell innerhalb eines Verwaltungsprozesses. Anbieter verkaufen beides oft als ein Produkt „KI-Assistent“, obwohl Daten, Rechte und Prüfschritte verschieden sind.

## Websites als Zugang zu Diensten {#serviceportal}

Im September 2026 kamen 61 % des Webverkehrs in Deutschland von Mobilgeräten.^[StatCounter: [Desktop vs Mobile Market Share Germany](https://gs.statcounter.com/platform-market-share/desktop-mobile/germany), September 2026.] 2013 nutzten erst 41 % der Deutschen ein Smartphone zum Surfen.^[ARD/ZDF-Onlinestudie 2013, nach [schieb.de](https://www.schieb.de/723141/41-prozent-der-deutschen-surfen-mit-dem-smartphone).] Im selben Zeitraum haben sich die Websites von Banken, Händlern und Behörden von Informationsseiten zu Zugängen für Dienste entwickelt.

In der Verwaltung regelt das Onlinezugangsgesetz diesen Wandel. Seine Änderung von 2024 hat die alte Umsetzungsfrist gestrichen und führt ab 2029 einen Rechtsanspruch auf digitalen Zugang zu Bundesleistungen ein.^[GvW: [OZG 2.0 in Kraft getreten](https://www.gvw.com/aktuelles/blog/detail/update-endlich-verfuegbar-ozg-20-in-kraft-getreten), 2024.] Anfang 2026 waren bundesweit 823 von 7.509 Einzelleistungen flächendeckend online, Bayern lag mit 19 % auf Platz drei der Länder.^[IW Köln: [Behörden-Digimeter 2026](https://www.iwkoeln.de/studien/klaus-heiner-roehl-jan-buechel-clemens-fabian-gruben-behoerden-digimeter-2026.html), 12.03.2026. Die Staatsregierung kommt mit anderer Zählweise auf über 1.600 Leistungen.]

::: {.beiuns}
Den Erklärtext zur Hundesteuer muss die Stadt nicht selbst schreiben. Er kommt per Schnittstelle aus dem BayernPortal, ergänzt werden nur Steuersatz, Ansprechperson und Öffnungszeiten.
:::

In Bayern stellt der Freistaat vieles zentral bereit: das BayernPortal mit Leistungsbeschreibungen und Online-Anträgen, die BayernID mit rund einer Million aktiven Konten (2024)^[[Macwelt](https://www.macwelt.de/article/2288811/bayern-id-konflikt-zwischen-sicherheit-und-komfort.html), 12.04.2024.] und Schnittstellen, über die Kommunen die Leistungsbeschreibungen auf ihrer Website anzeigen können.^[StMI: [Nutzungsbedingungen für Webservice-Schnittstellen](https://www.baybw-services.bayern.de/documents/Nutzungsbedingungen_für_Webservice-Schnittstellen.pdf), 2017.]

Öffentliche Websites müssen barrierefrei sein. In Bayern gilt dafür die BITV 2.0, dazu kommt eine jährlich geprüfte Erklärung zur Barrierefreiheit.^[[Bayerische Digitalverordnung](https://www.gesetze-bayern.de/Content/Pdf/BayDiV?all=True), §§ 9 bis 11.] In den Stichproben der Überwachungsstelle erfüllte 2023 und 2024 keine geprüfte Website die Vorgaben vollständig.^[Bayerischer Landtag: [Drs. 19/4712](https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Schriftliche%20Anfragen/19_0004712.pdf), 03.03.2025.] Seit Juni 2025 gelten vergleichbare Pflichten nach dem Barrierefreiheitsstärkungsgesetz auch für viele private Anbieter.^[IHK Karlsruhe: [Barrierefreiheitsstärkungsgesetz](https://www.ihk.de/karlsruhe/fachthemen/recht/internetrecht/fallback1433495812828/bfsg-6348406).]

::: {.folgen}
- [+]{.pro} Leistungsbeschreibungen, Online-Anträge und Login liefert das Land. Die Stadt bindet sie ein.
- [+]{.pro} Gut gebaute Seiten erfüllen mobile Nutzung und Barrierefreiheit zugleich.
- [−]{.con} Die Website verweist auf viele Portale: BayernPortal, Ratsinformationssystem, Abfall-App, Stellenportal. Ohne klare Struktur verlieren Nutzer den Überblick.
- [−]{.con} Barrierefreiheit ist Pflicht und wird geprüft. Baukastensysteme erfüllen sie nicht automatisch.
- [→]{.rec} Lokale Inhalte selbst pflegen, Landesdienste per Schnittstelle einbinden, nichts doppelt.
:::

## Statische Websites {#statisch}

Unter den 10.000 meistbesuchten Websites nutzten 2024 über 12 % vorgerenderte oder hybride Ansätze, 67 % mehr als im Vorjahr.^[HTTP Archive: [Web Almanac 2024, Jamstack](https://almanac.httparchive.org/en/2024/jamstack).] Bei einer statischen Website werden die Seiten bei jeder Änderung einmal erzeugt und als fertige Dateien ausgeliefert. Beim Abruf laufen weder Programmcode noch Datenbank. Die Redaktion arbeitet in einem getrennten Redaktionssystem, das nicht öffentlich erreichbar sein muss ([Headless CMS](#g-headless)).

In der Breite überwiegen klassische Systeme. Gut die Hälfte aller Websites nutzt ein CMS, WordPress allein rund 35 %, mit leicht sinkendem Anteil.^[HTTP Archive: [Web Almanac 2025, CMS](https://almanac.httparchive.org/de/2025/cms).]

Seiten aus statischen Generatoren wie Hugo hatten in den Messungen des HTTP Archive die besten Ladezeit-Kennzahlen und waren etwa halb so groß wie Seiten mit JavaScript-Frameworks.^[HTTP Archive: [Web Almanac 2021, Jamstack](https://almanac.httparchive.org/en/2021/jamstack).] Die Auslieferung über ein [Content-Delivery-Netz](#g-cdn) ist günstig und hält Lastspitzen aus. Serverseitige Sicherheitslücken wie die in PHP im Oktober 2026 (Kapitel [Betrieb und Sicherheit](#sicherheit)) betreffen statisch ausgelieferte Seiten nicht.

Öffentliche Stellen setzen ebenfalls darauf. Die US-Bundesverwaltung betreibt mit cloud.gov Pages eine Plattform für statische Websites, die Dutzende Behörden nutzen. Der Betreiber nennt als Gründe weniger Schwachstellen, nutzungsabhängige Kosten und Reserven für Lastspitzen.^[cloud.gov: [Why use Pages](https://docs.cloud.gov/pages/using-pages/why-use-pages); [cloud.gov Pages](https://cloud.gov/pages/).] Die Website digital.gov erzeugt rund 10.000 Seiten mit Hugo in etwa einer halben Minute.^[GSA: [digital.gov Platform](https://github.com/GSA/digitalgov.gov/wiki/digital.gov-Platform).] GOV.UK hält eine statische Kopie bereit, auf die bei Störungen automatisch umgeschaltet wird.^[GOV.UK Developer Docs: [Fall back to the static mirror](https://docs.publishing.service.gov.uk/manual/fall-back-to-mirror.html), 12.02.2026.]

::: {.folgen}
- [+]{.pro} Sicherheit, kurze Ladezeiten, geringe Hostingkosten, Stabilität unter Last.
- [+]{.pro} Inhalte liegen als strukturierte Dateien vor, versioniert und maschinenlesbar, direkt nutzbar für Suche und KI-Auskunft.
- [−]{.con} Formulare, Suche oder Login brauchen Zusatzdienste.
- [−]{.con} Die Redaktion braucht eine bequeme Oberfläche, sonst fehlt die Akzeptanz im Haus.
- [→]{.rec} Statisch ausliefern, getrennt redigieren, Anträge über das BayernPortal verlinken.
:::

## Suche und KI-Antworten {#suche}

Die Hälfte der deutschen Internetnutzer verwendet zumindest gelegentlich KI-Chats statt klassischer Suche.^[Bitkom: [Internet-Suche im Wandel](https://www.bitkom.org/Presse/Presseinformation/Internet-Suche-Wandel-Haelfte-nutzt-KI-Chats), 20.11.2025.] Google zeigt seit März 2025 auch in Deutschland KI-Übersichten über den Suchergebnissen, seit Oktober 2025 zusätzlich einen KI-Modus.^[[t3n](https://t3n.de/news/?p=1679953), 26.03.2025; [onlinemarketing.de](https://onlinemarketing.de/technologie/google-search-ai-mode-startet-in-deutschland), 08.10.2025.]

Websites erhalten dadurch noch weniger Besuche aus der Suche. Schon 2024, vor den KI-Übersichten, endeten in der EU 60 % der Google-Suchen ohne Klick. Auf 1.000 Suchen kamen 374 Klicks auf Websites außerhalb von Google.^[SparkToro/Datos: [2024 Zero-Click Search Study](https://sparktoro.com/blog/2024-zero-click-search-study-for-every-1000-us-google-searches-only-374-clicks-go-to-the-open-web-in-the-eu-its-360/), 01.07.2024.] Erscheint eine KI-Zusammenfassung, klicken Nutzer nur noch in 8 statt 15 % der Fälle auf ein Ergebnis.^[Pew Research Center: [Google users are less likely to click on links when an AI summary appears](https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/), 22.07.2025, US-Daten.] Bei Verwaltungsfragen beginnt gut die Hälfte der Deutschen bei einer Suchmaschine, rund ein Drittel geht direkt auf die Seite der eigenen Stadt oder Gemeinde.^[Initiative D21: [eGovernment MONITOR 2025](https://initiatived21.de/uploads/03_Studien-Publikationen/eGovernment-MONITOR/2025/eGovMon2025_final.pdf). 51 % beginnen bei einer Suchmaschine, 42 % auf Behördenseiten, davon 78 % auf der Seite der eigenen Kommune.]

::: {.beiuns}
Jemand fragt Gemini, ob er in Moosburg eine Gartenhütte aufstellen darf. Steht auf der Stadtseite strukturiert, dass Gebäude bis 75 m³ außerhalb des Außenbereichs verfahrensfrei sind ([Art. 57 BayBO](https://www.gesetze-bayern.de/Content/Document/BayBO-57)), der Bebauungsplan aber gilt und Herr Graßl im Bauamt zuständig ist, nennt die Antwort genau das, mit Durchwahl. Steht es nur in einem alten PDF, rät die KI.
:::

2026 nutzen 37 % der Deutschen KI-Werkzeuge wöchentlich, 2025 waren es 22 %. Bei den 14- bis 29-Jährigen sind es 68 %, ab 70 Jahren 8 %.^[ARD/ZDF-Medienstudie 2026, nach [ZDFheute](https://www.zdfheute.de/wissen/ard-zdf-medienstudie-2026-ki-tools-streaming-100.html), 22.09.2026.]

Gartner sagte 2024 voraus, dass das Volumen klassischer Suchmaschinen bis 2026 um 25 % sinkt.^[Gartner, nach [Slashdot](https://search.slashdot.org/story/24/03/04/170221/gartner-predicts-search-engine-volume-will-drop-25-by-2026-due-to-ai-chatbots-and-other-virtual-agents), 04.03.2024, und [Big Technology](https://www.bigtechnology.com/p/will-search-engine-traffic-really), 15.03.2024.] Google meldet dagegen ein Allzeithoch bei den Suchanfragen und über eine Milliarde monatliche Nutzer des KI-Modus.^[Google: [Q2 2026 earnings call](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q2-2026/), 22.07.2026.] Eigenständige KI-Werkzeuge machten Anfang 2026 in Europa weniger als 2 % der Suchvorgänge am Desktop aus.^[Datos, nach [PPC Land](https://ppc.land/ai-still-under-2-but-growing-datos-q1-2026-state-of-search-report/), 27.04.2026.] Die Zahl der Suchanfragen steigt also, die Zahl der Klicks auf Websites sinkt.

Die Antwort formuliert ein Modell des Suchanbieters auf Grundlage der Inhalte, die es auf Websites findet. Google verlangt dafür nach eigener Aussage keine besonderen Dateien oder Auszeichnungen, die üblichen Regeln für gut auffindbare Seiten gelten weiter.^[Google Search Central: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features), 10.12.2025.] Die vorgeschlagene Datei llms.txt für Sprachmodelle wertet Google Search nicht aus.^[Google Search Central: [Optimizing for Generative AI Features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide), 10.07.2026.] Von 137.000 untersuchten Websites hatten 28 % eine solche Datei, 97 % davon wurden im Mai 2026 kein einziges Mal abgerufen.^[Ahrefs: [We Analyzed 137K Sites](https://ahrefs.com/blog/llmstxt-study/), 15.06.2026.]

::: {.folgen}
- [+]{.pro} Die Stadt erreicht Menschen dort, wo sie fragen, ohne eigenes KI-Projekt.
- [+]{.pro} Gute Inhalte wirken für klassische Suche und KI-Antworten gleichermaßen.
- [−]{.con} Die Website wird seltener besucht. Aktuelle Hinweise werden seltener gesehen, Seitenaufrufe taugen kaum noch als Erfolgsmaß.
- [−]{.con} Die Formulierung liegt beim Anbieter. Veraltete oder widersprüchliche Inhalte werden weitergegeben.
- [→]{.rec} Korrekte, aktuelle, [strukturierte](#g-struktur) Inhalte sind die Voraussetzung für jede KI-Auskunft, fremde wie eigene. Die Seite muss weiterhin klassisch bedienbar bleiben, auch für ältere Menschen.
:::

## Datenqualität und Struktur {#daten}

Gartner erwartet, dass Organisationen bis Ende 2026 60 % ihrer KI-Projekte aufgeben, für die keine KI-tauglichen Daten vorliegen. 63 % der Organisationen haben keine passenden Verfahren für ihre Daten oder wissen es nicht.^[Gartner: [Lack of AI-Ready Data Puts AI Projects at Risk](https://www.gartner.com/en/newsroom/press-releases/2025-02-26-lack-of-ai-ready-data-puts-ai-projects-at-risk), 26.02.2025.] Wie sich ungeordnete Daten auswirken, zeigt Microsoft 365 Copilot. Der Assistent übernimmt die bestehenden Zugriffsrechte und damit jede zu weit gefasste Freigabe. Zwei Drittel von 279 befragten Microsoft-365-Verantwortlichen haben die Einführung deshalb verschoben oder gestoppt, 73 % befürchten, dass vertrauliche Inhalte offengelegt werden.^[CoreView: [State of Microsoft 365 Security and Governance 2026](https://www.coreview.com/news/66-percent-of-enterprises-delay-microsoft-copilot), 21.07.2026.]

Aufbereitete Daten bedeuten für eine Stadtverwaltung Zuständigkeiten als Datensätze statt als Fließtext, Leistungen mit Standardtext aus dem Landesportal und lokalen Angaben, Satzungen als Text statt als Scan und Termine mit Datum und Ort in eigenen Feldern. Zu jedem Eintrag gehören Stand, Quelle und Sichtbarkeit. Ein Musterdatensatz für die Gartenhütte:

| Feld | Inhalt | Zweck |
|------|--------|-------|
| Leistung | Verfahrensfreies Bauvorhaben (Gartenhütte, Geräteschuppen) | Verknüpfung mit dem BayernPortal |
| Rechtsgrundlage | Art. 57 Abs. 1 Nr. 1a BayBO | Quelle, die jede Antwort nennen kann |
| Lokale Regeln | Bebauungsplan des jeweiligen Gebiets, soweit vorhanden | Antwort nennt nicht nur Landesrecht |
| Zuständige Stelle | Stadtbauamt, SG 20 Stadtbau- und Planungsamt | Rolle statt Person, übersteht Personalwechsel |
| Ansprechperson | Thomas Graßl, Tel. 08761 684-40, Vertretung Herbert Held, Tel. 08761 684-41 | Aus dem Telefonverzeichnis übernommen |
| Stand | 01.10.2026, geprüft von der Sachgebietsleitung | Veraltetes wird erkennbar |
| Sichtbarkeit | öffentlich | Steuert, wer die Information abfragen kann |

Ändert sich die Zuständigkeit, wird sie an einer Stelle geändert. Website, KI-Antwort und interne Assistenz übernehmen die Änderung gleichzeitig.

::: {.folgen}
- [+]{.pro} Datenarbeit hängt nicht vom Modell ab. Sie wirkt sofort bei Suchmaschinen und später in jeder KI-Lösung.
- [+]{.pro} Sie braucht Fachwissen aus der Verwaltung, keine KI-Spezialisten, und lässt sich mit eigenem Personal, Studierenden oder Ehrenamtlichen erledigen.
- [−]{.con} Sie bindet Zeit in den Fachämtern und ist nach außen wenig sichtbar.
- [−]{.con} Sie macht Widersprüche und veraltete Inhalte sichtbar.
- [→]{.rec} Inventur, Struktur, Zuständigkeitsdaten und die Umwandlung von PDFs in Text früh einplanen. Jede KI-Funktion baut darauf auf.
:::

## Wachstum von Open Source {#oss}

Auf GitHub arbeiten über 180 Millionen Entwickler, allein 2025 kamen 36 Millionen hinzu. In Deutschland hat sich ihre Zahl seit 2020 mehr als verdreifacht.^[GitHub: [Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/), 28.10.2025.] 73 % der Unternehmen in Deutschland setzen [Open Source](#g-oss) ein.^[Bitkom: [Open Source Monitor 2025](https://www.bitkom.org/Presse/Presseinformation/Open-Source), 17.09.2025.]

Wer selbst eine Website oder ein Werkzeug baut, fängt damit nicht bei null an. Für die meisten Funktionen gibt es gepflegte, frei nutzbare Komponenten, etwa Karten auf Basis von OpenStreetMap, Veranstaltungskalender, Volltextsuche, Prüfwerkzeuge für Barrierefreiheit und [Vektorsuche](#g-embedding). Testautomatisierung, Hosting für statische Seiten und automatische Sicherheitsupdates sind für öffentliche Projekte kostenlos.^[GitHub Docs: [About GitHub's security features](https://docs.github.com/en/code-security/getting-started/github-security-features).]

::: {.folgen}
- [+]{.pro} Die Bausteine sind frei verfügbar und werden von großen Communities gepflegt. Sicherheitslücken werden öffentlich gemacht und meist schnell geschlossen.
- [+]{.pro} Für verbreitete Bausteine gibt es viele Fachleute. Das erleichtert die Suche nach Helfern und einen späteren Wechsel des Dienstleisters.
- [−]{.con} Die Auswahl braucht Kompetenz. Bausteine, die mehrere Personen pflegen, sind verlässlicher als solche mit einem einzelnen Maintainer.
- [→]{.rec} Bei eigener Entwicklung auf verbreitete Bausteine setzen. In Ausschreibungen Open Source zulassen oder verlangen und den Pflegezustand (Aktivität, Releases, Community) bewerten.
:::

## Open Source in Verwaltungen {#oss-verwaltung}

Seit 2025 stellen Länder, Großstädte und Ministerien in mehreren europäischen Staaten auf Open Source um und begründen das mit Kosten und Unabhängigkeit. Der Freistaat Bayern hat im Juni 2026 einen geplanten Microsoft-Rahmenvertrag abgesagt.

| Wer | Was | Wann |
|--------|------------------------|----|
| Freistaat Bayern | Geplanten Microsoft-365-Vertrag über fünf Jahre abgesagt, stattdessen „souveräner Arbeitsplatz“. Die Lizenzkosten waren von rund 30 auf fast 50 Mio. Euro pro Jahr gestiegen.^[[netzpolitik.org](https://netzpolitik.org/2026/bayerischer-landtag-streit-um-microsoft-eskaliert/), 23.01.2026; [Borns IT-Blog](https://borncity.com/blog/2026/05/28/rueckzieher-microsoft-365-deal-in-bayern-wohl-gescheitert/), 28.05.2026; [it-daily](https://www.it-daily.net/?p=178346), 03.06.2026.] | 2026 |
| München | Neue Stadtratskoalition macht Open Source zum Standard bei der Beschaffung.^[[heise](https://heise.de/-11292449), Mai 2026.] | 2026 |
| Schweiz, Bundesverwaltung | Test von openDesk auf 3.000 von über 54.000 Arbeitsplätzen.^[[Computerworld](https://www.computerworld.com/article/4219743/swiss-authorities-want-to-replace-microsoft-365-with-open-source-software.html), 08.09.2026.] | 2026 |
| Bund | openDesk mit rund 8.800 Lizenzen, Rahmenvertrag mit der Bundeswehr.^[Deutscher Bundestag: [Drs. 21/5502](https://dserver.bundestag.de/btd/21/055/2105502.pdf), 22.04.2026.] | 2025/26 |
| Schleswig-Holstein | 40.000 Postfächer auf Open-Xchange und Thunderbird migriert, rund 80 % der Arbeitsplätze mit LibreOffice. Erwartet werden über 15 Mio. Euro weniger Lizenzkosten pro Jahr bei 9 Mio. Euro Einmalinvestition.^[[Land Schleswig-Holstein](https://www.schleswig-holstein.de/DE/landesregierung/ministerien-behoerden/I/_startseite/Artikel2025/IV/251006_ox-umstellung-abschluss.html), 06.10.2025; [heise](https://heise.de/-11105459).] | 2025 |
| Internationaler Strafgerichtshof | Ersetzt Microsoft durch openDesk.^[[netzpolitik.org](https://netzpolitik.org/2025/sorge-vor-us-sanktionen-internationaler-strafgerichtshof-kickt-microsoft-aus-seiner-verwaltung/), 31.10.2025.] | 2025 |
| Österreichisches Bundesheer | 16.000 Arbeitsplätze auf LibreOffice.^[[Borns IT-Blog](https://borncity.com/win/2025/09/21/austrian-armed-forces-goes-open-source-libreoffice/), 21.09.2025.] | 2025 |
| Dänemark | Digitalministerium wechselt zu Linux und LibreOffice, Aarhus hat begonnen, Kopenhagen prüft.^[[heise](https://heise.de/-10438942), Juni 2025.] | 2025 |
| Frankreich | Lyon wechselt zu OnlyOffice und Linux, kleine Gemeinden können eine staatliche Bürosuite nutzen.^[[Le Monde Informatique](https://www.lemondeinformatique.fr/actualites/lire-lyon-s-eloigne-de-microsoft-pour-prioriser-l-open-source-97235.html), 24.06.2025; [Banque des Territoires](https://www.banquedesterritoires.fr/face-laugmentation-des-licences-de-microsoft-la-bureautique-libre-pousse-son-avantage), 12.12.2025.] | 2025 |
| Dortmund | Ratsbeschluss „Open Source, wo möglich“, proprietäre Beschaffung muss begründet werden.^[[OSOR](https://interoperable-europe.ec.europa.eu/collection/open-source-observatory-osor/news/dortmund-goes-open-source-first), 03.05.2021.] | 2021 |

63 % der befragten Verwaltungen nutzen Open Source, 37 % haben eine Strategie dafür.^[Bitkom: [Open Source Monitor 2025, Studienbericht](https://www.bitkom.org/sites/main/files/2025-09/Bitkom-Studienbericht-Open-Source-Monitor-2025.pdf), September 2025.] München hatte LiMux 2017 per Ratsbeschluss zurückgenommen.^[[cybernews](https://cybernews.com/de/tech/muenchen-ersetzt-microsoft-durch-open-source/), 13.05.2026.]

Neben Büroanwendungen laufen auch Fachanwendungen und Bürgerdienste auf offener Software.

| Software | Zweck | Im Einsatz |
|----------|------------------|------------------|
| Masterportal | Geoportal für Karten und Geodaten, entwickelt in Hamburg, MIT-Lizenz^[OSGeo: [Masterportal](https://www.osgeo.org/projects/masterportal/), abgerufen Oktober 2026.] | München nutzt es und zahlt 10.000 Euro im Jahr in den gemeinsamen Entwicklungsfonds, Göttingen stellt sein Geoportal darauf um.^[Landeshauptstadt München: [GeoPortal](https://opensource.muenchen.de/software/geoportal.html), abgerufen Oktober 2026; FOSSGIS 2026: [Göttingen auf mehr als einen Blick](https://pretalx.com/fossgis2026/talk/FEQSAA/), 27.03.2026.] |
| Decidim | Bürgerbeteiligung mit Vorschlägen, Abstimmungen und Bürgerhaushalt, entstanden in Barcelona | Über 400 Institutionen in mehr als 30 Ländern.^[NGI: [Decidim](https://ngi.eu/impact-stories/collaborative-tools/decidim/), 17.10.2024.] |
| X-Road | Datenaustausch zwischen Behörden, Rückgrat der estnischen Verwaltung | 2,2 Mrd. Transaktionen im Jahr, seit 2018 mit Finnland verbunden.^[e-Estonia: [X-Road](https://e-estonia.com/solutions/interoperability-services/x-road/), abgerufen Oktober 2026.] |
| Matrix | Offener Standard für Messenger, jede Behörde betreibt ihren eigenen Server | Tchap für über 300.000 Beschäftigte des französischen Staates, BundesMessenger für Behörden in Deutschland.^[Element: [Matrix in Germany](https://element.io/matrix-in-germany/projects/bwmessenger), Herstellerangabe, abgerufen Oktober 2026.] |

::: {.folgen}
- [+]{.pro} Referenzen gibt es auf Bundes-, Landes- und Stadtebene, auch in Bayern.
- [+]{.pro} Die Einsparungen sind belegt, die Lizenzpreise großer Anbieter steigen.
- [−]{.con} Die Migration bestehender Arbeitsplätze kostet Geld und Schulung und braucht politischen Rückhalt, sonst wird sie wie LiMux zurückgenommen.
- [→]{.rec} Der günstigste Einstieg ist eine Neuvergabe, etwa die der Website.
:::

## Nachnutzung und Public Code {#nachnutzung}

Software, die mit öffentlichem Geld entsteht, soll öffentlich nachnutzbar sein ([Public Money, Public Code](#g-pmpc)). Die Verwaltungsplattform openCode zählt über 5.500 Projekte und 10.800 Nutzer, der Bund vergab 2025 knapp ein Viertel seiner Softwareentwicklungsaufträge als Open Source.^[Deutscher Bundestag: [Drs. 21/5502](https://dserver.bundestag.de/btd/21/055/2105502.pdf), 22.04.2026.] Der IT-Planungsrat hat im März 2026 mit dem Deutschland-Stack über 50 offene Standards festgelegt,^[[heise](https://heise.de/-11225804), März 2026.] die EU-Kommission im Juni 2026 eine Open-Source-Strategie beschlossen.^[EU-Kommission: [Strategy for EU Open Digital Ecosystems](https://commission.europa.eu/news-and-media/news/commission-boosts-open-and-interoperable-digital-ecosystems-public-administrations-2026-06-03_en), 03.06.2026.]

::: {.beiuns}
Einen KI-Assistenten muss niemand neu entwickeln. MUCGPT und BärGPT liegen offen vor und laufen in mehreren Städten. Was Moosburg daraus anpasst, kann jede andere Gemeinde im Landkreis Freising übernehmen.
:::

Wo Code offen liegt, wird er übernommen. Münchens KI-Assistent MUCGPT ist auf GitHub veröffentlicht und läuft in Stuttgart als „ChatSTR“.^[Landeshauptstadt München: [MUCGPT 2.0](https://stadt.muenchen.de/news/mucgpt-neue-version.html), 30.06.2026.] F13 aus Baden-Württemberg steht seit Juli 2025 als Open Source bereit.^[Staatsministerium Baden-Württemberg: [KI-Assistenz F13 wird zur Open-Source-Software](https://www.baden-wuerttemberg.de/de/service/presse/pressemitteilung/pid/ki-assistenz-f13-wird-zur-open-source-software), 23.07.2025.] Beim Programm „Einer für Alle“ bleibt die Nachnutzung laut IT-Planungsrat hinter den Erwartungen, wegen technischer, rechtlicher und finanzieller Hürden.^[IT-Planungsrat: [Abschlussbericht EfA-Finanzierung](https://www.it-planungsrat.de/fileadmin/beschluesse/2025/Beschluss_2025_51_Gemeinsame_EfA-Finanzierung_Abschlussbericht.pdf), 10.10.2025.]

::: {.folgen}
- [+]{.pro} Kosten teilen: Was eine Großstadt entwickelt, kann eine Kleinstadt anpassen.
- [+]{.pro} Der Code bleibt bei der Stadt, auch wenn der Dienstleister wechselt.
- [−]{.con} Nachnutzung braucht Dokumentation und eine verantwortliche Stelle.
- [→]{.rec} In jeden Entwicklungsauftrag: Quellcode unter offener Lizenz, Veröffentlichung auf openCode, Daten in offenen Formaten.
:::

## Digitale Souveränität {#souveraenitaet}

Im Juni 2025 erklärte ein Vertreter von Microsoft France unter Eid vor dem französischen Senat, er könne nicht garantieren, dass Daten nicht an US-Behörden gehen.^[Sénat: [Commission d'enquête commande publique](https://senat.fr/compte-rendu-commissions/20250609/ce_commande_publique.html), 10.06.2025.] Ein Gutachten der Universität Köln für das Bundesinnenministerium kommt zu dem Schluss, dass US-Recht wie der CLOUD Act den Zugriff auch auf Daten in EU-Rechenzentren erlaubt, selbst wenn eine deutsche Tochterfirma sie betreibt. Maßgeblich sei die Kontrolle über die Daten, nicht ihr Speicherort.^[[datenrecht.ch](https://datenrecht.ch/en/us-zugriffsbefugnisse-auf-daten-in-der-cloud-gutachten-uni-koeln-vom-maerz-2025/), 21.01.2026, zum Gutachten vom März 2025.] Beim Internationalen Strafgerichtshof war 2025 das Mailkonto des Chefanklägers nach US-Sanktionen nicht mehr nutzbar. Wer es gesperrt hat, ist umstritten.^[[Computerwoche](https://www.computerwoche.de/article/3989073/trump-befiehlt-microsoft-sperrt-e-mail-account.html), 19.05.2025.]

::: {.beiuns}
Läuft ein Antwortfeld über einen US-Anbieter, ist ein Zugriff von US-Behörden auf die Bürgerfragen nicht auszuschließen, auch wenn die Server in Europa stehen. Die Fragen enthalten oft Name, Adresse oder Lebenslage. Mit einem offenen Modell beim kommunalen Rechenzentrum oder einem europäischen Hoster bleibt die Kontrolle in Europa.
:::

Microsoft erhöht die Preise für Microsoft 365 ab Juli 2026, ausdrücklich auch für Behörden.^[Microsoft: [2026 Microsoft 365 Packaging and Pricing Updates FAQ](https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates-FAQ), 24.03.2026.] Die EU-Kommission hat im Juni 2026 mit dem Cloud and AI Development Act einen Rahmen vorgeschlagen, mit dem öffentliche Auftraggeber die Souveränität von Angeboten bewerten sollen.^[EU-Kommission: [Proposal for a Cloud and AI Development Act](https://digital-strategy.ec.europa.eu/en/library/proposal-cloud-and-ai-development-act-cada), 03.06.2026.] Nur 24 % der Verwaltungen haben ihre digitalen Abhängigkeiten vollständig analysiert.^[Bitkom: [Open Source Monitor 2025, Studienbericht](https://www.bitkom.org/sites/main/files/2025-09/Bitkom-Studienbericht-Open-Source-Monitor-2025.pdf).]

::: {.folgen}
- [+]{.pro} Wer Code und Daten besitzt, kann den Dienstleister wechseln. Das begrenzt Preiserhöhungen.
- [+]{.pro} Politische Risiken und einseitige Preisänderungen treffen eine Stadt mit Alternativen weniger.
- [−]{.con} Souveränität erfordert eigene Kompetenz oder einen Partner, der Betrieb ohne Lock-in anbietet.
- [→]{.rec} Vor jeder Vergabe klären: Wem gehören Code, Inhalte und Zugänge? Kann die Stadt kurzfristig samt Daten wechseln? Wo werden Anfragen verarbeitet?
:::

## KI in der Softwareentwicklung {#ki-entwicklung}

84 % der Entwickler nutzten 2025 KI-Werkzeuge oder planten es,^[Stack Overflow Developer Survey 2025, nach [InfoWorld](https://infoworld.com/article/4031673/ai-use-among-software-developers-grows-but-trust-remains-an-issue-stack-overflow-survey.html), 30.07.2025.] 2026 arbeiten zwei Drittel mit Coding-Agenten.^[Stack Overflow: [2026 Developer Survey](https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/), 06.10.2026.] Fast neun von zehn KI-Nutzern sparen nach eigener Angabe mindestens eine Stunde pro Woche, jeder Fünfte acht Stunden oder mehr.^[JetBrains: [State of Developer Ecosystem 2025](https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/), Oktober 2025.] Eine kontrollierte Studie fand 2025 bei erfahrenen Open-Source-Entwicklern dagegen eine Verlangsamung um 19 %.^[METR, nach [TechCrunch](https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows), 11.07.2025.] Laut DORA-Report geht KI-Nutzung mit schnellerer Auslieferung und geringerer Stabilität einher.^[Google Cloud: [2025 DORA Report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report), 23.09.2025.]

::: {.beiuns}
Ein Abfallkalender mit Erinnerung ist als Prototyp an einem Wochenende gebaut, eine Baustellenkarte auf OpenStreetMap in wenigen Tagen, ein Formularhelfer zum passenden Antrag im BayernPortal in etwa einer Woche (eigene Schätzung). Gepflegt werden sie über eine Tabelle mit Terminen, Baustellen oder Anträgen. Alle drei laufen als statische Seiten auf kostenlosem Hosting.
:::

Auch Menschen ohne Programmierausbildung bauen inzwischen Software. Die Plattform Lovable, auf der Anwendungen per Beschreibung entstehen, wird nach eigener Angabe zu 80 % von ihnen genutzt und setzt über 500 Mio. Dollar im Jahr um.^[[The Next Web](https://thenextweb.com/news/lovable-build-economy-500m-arr-vibe-coding), 09.06.2026.] In der Verwaltung nutzen erst 12 % KI in der Softwareentwicklung.^[Bitkom: [Open Source Monitor 2025, Studienbericht](https://www.bitkom.org/sites/main/files/2025-09/Bitkom-Studienbericht-Open-Source-Monitor-2025.pdf).]

::: {.folgen}
- [+]{.pro} IT-affine Beschäftigte, Ehrenamtliche und Studierende bauen Werkzeuge, für die früher eine Agentur nötig war.
- [+]{.pro} Prototypen entstehen in Tagen. Wer zuerst testet und dann vergibt, schreibt genauere und günstigere Ausschreibungen.
- [−]{.con} Ungeprüfter KI-Code ist ein Qualitäts- und Sicherheitsrisiko. Produktivsysteme brauchen Review, Tests und eine verantwortliche Person.
- [→]{.rec} Eine kleine eigene Entwicklungskapazität, eine Stelle oder ein Kooperationspartner, bringt mehr als ein großer Einmalauftrag.
:::

## Offene Fortbildung {#fortbildung}

Hochschulen und öffentlich geförderte Plattformen bieten kostenlose Kurse zu Digitalisierung und KI an, meist ohne Zugangsvoraussetzungen und mit Zertifikat.

| Angebot | Träger | Inhalt |
|---------|--------|--------|
| KI-Campus | Stifterverband mit Hochschulen | KI von Grundlagen bis Fachkurs, offen lizenziert, über 100.000 registrierte Lernende und 45.000 ausgestellte Zertifikate.^[KI-Campus: [Kurzvorstellung](https://ki-campus.org/sites/default/files/2025-09/2025-09-01_KI-Campus_Kurzvorstellung.pdf), September 2025.] |
| eGov-Campus | IT-Planungsrat, FITKO, Hochschulen | E-Government-Module auf Hochschulniveau für Verwaltungsbeschäftigte, frei zugänglich, über 16 Kurse und knapp 6.000 Lernende (2023).^[[openHPI: eGov-Campus](https://open.hpi.de/pages/eGovCampus?locale=en); Hünemohr: [eGov-Campus](https://egov-campus.org/sites/default/files/2024-08/GI23_eGov-Campus_Beitrag_Huenemohr.pdf), 2023.] |
| openHPI | Hasso-Plattner-Institut | IT- und KI-Kurse, über 365.000 registrierte Nutzer und 1,3 Mio. Kurseinschreibungen.^[HPI: [openHPI](https://hpi.de/en/impact/openhpi/), 2026.] |
| Open vhb | Virtuelle Hochschule Bayern | Online-Kurse bayerischer Hochschulen, seit 2019 kostenlos für alle.^[[Forschung & Lehre](https://www.forschung-und-lehre.de/lehre/bayern-oeffnet-online-kurse-fuer-alle-1959), 16.07.2019.] |
| Elements of AI | Universität Helsinki | KI-Einführung für Laien, über 2 Mio. Angemeldete aus über 170 Ländern.^[[Elements of AI](https://www.elementsofai.com/), abgerufen Oktober 2026.] |
| Bayerische Verwaltungsschule | Freistaat Bayern | Ausbildung zu Digitallotsen, Kosten zu 80 % vom Freistaat getragen, darauf aufbauend „Digitalwirt“.^[[Haufe](https://www.haufe.de/oeffentlicher-dienst/digitalisierung-transformation/weiterbildung-zum-digitalwirt-in-bayern_524786_630268.html), August 2024.] |

::: {.beiuns}
Eine KI-Schulung muss die Stadt nicht einkaufen. Ein offener Kurs und eine interne Stunde zu eigenen Regeln und Beispielen decken die Schulungspflicht ab und kosten vor allem Arbeitszeit.
:::

Wer KI einsetzt, muss nach der KI-Verordnung die KI-Kompetenz der Beschäftigten fördern. Dokumentierte Schulungen genügen (Kapitel [Regulierung](#regulierung)).^[KI-Campus: [AI Omnibus recalibrates Article 4](https://ki-campus.org/en/blog/eu-ai-act-ai-omnibus-recalibrates-article-4-ai-literacy-remains-mandatory), 28.07.2026.] BayernKI dürfen Beschäftigte erst nach einer Schulung nutzen.^[[Regensburger Nachrichten](https://www.regensburger-nachrichten.de/panorama/97357-landratsamt-regensburg-startet-pilotprojekt-zu-kuenstlicher-intelligenz), 04.06.2025.]

::: {.folgen}
- [+]{.pro} Grundlagenwissen ist kostenlos und jederzeit verfügbar.
- [+]{.pro} Beschäftigte und Ehrenamtliche können mit denselben Kursen lernen und zusammenarbeiten.
- [−]{.con} Selbstlernkurse brauchen Zeit im Dienstplan und jemanden, der sie anstößt.
- [→]{.rec} Fortbildungszeit für Digitalisierung und KI freigeben, offene Kurse nutzen, Erfahrungen intern weitergeben.
:::

## Eigenentwicklungen in Verwaltungen {#eigenentwicklung}

Größere Verwaltungen entwickeln ihre KI-Assistenten inzwischen selbst, oft als Open Source und ohne externen Generalunternehmer. Münchens MUCGPT verarbeitet über 10.000 Chats am Tag.

| Wer | Was | Reichweite | Code |
|-----|-----|------------|------|
| München, MUCGPT^[Landeshauptstadt München: [MUCGPT 2.0](https://stadt.muenchen.de/news/mucgpt-neue-version.html), 30.06.2026.] | Assistent mit eigenen, teilbaren Assistenten und [MCP](#g-mcp)-Anbindungen | über 15.000 regelmäßige Nutzer | offen, auch in Stuttgart im Einsatz |
| Berlin, BärGPT^[[CityLAB Berlin: BärGPT](https://citylab-berlin.org/en/projects/baergpt/); Senatskanzlei Berlin, 25.11.2025.] | Landeseigener Assistent vom CityLAB | über 20.000 Nutzer | offen, modellunabhängig |
| Baden-Württemberg, F13 | Verwaltungsassistenz aus dem InnoLab_bw | Land und Kommunen in Baden-Württemberg | offen seit Juli 2025 |
| Hamburg, LLMoin^[Senatskanzlei Hamburg: [LLMoin](https://www.hamburg.de/politik-und-verwaltung/behoerden/senatskanzlei/aktuelles/pressemeldungen/hamburg-etabliert-ki-assistenten-llmoin-als-bundesweit-nutzbares-erfolgsmodell-1127988), 15.12.2025.] | Assistent, mit Dataport entwickelt | 40.000 Beschäftigte, übernommen von vier Ländern | nicht offen |
| Bund, KIPITZ^[Deutscher Bundestag: [hib 635/2026](https://www.bundestag.de/presse/hib/kurzmeldungen-1202030), 10.08.2026.] | Zentrale Plattform im ITZBund | Bundesverwaltung | nur offene Modelle |
| Vereinigtes Königreich, Humphrey^[[Computing](https://www.computing.co.uk/news/2025/ai/humphrey-ai-trialled-by-25-local-authorities), 27.05.2025.] | Eigenbau, u. a. für Sitzungsprotokolle | Protokoll-Werkzeug in 25 Kommunen getestet, rund eine Stunde Ersparnis je Sitzungsstunde | Eigenbau |
| Stadt Bern^[Berner Fachhochschule: [Open Source Chatbot der Einwohnerdienste](https://www.bfh.ch/ahb/de/forschung/forschungsprojekte/2024-487-206-324/), 2024/25.] | Prototyp für die Einwohnerdienste | 296 Dokumente als Wissensbasis | offen |

::: {.beiuns}
Zu Rathaus, Service und Bauen umfasst die Stadtseite mehrere hundert Seiten, also die Größenordnung des Berner Prototyps. Ein Antwortfeld für Gartenhütte, Sperrmüll oder Hundesteuer ist damit vor allem eine Frage der Arbeitszeit.
:::

Kleine Kommunen beginnen meist mit Regeln. Hagenow in Mecklenburg-Vorpommern hat zuerst eine Dienstvereinbarung und einen Ethikbeirat eingerichtet und empfiehlt Kleinstädten fertige oder selbst betriebene Open-Source-Lösungen statt teurer Einzelentwicklung.^[[Tagesspiegel Background](https://background.tagesspiegel.de/smart-city-und-stadtentwicklung/briefing/ki-in-kleinstaedten-beginnt-klein), 12.08.2026.]

::: {.folgen}
- [+]{.pro} Referenzarchitekturen liegen offen vor und sind im Großbetrieb erprobt.
- [+]{.pro} Eine Kleinstadt hat Hunderte Dokumente, nicht Hunderttausende. Das ist technisch überschaubar.
- [+]{.pro} Offene, verbreitete Bausteine können Agenturen und Freelancer übernehmen, ohne Zustimmung des ursprünglichen Anbieters. Eine Übergabe ist einfacher als früher, weil sich Abhängigkeiten automatisch aktualisieren und KI-Werkzeuge fremden Code erklären.
- [−]{.con} Großstädte haben Teams für den Betrieb, eine Kleinstadt nicht. Betrieb und Verantwortung müssen vorher geklärt sein.
- [→]{.rec} Bausteine nachnutzen und lokal anpassen, gern gemeinsam mit Nachbarkommunen oder dem Landkreis.
:::

## Betrieb und Sicherheit {#sicherheit}

Am 21. Oktober 2026 nahmen nach einer Warnung des BSI der Stufe Orange zahlreiche Behörden und Kommunen ihre Websites vom Netz, darunter Mainz, Kassel und Halberstadt. In Münster trennte der kommunale IT-Dienstleister vorsorglich alle externen Verbindungen.^[[ZDFheute](https://zdfheute.de/politik/sicherheitsluecke-php-webseiten-onlinedienste-cybersicherheit-bsi-100.html), [Volksstimme](https://www.volksstimme.de/panorama/stadte-und-klinik-schranken-onlineangebote-ein-4342768), [ms-aktuell](https://ms-aktuell.de/muenster/php-sicherheitsluecke-in-muenster-stadt/), jeweils 21./22.10.2026.]

Auslöser waren zwei Lücken in PHP („PHP2Shell“, CVE-2026-109618 und CVE-2026-109619), über die Angreifer ohne Anmeldung Code ausführen können. Betroffen ist jede Website, die PHP auf dem Server ausführt, also auch WordPress, TYPO3, Drupal und viele Kommunal-CMS.^[Rapid7: [CVE-2026-109618 and CVE-2026-109619](https://www.rapid7.com/blog/post/etr-cve-2026-109618-and-cve-2026-109619-critical-unauthenticated-remote-code-execution-in-php/), 21.10.2026.] Nur etwa ein Drittel der erkennbaren PHP-Installationen läuft auf einer Version, für die es ein Update gibt.^[Bitsight: [PHP2Shell](https://www.bitsight.com/blog/critical-vulnerability-alert-cve-2026-109618-and-cve-2026-109619-php2shell), 21.10.2026.] Das BSI erwartete Massenangriffe binnen Stunden, auch weil KI-Werkzeuge Patches schnell in Angriffe übersetzen.^[[ingenieur.de](https://www.ingenieur.de/kritische-php-luecken-bsi-warnt-vor-angriffen-auf-webserver-e0529b4b-15c8-444a-974a-00919edb30b6/), 21.10.2026.]

::: {.beiuns}
Eine statisch ausgelieferte Stadtseite wäre an diesem Tag online geblieben, gleich auf welcher PHP-Version der Server läuft.
:::

2026 gab es außerdem kritische Lücken in TYPO3, Drupal und verbreiteten WordPress-Plugins sowie aufgekaufte Plugins mit eingebauter Hintertür.^[[TYPO3 Security Advisory](https://news.typo3.com/security/advisory/typo3-core-sa-2026-017), 09.06.2026; [The DropTimes](https://www.thedroptimes.com/69877/drupal-sa-core-2026-004-postgresql-sql-injection), 20.05.2026; [t3n](https://t3n.de/news/wordpress-plugins-backdoor-infiziert-1738354/), 19.04.2026.] Der Angriff auf die Südwestfalen-IT legte 2023 72 Verbandskommunen lahm, die vollständige Wiederherstellung dauerte elf Monate. Der Patch für die ausgenutzte Lücke war seit Wochen verfügbar, aber nicht eingespielt.^[[ZfK](https://www.zfk.de/digitalisierung/cyberangriff-auf-suedwestfalen-it-monatelanger-krisenmodus-und-millionenkosten), 30.10.2024; [Borns IT-Blog](https://borncity.com/blog/2024/01/26/ransomware-bei-kommunal-it-dienstleister-sdwestfalen-it-nachlese-it-forensik-bericht-teil-1/), 26.01.2024.] In Bayern bearbeitete das Landesamt für Sicherheit in der Informationstechnik seit 2019 rund 1.600 Vorfälle im kommunalen Bereich.^[Bayerischer Landtag: [Drs. 19/6511](https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Schriftliche%20Anfragen/19_0006511.pdf), 29.04.2025.]

Den Betrieb erleichtern automatische Updates von Abhängigkeiten, Container und Schutzregeln beim Hoster, die auch kleinen Teams zur Verfügung stehen. Bei PHP2Shell waren Schutzregeln von Cloudflare rund neun Stunden vor der Veröffentlichung der Lücken aktiv, auch für Kunden im kostenlosen Tarif. AWS und Vercel zogen am selben Tag nach.^[Cloudflare: [Cloudflare deploys protections against php2shell vulnerability](https://blog.cloudflare.com/php-vulnerabilities-waf-protection/), 21.10.2026, nach [PPC Land](https://ppc.land/cloudflare-blocks-php2shell-exploits-9-hours-before-php-flaws-went-public/); [AWS Security Bulletin 2026-143](https://aws.amazon.com/security/security-bulletins/2026-143-aws/), 21.10.2026; [Vercel](https://vercel.com/kb/bulletin/php2shell-security-bulletin), 21.10.2026.] Solche Regeln ersetzen das Update nicht, verschaffen aber Zeit. Statisch ausgelieferte Seiten waren nicht betroffen.

::: {.folgen}
- [+]{.pro} Automatische Updates und Schutzregeln beim Hoster vereinfachen den Betrieb, auch ohne eigene Sicherheitsabteilung.
- [+]{.pro} Statische Auslieferung entfernt die größte Angriffsfläche.
- [−]{.con} Auch ein Wartungsvertrag schützt nicht vor Abschaltungen im Notfall.
- [−]{.con} KI verkürzt die Zeit zwischen Patch und Angriff auf Stunden. Wöchentliches Patchen reicht nicht.
- [→]{.rec} In Verträge: Patch-Fristen in Stunden, Informationspflicht gegenüber der Stadt, offengelegter Versionsstand. In der Architektur: möglichst wenig öffentlich erreichbarer Servercode.
:::

## Offene Sprachmodelle {#modelle}

[Offene Modelle](#g-openweight) liegen im Schnitt rund vier Monate hinter den besten geschlossenen.^[Epoch AI: [Open vs. closed models](https://epoch.ai/data-insights/open-closed-eci-gap), 29.05.2026.] Modelle, die auf handelsüblichen Grafikkarten laufen, erreichen das Niveau der Spitzenmodelle innerhalb eines Jahres.^[Epoch AI: [Open-weight models](https://epoch.ai/topics/open-models), abgerufen Oktober 2026.]

OpenAI hat 2025 mit gpt-oss offene Modelle veröffentlicht, die kleinere Variante läuft mit 16 GB Grafikspeicher.^[[The Register](https://www.theregister.com/2025/08/05/openai_open_gpt/), 05.08.2025.] Mistral aus Frankreich bietet seine Modellfamilie von 3 Milliarden Parametern bis zum Großmodell unter der freien Apache-Lizenz an.^[Mistral AI: [Mistral 3](https://mistral.ai/news/mistral-3), 02.12.2025.] Dazu kommen staatlich geförderte europäische Modelle wie Apertus aus der Schweiz und Teuken aus Deutschland sowie chinesische Modelle. Ende 2025 entfiel rund ein Drittel der Nutzung auf der Plattform OpenRouter auf offene Modelle.^[Aubakirova u. a.: [State of AI. An Empirical 100 Trillion Token Study with OpenRouter](https://arxiv.org/html/2601.10088v1), Januar 2026.]

Der Abstand zur Spitze ist 2026 leicht gewachsen, und Meta hat sich mit seinem neuesten Spitzenmodell von offenen Gewichten abgewandt.^[[The Decoder](https://the-decoder.com/meta-is-reportedly-ditching-open-llama-models-for-avocado-a-closed-model-built-for-direct-sales/), 10.12.2025.] Für Auskunft und Zusammenfassung genügen offene Modelle.

::: {.folgen}
- [+]{.pro} Anfragen und Dokumente bleiben im Haus oder bei einem Hoster der Wahl. Preis- und Lizenzänderungen eines Anbieters treffen die Stadt nicht.
- [+]{.pro} Für Auskunft genügt ein kleines Modell auf einem Rechner mit Grafikkarte, weil die Fakten aus der Suche kommen (Kapitel [RAG](#rag)).
- [−]{.con} Eigener Betrieb braucht Kompetenz. Für anspruchsvolle Aufgaben sind geschlossene Modelle besser.
- [−]{.con} Lizenzen unterscheiden sich und können sich ändern.
- [→]{.rec} Modellunabhängig bauen, wie MUCGPT und BärGPT, und mit einem offenen Modell beginnen.
:::

## RAG statt Fine-Tuning {#rag}

Für Auskunftssysteme hat sich [RAG](#g-rag) gegenüber [Fine-Tuning](#g-finetuning) durchgesetzt. Das Modell bleibt allgemein, das Wissen liegt in einem durchsuchbaren Index, der sich täglich aktualisieren und nach Berechtigungen filtern lässt. Modelle nutzen neues Faktenwissen über Retrieval zuverlässiger als über Nachtraining, besonders bei wenig verbreitetem Wissen wie lokalen Regelungen.^[Ovadia u. a.: [Fine-Tuning or Retrieval?](https://aclanthology.org/2024.emnlp-main.15), EMNLP 2024; Soudani u. a.: [Fine Tuning vs. RAG for Less Popular Knowledge](https://arxiv.org/html/2403.01432v3), 2024.] Fine-Tuning eignet sich für Stil und Format, nicht für Satzungen, die sich ändern.

FIGURE:modell

Das Training übernimmt der Hersteller. Bei jeder Anfrage läuft nur die [Inferenz](#g-inferenz), also die Anwendung des fertigen Modells. Ein [Agent](#g-agent) ruft dabei zusätzlich Werkzeuge auf, etwa einen Kalender oder ein Formular.

Bei RAG trägt jeder Textabschnitt Metadaten wie Quelle, Gültigkeit und Berechtigungsgruppe. Die Suche liefert nur Abschnitte, die die anfragende Person sehen darf, bevor das Modell sie erhält. Bei Fine-Tuning ist das nicht möglich, denn was in den Gewichten steckt, kann jede Person abrufen, die das Modell nutzt. Die Rechte kommen aus den bestehenden Gruppen im Verzeichnisdienst oder Dokumentenmanagement.

| Dokumentklasse | Beispiel | Bürger | Alle Beschäftigten | Bauamt | Personalamt | Stadtrat |
|----------------|----------|:---:|:---:|:---:|:---:|:---:|
| Satzungen, Leistungsbeschreibungen | Gartenhütte, Stellplatzsatzung | ✓ | ✓ | ✓ | ✓ | ✓ |
| Öffentliche Ratsunterlagen | Beschlüsse öffentlicher Sitzungen | ✓ | ✓ | ✓ | ✓ | ✓ |
| Dienstanweisungen | Dienstanweisung zur Vergabe | – | ✓ | ✓ | ✓ | – |
| Bauakten | Unterlagen zu einem laufenden Bauantrag | – | – | ✓ | – | – |
| Nichtöffentliche Sitzungsunterlagen | Vorlage zu einem Grundstücksverkauf der Stadt | – | – | je nach Zuständigkeit | – | ✓ |
| Personaldaten | Private Kontaktdaten, Personalakte | – | – | – | ✓ | – |

Eine Bürgerin fragt auf der Website nach der Gartenhütte. Gesucht wird nur in den ersten beiden Zeilen. Herr Graßl fragt intern nach den Auflagen für einen laufenden Bauantrag, dann wird zusätzlich in den Bauakten gesucht. Stellt jemand aus dem Bürgerbüro dieselbe Frage, lautet die Antwort „keine Unterlagen gefunden“. Die dienstliche Durchwahl von Herrn Graßl ist über die Zuständigkeit öffentlich, seine private Nummer nicht.

::: {.folgen}
- [+]{.pro} Website-Auskunft und interne Assistenz können Index und Modell teilen.
- [+]{.pro} Aktualisieren heißt Dokument ändern. Jede Antwort nennt ihre Quelle.
- [+]{.pro} Das Modell ist austauschbar, der Wert steckt in Index und Metadaten.
- [−]{.con} Rechte müssen an den Dokumenten hängen. Falsch freigegebene Dateien findet eine KI schneller als jeder Mensch.
- [→]{.rec} Bei Angeboten prüfen, ob das Wissen über einen Index mit Rechten angebunden wird. Training auf eigenen Daten ist für Auskunft selten nötig.
:::

## Preisentwicklung bei KI {#preise}

Der Preis für eine gleichbleibende KI-Leistung fällt seit 2023 um etwa das Dreizehnfache pro Jahr.^[Epoch AI: [The Plunging Price of Thought](https://epoch.ai/publications/the-plunging-price-of-thought), 22.09.2026.] Je nach Methode liegen die Schätzungen zwischen dem Fünf- und dem Dreizehnfachen.^[a16z: [Welcome to LLMflation](https://www.a16z.com/llmflation-llm-inference-cost), 12.11.2024; MIT FutureTech: [The Price of Progress](https://arxiv.org/html/2511.23455v1), November 2025.] Am schnellsten fällt der Preis kurz nachdem ein neues Leistungsniveau erstmals erreicht wurde, also bei Funktionen, die gerade als Neuheit verkauft werden.

FIGURE:preise

::: {.beiuns}
Ein Antwortfeld mit angenommen 5.000 Anfragen im Monat verbraucht grob 20 Mio. Eingabe- und 2,5 Mio. Ausgabe-[Token](#g-token). Mit kleinen Modellen kostet das zu Listenpreisen etwa 3 bis 30 Dollar im Monat (eigene Überschlagsrechnung). Teuer sind Integration, Daten und Betrieb.
:::

Zwischen Rohkosten und Endpreis liegt eine große Spanne. Manche KI-Anbieter arbeiten mit negativen Margen, weil sie teure Spitzenmodelle einkaufen.^[Wing VC: [Who Makes Money When Inference Gets 10x Cheaper?](https://www.wing.vc/content/who-makes-money-when-inference-gets-10x-cheaper), August 2026.] Bei Lizenzen pro Arbeitsplatz zahlt der Kunde den Preis vom Vertragsschluss, auch wenn die Rohkosten ein Jahr später ein Zehntel betragen. Microsoft 365 Copilot kostet 30 Dollar pro Person und Monat, für Organisationen mit bis zu 300 Beschäftigten seit Dezember 2025 21 Dollar.^[Microsoft: [Microsoft 365 Copilot Business](https://www.microsoft.com/en-us/microsoft-365/blog/2025/12/02/microsoft-365-copilot-business-the-future-of-work-for-small-businesses/), 02.12.2025.]

::: {.folgen}
- [+]{.pro} In zwölf Monaten gibt es dieselbe Qualität für einen Bruchteil des Preises oder bessere Qualität zum selben Preis.
- [+]{.pro} Bei kommunalen Mengen sind Modellkosten gering. Das Geld gehört in Daten und Integration.
- [−]{.con} Mehrjährige Festpreise geben sinkende Kosten nicht weiter.
- [−]{.con} Die günstigsten Angebote kommen teils von Anbietern, die datenschutzrechtlich ausscheiden.
- [→]{.rec} Verträge so gestalten, dass sinkende Preise ankommen, etwa über nutzungsabhängige Abrechnung. Eigener Betrieb ist eine Alternative.
:::

## Preismodelle der Softwarehersteller {#saas}

Atlassian senkte 2025 den Preis seines KI-Assistenten Rovo von über 20 auf 5 Dollar, Microsoft im Dezember 2025 den von Copilot für kleinere Organisationen von 30 auf 21 Dollar.^[Microsoft: [Microsoft 365 Copilot Business](https://www.microsoft.com/en-us/microsoft-365/blog/2025/12/02/microsoft-365-copilot-business-the-future-of-work-for-small-businesses/), 02.12.2025; [TechTarget](https://techtarget.com/searchitoperations/news/366622263/Atlassian-Rovo-pricing-shifts-amid-AI-adoption-struggles), 09.04.2025.] Die Grundpreise der [SaaS](#g-saas)-Pakete steigen dagegen. Google hat Gemini 2025 in Workspace aufgenommen und die Preise um bis zu 22 % erhöht, Microsoft 365 wird ab Juli 2026 teurer.^[[9to5Google](https://9to5google.com/2025/01/15/google-workspace-price-increase-2025/), 15.01.2025; Microsoft: [2026 Microsoft 365 Pricing Updates FAQ](https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates-FAQ), 24.03.2026.] Auch die Abrechnung wechselt. Zendesk berechnet seit August 2024 nur Anfragen, die seine KI selbstständig gelöst hat,^[Zendesk: [Outcome-based pricing](https://zendesk.co.uk/newsroom/articles/zendesk-outcome-based-pricing), 28.08.2024.] Salesforce kehrte nach einem Versuch mit Abrechnung pro Aktion Ende 2025 auf Wunsch der Kunden zu Lizenzen pro Person zurück.^[[The Register](https://www.theregister.com/2025/12/12/ai_agents_salesforce_pricing/), 12.12.2025.]

Offene Alternativen gewinnen Nutzer. LibreOffice wurde nach dem Release im August 2026 in der ersten Woche über eine Million Mal heruntergeladen, so oft wie nie zuvor.^[[OMG! Ubuntu](https://www.omgubuntu.co.uk/2026/09/libreoffice-download-record), 02.09.2026.]

::: {.folgen}
- [+]{.pro} Sinkende Preise für KI-Zusätze stärken die Verhandlungsposition auch kleiner Kunden.
- [+]{.pro} Offene Alternativen werden für mehr Anwendungen tragfähig, auch als Eigenentwicklung.
- [−]{.con} Grundpreise steigen weiter, und häufig wechselnde Preismodelle machen Kosten schwer planbar.
- [→]{.rec} Preisanpassung und Datenexport vertraglich sichern, bei jeder Verlängerung offene Alternativen prüfen.
:::

## Regulierung {#regulierung}

Die KI-Verordnung der EU ist in Kraft, wird aber weiter angepasst. Im Juli 2026 hat der KI-Omnibus die Pflichten für Hochrisiko-KI auf Dezember 2027 und August 2028 verschoben.^[[Cuatrecasas](https://www.cuatrecasas.com/en/spain/intellectual-property/art/digital-omnibus-ai-has-been-published), 24.07.2026.] Mehrere weitere Gesetze sind erst vorgeschlagen.

FIGURE:regulierung

Wer KI einsetzt, muss schon jetzt die KI-Kompetenz der Beschäftigten fördern, dokumentierte Schulungen genügen.^[[Lewis Silkin](https://www.lewissilkin.com/en/insights/2026/07/27/the-digital-omnibus-on-ai-enters-into-force-today-102nedo), 27.07.2026.] Seit August 2026 müssen KI-erzeugte Texte, die die Öffentlichkeit über Angelegenheiten von öffentlichem Interesse informieren, gekennzeichnet werden, außer ein Mensch hat sie redaktionell geprüft und verantwortet sie.^[[AI Act, Art. 50](https://artificialintelligenceact.eu/transparency-rules-article-50/).] Das deutsche Durchführungsgesetz macht die Bundesnetzagentur zur Aufsicht. Für öffentliche Stellen der Länder und Kommunen bestimmt das Landesrecht die Zuständigkeit, Bußgelder gegen Behörden sieht das Gesetz nicht vor.^[KI-Marktüberwachungs- und Innovationsförderungsgesetz, [BGBl. 2026 I Nr. 223](https://www.inkasso.de/fileadmin/user_upload/mitgliederinformationen/2026_07_28_bgbl_223.pdf), 28.07.2026.] Der Bundesrat kritisierte, dass Aufsicht und Kosten damit bei Ländern und Kommunen liegen.^[Bundesrat: [Drs. 97/1/26](https://dserver.bundestag.de/brd/2026/0097-1-26.pdf), 16.03.2026.]

Für die Beschaffung ist noch vieles offen. Der Cloud and AI Development Act soll öffentliche Auftraggeber verpflichten, je nach Risiko eine von vier Souveränitätsstufen festzulegen, unabhängig von Schwellenwerten.^[[Eubelius](https://www.eubelius.com/en/news/the-cloud-and-ai-development-act-cada-public-procurement-sets-the-tone-as-a-strategic-tool-to), 15.06.2026.] Die geplante EU-Vergabeverordnung sieht eine Bevorzugung europäischer Anbieter vor, eine Einigung ist bis Ende 2027 angestrebt.^[[HSF Kramer](https://www.hsfkramer.com/it/notes/crt/2026-09/the-eu-public-procurement-act-the-commission-proposes-a-european-preference-framework), 21.09.2026.] Die Änderungen an der DSGVO aus dem Digital-Omnibus sind im Rat abgestimmt, das Parlament folgt voraussichtlich Anfang 2027.^[[nicfab](https://www.nicfab.eu/en/posts/digital-omnibus-council/), 21.10.2026.]

::: {.folgen}
- [+]{.pro} Für Auskunft und Textentwürfe sind die Pflichten überschaubar: Schulung, Kennzeichnung, menschliche Freigabe.
- [+]{.pro} Die neuen Beschaffungsregeln begünstigen europäische und offene Lösungen.
- [−]{.con} Viele Details sind offen, die Aufsicht über Kommunen regeln die Länder.
- [−]{.con} Lange Verträge müssen sich an kommende Beschaffungsregeln anpassen lassen.
- [→]{.rec} Anpassungsklauseln für kommende Regeln vorsehen. Jetzt umsetzen, was schon gilt: Schulungen dokumentieren, öffentliche KI-Texte von Menschen freigeben lassen, Assistenten als KI kennzeichnen.
:::

## Zentrale KI-Angebote des Staates {#staat}

::: {.beiuns}
Bietet der Freistaat BayernKI später allen Kommunen an, sollte eine eigene Lösung daneben bestehen oder dorthin umziehen können. Aufbereitete Daten lassen sich in jedes dieser Systeme übernehmen.
:::

Mehrere Staaten und Länder stellen KI zentral für Behörden und Kommunen bereit. In Bayern nutzt die Staatsverwaltung seit Oktober 2024 „BayernKI“, 50 Kommunen testen es.^[Bayerischer Landtag: [Drs. 19/7797](https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Schriftliche%20Anfragen/19_0007797.pdf), 01.09.2025.]

| Wer | Angebot | Stand |
|-----|---------|-------|
| Freistaat Bayern | BayernKI für die Staatsverwaltung, Pilot mit 50 Kommunen. Rollout-Termin für Kommunen offen.^[Bayerischer Gemeindetag: [Forum Digitalisierung](https://www.bay-gemeindetag.de/media/27002/forum_3_-digitalisierung.pdf), 22.10.2025.] | Pilot seit 2025 |
| Bund | Souveräne KI-Plattform von Telekom und SAP für Bund, Länder und Kommunen als Teil des Deutschland-Stacks.^[[Deutsche Telekom](https://www.telekom.com/de/newsroom/aktuelles/medieninformationen/2026/05/telekom-baut-souveraene-ki-plattform-fuer-die-bundesregierung), 21.05.2026.] | 2026 |
| Baden-Württemberg | F13 als Open Source auch für Kommunen nutzbar. | seit 2025 |
| Hamburg, Dataport | LLMoin für Kommunen über den IT-Dienstleister. | seit 2025 |
| Frankreich | Albert für Gebietskörperschaften kostenlos, Nachfolger auf Basis von Mistral im Test mit 10.000 Bediensteten.^[[WEKA](https://www.weka.fr/actualite/?p=209194), 09.01.2026.] | 2024 bis 2026 |
| Schweden | Kommunen betreiben die Plattform Eneo gemeinsam als Open Source.^[Sundsvalls kommun: [Eneo](https://utveckling.sundsvall.se/inlagg/inlagg/2025-09-25-eneo---ett-steg-mot-en-hallbar-och-demokratisk-ai), 25.09.2025.] | seit 2025 |
| Estland | Bürokratt als gemeinsames Netz von Assistenten, Betrieb in der Staatscloud für rund 150 Euro pro Einrichtung und Monat plus Modellkosten.^[[Apolitical](https://apolitical.co/en/navigator/case-studies/burokratt-estonia-s-single-network-of-ai-assistants-replacing-dozens-of-separate-agency-chatbots), 06.07.2026.] | seit 2021 |
| Niederlande, Schweiz, Spanien | Staatlich geförderte offene Sprachmodelle: GPT-NL, Apertus, ALIA. | 2025/26 |

Die schwedischen Kommunen haben die Zusammenarbeit mit dem ursprünglichen Anbieter beendet und führen die Plattform als Verein weiter, weil Teile des Codes geschlossen blieben.

::: {.folgen}
- [+]{.pro} Landes- und Bundesangebote übernehmen Beschaffung, Datenschutzprüfung und Betrieb.
- [+]{.pro} Gemeinsame Plattformen setzen Standards, an die eigene Daten anschließen können.
- [−]{.con} Der Zeitplan ist offen. Landesangebote zielen auf interne Assistenz, die Auskunft auf der eigenen Website bleibt Sache der Stadt.
- [→]{.rec} Interne KI-Assistenz so wählen, dass ein späterer Wechsel zu einem Landesangebot möglich bleibt. Pilotteilnahme bei BayernKI anfragen, Daten vorbereiten.
:::

## Ausblick {#ausblick}

Liegen Inhalte strukturiert vor, kann ein Sprachmodell daraus mehr erzeugen als Antworten. Technisch ist das heute möglich, in Kommunen aber kaum erprobt. Es gehört deshalb schon in die Planung der Architektur.

- **Antwortseiten statt Chatfenster.** Ein Antwortfeld erzeugt eine Seite im Stadtdesign mit Antwort, Quellen, zuständiger Person und Formularlink. Häufige Fragen werden zwischengespeichert, Anfragen protokolliert.
- **Seiten per Beschreibung.** Die Redaktion beschreibt, was sie braucht, etwa eine Seite zum Stadtfest mit Programm aus dem Kalender und Hinweis zur Straßensperrung. Das System erstellt einen Entwurf im Designsystem, ein Mensch gibt frei. Auch klassische CMS rüsten nach, TYPO3 etwa mit einer Erweiterung für KI-Suche und Zusammenfassungen.^[TYPO3: [This Month in TYPO3, May 2026](https://news.typo3.com/article/this-month-in-typo3-may-2026).]
- **Sharepic-Generatoren.** Aus einem Kalendereintrag entstehen Grafiken im Stadtdesign für soziale Netzwerke und Aushang.
- **Eine Quelle für mehrere Kanäle.** Eine Meldung wird einmal geschrieben und erscheint auf der Website, im Amtsblatt, im Newsletter und in sozialen Netzwerken. Die Website dient dabei als Archiv.^[[KOMMUNAL](https://kommunal.de/raus-aus-dem-rathaus-rein-den-feed), 08.10.2026.]
- **Leichte Sprache, Übersetzungen, Alternativtexte.** Entwürfe entstehen automatisch, Menschen prüfen. Für Gemeinden ist Leichte Sprache in Bayern bisher nur empfohlen, mit KI wird sie bezahlbar.
- **Ratsinformation.** Kurzfassungen von Sitzungsvorlagen und eine Suche über Beschlüsse, öffentlich für öffentliche Unterlagen und intern für den Rest (Kapitel [RAG](#rag)).

::: {.folgen}
- [+]{.pro} Weniger Doppelarbeit, einheitliches Erscheinungsbild.
- [+]{.pro} Mehrsprachigkeit und Leichte Sprache werden bezahlbar.
- [−]{.con} Ohne Freigabeprozess veröffentlicht die Stadt Fehler unter eigenem Namen. Kennzeichnungspflichten gelten.
- [−]{.con} Fest eingebaute KI-Funktionen eines CMS binden an dessen Hersteller.
- [→]{.rec} Die Grundlage früh legen, mit strukturierten Inhalten, einem Designsystem mit Vorlagen und offenen Schnittstellen.
:::

## Fazit {#fazit}

Die Investition, die sich in jedem Fall lohnt, ist die Datengrundlage. Auf ihr lassen sich verschiedene Wege aufbauen, einzeln oder kombiniert.

| Weg | Was | Aufwand | Passt, wenn |
|------|--------------|--------|--------------|
| Fertige Lösung | KI-Funktionen eines Anbieters, eingebunden in die eigene Website | Lizenz oder Projektpreis | schnell ein Ergebnis gebraucht wird und Schnittstellen und Datenexport offen sind |
| Gemeinsame Angebote | Plattformen von Land, Bund oder anderen Kommunen, etwa BayernKI | Beteiligung, Anpassung, Datenpflege | der Zeitplan dieser Angebote zum eigenen Bedarf passt |
| Eigener Aufbau | Offene Bausteine und offenes Modell auf den eigenen Inhalten | Vor allem Arbeitszeit | IT-affine Leute im Haus, im Ehrenamt oder in einer Kooperation verfügbar sind |

Ein möglicher Ablauf:

1. **Datengrundlage.** Inventur der Inhalte, Zuständigkeiten als Datensätze, Leistungsbeschreibungen per Schnittstelle aus dem BayernPortal, PDFs in Text, strukturierte Daten nach schema.org.
2. **Offene Architektur.** Statisch ausgeliefert, Code und Inhalte im Besitz der Stadt, offene Schnittstellen.
3. **Erfahrung sammeln.** Ein Antwortfeld als Prototyp, mit Protokollierung und Quellenangaben, zuerst intern getestet. Beteiligte lernen mit offenen Kursen, eine Pilotteilnahme bei BayernKI wird angefragt.
4. **Regelmäßig neu bewerten.** Preise und Regeln ändern sich schnell. Eigene Erfahrungswerte machen jede weitere Entscheidung leichter.

### Prüffragen für jede Lösung {#pruefragen}

::: {.checklist}
- Gehören Code, Inhalte und Zugangsdaten der Stadt, und unter welcher Lizenz steht der Code?
- Lassen sich alle Inhalte jederzeit vollständig in offenen Formaten exportieren?
- Wo werden Anfragen verarbeitet, mit welchem Modell, und ist es austauschbar?
- Passen sich die Kosten an, wenn Modelle günstiger werden?
- Wächst die Lösung mit neuen Entwicklungen mit, etwa mit Redaktionssystemen, die Seiten nach einer Beschreibung entwerfen (Kapitel [Ausblick](#ausblick))?
:::

## Glossar {#glossar}

[Agent, Tool Use]{#g-agent}
:   Das Modell ruft selbst Werkzeuge auf, etwa Suche, Datenbank, Formular oder Kalender.

[Content-Delivery-Netz (CDN)]{#g-cdn}
:   Verteilt fertige Dateien über viele Server. Schnell und belastbar bei hohem Andrang.

[Crawler, Suchindex]{#g-crawler}
:   Programme von Suchmaschinen und KI-Anbietern, die öffentliche Seiten lesen und indexieren. Grundlage für klassische Suche und KI-Suche.

[Embedding, Vektorsuche]{#g-embedding}
:   Texte werden als Zahlenvektoren gespeichert, damit inhaltlich ähnliche Passagen auch ohne gleiche Wörter gefunden werden. „Sofa entsorgen“ findet „Sperrmüll“.

[Fine-Tuning]{#g-finetuning}
:   Nachtrainieren eines Modells mit eigenen Daten. Das Wissen steckt danach in den Gewichten. Es ist schwer zu aktualisieren, nicht nach Berechtigung filterbar und nicht zitierbar.

[Halluzination]{#g-halluzination}
:   Plausibel klingende, falsche Ausgabe. Mit RAG und Quellenangaben deutlich seltener, aber nicht ausgeschlossen.

[Headless CMS, statische Website]{#g-headless}
:   Seiten werden vorab als fertige Dateien erzeugt und ohne Datenbank ausgeliefert. Die Redaktion pflegt Inhalte in einem getrennten, nicht öffentlich erreichbaren Redaktionssystem.

[Inferenz, Hosting]{#g-inferenz}
:   Der laufende Betrieb eines Modells beim Anbieter, bei einem EU-Hoster, beim kommunalen IT-Dienstleister oder auf eigener Hardware.

[KI-Suche]{#g-kisuche}
:   Google-KI-Übersichten und KI-Modus, ChatGPT Search, Perplexity, Copilot. Sie suchen im Web und fassen Treffer zu einer Antwort zusammen. Das Modell gehört dem Anbieter.

[MCP (Model Context Protocol)]{#g-mcp}
:   Offener Standard, um Datenquellen und Werkzeuge an beliebige Modelle anzuschließen. Eine Anbindung bleibt beim Modellwechsel nutzbar.

[Open Source]{#g-oss}
:   Software, deren Quellcode unter einer Lizenz veröffentlicht ist, die Nutzung, Änderung und Weitergabe erlaubt.

[Open Weight, Closed Weight]{#g-openweight}
:   Bei Open-Weight-Modellen sind die Modelldateien frei herunterladbar und auf eigener Hardware nutzbar, etwa Mistral, gpt-oss, Qwen oder Apertus. Closed-Weight-Modelle sind nur über die Schnittstelle des Herstellers nutzbar, etwa GPT, Claude oder Gemini. Open Weight heißt nicht automatisch Open Source, die Trainingsdaten bleiben meist geschlossen.

[Public Money, Public Code]{#g-pmpc}
:   Grundsatz, nach dem mit öffentlichem Geld entwickelte Software unter freier Lizenz veröffentlicht wird.

[RAG (Retrieval-Augmented Generation)]{#g-rag}
:   Zuerst werden passende Abschnitte aus eigenen Dokumenten gesucht, dann formuliert das Modell auf dieser Grundlage eine Antwort mit Quellen.

[SaaS (Software as a Service)]{#g-saas}
:   Software, die über das Internet genutzt und meist pro Person und Monat abgerechnet wird, etwa Microsoft 365 oder Salesforce.

[Sprachmodell (LLM)]{#g-llm}
:   Erzeugt aus einer Eingabe Text. Kennt nur, was im Training vorkam oder bei der Anfrage mitgegeben wird. Über eine Kleinstadt weiß es von sich aus wenig, und das oft veraltet.

[Strukturierte Daten]{#g-struktur}
:   Maschinenlesbare Auszeichnung nach schema.org, etwa für Öffnungszeiten, Veranstaltungen, Ansprechpersonen und Leistungen. Nützt Suchmaschinen, KI-Suche und eigenen Assistenten.

[Token]{#g-token}
:   Abrechnungseinheit für Sprachmodelle, etwa drei Viertel eines Wortes. Preise gelten pro Million Token.
