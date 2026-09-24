# WoodMatch – Werbeclip für Instagram & Facebook

**Datei:** `woodmatch-reel-9x16.mp4` · 1080×1920 (9:16) · 30 s · 30 fps · H.264, ohne Ton
Passt für Instagram Reels/Stories, Facebook Reels/Stories und als 9:16-Anzeige im Meta-Werbeanzeigenmanager.

## Ablauf
| Zeit | Szene | Botschaft |
|---|---|---|
| 0–3,5 s | Waldfoto, Hook | „Du hast Wald? Und weißt nicht genau, wo er liegt, was drinsteht – und was er wert ist?“ |
| 3,5–7 s | Logo | WoodMatch – Die Plattform für Privatwaldbesitzer |
| 7–11,5 s | 01 Wald finden | Flurnummer eingeben → Flurstücke auf der Karte |
| 11,5–16 s | 02 Wald verstehen | Fläche, Baumarten, Holzvorrat (Dashboard) |
| 16–20,5 s | 03 Profis finden | Maßnahme planen → Angebote geprüfter Forstprofis, Förderung |
| 20,5–25 s | 04 Holz verkaufen | Polter anlegen → Angebot vom Sägewerk |
| 25–30 s | Call-to-Action | „Dein Wald. In deiner Hand.“ · Kostenlos starten · app.woodmatch.de |

## Vorschlag Beitragstext

> Du hast Wald – aber keinen Überblick? 🌲
>
> Mit WoodMatch findest du deine Flurstücke per Flurnummer, siehst Fläche, Baumarten und Holzvorrat auf einen Blick, findest geprüfte Forstprofis und verkaufst dein Holz direkt – ohne Zwischenhandel.
>
> ✅ Kostenlos & unverbindlich
> ✅ Auch ohne forstliches Fachwissen
> ✅ Bereits 340 Waldbesitzer & 1.200+ Hektar
>
> 👉 Jetzt starten: app.woodmatch.de
>
> #Privatwald #Waldbesitzer #Forstwirtschaft #Wald #Holzverkauf #Waldumbau #Nachhaltigkeit #WoodMatch

## Hinweise
- **Musik:** Das Video hat bewusst keine Tonspur. Lizenzfreie Musik direkt in Instagram/Facebook aus der Musikbibliothek wählen (bei Anzeigen: „Sound Collection“ von Meta).
- Beispieldaten im Clip (Waldemar, Polter „Althang“, 89 €/Efm, Anbieternamen) sind illustrativ – angelehnt an die Mockups auf woodmatch.de.
- Die Zahlen im CTA (1.200+ ha, 340 Waldbesitzer, 0 €) stammen von woodmatch.de – vor dem Posten auf Aktualität prüfen.

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
