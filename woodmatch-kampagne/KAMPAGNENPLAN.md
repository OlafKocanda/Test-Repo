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
| Video A: Produkt-Demo mit Waldemar | 9:16, 38 s | `woodmatch-ad/woodmatch-reel-9x16.mp4` | Anzeige + organisches Reel |
| Video B: „Waldemars Geschichte“ | 9:16, 31 s | `woodmatch-ad/woodmatch-reel-B-story.mp4` | Anzeige + organisches Reel |
| Karussell 1: „Weißt du, was in deinem Wald steckt?“ | 4:5, 7 Slides | `woodmatch-ad/carousels/export/karussell-1-fragen/` | Organisch + dritte Anzeigenvariante |
| Karussell 2: „Was kostet WoodMatch?“ | 4:5, 6 Slides | `…/karussell-2-kostenlos/` | Organisch (räumt den Einwand „Was kostet das?“ aus) |
| Karussell 3: „So wird dein Wald digital“ | 4:5, 6 Slides | `…/karussell-3-so-gehts/` | Organisch + Retargeting auf Video-Zuschauer |
| Karussell „Was ist dein Wald 2026 wert?“ | 4:5, 5 Slides | Canva: https://canva.link/7ory9ufugfhykgq | Nur als Entwurf, anderer Stil. Besser im Stil der Karussells 1–3 nachbauen |
| Blog (6 Artikel) | Link | woodmatch.de/wissen | Karussells + Facebook-Link-Posts |

## Bezahlter Test (500 €, ca. 4 Wochen)

| Phase | Budget | Inhalt |
|---|---|---|
| Woche 1–2 | ca. 250 € (ca. 18 €/Tag) | 1 Kampagne, 1 Anzeigengruppe (DE ohne BY, 28–65+, breit), 3 Anzeigen: Video A, Video B, Karussell 1 |
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

| Woche | Mo | Mi | Fr |
|---|---|---|---|
| 1 | Karussell 1 „Weißt du, was in deinem Wald steckt?“ | Reel: Video A | Karussell 2 „Was kostet WoodMatch?“ |
| 2 | Blog: „Wald geerbt: Was jetzt?“ | Reel: Video B | Karussell 3 „So wird dein Wald digital“ |
| 3 | Blog: „Was ist mein Wald 2026 wert?“ | Reel: A1-Konzept „Was ist dein Wald wert?“ (neu drehen) | Blog: „Waldpflegevertrag“ |
| 4 | Blog: „Borkenkäfer-Check“ | Reel: Andreas als Talking Head (A3) | Blog: „Waldversicherung“ / „EUDR“ |

Blog-Posts: Auf Instagram als Karussell mit „Link in Bio“ oder Link-Sticker in der Story, auf Facebook als Link-Post mit
`?utm_source=facebook&utm_medium=organic&utm_campaign=blog` (bzw. `utm_source=instagram`).

## Vor dem Start klären

1. **„Keine Laufzeit“** (Karussell 2): Stimmt das für Waldbesitzer? Sonst die Slide ändern.
2. **Matching „BALD“** (Video A): Das ist in Ordnung, solange es so gekennzeichnet bleibt. Keine Funktion als live bewerben, die es noch nicht gibt.
3. **Musik** (Damtaro – Forest, freetouse.com): Die Lizenz muss Werbeanzeigen erlauben, eventuell ist ein Credit im Text nötig.
4. **KI-Bilder in Video B:** Meta kennzeichnet solche Bilder eventuell mit „KI-Info“. Offenlegen ist die sichere Variante.
5. **Beispielwerte** (1.920 Fm, ≈ 96 T€) sind als BEISPIEL gekennzeichnet, das so lassen.
6. **Länge von Video A:** 38 s sind für Anzeigen lang. Eine gekürzte Version mit 15–20 s (Hook → Flurstück → Holzwert → CTA) testen.

## Checkliste bis zum Start

- [ ] Umami auf woodmatch.de und app.woodmatch.de einbauen, Event `registrierung_abgeschlossen` anlegen
- [ ] UTM-Quelle bei der Registrierung speichern
- [ ] Werbekonto anlegen, Facebook-Seite und Instagram verbinden, Ausgabenlimit von 500 € setzen
- [ ] Link in Bio einrichten (Registrierung + Blog)
- [ ] Offene Punkte 1–4 klären
- [ ] Woche 1 organisch posten
- [ ] Anzeigen starten (ca. Mitte Oktober)
