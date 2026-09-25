# WoodMatch – Kampagnenplan Social Media (Herbst 2026)

Stand: 25.09.2026 · Grundlage: Briefing „WoodMatch – Briefing für Marketing Manager“ und die fertigen Creatives aus Branch `claude/woodmatch-social-ads-qg0ba8` (Ordner `woodmatch-ad/`).

## Eckdaten

| | |
|---|---|
| Ziel | Registrierungen auf app.woodmatch.de |
| Budget | 500 € als Test (harte Obergrenze über das Ausgabenlimit des Werbekontos) |
| Gebiet | Deutschland. Empfehlung für die bezahlten Anzeigen: Bayern ausschließen (keine offenen Flurstücksdaten, daher kein Aha-Erlebnis mit der Flurnummer) |
| Kanäle | Instagram und Facebook, gleiche Inhalte über die Meta Business Suite |
| Messung | UTM-Parameter + Umami (Event `registrierung_abgeschlossen`) + UTM-Quelle bei der Registrierung speichern |
| Meta-Kampagnenziel | Traffic, optimiert auf Link-Klicks (ohne Pixel kann Meta nicht auf Registrierungen optimieren) |

## Vorhandene Creatives

| Asset | Format | Datei | Einsatz |
|---|---|---|---|
| Video A: Produkt-Demo mit Waldemar | 9:16, 38 s | `woodmatch-kampagne/video/woodmatch-reel-A-eigene-musik.mp4` | Organisches Reel |
| Video A kurz | 9:16, 19 s | `woodmatch-kampagne/video/woodmatch-reel-kurz-eigene-musik.mp4` | Anzeige (Hook → Flurnummer → Wald auf einen Blick → Kostenlos → CTA) |
| Video B: „Waldemars Geschichte“ | 9:16, 31 s | `woodmatch-kampagne/video/woodmatch-reel-B-eigene-musik.mp4` | Anzeige + organisches Reel |
| Karussell 1: „Weißt du, was in deinem Wald steckt?“ | 4:5, 7 Slides | `woodmatch-ad/carousels/export/karussell-1-fragen/` | Organisch + dritte Anzeigenvariante |
| Karussell 2: „Was kostet WoodMatch?“ | 4:5, 6 Slides | `…/karussell-2-kostenlos/` | Organisch (räumt den Einwand „Was kostet das?“ aus) |
| Karussell 3: „So wird dein Wald digital“ | 4:5, 6 Slides | `…/karussell-3-so-gehts/` | Organisch + Retargeting auf Video-Zuschauer |
| Comeback-Karussell „Es war still bei uns“ | 4:5, 4 Slides | `woodmatch-kampagne/posts/export/post-1-comeback/` | Erster organischer Post |
| „Wusstest du? 48 % Privatwald“ | 4:5, 1 Bild | `woodmatch-kampagne/posts/export/post-2-wusstest-du/` | Zweiter organischer Post |
| 6 Blog-Karussells (Waldwert, Wald geerbt, Borkenkäfer, Versicherung, Pflegevertrag, EUDR) | 4:5, je 6 Slides | `woodmatch-kampagne/posts/export/blog-*/` | Organisch, auf Facebook mit Link zum Artikel |
| Eigene Musik (lizenzfrei, per Code erzeugt) | 40 s | `woodmatch-kampagne/video/musik/` | Liegt unter allen drei Videos |

## Bezahlter Test (500 €, ca. 4 Wochen)

| Phase | Budget | Inhalt |
|---|---|---|
| Woche 1–2 | ca. 250 € (ca. 18 €/Tag) | 1 Kampagne, 1 Anzeigengruppe (DE ohne BY, 28–65+, breit), 3 Anzeigen: Video A kurz, Video B, Karussell 1 |
| Auswertung nach ca. 10 Tagen | – | Das schwächste Creative nach Kosten pro Registrierung abschalten (Ersatzkriterium: Link-Klickrate) |
| Woche 3–4 | ca. 250 € | Gewinner weiterlaufen lassen. Dazu Retargeting mit Karussell 3 an alle, die Video A oder B zu mindestens 50 % gesehen haben (funktioniert ohne Pixel) |

