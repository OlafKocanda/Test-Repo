"""Erzeugt eine eigene, lizenzfreie Hintergrundmusik für die WoodMatch-Videos.

Komplett per Code synthetisiert (keine Samples, keine fremden Aufnahmen), daher
frei für Anzeigen nutzbar. Ruhiger Aufbau in D-Dur, ab ca. 20 s kommen Beat und
Melodie dazu.

Nutzung: python3 make_music.py [ausgabe.wav] [dauer_s]
"""
import sys
import wave

import numpy as np

SR = 44100
BPM = 96
BEAT = 60 / BPM
BAR = 4 * BEAT
OUT = sys.argv[1] if len(sys.argv) > 1 else "woodmatch-musik.wav"
DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 40.0
N = int(SR * DUR)
rng = np.random.default_rng(7)


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


# D – A – Bm – G (MIDI-Grundtöne + Akkordtöne)
CHORDS = [
    (50, [62, 66, 69]),  # D
    (45, [61, 64, 69]),  # A
    (47, [62, 66, 71]),  # Bm
    (43, [62, 67, 71]),  # G
]


def env(n, a, r):
    e = np.ones(n)
    na, nr = int(a * SR), int(r * SR)
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


def lowpass(x, cutoff):
    # Einfacher Tiefpass 1. Ordnung, zweimal angewendet, über FFT (schnell)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    h = 1 / (1 + (f / cutoff) ** 4)
    return np.fft.irfft(np.fft.rfft(x) * h, len(x))


def add(buf, sig, t):
    i = int(t * SR)
    j = min(len(buf), i + len(sig))
    if i < len(buf):
        buf[i:j] += sig[: j - i]


def pad_note(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = sum(np.sin(2 * np.pi * freq * d * t + rng.uniform(0, 6)) for d in (0.996, 1.0, 1.004))
    s += 0.3 * sum(np.sin(2 * np.pi * 2 * freq * d * t) for d in (0.998, 1.002))
    return s * env(n, 0.9, 0.9)


def pluck(freq, dur=1.6):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 7):
        s += np.sin(2 * np.pi * freq * k * t) / k * np.exp(-t * (2.5 + 1.8 * k))
    return s * env(n, 0.003, 0.05)


def bell(freq, dur=2.5):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.4 * np.sin(2 * np.pi * freq * 2.01 * t) * np.exp(-t * 3)
    return s * np.exp(-t * 1.6) * env(n, 0.005, 0.1)


def bass(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    return (np.sin(2 * np.pi * freq * t) + 0.25 * np.sin(4 * np.pi * freq * t)) * env(n, 0.02, 0.3)


def kick():
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    f = 50 + 70 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def shaker():
    n = int(0.09 * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n) * np.exp(-t * 55)
    return np.diff(np.concatenate([[0], x]))  # Hochpass-Charakter


pad, pl, bl, bs, dr = (np.zeros(N) for _ in range(5))
bars = int(np.ceil(DUR / BAR))
DROP = 8  # ab Takt 9 (≈ 20 s) Beat und Melodie
MELODY = [(0, 74), (1.5, 76), (2, 78), (3, 76)]  # Beat-Offset, MIDI

for b in range(bars):
    t0 = b * BAR
    root, notes = CHORDS[b % 4]
    for m in notes:
        add(pad, pad_note(hz(m - 12), BAR + 0.9), t0)
    arp = [notes[0], notes[1], notes[2], notes[1] + 12, notes[2], notes[1], notes[0] + 12, notes[2]]
    vol = 0.35 if b < 4 else 0.7
    for i, m in enumerate(arp):
        add(pl, pluck(hz(m)) * vol * (1.0 if i % 2 == 0 else 0.75), t0 + i * BEAT / 2)
    if b >= 4:
        add(bs, bass(hz(root - 12), BAR * 0.95), t0)
    if b >= DROP:
        for k in range(4):
            add(dr, kick() * (1.0 if k in (0, 2) else 0.6), t0 + k * BEAT)
        for k in range(8):
            add(dr, shaker() * (0.14 if k % 2 else 0.07), t0 + k * BEAT / 2)
        if b % 2 == 0:
            for off, m in MELODY:
                add(bl, bell(hz(m + (0 if b % 4 == 0 else -2))), t0 + off * BEAT)
    elif b == DROP - 1:  # kleiner Aufbau vor dem Drop
        for k in range(8):
            add(dr, shaker() * 0.03 * (k + 1), t0 + BAR / 2 + k * BEAT / 16)

pad = lowpass(pad, 1400)
swell = np.clip(np.arange(N) / SR / 6, 0, 1)
dry = 0.16 * pad * swell + 0.22 * pl + 0.20 * bl + 0.30 * bs + 0.45 * dr


def reverb(x, seed):
    r = np.random.default_rng(seed)
    n = int(2.2 * SR)
    t = np.arange(n) / SR
    ir = r.standard_normal(n) * np.exp(-t * 3.2)
    ir[: int(0.02 * SR)] = 0
    L = len(x) + n
    y = np.fft.irfft(np.fft.rfft(x, L) * np.fft.rfft(ir, L), L)[: len(x)]
    return y / np.max(np.abs(y)) * np.max(np.abs(x))


wet_src = 0.16 * pad * swell + 0.22 * pl + 0.20 * bl
left = dry + 0.35 * reverb(wet_src, 1)
right = dry + 0.35 * reverb(wet_src, 2)
st = np.stack([left, right], 1)
st *= env(N, 0.8, 2.5)[:, None]
st = np.tanh(st / np.max(np.abs(st)) * 1.0)
st = st / np.max(np.abs(st)) * 0.89  # ≈ −1 dBFS

with wave.open(OUT, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print("fertig:", OUT, f"{DUR:.0f} s")
