"""Drei Musikstücke für die WoodMatch-Videos, gespielt mit echten Orchester-Samples (VSCO-2-CE, CC0).

Nutzung: python3 songs.py <aufbruch|morgenlicht|voran> <ausgabe.wav> <dauer_s> <hoehepunkt_takt>
  Der Höhepunkt (voller Refrain) beginnt am Anfang von <hoehepunkt_takt>.
  Taktlängen: aufbruch 2,4 s · morgenlicht 2,22 s · voran 2,0 s
Beispiel: python3 songs.py aufbruch musik-A.wav 38 10   # Höhepunkt bei 24 s
"""
import sys

from orchester import SR, Instrument, Track, mixdown, peak_time, piano_map

PERC = "Percussion"
fixed = lambda n: 60  # noqa: E731  Schlagwerk ohne Tonhöhe


def strings_sus():
    return (Instrument("Strings/Violin Section/susVib", release=0.6, attack=0.06),
            Instrument("Strings/Viola Section/susvib", release=0.6, attack=0.06),
            Instrument("Strings/Cello Section/susvib", release=0.6, attack=0.06),
            Instrument("Strings/Solo Contrabass/SusNV", release=0.6, attack=0.05))


def drums():
    return dict(
        bd=Instrument(PERC, pattern="BDrumNewhit*", notemap=fixed, release=0.6),
        sn=Instrument(PERC, pattern="Snare2-HitNS*", notemap=fixed),
        crash=Instrument(PERC, pattern="cymbal-crash1_*", notemap=fixed),
        timp=Instrument("Percussion/Timpani", pattern="Timpani1_Hit*", notemap=lambda n: 41, tune=0.46, release=1.2),
    )


def swell_into(track, t_peak, path="Percussion/susCymb1-cresc-Median_v1.wav", gain=1.0):
    """Becken-Crescendo so anlegen, dass sein Höhepunkt genau auf t_peak fällt."""
    tp, x = peak_time(path)
    seg = x[: int((tp + 0.5) * SR)]
    start = t_peak - tp
    if start < 0:
        seg, start = seg[int(-start * SR):], 0.0
    track.add(seg, start, gain)


def final_hit(T, t, root, tones, vln, vla, vc, cb, dur, D, extra=()):
    T["vc"].note(vc, root + 12, t, dur, 0.9)
    T["cb"].note(cb, root, t, dur, 0.9)
    for m in tones:
        T["vla"].note(vla, m, t, dur, 0.85)
        T["vln"].note(vln, m + 12, t, dur, 0.85)
    T["perc"].note(D["crash"], 60, t, None, 1.0)
    T["bd"].note(D["bd"], 60, t, None, 1.0)
    for tr, inst, m in extra:
        T[tr].note(inst, m, t, dur, 0.85)


