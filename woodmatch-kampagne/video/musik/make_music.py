"""Erzeugt eine eigene, lizenzfreie Hintergrundmusik für die WoodMatch-Videos.

Komplett per Code synthetisiert (keine Samples, keine fremden Aufnahmen), daher
frei für Anzeigen nutzbar. Motivierender Pop-Beat in D-Dur mit 122 BPM:
Beat ab Sekunde 2, Aufbau mit Riser, ab dem Drop-Takt volle Energie mit Melodie.

Nutzung: python3 make_music.py [ausgabe.wav] [dauer_s] [drop_takt]
  Ein Takt dauert ca. 1,97 s. Beispiele:
  python3 make_music.py musik-A.wav 38 11      # Drop ≈ 21,6 s (Marktplatz-Szene)
  python3 make_music.py musik-kurz.wav 19 4    # Drop ≈ 7,9 s
"""
import sys
import wave

import numpy as np

SR = 44100
BPM = 122
BEAT = 60 / BPM
BAR = 4 * BEAT
OUT = sys.argv[1] if len(sys.argv) > 1 else "woodmatch-musik.wav"
DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 40.0
DROP = int(sys.argv[3]) if len(sys.argv) > 3 else 8
N = int(SR * DUR)
rng = np.random.default_rng(7)


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


# Bm – G – D – A (vi–IV–I–V, der klassische „Aufbruch“-Loop)
CHORDS = [
    (47, [62, 66, 71]),  # Bm
    (43, [62, 67, 71]),  # G
    (50, [62, 66, 69]),  # D
    (45, [61, 64, 69]),  # A
]
# Melodie je Takt: (Beat-Offset, MIDI, Länge in Beats)
MELODY = [
    [(0, 78, 1), (1, 76, 0.5), (1.5, 74, 1), (2.5, 76, 1.5)],
    [(0, 74, 1), (1, 71, 0.5), (1.5, 74, 1), (2.5, 79, 1.5)],
    [(0, 78, 1.5), (1.5, 81, 0.5), (2, 78, 1), (3, 76, 1)],
    [(0, 76, 1), (1, 73, 0.5), (1.5, 76, 1), (2.5, 81, 1.5)],
]


def env(n, a, r):
    e = np.ones(n)
    na, nr = min(n, int(a * SR)), min(n, int(r * SR))
    if na:
        e[:na] = np.linspace(0, 1, na)
    if nr:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


def filt(x, lo=None, hi=None):
    f = np.fft.rfftfreq(len(x), 1 / SR)
    h = np.ones_like(f)
    if hi:
        h *= 1 / (1 + (f / hi) ** 4)
    if lo:
        h *= 1 / (1 + (lo / np.maximum(f, 1)) ** 4)
    return np.fft.irfft(np.fft.rfft(x) * h, len(x))


def add(buf, sig, t):
    i = int(t * SR)
    j = min(len(buf), i + len(sig))
    if 0 <= i < len(buf):
        buf[i:j] += sig[: j - i]


def saw(freq, t, detune=(0.994, 1.0, 1.006)):
    return sum(2 * ((freq * d * t + rng.uniform()) % 1) - 1 for d in detune) / len(detune)


