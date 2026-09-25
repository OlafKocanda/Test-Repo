# WoodMatch – Werbeclip für Instagram & Facebook

**Datei:** `woodmatch-reel-9x16.mp4` · 1080×1920 (9:16) · 37 s · 30 fps · H.264 + AAC-Ton
Passt für Instagram Reels/Stories, Facebook Reels/Stories und als 9:16-Anzeige im Meta-Werbeanzeigenmanager.

## Ablauf
| Zeit | Szene | Inhalt |
|---|---|---|
| 0–3 s | Hook (Waldfoto) | „Du hast Wald? Und willst endlich wissen, was in ihm steckt?“ |
| 3–6 s | Logo | WoodMatch – Die Plattform für Privatwaldbesitzer |
| 6–10 s | 01 Überblick | Screenshot Übersicht, Zoom auf Handlungsempfehlungen |
| 10–14 s | 02 Karte & Geodaten | Screenshot Flurstücke, Zoom auf Kartenebenen (Baumart, Kronenhöhe, Sentinel-2 …) |
| 14–18 s | 03 Objekte | Baumarten-Karte + Menü „Neues Objekt“ (Polter setzen) |
| 18–22 s | 04 Maßnahmen – **Bald verfügbar** | Screenshot Maßnahme-Assistent, deutlich als „Bald verfügbar“ markiert |
| 22–27 s | 05 **Nur bei WoodMatch: Marktplatz mit Matching** | Screenshot Suche („Deine Flurstücke im Arbeitsgebiet“) + Match-Karten FBG / Forstprofis / Holzkäufer – Musik-Drop genau hier |
| 27–32 s | Preis | Kostenlos starten. Kostenlos bleiben. Kein Abo · keine Grundgebühr · keine versteckten Kosten · Provision nur bei Vermittlung |
| 32–37 s | Call-to-Action | „Dein Wald. In deiner Hand.“ · Kostenlos starten · app.woodmatch.de |

## Vorschlag Beitragstext

> Du hast Wald – aber keinen Überblick? 🌲
>
> Mit WoodMatch siehst du deine Flurstücke mit Satelliten- und Geodaten, erfasst Bestände, Bäume und Polter – und findest über unseren Marktplatz mit Matching automatisch die passenden Partner: FBGs, Forstprofis und Holzkäufer.
>
> ✅ Kostenlos starten – und kostenlos bleiben
> ✅ Kein Abo, keine Grundgebühr
> ✅ Auch ohne forstliches Fachwissen
>
> 👉 Jetzt starten: app.woodmatch.de
>
> #Privatwald #Waldbesitzer #Forstwirtschaft #Wald #Holzverkauf #Waldumbau #Nachhaltigkeit #WoodMatch

## Hinweise
- **Musik:** „Forest“ von Damtaro (freetouse.com), Ausschnitt ab 0:11,6 mit Ein-/Ausblendung. Bitte die Lizenzbedingungen von freetouse.com prüfen (ggf. Credit in der Beschreibung: „Music: Damtaro – Forest, freetouse.com“).
- **Screenshots** sind echte App-Screenshots (Account Olaf Kocanda). Die Flurstücksliste ist nur kurz und klein im Bild; bei Bedarf kann sie unkenntlich gemacht werden.
- Maßnahmen sind als „Bald verfügbar“ gekennzeichnet. Keine Nutzer-/Flächenzahlen mehr im Video.

## Video anpassen & neu rendern
Der Clip ist eine HTML-Animation (`index.html`), die Frame für Frame aufgenommen wird.
- Vorschau im Browser: `index.html` öffnen (Endlosschleife) oder `index.html?t=12.5` für einen einzelnen Zeitpunkt.
- Texte, Zahlen und Timing stehen direkt in `index.html` (Timeline am Ende der Datei).
- Neu rendern (benötigt Node, Playwright + Chromium, ffmpeg):
  ```
  npm i playwright   # falls nicht vorhanden
  node render.mjs woodmatch-reel-9x16.mp4
  node render.mjs --stills 2,10,29   # einzelne PNG-Vorschaubilder
  ```
