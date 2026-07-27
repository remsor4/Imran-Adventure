import math
import os
import wave

import numpy as np


SAMPLE_RATE = 44100
DURATION = 60.0
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)
TEMPO = 176.0
BEAT = 60.0 / TEMPO
BAR = BEAT * 4.0
RNG = np.random.default_rng(1707)

mix = np.zeros((TOTAL_SAMPLES, 2), dtype=np.float32)


def midi_frequency(note):
    return 440.0 * (2.0 ** ((note - 69.0) / 12.0))


def envelope(length, attack, release):
    env = np.ones(length, dtype=np.float32)
    attack_samples = min(length, max(1, int(attack * SAMPLE_RATE)))
    release_samples = min(length, max(1, int(release * SAMPLE_RATE)))
    env[:attack_samples] = np.linspace(0.0, 1.0, attack_samples, dtype=np.float32)
    env[-release_samples:] *= np.linspace(1.0, 0.0, release_samples, dtype=np.float32)
    return env


def oscillator(freq, length, kind, vibrato=0.0):
    t = np.arange(length, dtype=np.float32) / SAMPLE_RATE
    phase = 2.0 * np.pi * freq * t
    if vibrato:
        phase += vibrato * np.sin(2.0 * np.pi * 5.2 * t)
    if kind == "sine":
        return np.sin(phase)
    if kind == "triangle":
        return (2.0 / np.pi) * np.arcsin(np.sin(phase))
    if kind == "soft_saw":
        signal = np.zeros(length, dtype=np.float32)
        for harmonic in range(1, 7):
            signal += ((-1.0) ** (harmonic + 1)) * np.sin(phase * harmonic) / harmonic
        return signal * 0.55
    if kind == "brass":
        signal = np.sin(phase)
        signal += 0.55 * np.sin(phase * 2.0)
        signal += 0.28 * np.sin(phase * 3.0)
        signal += 0.12 * np.sin(phase * 4.0)
        return signal * 0.52
    if kind == "horn":
        horn_phase = phase + 0.025 * np.sin(2.0 * np.pi * 4.2 * t)
        signal = np.sin(horn_phase)
        signal += 0.48 * np.sin(horn_phase * 2.0)
        signal += 0.20 * np.sin(horn_phase * 3.0)
        signal += 0.08 * np.sin(horn_phase * 5.0)
        return signal * 0.55
    if kind == "violin":
        bow_phase = phase + 0.095 * np.sin(2.0 * np.pi * 5.8 * t)
        signal = np.sin(bow_phase)
        signal += 0.62 * np.sin(bow_phase * 2.0)
        signal += 0.40 * np.sin(bow_phase * 3.0)
        signal += 0.25 * np.sin(bow_phase * 4.0)
        signal += 0.15 * np.sin(bow_phase * 5.0)
        bow_noise = RNG.standard_normal(length).astype(np.float32)
        signal += bow_noise * 0.018
        return signal * 0.43
    if kind == "strings":
        signal = np.zeros(length, dtype=np.float32)
        for detune, weight in [(0.996, 0.30), (1.0, 0.42), (1.004, 0.30)]:
            string_phase = phase * detune + 0.035 * np.sin(2.0 * np.pi * 5.1 * t)
            voice = np.sin(string_phase)
            voice += 0.48 * np.sin(string_phase * 2.0)
            voice += 0.25 * np.sin(string_phase * 3.0)
            signal += voice * weight
        return signal * 0.42
    if kind == "cello":
        cello_phase = phase + 0.045 * np.sin(2.0 * np.pi * 4.8 * t)
        signal = np.sin(cello_phase)
        signal += 0.40 * np.sin(cello_phase * 2.0)
        signal += 0.18 * np.sin(cello_phase * 3.0)
        return signal * 0.58
    return np.sin(phase)


def add_note(start, duration, note, volume, kind="sine", pan=0.0, attack=0.01, release=0.08, vibrato=0.0):
    start_sample = int(start * SAMPLE_RATE)
    length = int(duration * SAMPLE_RATE)
    if start_sample >= TOTAL_SAMPLES or length <= 0:
        return
    length = min(length, TOTAL_SAMPLES - start_sample)
    signal = oscillator(midi_frequency(note), length, kind, vibrato)
    signal *= envelope(length, attack, release) * volume
    left = math.sqrt((1.0 - pan) * 0.5)
    right = math.sqrt((1.0 + pan) * 0.5)
    mix[start_sample:start_sample + length, 0] += signal * left
    mix[start_sample:start_sample + length, 1] += signal * right


