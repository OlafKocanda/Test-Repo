"""Kleine Sampler- und Mix-Engine für die WoodMatch-Musik.

Nutzt echte Instrumentenaufnahmen aus „VS Chamber Orchestra: Community Edition“
(VSCO-2-CE, Lizenz CC0 1.0, frei auch für kommerzielle Nutzung):
https://github.com/sgossner/VSCO-2-CE

Samples holen (nur die benötigten Ordner, ca. 1 GB):
  git clone --filter=blob:none --no-checkout https://github.com/sgossner/VSCO-2-CE vsco
  cd vsco && git sparse-checkout init --no-cone
  cp ../vsco-sparse-checkout.txt .git/info/sparse-checkout && git checkout master
Pfad zu den Samples: Umgebungsvariable VSCO_DIR (Standard: ./vsco).
"""
import glob
import os
import re
import wave

import numpy as np
import soundfile as sf
from scipy import ndimage, signal

SR = 44100
VSCO = os.environ.get("VSCO_DIR", os.path.join(os.path.dirname(__file__), "vsco"))
NOTE = {"C": 0, "C#": 1, "D": 2, "D#": 3, "E": 4, "F": 5, "F#": 6, "G": 7, "G#": 8, "A": 9, "A#": 10, "B": 11}
rng = np.random.default_rng(11)


def _load(path):
    x, sr = sf.read(path, always_2d=True, dtype="float32")
    if sr != SR:
        x = signal.resample_poly(x, SR, sr, axis=0).astype("float32")
    if x.shape[1] == 1:
        x = np.repeat(x, 2, 1)
    x = x[:, :2]
    a = np.abs(x).max(1)
    on = np.argmax(a > 0.02 * a.max())
    return x[max(0, on - int(0.004 * SR)):]


class Instrument:
    """Ordner mit Einzelnoten. octave_shift: Dateiname-Oktave → MIDI (VSCO meist +2, Harfe +1)."""

    def __init__(self, folder, octave_shift=2, pattern="*.wav", notemap=None, release=0.25, attack=0.0, tune=0.0):
        self.samples = {}  # midi -> {dyn: [arrays]}
        self.release, self.attack, self.tune = release, attack, tune  # tune: Sample klingt um so viele Halbtöne höher
        self.rr = {}
        for p in sorted(glob.glob(os.path.join(VSCO, folder, pattern))):
            name = os.path.basename(p)
            if notemap:
                midi = notemap(name)
                if midi is None:
                    continue
            else:
                m = re.search(r"_([A-G]#?)(-?\d)(?=[_.])", name)
                if not m:
                    continue
                midi = 12 * (int(m.group(2)) + octave_shift) + NOTE[m.group(1)]
            d = re.search(r"(?:_v|dyn)(\d)", name)
            dyn = int(d.group(1)) if d else {"pp": 1, "mp": 2, "mf": 3, "f": 4, "ff": 5, "loud": 4}.get(
                (re.search(r"_(pp|mp|mf|ff|f|loud)(?=[_.])", name) or [None, "mf"])[1], 3)
            self.samples.setdefault(midi, {}).setdefault(dyn, []).append(p)
        if not self.samples:
            raise FileNotFoundError(f"Keine Samples in {folder}")
        self.keys = np.array(sorted(self.samples))
        self._cache = {}

    def _get(self, path):
        if path not in self._cache:
            self._cache[path] = _load(path)
        return self._cache[path]

    def render(self, midi, vel=0.7, dur=None, attack=None, release=None):
        src = int(self.keys[np.argmin(np.abs(self.keys - midi))])
        layers = sorted(self.samples[src])
        dyn = layers[min(len(layers) - 1, int(round(vel * (len(layers) - 1))))]
        paths = self.samples[src][dyn]
        k = (src, dyn)
        self.rr[k] = (self.rr.get(k, -1) + 1) % len(paths)
        x = self._get(paths[self.rr[k]])
        ratio = 2 ** ((midi - src - self.tune) / 12)
        rel = self.release if release is None else release
        att = self.attack if attack is None else attack
        n_out = len(x) / ratio if dur is None else min(len(x) / ratio, (dur + rel) * SR)
        n_out = int(n_out)
        if ratio != 1:
            pos = np.arange(n_out) * ratio
            y = np.stack([np.interp(pos, np.arange(len(x)), x[:, c]) for c in (0, 1)], 1)
        else:
            y = x[:n_out].copy()
        if dur is not None:
            nr = int(rel * SR)
            end = min(len(y), int(dur * SR) + nr)
            y = y[:end]
            if nr and len(y) > nr:
                y[-nr:] *= np.linspace(1, 0, nr)[:, None] ** 1.5
        if att:
            na = min(len(y), int(att * SR))
            y[:na] *= np.linspace(0, 1, na)[:, None]
        return y * (0.55 + 0.45 * vel)


