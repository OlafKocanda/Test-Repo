# WoodMatch – Karussell-Posts (Instagram & Facebook)

Format: **1080×1350 px (4:5)**, PNG, je Slide eine Datei in `export/<karussell>/01.png …`.
Alle Karussells ohne Fotos – illustrierter Wald, Höhenlinien und nachgebaute App-Screens. Hintergrund, Wald und Wanderweg laufen als Panorama über alle Slides und machen Lust aufs Weiterwischen.

| Karussell | Slides | Idee | Ziel |
|---|---|---|---|
| `karussell-1-fragen` – „Weißt du, was in deinem Wald steckt?“ | 7 | 5 Fragen, die sich fast jeder Waldbesitzer stellt, je mit Antwort aus der App | Neugier, Reichweite, Speichern |
| `karussell-2-kostenlos` – „Was kostet WoodMatch?“ | 6 | 0 € · kein Abo · keine Grundgebühr · Provision nur bei Vermittlung | Vertrauen, Einwand „Was kostet das?“ ausräumen |
| `karussell-3-so-gehts` – „So wird dein Wald digital“ | 6 | Anleitung in 3 Schritten (+ Bonus) mit App-Screens | Registrierung, Retargeting |

Beispielwerte (Flur 23 · 7, 45 % Fichte, 1.920 Fm, ≈ 96 T€) sind als **BEISPIEL** gekennzeichnet.

## Beitragstexte

**Karussell 1**
> Weißt du, was in deinem Wald steckt? 🌲 Wo genau liegen deine Flurstücke, welche Bäume stehen drin, wie viel Holz ist da – und wer hilft dir weiter? 👉 Wisch dich durch die 5 Fragen.
> Alle Antworten findest du kostenlos auf app.woodmatch.de
> #Privatwald #Waldbesitzer #Wald #Forstwirtschaft #Waldumbau #WoodMatch

**Karussell 2**
> „Was kostet WoodMatch?“ – die Frage hören wir am häufigsten. Die ehrliche Antwort: 0 € Nutzungsgebühr. Kein Abo, keine Grundgebühr, keine versteckten Kosten. Wie wir trotzdem Geld verdienen? Wisch mal rüber 👉
> #Privatwald #Waldbesitzer #Forstwirtschaft #WoodMatch

**Karussell 3**
> Dein Wald – digital in 3 Schritten: Flurstück suchen, Wald verstehen, Maßnahmen planen. Ganz ohne forstliches Fachwissen. 💻🌳
> Jetzt kostenlos starten: app.woodmatch.de
> #Privatwald #Waldbesitzer #Digitalisierung #Forst #WoodMatch

## Tipps
- Als **Karussell-Anzeige** im Werbeanzeigenmanager: jede Slide als eigene Karte, Ziel-URL auf allen Karten `app.woodmatch.de`, „Die besten Karten zuerst anzeigen“ **aus** (die Reihenfolge erzählt die Geschichte).
- Für den A/B-Test gegen die Videos eignet sich Karussell 1 (gleiche Botschaft, anderes Format).

## Neu rendern
```
node capture-laptop.mjs            # App-Screens aus ../index.html als Laptop-PNGs
node render-carousel.mjs karussell-1-fragen.html
```
