// Inhalte der Blog-Karussells. Alle Zahlen stammen aus den Artikeln auf woodmatch.de/wissen (Stand 09/2026).
// Slide-Typen: cover, text, list, stats, big, cta. <em>…</em> = grün hervorgehoben.
const BLOG = {
  waldwert: {
    url: 'woodmatch.de/blog/waldwert',
    slides: [
      { t: 'cover', kick: 'Ratgeber', h: 'Was ist dein Wald 2026 <em>wert?</em>', p: 'Holzpreise, Methoden und eine Beispielrechnung.' },
      { t: 'text', kick: 'Erst mal wichtig', h: 'Waldwert ist mehr als der <em>Holzpreis.</em>', p: 'Er setzt sich zusammen aus stehendem Holzvorrat, Boden, Lage und Zuwachs.', card: 'Laubholz zieht 2026 an, Nadelholz kämpft weiter mit Überangebot.' },
      { t: 'stats', kick: 'Holzpreise 2026', h: 'Was bringt <em>Stammholz?</em>', note: 'Richtwerte Mitteldeutschland, je Festmeter', rows: [['Fichte', '85–110 €'], ['Douglasie', '95–130 €'], ['Buche', '80–115 €'], ['Eiche', '180–350 €']] },
      { t: 'stats', kick: 'Beispielrechnung', h: '8 ha Buche, <em>80 Jahre,</em> Hessen', rows: [['Holzvorrat', '2.240 fm'], ['Bruttoerlös', '180.320 €'], ['Erntekosten (35 €/fm)', '−78.400 €'], ['Netto-Holzwert', '≈ 101.920 €']], hl: 3 },
      { t: 'big', kick: 'Achtung Schadholz', big: 'bis −60 %', h: 'Kalamitätspreise liegen <em class="nw">40–60 %</em> unter Normalpreisen.', p: 'Der richtige Verkaufszeitpunkt zählt.' },
      { t: 'cta', h: 'Deinen Holzwert <em>in Sekunden</em> sehen.', p: 'Flurnummer eingeben, WoodMatch schätzt Vorrat und Wert. Kostenlos.' },
    ],
  },
  geerbt: {
    url: 'woodmatch.de/blog/geerbt',
    slides: [
      { t: 'cover', kick: 'Ratgeber', h: 'Wald geerbt – <em>und jetzt?</em>', p: 'Behalten, verpachten oder verkaufen: drei Szenarien.' },
      { t: 'list', kick: 'Schritt 1', h: 'Vor jeder Entscheidung <em>klären:</em>', items: ['Eigentumsverhältnisse', 'Zustand des Bestands', 'Bestehende Pachtverträge', 'Steuerliche Situation'] },
      { t: 'big', kick: 'Szenario 1 · Behalten', big: '80–120 T€', h: 'Netto-Holzwert bei <em>10 ha Mischwald</em> mittlerer Bonität.', p: 'Wertzuwachs 500–700 €/ha im Jahr. Braucht aber Zeit und Lernbereitschaft.' },
      { t: 'big', kick: 'Szenario 2 · Verpachten', big: '10–40 €', h: 'Pacht pro Hektar und Jahr, bei 10 ha also <em>100–400 € im Jahr.</em>', p: 'Passives Einkommen, der Vertrag muss aber genau passen.' },
      { t: 'text', kick: 'Szenario 3 · Verkaufen', h: 'Sofort Geld – <em>aber mit Kosten.</em>', p: 'Notarkosten liegen bei ca. 1,5–2 % des Kaufpreises. Bei Verkauf innerhalb von 10 Jahren nach Erwerb kann Spekulationssteuer anfallen.', card: 'Erbengemeinschaft? Entscheidungen brauchen grundsätzlich Einstimmigkeit (§ 2038 BGB).' },
      { t: 'cta', h: 'Erst mal <em>verstehen,</em> was du geerbt hast.', p: 'Mit WoodMatch siehst du Fläche, Baumarten und Holzwert, und findest die FBG in deiner Nähe.' },
    ],
  },
  borkenkaefer: {
    url: 'woodmatch.de/blog/borkenkafer',
    slides: [
      { t: 'cover', kick: 'Checkliste', h: 'Borkenkäfer <em>früh erkennen.</em>', p: 'Der 5-Punkte-Check für deinen Wald.' },
      { t: 'list', kick: 'Die 5 Warnsignale', h: 'Darauf <em>achten:</em>', num: true, items: ['Bohrmehl am Stammfuß', 'Harztropfen an der Rinde', 'Spechtspuren am Stamm', 'Abblätternde Rinde', 'Verfärbte Nadeln'] },
      { t: 'big', kick: 'Es geht schnell', big: '4–8', h: '<em>Wochen</em> vom ersten Einbohren bis zum Absterben des Baumes.', p: 'Je nach Wetterlage.' },
      { t: 'list', kick: 'Befall gefunden?', h: 'Jetzt <em>sofort handeln:</em>', num: true, items: ['Bäume markieren, Dienstleister informieren', 'Einschlag und Abtransport in 3–4 Wochen', 'Holz entrinden oder nass lagern', 'Alles dokumentieren'] },
      { t: 'text', kick: 'Routine', h: 'Von April bis August <em>alle 4–6 Wochen</em> durch den Bestand gehen.', p: 'Langfristig senkt ein standortgerechter Mischwald mit Laubholz das Risiko.' },
      { t: 'cta', h: 'Befall erkennen, <em>Hilfe finden.</em>', p: 'Mit WoodMatch dokumentierst du Schäden und findest Forstdienstleister in deiner Region.' },
    ],
  },
  versicherung: {
    url: 'woodmatch.de/blog/waldversicherung',
    slides: [
      { t: 'cover', kick: 'Ratgeber', h: 'Waldversicherung: sinnvoll oder <em>Geld&shy;verschwendung?</em>', p: 'Bausteine, Kosten und die entscheidende Frage.' },
      { t: 'list', kick: 'Die Bausteine', h: 'Einzeln oder <em>kombiniert</em> versicherbar:', items: ['Waldbrand', 'Sturm und Schneebruch', 'Schadinsekten wie Borkenkäfer'] },
      { t: 'stats', kick: 'Was kostet das?', h: 'Beispiel <em>10 ha Mischwald</em>', note: 'Mittlere Risikoklasse, pro Hektar und Jahr', rows: [['Waldbrand', '8–18 €'], ['Sturm & Schneebruch', '22–45 €'], ['Borkenkäfer', '35–80 €'], ['Kombi-Paket', '60–120 €']], hl: 3 },
      { t: 'big', kick: 'Die Leitfrage', big: '?', h: 'Würde ein Totalschaden deine <em>Lebensplanung gefährden?</em>', p: 'Dann brauchst du eine Versicherung.' },
      { t: 'list', kick: 'Selbst-Check', h: 'Frag dich <em>ehrlich:</em>', num: true, items: ['Wie viel Holzwert steht im Bestand?', 'Könntest du einen Wiederaufbau überbrücken?', 'Liegt dein Wald in einer Risikozone?'] },
      { t: 'cta', h: 'Kenne deinen Holzwert, <em>bevor du versicherst.</em>', p: 'WoodMatch zeigt dir Bestand und Wert, die Basis für jede Entscheidung.' },
    ],
  },
  pflegevertrag: {
    url: 'woodmatch.de/blog/waldpflegevertrag',
    slides: [
      { t: 'cover', kick: 'Ratgeber', h: 'Wer kümmert sich, wenn du es <em>nicht selbst kannst?</em>', p: 'Der Waldpflegevertrag einfach erklärt.' },
      { t: 'text', kick: 'Das Prinzip', h: 'Du bleibst <em>Eigentümer und Entscheider.</em>', p: 'Ein Dienstleister übernimmt die Arbeit, die Erlöse bleiben bei dir. Anders als bei einer Pacht.' },
      { t: 'list', kick: 'Was dazugehört', h: 'Das kann ein <em>Profi</em> übernehmen:', items: ['Durchforstung und Bestandspflege', 'Pflanzung und Kulturpflege', 'Holzernte und Vermarktung', 'Verkehrssicherung', 'Hilfe bei Förderanträgen'] },
      { t: 'stats', kick: 'Preise 2026', h: 'Womit du <em>rechnen</em> kannst:', rows: [['Forstwirt', '45–70 €/h'], ['Holzernte', '18–30 €/fm'], ['Pflanzung', '1,50–4 €/Stück'], ['Komplettbetreuung', '30–90 €/ha/Jahr']] },
      { t: 'big', kick: 'Oft übersehen', big: '!', h: 'Ohne schriftliche Übertragung <em>haftest du weiter</em> für die Verkehrssicherung.', p: 'Das gehört ausdrücklich in den Vertrag.' },
      { t: 'cta', h: 'Den passenden <em>Partner</em> finden.', p: 'WoodMatch vermittelt dir die FBG und Forstprofis in deiner Region.' },
    ],
  },
  eudr: {
    url: 'woodmatch.de/blog/eudr',
    slides: [
      { t: 'cover', kick: 'Ratgeber', h: 'EUDR: Was heißt das <em>für deinen Wald?</em>', p: 'Die EU-Entwaldungsverordnung einfach erklärt.' },
      { t: 'text', kick: 'Worum geht es?', h: 'Wer Holz verkauft, braucht einen <em>Herkunftsnachweis.</em>', p: 'Er zeigt, dass das Holz nicht zur Entwaldung beigetragen hat. Das gilt schon beim Verkauf an das regionale Sägewerk.' },
      { t: 'list', kick: 'Wer ist betroffen?', h: 'Kurz <em>gesagt:</em>', items: ['Holzverkäufer: ja', 'Eigennutzer: in der Regel nicht', 'FBG-Mitglieder: Geodaten selbst liefern'] },
      { t: 'list', kick: 'Diese Nachweise', h: 'brauchst du <em>beim Verkauf:</em>', items: ['Geo-Koordinaten der Fläche', 'Erntedatum und -menge', 'Legalitätsnachweis'] },
      { t: 'list', kick: 'Deine To-dos', h: 'In 3 Schritten <em>vorbereitet:</em>', num: true, items: ['Flurstücke digital erfassen', 'Einschläge dokumentieren', 'Mit der FBG klären, wer meldet'] },
      { t: 'cta', h: 'Flurstücke erfassen, <em>Geodaten exportieren.</em>', p: 'Mit WoodMatch legst du deine Flächen digital an und exportierst sie als GeoJSON.' },
    ],
  },
};