class Track:
    """Stereo-Spur mit Pan, Hallanteil und Ziel-Lautstärke."""

    def __init__(self, dur, pan=0.0, reverb=0.25, level_db=-20.0, humanize=0.006, hp=None):
        self.buf = np.zeros((int(dur * SR) + SR * 4, 2), "float32")
        self.pan, self.reverb, self.level_db, self.humanize, self.hp = pan, reverb, level_db, humanize, hp

    def add(self, y, t, gain=1.0):
        t += rng.normal(0, self.humanize) if self.humanize else 0
        i = max(0, int(t * SR))
        j = min(len(self.buf), i + len(y))
        if j > i:
            self.buf[i:j] += y[: j - i] * gain

    def note(self, inst, midi, t, dur=None, vel=0.7, **kw):
        v = float(np.clip(vel + rng.normal(0, 0.04), 0.05, 1.0))
        self.add(inst.render(midi, v, dur, **kw), t, 0.4 + 0.6 * v)

    def out(self):
        a = (self.pan + 1) * np.pi / 4
        y = self.buf
        if self.hp:  # Low-Cut gegen Matsch im Tiefmittenbereich
            y = signal.sosfilt(signal.butter(2, self.hp, "highpass", fs=SR, output="sos"), y, axis=0)
        return y * np.array([np.cos(a), np.sin(a)], "float32") * np.sqrt(2)


def hall_ir(length=3.0, seed=3):
    """Stereo-Impulsantwort eines Konzertsaals: frühe Reflexionen + frequenzabhängiger Nachhall."""
    r = np.random.default_rng(seed)
    n = int(length * SR)
    t = np.arange(n) / SR
    ir = np.zeros((n, 2))
    for c in (0, 1):
        tail = np.zeros(n)
        for lo, hi, rt in ((20, 300, 2.9), (300, 2000, 2.4), (2000, 6000, 1.7), (6000, 16000, 0.9)):
            sos = signal.butter(2, [lo, hi], "bandpass", fs=SR, output="sos")
            tail += signal.sosfilt(sos, r.standard_normal(n)) * np.exp(-6.9 * t / rt)
        tail *= np.clip((t - 0.022) / 0.03, 0, 1)
        for _ in range(14):
            d = r.uniform(0.007, 0.07)
            tail[int(d * SR)] += r.uniform(0.3, 0.8) * (1 - d * 8)
        ir[:, c] = tail
    return ir / np.abs(ir).max()


def _rms_db(x):
    a = np.sqrt(np.mean(x ** 2, 1))
    act = a[a > 1e-4]
    return 20 * np.log10(np.sqrt(np.mean(act ** 2)) + 1e-12) if len(act) else -120


def mixdown(tracks, dur, out_path, fade_out=2.5, master_db=-1.0):
    n = int(dur * SR)
    dry = np.zeros((n, 2))
    send = np.zeros((n, 2))
    for tr in tracks:
        y = tr.out()[:n]
        if not np.any(y):
            continue
        y = y * 10 ** ((tr.level_db - _rms_db(y)) / 20)
        dry[: len(y)] += y
        send[: len(y)] += y * tr.reverb
    ir = hall_ir()
    wet = np.stack([signal.fftconvolve(send[:, c], ir[:, c])[:n] for c in (0, 1)], 1)
    wet = signal.sosfilt(signal.butter(2, 180, "highpass", fs=SR, output="sos"), wet, axis=0)
    mix = dry + 0.45 * wet
    mix = signal.sosfilt(signal.butter(2, 28, "highpass", fs=SR, output="sos"), mix, axis=0)
    # Bus-Kompressor (sanft, klebt die Instrumente zusammen)
    env = np.sqrt(signal.lfilter([0.0005], [1, -0.9995], np.mean(mix ** 2, 1)))
    lvl = 20 * np.log10(env + 1e-9)
    thr = np.percentile(lvl[lvl > -60], 70)
    gr = np.minimum(0, (thr - lvl) * (1 - 1 / 2.0))
    mix *= 10 ** (gr / 20)[:, None]
    # Fade-out
    nf = int(fade_out * SR)
    mix[-nf:] *= np.linspace(1, 0, nf)[:, None] ** 1.3
    # Limiter mit 5 ms Vorschau
    ceil = 10 ** (master_db / 20)
    mix *= ceil / np.percentile(np.abs(mix), 99.95) * 1.25
    g = np.minimum(1, ceil / (np.abs(mix).max(1) + 1e-9))
    la = int(0.005 * SR)
    g = ndimage.minimum_filter1d(g, 2 * la + 1)
    g = signal.lfilter([0.02], [1, -0.98], g)
    g = ndimage.minimum_filter1d(g, 2 * la + 1)
    mix = np.clip(mix * g[:, None], -ceil, ceil)
    with wave.open(out_path, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((mix * 32767).astype("<i2").tobytes())
    return out_path


def piano_map(name):
    m = re.search(r"_(\d{3})\.wav$", name)
    return 21 + 2 * int(m.group(1)) if m else None


def peak_time(inst_path):
    """Zeitpunkt (s) des lautesten Moments einer Datei, z. B. Höhepunkt eines Becken-Crescendos."""
    x = _load(os.path.join(VSCO, inst_path))
    a = ndimage.uniform_filter1d(np.abs(x).max(1), 2000)
    return np.argmax(a) / SR, x