def add_chord(start, duration, notes, volume, kind, spread=0.35, attack=0.08, release=0.2):
    count = max(1, len(notes) - 1)
    for index, note in enumerate(notes):
        pan = -spread + (2.0 * spread * index / count)
        add_note(start, duration, note, volume / len(notes), kind, pan, attack, release, 0.025)


def add_orchestral_drum(start, volume=0.28, pitch=58.0):
    start_sample = int(start * SAMPLE_RATE)
    length = int(0.55 * SAMPLE_RATE)
    if start_sample >= TOTAL_SAMPLES:
        return
    length = min(length, TOTAL_SAMPLES - start_sample)
    t = np.arange(length, dtype=np.float32) / SAMPLE_RATE
    sweep = pitch * (1.0 + 0.8 * np.exp(-t * 18.0))
    phase = 2.0 * np.pi * np.cumsum(sweep) / SAMPLE_RATE
    body = np.sin(phase) + 0.35 * np.sin(phase * 0.5)
    noise = RNG.standard_normal(length).astype(np.float32)
    noise = np.concatenate(([0.0], np.diff(noise)))
    signal = (body * 0.8 + noise * 0.07) * np.exp(-t * 7.0) * volume
    mix[start_sample:start_sample + length, 0] += signal * 0.72
    mix[start_sample:start_sample + length, 1] += signal * 0.72


def add_snare(start, volume=0.12):
    start_sample = int(start * SAMPLE_RATE)
    length = int(0.22 * SAMPLE_RATE)
    if start_sample >= TOTAL_SAMPLES:
        return
    length = min(length, TOTAL_SAMPLES - start_sample)
    t = np.arange(length, dtype=np.float32) / SAMPLE_RATE
    noise = RNG.standard_normal(length).astype(np.float32)
    high = np.concatenate(([0.0], np.diff(noise)))
    tone = np.sin(2.0 * np.pi * 185.0 * t)
    signal = (high * 0.34 + tone * 0.24) * np.exp(-t * 20.0) * volume
    mix[start_sample:start_sample + length, 0] += signal * 0.70
    mix[start_sample:start_sample + length, 1] += signal * 0.70


def add_cymbal(start, duration=1.8, volume=0.08):
    start_sample = int(start * SAMPLE_RATE)
    length = int(duration * SAMPLE_RATE)
    if start_sample >= TOTAL_SAMPLES:
        return
    length = min(length, TOTAL_SAMPLES - start_sample)
    t = np.arange(length, dtype=np.float32) / SAMPLE_RATE
    noise = RNG.standard_normal(length).astype(np.float32)
    high = np.concatenate(([0.0], np.diff(noise)))
    signal = high * np.exp(-t * 2.7) * volume
    mix[start_sample:start_sample + length, 0] += signal * 0.68
    mix[start_sample:start_sample + length, 1] += signal * 0.76


def add_riser(start, duration, volume=0.10):
    start_sample = int(start * SAMPLE_RATE)
    length = int(duration * SAMPLE_RATE)
    if start_sample >= TOTAL_SAMPLES:
        return
    length = min(length, TOTAL_SAMPLES - start_sample)
    t = np.arange(length, dtype=np.float32) / SAMPLE_RATE
    progress = t / max(duration, 0.001)
    noise = RNG.standard_normal(length).astype(np.float32)
    smooth = np.cumsum(noise)
    smooth /= max(1.0, np.max(np.abs(smooth)))
    tone = np.sin(2.0 * np.pi * (110.0 * t + 130.0 * t * progress))
    signal = (smooth * 0.25 + tone * 0.55) * (progress ** 1.6) * volume
    mix[start_sample:start_sample + length, 0] += signal * 0.65
    mix[start_sample:start_sample + length, 1] += signal * 0.78


def add_choir(start, duration, root, volume):
    notes = [root, root + 7, root + 12]
    for index, note in enumerate(notes):
        add_note(start, duration, note, volume / 3.0, "sine", -0.25 + index * 0.25, 0.35, 0.6, 0.08)
        add_note(start, duration, note + 12, volume / 7.0, "triangle", 0.25 - index * 0.2, 0.4, 0.7, 0.05)


