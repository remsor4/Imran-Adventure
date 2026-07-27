from __future__ import annotations

import argparse
import math
import random
import struct
import wave
from pathlib import Path


SAMPLE_RATE = 48_000
DURATION = 2.0
FRAME_COUNT = int(SAMPLE_RATE * DURATION)


def pan_gains(pan: float) -> tuple[float, float]:
    angle = (pan + 1.0) * math.pi / 4.0
    return math.cos(angle), math.sin(angle)


def add_bell(
    left: list[float],
    right: list[float],
    start: float,
    duration: float,
    frequency: float,
    amplitude: float,
    pan: float,
) -> None:
    start_frame = int(start * SAMPLE_RATE)
    end_frame = min(FRAME_COUNT, start_frame + int(duration * SAMPLE_RATE))
    gain_left, gain_right = pan_gains(pan)
    partials = ((1.0, 1.0), (2.01, 0.36), (3.97, 0.16), (6.11, 0.07))

    for frame in range(start_frame, end_frame):
        t = (frame - start_frame) / SAMPLE_RATE
        attack = min(1.0, t / 0.008)
        decay = math.exp(-4.2 * t / duration)
        sample = 0.0
        for ratio, gain in partials:
            sample += gain * math.sin(2.0 * math.pi * frequency * ratio * t)
        sample *= amplitude * attack * decay
        left[frame] += sample * gain_left
        right[frame] += sample * gain_right


def add_low_knock(
    left: list[float],
    right: list[float],
    start: float,
    amplitude: float,
) -> None:
    start_frame = int(start * SAMPLE_RATE)
    duration = 0.22
    end_frame = min(FRAME_COUNT, start_frame + int(duration * SAMPLE_RATE))
    rng = random.Random(int(start * 10_000) + 17)
    low_noise = 0.0

    for frame in range(start_frame, end_frame):
        t = (frame - start_frame) / SAMPLE_RATE
        envelope = math.exp(-18.0 * t)
        raw_noise = rng.uniform(-1.0, 1.0)
        low_noise += 0.08 * (raw_noise - low_noise)
        body = math.sin(2.0 * math.pi * 105.0 * t)
        sample = amplitude * envelope * (0.78 * body + 0.22 * low_noise)
        left[frame] += sample * 0.72
        right[frame] += sample * 0.72


def add_wood_creak(left: list[float], right: list[float]) -> None:
    start = 0.12
    duration = 0.63
    start_frame = int(start * SAMPLE_RATE)
    end_frame = int((start + duration) * SAMPLE_RATE)
    rng = random.Random(7231)
    phase = 0.0
    filtered_noise = 0.0

    for frame in range(start_frame, end_frame):
        t = (frame - start_frame) / SAMPLE_RATE
        progress = t / duration
        envelope = math.sin(math.pi * progress) ** 0.72
        frequency = 185.0 + 250.0 * progress + 24.0 * math.sin(2.0 * math.pi * 3.4 * t)
        phase += 2.0 * math.pi * frequency / SAMPLE_RATE
        raw_noise = rng.uniform(-1.0, 1.0)
        filtered_noise += 0.035 * (raw_noise - filtered_noise)
        grain = 0.72 + 0.28 * math.sin(2.0 * math.pi * 31.0 * t + filtered_noise)
        sample = envelope * (0.10 * math.sin(phase) * grain + 0.028 * filtered_noise)
        pan = -0.12 + 0.24 * progress
        gain_left, gain_right = pan_gains(pan)
        left[frame] += sample * gain_left
        right[frame] += sample * gain_right


def add_magic_rise(left: list[float], right: list[float]) -> None:
    start = 0.72
    duration = 0.82
    start_frame = int(start * SAMPLE_RATE)
    end_frame = int((start + duration) * SAMPLE_RATE)
    phase_a = 0.0
    phase_b = 0.0

    for frame in range(start_frame, end_frame):
        t = (frame - start_frame) / SAMPLE_RATE
        progress = t / duration
        envelope = math.sin(math.pi * min(1.0, progress)) ** 0.65
        frequency_a = 520.0 * (2.0 ** (1.35 * progress))
        frequency_b = 760.0 * (2.0 ** (0.85 * progress))
        phase_a += 2.0 * math.pi * frequency_a / SAMPLE_RATE
        phase_b += 2.0 * math.pi * frequency_b / SAMPLE_RATE
        tremolo = 0.76 + 0.24 * math.sin(2.0 * math.pi * 8.0 * t)
        sample = envelope * tremolo * (0.035 * math.sin(phase_a) + 0.022 * math.sin(phase_b))
        left[frame] += sample * (0.82 - 0.18 * progress)
        right[frame] += sample * (0.64 + 0.18 * progress)


def add_reverb(channel: list[float], other: list[float]) -> list[float]:
    output = channel.copy()
    taps = ((0.057, 0.16), (0.113, 0.095), (0.181, 0.055))
    for delay_seconds, gain in taps:
        delay = int(delay_seconds * SAMPLE_RATE)
        for frame in range(delay, FRAME_COUNT):
            output[frame] += channel[frame - delay] * gain
            output[frame] += other[frame - delay] * gain * 0.24
    return output


def synthesize() -> tuple[list[float], list[float]]:
    left = [0.0] * FRAME_COUNT
    right = [0.0] * FRAME_COUNT

    add_low_knock(left, right, 0.05, 0.34)
    add_wood_creak(left, right)
    add_low_knock(left, right, 0.58, 0.22)
    add_magic_rise(left, right)

    arpeggio = (
        (0.77, 587.33, -0.30),
        (0.96, 830.61, 0.22),
        (1.15, 1174.66, -0.12),
        (1.34, 1661.22, 0.30),
    )
    for start, frequency, pan in arpeggio:
        add_bell(left, right, start, 0.62, frequency, 0.085, pan)

    final_chord = (
        (1318.51, -0.28, 0.090),
        (1661.22, 0.00, 0.078),
        (1975.53, 0.28, 0.070),
        (2637.02, 0.10, 0.042),
    )
    for frequency, pan, amplitude in final_chord:
        add_bell(left, right, 1.50, 0.50, frequency, amplitude, pan)

    reverbed_left = add_reverb(left, right)
    reverbed_right = add_reverb(right, left)

    fade_start = int(1.86 * SAMPLE_RATE)
    for frame in range(fade_start, FRAME_COUNT):
        fade = 1.0 - (frame - fade_start) / (FRAME_COUNT - fade_start)
        reverbed_left[frame] *= max(0.0, fade)
        reverbed_right[frame] *= max(0.0, fade)

    peak = max(
        max(abs(sample) for sample in reverbed_left),
        max(abs(sample) for sample in reverbed_right),
        1e-9,
    )
    normalization = 0.88 / peak
    return (
        [math.tanh(sample * normalization) for sample in reverbed_left],
        [math.tanh(sample * normalization) for sample in reverbed_right],
    )


def write_wav(output_path: Path, left: list[float], right: list[float]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output_path), "wb") as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        frames = bytearray()
        for sample_left, sample_right in zip(left, right):
            value_left = int(max(-1.0, min(1.0, sample_left)) * 32767)
            value_right = int(max(-1.0, min(1.0, sample_right)) * 32767)
            frames.extend(struct.pack("<hh", value_left, value_right))
        wav_file.writeframes(frames)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("assets/audio/sfx/ouverture-coffre-commune.wav"),
    )
    args = parser.parse_args()
    left, right = synthesize()
    write_wav(args.output, left, right)


if __name__ == "__main__":
    main()