def pad_note(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    return saw(freq, t) * env(n, 0.05, 0.3)


def pluck(freq, dur=0.45):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = saw(freq, t, (0.997, 1.003)) * np.exp(-t * 9)
    return s * env(n, 0.002, 0.03)


def lead(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    vib = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * t) * np.clip(t * 3, 0, 1)
    s = 0.6 * saw(freq * vib, t, (0.996, 1.004)) + 0.4 * np.sign(np.sin(2 * np.pi * freq * t))
    return s * env(n, 0.01, 0.12)


def bass(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.35 * saw(freq, t, (1.0,))
    return s * env(n, 0.005, 0.04)


def kick():
    n = int(0.3 * SR)
    t = np.arange(n) / SR
    f = 48 + 110 * np.exp(-t * 35)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 11) + 0.15 * rng.standard_normal(n) * np.exp(-t * 300)


def clap():
    n = int(0.25 * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    e = np.exp(-t * 22)
    for d in (0.0, 0.011, 0.022):  # drei kurze Anschläge wie Händeklatschen
        e += 0.6 * np.exp(-np.maximum(t - d, 0) * 180) * (t >= d)
    return filt(x * e, lo=900, hi=6000)


def hat(open_=False):
    n = int((0.22 if open_ else 0.05) * SR)
    t = np.arange(n) / SR
    return filt(rng.standard_normal(n), lo=7000) * np.exp(-t * (14 if open_ else 80))


pad, arp, ld, bs, dr = (np.zeros(N) for _ in range(5))
bars = int(np.ceil(DUR / BAR)) + 1

for b in range(bars):
    t0 = b * BAR
    root, notes = CHORDS[b % 4]
    full = b >= DROP
    build = b == DROP - 1
    # Flächen
    for m in notes:
        add(pad, pad_note(hz(m - 12), BAR), t0)
    # 16tel-Arpeggio, vor dem Drop als 8tel
    seq = [notes[0], notes[1], notes[2], notes[1] + 12, notes[2] + 12, notes[1] + 12, notes[2], notes[1]]
    step = BEAT / 4 if full else BEAT / 2
    for i in range(int(round(BAR / step))):
        add(arp, pluck(hz(seq[i % 8])) * (1.0 if i % 4 == 0 else 0.7), t0 + i * step)
    # Bass: treibende 8tel ab Takt 2
    if b >= 1:
        for k in range(8):
            oct_ = 12 if (full and k % 2) else 0
            add(bs, bass(hz(root - 12 + oct_), BEAT / 2 * 0.9), t0 + k * BEAT / 2)
    # Drums
    if b >= 1 and not build:
        for k in range(4):
            add(dr, kick(), t0 + k * BEAT)
    if b >= 2:
        for k in (1, 3):
            add(dr, clap() * (0.9 if full else 0.6), t0 + k * BEAT)
    for k in range(8):
        add(dr, hat(open_=full and k % 2 == 1) * (0.5 if k % 2 else 0.25), t0 + k * BEAT / 2)
    if full:
        for k in range(16):
            if k % 2:
                add(dr, hat() * 0.18, t0 + k * BEAT / 4)
    if build:  # Clap-Wirbel als Aufbau zum Drop
        for k in range(16):
            add(dr, clap() * (0.2 + 0.05 * k), t0 + k * BEAT / 4)
    # Melodie ab dem Drop
    if full:
        for off, m, ln in MELODY[b % 4]:
            add(ld, lead(hz(m), ln * BEAT * 0.95), t0 + off * BEAT)

# Riser (Rauschen, das sich im Takt vor dem Drop öffnet)
riser = np.zeros(N)
r0, r1 = int((DROP - 1) * BAR * SR), int(DROP * BAR * SR)
if 0 < r0 < N:
    r1 = min(r1, N)
    n = r1 - r0
    x = filt(rng.standard_normal(n), lo=2500) * np.linspace(0, 1, n) ** 2
    riser[r0:r1] = x

# Sidechain-Pumpen: Flächen und Bass ducken auf jedem Kick
t = np.arange(N) / SR
phase = (t % BEAT) / BEAT
pump = np.where(t >= BAR, 0.35 + 0.65 * np.clip(phase / 0.45, 0, 1) ** 0.7, 1.0)

pad = filt(pad, hi=2600 if DROP > 0 else 3000)
arp = filt(arp, hi=5500)
mix = (0.20 * pad * pump + 0.20 * arp + 0.17 * ld + 0.34 * bs * pump + 0.55 * dr + 0.12 * riser)


def reverb(x, seed, length=1.4, decay=4.0):
    r = np.random.default_rng(seed)
    n = int(length * SR)
    tt = np.arange(n) / SR
    ir = r.standard_normal(n) * np.exp(-tt * decay)
    ir[: int(0.015 * SR)] = 0
    L = len(x) + n
    y = np.fft.irfft(np.fft.rfft(x, L) * np.fft.rfft(ir, L), L)[: len(x)]
    return y / (np.max(np.abs(y)) + 1e-9) * np.max(np.abs(x))


wet = 0.20 * pad * pump + 0.20 * arp + 0.17 * ld + 0.1 * dr
left = mix + 0.22 * reverb(wet, 1)
right = mix + 0.22 * reverb(wet, 2)
st = np.stack([left, right], 1)
st *= np.where(t < DROP * BAR, 0.72, 1.0)[:, None]  # Drop deutlich lauter als der Aufbau
st *= env(N, 0.05, 2.0)[:, None]
st = np.tanh(st / np.max(np.abs(st)) * 1.3)
st = st / np.max(np.abs(st)) * 0.89  # ≈ −1 dBFS

with wave.open(OUT, "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((st * 32767).astype("<i2").tobytes())
print("fertig:", OUT, f"{DUR:.0f} s, Drop bei {DROP * BAR:.1f} s")