def add_ostinato(bar_start, chord, intensity, phase_two=False, kind="strings"):
    pattern = [0, 1, 2, 1, 0, 1, 3, 1, 0, 2, 1, 2, 3, 2, 1, 2]
    octave = 12 if phase_two else 0
    for step, chord_index in enumerate(pattern):
        start = bar_start + step * (BEAT / 4.0)
        note = chord[chord_index % len(chord)] + octave
        pan = -0.45 if step % 2 == 0 else 0.45
        add_note(start, BEAT * 0.22, note, intensity, kind, pan, 0.003, 0.050)


def add_melody(bar_start, motif, volume, octave=0, kind="violin"):
    for index, note in enumerate(motif):
        start = bar_start + index * (BEAT / 2.0)
        duration = BEAT * (0.72 if index in (3, 7) else 0.50)
        add_note(start, duration, note + octave, volume, kind, 0.06, 0.035, 0.12, 0.10)
        add_note(start, duration, note + octave - 12, volume * 0.22, "strings", -0.18, 0.04, 0.12, 0.035)


chords = [
    [50, 57, 62, 65],
    [46, 53, 58, 62],
    [43, 50, 55, 58],
    [45, 52, 57, 61],
]
chaos_motif = [74, 73, 69, 65, 67, 66, 62, 61]
imran_motif = [65, 67, 69, 74, 72, 69, 67, 69]

# Intro: a short rise that reaches combat intensity quickly.
for bar_index in range(2):
    start = bar_index * BAR
    chord = chords[bar_index % len(chords)]
    add_chord(start, BAR, [chord[0] - 12, chord[1] - 12, chord[2] - 12], 0.13 + bar_index * 0.025, "cello", 0.25, 0.25, 0.4)
    add_chord(start, BAR, [chord[0], chord[1], chord[2]], 0.065 + bar_index * 0.015, "strings", 0.34, 0.18, 0.35)
    add_choir(start, BAR, chord[0], 0.035 + bar_index * 0.012)
    add_orchestral_drum(start, 0.17 + bar_index * 0.035, 48.0)
    add_orchestral_drum(start + BEAT * 2.0, 0.14 + bar_index * 0.025, 56.0)
    add_melody(start, chaos_motif, 0.045 + bar_index * 0.012, -12)
add_riser(BAR * 0.75, BAR * 1.25, 0.16)
add_cymbal(BAR * 2.0 - 0.08, 1.4, 0.12)

# Phase 1: fast string pulse led by a powerful solo violin.
phase_one_start = BAR * 2.0
phase_one_bars = 14
for bar_index in range(phase_one_bars):
    start = phase_one_start + bar_index * BAR
    chord = chords[bar_index % 4]
    add_ostinato(start, chord, 0.036, False, "strings")
    add_chord(start, BAR * 0.95, [chord[0] - 12, chord[1] - 12, chord[2] - 12], 0.13, "cello", 0.3, 0.05, 0.18)
    add_chord(start, BEAT * 1.25, [chord[0], chord[1], chord[2]], 0.18, "horn", 0.22, 0.018, 0.14)
    add_chord(start + BEAT * 2.0, BEAT * 0.9, [chord[1], chord[2], chord[3]], 0.10, "horn", 0.22, 0.015, 0.12)
    add_choir(start, BAR, chord[0], 0.038)
    for beat_index in range(4):
        add_orchestral_drum(start + beat_index * BEAT, 0.24 if beat_index % 2 == 0 else 0.17, 54.0 + beat_index * 3.0)
    add_snare(start + BEAT, 0.11)
    add_snare(start + BEAT * 3.0, 0.12)
    motif = chaos_motif if bar_index % 4 in (0, 1) else imran_motif
    add_melody(start, motif, 0.072)
    if bar_index % 2 == 1:
        add_cymbal(start + BAR - 0.10, 1.0, 0.075)

# Transition: the solo violin rises with the pulse from the Chaos Stone.
transition_start = phase_one_start + phase_one_bars * BAR
transition_duration = BAR * 2.0
add_riser(transition_start, transition_duration, 0.23)
for index in range(12):
    hit = transition_start + index * (transition_duration / 12.0)
    add_orchestral_drum(hit, 0.13 + index * 0.012, 48.0 + index * 2.4)
    add_note(hit, BEAT * 0.42, 62 + index, 0.052 + index * 0.003, "violin", 0.0, 0.018, 0.10, 0.12)
add_cymbal(transition_start + transition_duration - 0.05, 2.0, 0.16)

