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

---

# Variante B – „Waldemars Geschichte“ (A/B-Test)

**Datei:** `woodmatch-reel-B-story.mp4` · 1080×1920 (9:16) · 31 s · 30 fps · H.264 + AAC-Ton
**Quelle:** `variante-b.html` · rendern mit `PAGE=variante-b.html MUSIC_START=7 node render.mjs woodmatch-reel-B-story.mp4`

## Idee
Variante A erklärt das **Produkt** (schnelle Feature-Demo in der App). Variante B erzählt eine **Geschichte**: ruhig, filmisch, emotional – für die typische Zielgruppe (Privatwaldbesitzer, häufig 50+, oft geerbter Wald ohne forstliches Vorwissen). Wenig Text pro Bild, große Untertitel (funktioniert ohne Ton), echte Menschen statt UI.

| Zeit | Einstellung | Untertitel |
|---|---|---|
| 0–4 s | Waldemar am Waldrand im Morgennebel (Kinobalken fahren auf) | „Das ist Waldemar.“ · „Er hat 6 Hektar Wald geerbt.“ |
| 4–8,5 s | Alte Flurkarte am Küchentisch | „Aber wo genau liegt er?“ · „Was steht drin?“ · „Und was ist er wert?“ |
| 8,5–12 s | Schwarzblende | „Früher: Aktenordner, Telefonate & Fragezeichen.“ → **WoodMatch** |
| 12–20,5 s | Waldemar mit Laptop am Waldweg + Glas-Karten aus der App | „Heute hat Waldemar seinen Wald im Griff.“ – 8 Flurstücke · 6,6 ha → Holzvorrat/-wert → FBG ✓ Beitritt angefragt |
| 20,5–25 s | Handschlag mit Forstunternehmer vor Holzpolter | „Maßnahmen planen – und umsetzen.“ |
| 25–31 s | Blick in die Baumkronen → CTA | „Weil jeder Wald eine Zukunft verdient.“ → „Und dein Wald? Dein Wald. In deiner Hand.“ · Kostenlos starten · Kein Abo |

Musik: gleicher Track wie A (Damtaro – Forest), Ausschnitt ab 0:07 – ruhiger Aufbau, der Drop fällt auf den CTA.

**Bilder:** KI-generiert mit Canva (Waldemar ist eine fiktive Person). Exportiert aus dem Canva-Design „WoodMatch Instagram-Story-Container“.

## Empfehlung für den A/B-Test
- **Gleich halten:** Zielgruppe, Budget, Laufzeit, Platzierung (Reels + Stories), Beitragstext, CTA-Button („Mehr dazu“ / „Registrieren“), Ziel-URL. Nur das Video unterscheidet sich.
- **Meta A/B-Test** im Werbeanzeigenmanager („A/B-Test erstellen“ → Variable *Creative*), mind. 7 Tage bzw. bis ~100 Registrierungen pro Variante.
- **Kennzahlen:** Hook-Rate (3-Sek.-Views / Impressionen), ThruPlay-Rate, Link-CTR, Kosten pro Registrierung. Erwartung: B hält Ältere länger (Watchtime), A bringt technikaffinere Nutzer mit höherer Klickabsicht – entscheidend ist **Kosten pro Registrierung**.
- **Hinweis Transparenz:** KI-generierte, fotorealistische Bilder – Meta kennzeichnet solche Inhalte ggf. automatisch („KI-Info“). Optional in der Anzeige offenlegen.
