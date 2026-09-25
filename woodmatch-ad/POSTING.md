# WoodMatch – Werbeclip für Instagram & Facebook

**Datei:** `woodmatch-reel-9x16.mp4` · 1080×1920 (9:16) · 38 s · 30 fps · H.264 + AAC-Ton
Passt für Instagram Reels/Stories, Facebook Reels/Stories und als 9:16-Anzeige im Meta-Werbeanzeigenmanager.

Die App-Oberflächen sind **nach den echten Screenshots nachgebaut** (HTML) und animiert: Mauszeiger, Eingaben, hochzählende Kennzahlen, Kamerafahrten. Beispielnutzer: *Waldemar Holzhausen*, alle Flurstücks- und Objektdaten sind fiktiv.

## Ablauf
| Zeit | Szene | Animation |
|---|---|---|
| 0–2,6 s | Hook (Waldfoto) | „Du hast Wald? Hol mehr aus ihm raus.“ |
| 2,6–5 s | Logo | WoodMatch – Die Plattform für Privatwaldbesitzer |
| 5–9,8 s | 01 Überblick | „Guten Morgen, Waldemar“ – Kennzahlen zählen hoch, Zoom auf Handlungsempfehlungen (Score 49) |
| 9,8–14,8 s | 02 Flurstücke | Klick „Flurstück suchen“, Eingabe „Holzhausen · Flur 23 · 7“, Treffer in Tabelle + Karte, Kartenebene „Baumart“ wird eingeschaltet |
| 14,8–19,2 s | 03 Objekte | „Neues Objekt“ → „Polter setzen“ → Klick in die Karte → „Polter angelegt · 48 Fm“ |
| 19,2–23,4 s | 04 Maßnahmen | Assistent: „Holzernte“ wählen → Weiter → 2 Objekte auf der Karte auswählen |
| 23,4–28 s | 05 **Nur bei WoodMatch: Marktplatz & Matching** | Suche: „Deine Flurstücke im Arbeitsgebiet“ → „Beitritt anfragen“ ✓ · danach **BALD:** automatisches Matching mit Forstprofis, Holzkäufern, Sägewerken – Musik-Drop hier |
| 28–32,8 s | Preis | Kostenlos starten. Kostenlos bleiben. Kein Abo · keine Grundgebühr · keine versteckten Kosten · Provision nur bei Vermittlung |
| 32,8–38 s | Call-to-Action | „Dein Wald. In deiner Hand.“ · Kostenlos starten · app.woodmatch.de |

## Vorschlag Beitragstext

> Du hast Wald – aber keinen Überblick? 🌲
>
> Mit WoodMatch siehst du deine Flurstücke mit Satelliten- und Geodaten, erfasst Bestände, Bäume und Polter – und planst Maßnahmen Schritt für Schritt und findest die FBG in deiner Nähe. Bald neu: automatisches Matching mit Forstprofis und Holzkäufern.
>
> ✅ Kostenlos starten – und kostenlos bleiben
> ✅ Kein Abo, keine Grundgebühr
> ✅ Auch ohne forstliches Fachwissen
>
> 👉 Jetzt starten: app.woodmatch.de
>
> #Privatwald #Waldbesitzer #Forstwirtschaft #Wald #Holzverkauf #Waldumbau #Nachhaltigkeit #WoodMatch

## Hinweise
- **Musik:** „Forest“ von Damtaro (freetouse.com), Ausschnitt ab 0:10,6 mit Ein-/Ausblendung. Bitte die Lizenzbedingungen von freetouse.com prüfen (ggf. Credit in der Beschreibung: „Music: Damtaro – Forest, freetouse.com“).
- Maßnahmen sind als verfügbar dargestellt, das automatische Matching als „BALD“. Keine Nutzer-/Flächenzahlen im Video.
- Die Kennzahlen im Dashboard (6,6 ha, 1.920 Fm, ≈ 96.000 €, 1.760 t) sind Beispielwerte der fiktiven Person.

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