# Phase 2: denser strings, higher violin, percussion, horns, and choir.
phase_two_start = transition_start + transition_duration
phase_two_chords = [
    [50, 57, 62, 65],
    [48, 55, 60, 64],
    [46, 53, 58, 62],
    [45, 52, 57, 61],
]
phase_two_bars = 21
for bar_index in range(phase_two_bars):
    start = phase_two_start + bar_index * BAR
    chord = phase_two_chords[bar_index % 4]
    add_ostinato(start, chord, 0.039, False, "strings")
    add_ostinato(start + BEAT / 8.0, [note - 12 for note in chord], 0.025, True, "strings")
    add_chord(start, BAR * 0.96, [chord[0] - 12, chord[1] - 12, chord[2] - 12], 0.16, "cello", 0.35, 0.04, 0.16)
    add_chord(start, BEAT * 1.35, [chord[0], chord[1], chord[2], chord[3]], 0.23, "horn", 0.28, 0.012, 0.15)
    add_chord(start + BEAT * 2.0, BEAT * 1.15, [chord[1], chord[2], chord[3]], 0.16, "horn", 0.28, 0.012, 0.14)
    add_choir(start, BAR, chord[0], 0.060)
    for beat_index in range(4):
        add_orchestral_drum(start + beat_index * BEAT, 0.23 if beat_index % 2 else 0.33, 55.0 + beat_index * 3.0)
        add_snare(start + beat_index * BEAT + BEAT * 0.5, 0.075)
    add_snare(start + BEAT, 0.14)
    add_snare(start + BEAT * 3.0, 0.16)
    motif = chaos_motif if bar_index % 4 < 2 else imran_motif
    lead_octave = 0 if bar_index < 10 else 12
    add_melody(start, motif, 0.086, lead_octave)
    if bar_index % 4 in (1, 3):
        add_melody(start + BEAT * 0.25, [note - 5 for note in motif], 0.032, lead_octave)
    if bar_index % 2 == 1:
        add_cymbal(start + BAR - 0.08, 1.3, 0.105)

# Defeat and opening: the violin collapses into a brighter final color.
defeat_start = phase_two_start + phase_two_bars * BAR
add_cymbal(defeat_start, 2.4, 0.16)
add_orchestral_drum(defeat_start, 0.36, 42.0)
for index in range(8):
    start = defeat_start + index * 0.23
    add_note(start, 0.8, 74 - index, 0.07, "violin", -0.25 + index * 0.1, 0.035, 0.25, 0.12)
add_riser(defeat_start, 2.0, 0.08)

bright_start = defeat_start + 2.2
bright_chord = [50, 57, 62, 66]
bright_duration = max(1.0, DURATION - bright_start - 0.15)
add_chord(bright_start, bright_duration, bright_chord, 0.20, "strings", 0.4, 0.25, 0.8)
add_choir(bright_start, bright_duration, 50, 0.055)
for index, note in enumerate([62, 66, 69, 74, 78, 81]):
    add_note(bright_start + index * 0.45, 0.72, note, 0.075, "violin", -0.2 + index * 0.08, 0.035, 0.20, 0.12)
    add_note(bright_start + index * 0.45, 0.5, note + 12, 0.018, "sine", 0.25, 0.015, 0.18, 0.03)

# Gentle stereo delays for space.
for delay_seconds, gain, cross in [(0.075, 0.12, False), (0.145, 0.08, True), (0.285, 0.045, False)]:
    delay = int(delay_seconds * SAMPLE_RATE)
    if cross:
        mix[delay:, 0] += mix[:-delay, 1] * gain
        mix[delay:, 1] += mix[:-delay, 0] * gain
    else:
        mix[delay:] += mix[:-delay] * gain

# Master fade, soft saturation, and normalization.
fade_in = int(0.35 * SAMPLE_RATE)
fade_out = int(1.2 * SAMPLE_RATE)
mix[:fade_in] *= np.linspace(0.0, 1.0, fade_in, dtype=np.float32)[:, None]
mix[-fade_out:] *= np.linspace(1.0, 0.0, fade_out, dtype=np.float32)[:, None]
mix = np.tanh(mix * 1.15)
peak = float(np.max(np.abs(mix)))
if peak > 0.0:
    mix *= 0.80 / peak

output_path = os.environ["TATA_LISA_WAV"]
os.makedirs(os.path.dirname(output_path), exist_ok=True)
pcm = np.clip(mix * 32767.0, -32768, 32767).astype("<i2")
with wave.open(output_path, "wb") as wav_file:
    wav_file.setnchannels(2)
    wav_file.setsampwidth(2)
    wav_file.setframerate(SAMPLE_RATE)
    wav_file.writeframes(pcm.tobytes())

print(output_path)