- Platzierungen: Reels, Feed und Stories auf Facebook und Instagram, kein Audience Network.
- Kein formaler Meta-A/B-Test: Der braucht deutlich mehr Budget, als der Test hat (ca. 100 Registrierungen pro Variante). Wir vergleichen einfach die Kosten pro Registrierung.
- Grobe Erwartung: 500–1.200 Klicks und 15–90 Registrierungen, also 6–30 € pro Registrierung.

UTM-Vorlage für alle Anzeigen:
```
?utm_source=meta&utm_medium=paid_social&utm_campaign=wm_test_okt26&utm_content={{ad.name}}&utm_term={{placement}}
```

## Redaktionsplan organisch (4 Wochen, 3 Posts pro Woche)

Die ersten 1–2 Wochen läuft das Profil organisch an, danach starten die Anzeigen. Wer dann auf eine Anzeige klickt, sieht schon ein gefülltes Profil.

Vorlauf: Comeback-Karussell „Es war still bei uns“, 2–3 Tage später „Wusstest du? 48 %“. Die Umfrage lieber als Story mit Umfrage-Sticker.

| Woche | Mo | Mi | Fr |
|---|---|---|---|
| 1 | Karussell 1 „Weißt du, was in deinem Wald steckt?“ | Reel: Video A | Karussell 2 „Was kostet WoodMatch?“ |
| 2 | Blog-Karussell „Wald geerbt“ | Reel: Video B | Blog-Karussell „Waldwert“ |
| 3 | Karussell 3 „So wird dein Wald digital“ | Reel: A1-Konzept oder Video A kurz | Blog-Karussell „Waldpflegevertrag“ |
| 4 | Blog-Karussell „Borkenkäfer“ | Reel: Andreas als Talking Head (A3) | Blog-Karussell „Waldversicherung“ |
| 5 | Blog-Karussell „EUDR“ | | |

Blog-Posts: Auf Instagram als Karussell mit „Link in Bio“ oder Link-Sticker in der Story, auf Facebook als Link-Post mit
`?utm_source=facebook&utm_medium=organic&utm_campaign=blog` (bzw. `utm_source=instagram`).

## Geklärt

1. **„Keine Laufzeit“** (Karussell 2): stimmt, die Slide bleibt.
2. **Musik:** Die kostenlose Lizenz von freetouse.com deckt keine Werbung und keine Firmen-Posts ab (freetouse.com/license). Deshalb ist die Tonspur in allen drei Videos durch eine **eigene, per Code erzeugte Musik** ersetzt (`video/musik/make_music.py`). Keine Samples, keine fremden Rechte. Die Originaldateien mit freetouse-Musik aus `woodmatch-ad/` nicht mehr verwenden.
3. **KI-Bilder in Video B:** Im Anzeigentext am Ende ergänzen: „Bilder KI-generiert, Personen fiktiv.“ Meta setzt eventuell zusätzlich das Label „KI-Info“.
4. **Matching „BALD“** (Video A) und **Beispielwerte** (1.920 Fm, ≈ 96 T€) bleiben so gekennzeichnet.

## Checkliste bis zum Start

- [ ] Umami auf woodmatch.de und app.woodmatch.de einbauen, Event `registrierung_abgeschlossen` anlegen
- [ ] UTM-Quelle bei der Registrierung speichern
- [ ] Werbekonto anlegen, Facebook-Seite und Instagram verbinden, Ausgabenlimit von 500 € setzen
- [ ] Link in Bio einrichten (Registrierung + Blog)
- [ ] Comeback-Post und „Wusstest du?“ posten
- [ ] Woche 1 organisch posten
- [ ] Anzeigen starten (ca. Mitte Oktober)