# ---------------------------------------------------------------------------
def aufbruch(dur, C):
    B = 60 / 100
    BAR = 4 * B
    CH = [(47, [59, 62, 66]), (43, [59, 62, 67]), (50, [62, 66, 69]), (45, [61, 64, 69])]  # Bm G D A
    MEL = [
        [[(0, 59, 1), (1, 62, 1), (2, 66, 2)], [(0, 67, 3), (3, 66, 1)], [(0, 66, 1), (1, 64, 1), (2, 62, 2)], [(0, 64, 4)]],
        [[(0, 62, 1), (1, 66, 1), (2, 71, 2)], [(0, 71, 3), (3, 69, 1)], [(0, 69, 1), (1, 66, 1), (2, 74, 2)], [(0, 73, 4)]],
    ]
    vln, vla, vc, cb = strings_sus()
    vln_s, vla_s, vc_s = (Instrument("Strings/Violin Section/Spic"), Instrument("Strings/Viola Section/spic"),
                          Instrument("Strings/Cello Section/spic"))
    cb_s = Instrument("Strings/Solo Contrabass/Spic")
    horn = Instrument("Brass/F Horn/sus", release=0.5, attack=0.05)
    tbn = Instrument("Brass/Tenor Trombone/sus", release=0.5, attack=0.05)
    D = drums()
    T = dict(
        vln=Track(dur, -0.4, 0.38, -21, hp=220), vla=Track(dur, 0.15, 0.38, -23, hp=130), vc=Track(dur, 0.35, 0.34, -22),
        cb=Track(dur, 0.45, 0.3, -25), mel=Track(dur, -0.25, 0.42, -18, hp=90),
        ost=Track(dur, 0.25, 0.28, -19, 0.004), ost_hi=Track(dur, -0.3, 0.3, -23, 0.004, hp=300),
        horn=Track(dur, -0.15, 0.45, -23, hp=100), bd=Track(dur, 0, 0.14, -21, 0.003), timp=Track(dur, 0.05, 0.25, -22, 0.003),
        perc=Track(dur, 0.1, 0.25, -26, 0.003, hp=150),
    )
    end = int((dur - 2.6) // BAR)
    for b in range(end):
        t0 = b * BAR
        i = (b - C) % 4
        r, tones = CH[i]
        climax, build = b >= C, C - 2 <= b < C
        verse = 1 <= b < C - 2
        late = verse and b >= (C - 1) // 2  # zweite Strophenhälfte: eine Schicht mehr
        v = 0.88 if climax else (0.7 + 0.08 * (b - C + 2) if build else 0.62)
        # Ostinato Celli + Kontrabass (3+3+2-Akzente)
        for k, m in enumerate([r, r, r, r + 12, r, r, r + 12, r + 7]):
            acc = k in (0, 3, 6)
            T["ost"].note(vc_s, m, t0 + k * B / 2, None, v if acc else v - 0.2)
            if b >= 1 and acc:
                T["ost"].note(cb_s, r - 12, t0 + k * B / 2, None, v)
        # Bratschen 8tel ab Takt 2
        if b >= 1:
            for k in range(8):
                T["vla"].note(vla_s, tones[1 + k % 2], t0 + k * B / 2, None, v - 0.15)
        # Geigen: 8tel in der zweiten Strophenhälfte, 16tel ab dem Aufbau
        if late:
            for k in range(8):
                T["ost_hi"].note(vln_s, [tones[2] + 12, tones[1] + 12][k % 2], t0 + k * B / 2, None, v - 0.2)
        if verse:
            T["vc"].note(vc, r, t0, BAR, 0.5, attack=0.3)
            T["cb"].note(cb, r - 12, t0, BAR, 0.5, attack=0.3)
        if build or climax:
            seq = [tones[0] + 12, tones[1] + 12, tones[2] + 12, tones[1] + 12]
            for k in range(16):
                T["ost_hi"].note(vln_s, seq[k % 4], t0 + k * B / 4, None, (v - 0.1) if k % 4 == 0 else v - 0.25)
        # Schwebender Geigen-Ton im Intro
        if not climax:
            T["vln"].note(vln, tones[2] + 12, t0, BAR, 0.3 + 0.1 * build, attack=0.6)
        # Hörner im Aufbau als Crescendo-Fläche
        if build:
            for m in tones[1:]:
                T["horn"].note(horn, m - 12, t0, BAR, v - 0.1, attack=0.8)
        # Höhepunkt: Melodie (Hörner + Posaune, Geigen eine Oktave höher), Streicherflächen
        if climax:
            for off, m, ln in MEL[((b - C) // 4) % 2][i]:
                T["mel"].note(horn, m, t0 + off * B, ln * B, 0.85)
                T["mel"].note(tbn, m - 12, t0 + off * B, ln * B, 0.7)
                T["vln"].note(vln, m + 12, t0 + off * B, ln * B, 0.8)
            T["vc"].note(vc, r, t0, BAR, 0.75)
            T["cb"].note(cb, r - 12, t0, BAR, 0.75)
            for m in tones[1:]:
                T["vla"].note(vla, m, t0, BAR, 0.65)
        # Schlagwerk
        if verse:
            for k in (0, 2):
                T["bd"].note(D["bd"], 60, t0 + k * B, None, 0.55)
            T["timp"].note(D["timp"], {47: 47, 43: 43, 50: 38, 45: 45}[r], t0, None, 0.5)
        if build:
            for k in (0, 3, 6):
                T["bd"].note(D["bd"], 60, t0 + k * B / 2, None, 0.6)
            for k in (0, 2):
                T["timp"].note(D["timp"], 38 if i % 2 else 45, t0 + k * B, None, v)
            if b == C - 1:  # Snare-Wirbel in den Höhepunkt
                for k in range(16):
                    T["perc"].note(D["sn"], 60, t0 + 2 * B + k * B / 8, None, 0.25 + 0.04 * k)
        if climax:
            for k in (0, 3, 6):
                T["bd"].note(D["bd"], 60, t0 + k * B / 2, None, 0.9)
                T["timp"].note(D["timp"], {47: 47, 43: 43, 50: 38, 45: 45}[r], t0 + k * B / 2, None, 0.85)
            for k in (1, 3):
                T["perc"].note(D["sn"], 60, t0 + k * B, None, 0.6)
            if (b - C) % 4 == 0:
                T["perc"].note(D["crash"], 60, t0, None, 0.9 if b == C else 0.6)
    swell_into(T["perc"], C * BAR)
    t_end = end * BAR
    final_hit(T, t_end, 38, [62, 66, 69], vln, vla, vc, cb, dur - t_end, D,
              extra=[("mel", horn, 62), ("mel", horn, 66), ("mel", tbn, 50)])
    T["timp"].note(D["timp"], 38, t_end, None, 1.0)
    return list(T.values())


# ---------------------------------------------------------------------------
def morgenlicht(dur, C):
    B = 60 / 108
    BAR = 4 * B
    CH = [(43, [67, 71, 74]), (38, [66, 69, 74]), (40, [64, 67, 71]), (36, [64, 67, 72])]  # G D Em C
    MEL = [
        [[(0, 71, 1.5), (1.5, 74, 0.5), (2, 79, 2)], [(0, 78, 1), (1, 76, 1), (2, 74, 2)],
         [(0, 76, 1.5), (1.5, 79, 0.5), (2, 83, 2)], [(0, 81, 1), (1, 79, 1), (2, 76, 1), (3, 74, 1)]],
        [[(0, 74, 1.5), (1.5, 79, 0.5), (2, 83, 2)], [(0, 81, 1), (1, 78, 1), (2, 74, 2)],
         [(0, 79, 1), (1, 83, 1), (2, 86, 2)], [(0, 84, 1), (1, 83, 1), (2, 79, 2)]],
    ]
    vln, vla, vc, cb = strings_sus()
    piano = Instrument("Keys/Upright Piano", notemap=piano_map, release=0.5)
    vc_p = Instrument("Strings/Cello Section/pizzT")
    vln_p = Instrument("Strings/Violin Section/Pizz")
    glock = Instrument("Percussion/Glock", release=1.5)
    horn = Instrument("Brass/F Horn/sus", release=0.6, attack=0.1)
    tamb = Instrument(PERC, pattern="Tamb1-Hit*", notemap=fixed)
    D = drums()
    T = dict(
        pno=Track(dur, 0.0, 0.26, -18, 0.005), vln=Track(dur, -0.35, 0.4, -19, hp=220), vla=Track(dur, 0.15, 0.38, -24, hp=130),
        vc=Track(dur, 0.35, 0.34, -23), cb=Track(dur, 0.45, 0.3, -26), pizz=Track(dur, 0.3, 0.25, -23, 0.004),
        pizz_hi=Track(dur, -0.3, 0.28, -26, 0.004, hp=250), glock=Track(dur, -0.1, 0.35, -26, hp=500),
        horn=Track(dur, -0.2, 0.45, -26, hp=100), bd=Track(dur, 0, 0.14, -22, 0.003),
        perc=Track(dur, 0.15, 0.2, -25, 0.004, hp=150), timp=Track(dur, 0, 0.2, -30),
    )
    end = int((dur - 2.6) // BAR)
    for b in range(end):
        t0 = b * BAR
        i = (b - C) % 4
        r, tn = CH[i]
        climax, build = b >= C, C - 2 <= b < C
        verse = 1 <= b < C - 2
        late = verse and b >= (C - 1) // 2
        pv = 0.8 if climax else (0.65 if build else (0.58 if verse else 0.5))
        t = [tn[0], tn[1], tn[2], tn[0] + 12]
        for k, j in enumerate([0, 1, 2, 1, 3, 1, 2, 1]):
            T["pno"].note(piano, t[j], t0 + k * B / 2, B * 0.9, pv if k % 4 == 0 else pv - 0.12)
        T["pno"].note(piano, r, t0, 2 * B, pv)
        T["pno"].note(piano, r + 12, t0, 2 * B, pv - 0.1)
        T["pno"].note(piano, r + 12, t0 + 2 * B, 2 * B, pv - 0.2)
        if b >= 1:
            for k in (0, 1.5, 2, 3.5) if (climax or build) else (0, 2):
                T["pizz"].note(vc_p, r + 12, t0 + k * B, None, 0.7 if k in (0, 2) else 0.5)
        if b >= 2:
            for k in (1, 3, 5, 7):
                T["pizz_hi"].note(vln_p, tn[1 + (k // 2) % 2], t0 + k * B / 2, None, 0.45)
            if not climax:
                T["glock"].note(glock, tn[2] + 12, t0, None, 0.4)
        if verse:
            for k in (0, 2):
                T["bd"].note(D["bd"], 60, t0 + k * B, None, 0.45)
            if late:
                T["vc"].note(vc, r + 12, t0, BAR, 0.5, attack=0.4)
                for k in range(8):
                    T["perc"].note(tamb, 60, t0 + k * B / 2, None, 0.3 if k % 2 else 0.18)
        if build:
            for m in tn[:2]:
                T["vla"].note(vla, m - 12, t0, BAR, 0.6, attack=BAR * 0.9)
            T["vc"].note(vc, r + 12, t0, BAR, 0.6, attack=BAR * 0.9)
            for k in range(8):
                T["perc"].note(tamb, 60, t0 + k * B / 2, None, 0.25 + 0.03 * k + 0.1 * (b == C - 1))
            for k in (0, 2):
                T["bd"].note(D["bd"], 60, t0 + k * B, None, 0.45)
        if climax:
            for off, m, ln in MEL[((b - C) // 4) % 2][i]:
                T["vln"].note(vln, m, t0 + off * B, ln * B, 0.85)
                T["glock"].note(glock, m + 12, t0 + off * B, None, 0.5)
            for m in tn[:2]:
                T["vla"].note(vla, m - 12, t0, BAR, 0.65)
                T["horn"].note(horn, m - 12, t0, BAR, 0.55)
            T["vc"].note(vc, r + 12, t0, BAR, 0.7)
            T["cb"].note(cb, r, t0, BAR, 0.7)
            for k in (0, 2, 2.5):
                T["bd"].note(D["bd"], 60, t0 + k * B, None, 0.8 if k != 2.5 else 0.55)
            for k in (1, 3):
                T["perc"].note(D["sn"], 60, t0 + k * B, None, 0.55)
            for k in range(8):
                T["perc"].note(tamb, 60, t0 + k * B / 2, None, 0.5 if k % 2 else 0.3)
            if (b - C) % 4 == 0:
                T["perc"].note(D["crash"], 60, t0, None, 0.85 if b == C else 0.55)
    swell_into(T["perc"], C * BAR, gain=0.8)
    t_end = end * BAR
    final_hit(T, t_end, 31, [67, 71, 74], vln, vla, vc, cb, dur - t_end, D,
              extra=[("pno", piano, 43), ("pno", piano, 55), ("pno", piano, 71), ("pno", piano, 79), ("horn", horn, 59)])
    T["glock"].note(glock, 91, t_end, None, 0.6)
    return list(T.values())


# ---------------------------------------------------------------------------
def voran(dur, C):
    B = 60 / 120
    BAR = 4 * B
    S = B / 4
    CH = [(45, [69, 73, 76]), (38, [66, 69, 74]), (42, [66, 69, 73]), (40, [64, 68, 71])]  # A D F#m E
    MEL = [
        [[(0, 76, 1), (1, 73, .5), (1.5, 76, .5), (2, 81, 2)], [(0, 78, 1), (1, 76, 1), (2, 74, 1), (3, 73, 1)],
         [(0, 73, 1), (1, 69, .5), (1.5, 73, .5), (2, 78, 2)], [(0, 76, 1.5), (1.5, 74, .5), (2, 71, 2)]],
        [[(0, 81, 1), (1, 80, .5), (1.5, 81, .5), (2, 85, 2)], [(0, 86, 1), (1, 85, 1), (2, 83, 1), (3, 81, 1)],
         [(0, 81, 1), (1, 78, .5), (1.5, 81, .5), (2, 85, 2)], [(0, 83, 2), (2, 80, 2)]],
    ]
    vln, vla, vc, cb = strings_sus()
    mar = Instrument("Percussion/Marimba", release=0.4)
    harp = Instrument("Strings/Harp", octave_shift=1, release=0.8)
    vc_p = Instrument("Strings/Cello Section/pizzT")
    vln_p = Instrument("Strings/Violin Section/Pizz")
    flute = Instrument("Woodwinds/Flute/susvib", release=0.25, attack=0.03)
    clar = Instrument("Woodwinds/Clarinet/susLong", release=0.25, attack=0.03)
    horn = Instrument("Brass/F Horn/sus", release=0.6, attack=0.15)
    shak = Instrument(PERC, pattern="Tamb1-Shake*", notemap=fixed)
    tamb = Instrument(PERC, pattern="Tamb1-Hit*", notemap=fixed)
    clav = Instrument(PERC, pattern="Claves1*", notemap=fixed)
    conga = Instrument(PERC, pattern="Conga-HitN*", notemap=fixed)
    frame = Instrument("Miscellania Raw/Misc 2", pattern="rtomtom_frame*", notemap=fixed)
    D = drums()
    T = dict(
        mar=Track(dur, -0.2, 0.25, -19, 0.004), harp=Track(dur, 0.3, 0.35, -23, 0.004), pizz=Track(dur, 0.25, 0.25, -21, 0.004),
        pizz_hi=Track(dur, -0.35, 0.28, -26, 0.004, hp=250), mel=Track(dur, -0.1, 0.35, -18, hp=150),
        vla=Track(dur, 0.15, 0.38, -25, hp=130), vc=Track(dur, 0.35, 0.34, -24), cb=Track(dur, 0.45, 0.3, -27),
        horn=Track(dur, -0.25, 0.45, -26, hp=100), bd=Track(dur, 0, 0.12, -21, 0.003),
        groove=Track(dur, 0.2, 0.18, -25, 0.003), perc=Track(dur, -0.1, 0.18, -25, 0.003, hp=200),
        vln=Track(dur, -0.4, 0.4, -28, hp=220),
    )
    end = int((dur - 2.6) // BAR)
    for b in range(end):
        t0 = b * BAR
        i = (b - C) % 4
        r, tn = CH[i]
        climax, build = b >= C, C - 2 <= b < C
        mv = 0.85 if climax else (0.7 if build else 0.55)
        notes = [tn[0] - 12, tn[2] - 12, tn[0], tn[1], tn[2] - 12, tn[0]]
        for k, st in enumerate([0, 3, 6, 8, 11, 14]):
            T["mar"].note(mar, notes[k], t0 + st * S, None, mv if st in (0, 8) else mv - 0.15)
        for st in [0, 6, 8, 14] if b >= 1 else [0, 8]:
            T["pizz"].note(vc_p, r + 12 if st in (0, 8) else r + 19, t0 + st * S, None, 0.75 if st in (0, 8) else 0.55)
        if b >= 2:
            arp = [r + 12, r + 19, r + 24, tn[1], tn[2], tn[0] + 12, tn[1] + 12, tn[2] + 12]
            for k, m in enumerate(arp):
                T["harp"].note(harp, m, t0 + k * B / 2, None, 0.5 if not climax else 0.6)
        # Groove
        for st in [0, 8] if not climax else [0, 8, 10]:
            T["groove"].note(frame, 60, t0 + st * S, None, 0.6 if st != 10 else 0.4)
        if b >= 1:
            for st in range(16):
                T["perc"].note(shak, 60, t0 + st * S, None, 0.35 if st % 2 else 0.2)
            for st in (0, 3, 6, 10, 12):
                T["groove"].note(clav, 60, t0 + st * S, None, 0.3)
            for st in (7, 15):
                T["groove"].note(conga, 60, t0 + st * S, None, 0.5)
        if build or climax:
            for k in (1, 3, 5, 7):
                T["pizz_hi"].note(vln_p, tn[1 + (k // 2) % 2], t0 + k * B / 2, None, 0.5)
        if build:
            for m in tn[:2]:
                T["vla"].note(vla, m - 12, t0, BAR, 0.6, attack=BAR * 0.9)
            T["vc"].note(vc, r + 12, t0, BAR, 0.6, attack=BAR * 0.9)
            if b == C - 1:
                for k in range(8):
                    T["groove"].note(conga, 60, t0 + 2 * B + k * B / 4, None, 0.35 + 0.07 * k)
        if climax:
            for off, m, ln in MEL[((b - C) // 4) % 2][i]:
                T["mel"].note(flute, m, t0 + off * B, ln * B * 0.95, 0.8)
                T["mel"].note(clar, m - 12, t0 + off * B, ln * B * 0.95, 0.6)
            for m in tn[:2]:
                T["vla"].note(vla, m - 12, t0, BAR, 0.6)
            T["vc"].note(vc, r + 12, t0, BAR, 0.65)
            T["cb"].note(cb, r, t0, BAR, 0.65)
            T["horn"].note(horn, tn[0] - 12, t0, BAR, 0.5)
            for k in (0, 2):
                T["bd"].note(D["bd"], 60, t0 + k * B, None, 0.8)
            for k in (1, 3):
                T["perc"].note(tamb, 60, t0 + k * B, None, 0.8)
                T["perc"].note(D["sn"], 60, t0 + k * B, None, 0.4)
            if (b - C) % 4 == 0:
                T["perc"].note(D["crash"], 60, t0, None, 0.8 if b == C else 0.5)
    swell_into(T["perc"], C * BAR, "Percussion/susCymb1-cresc-Short_v1.wav", gain=0.8)
    t_end = end * BAR
    final_hit(T, t_end, 33, [69, 73, 76], vln, vla, vc, cb, dur - t_end, D,
              extra=[("harp", harp, 45), ("harp", harp, 57), ("harp", harp, 69), ("harp", harp, 81), ("mar", mar, 69),
                     ("mel", flute, 81), ("mel", clar, 69)])
    return list(T.values())


SONGS = {"aufbruch": aufbruch, "morgenlicht": morgenlicht, "voran": voran}

if __name__ == "__main__":
    name, out, dur, climax = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
    tracks = SONGS[name](dur, climax)
    mixdown(tracks, dur, out)
    print("fertig:", out)
