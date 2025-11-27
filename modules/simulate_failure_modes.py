"""
simulate_failure_modes.py
-----------------------------------------
Simulates realistic BCI signal failure events such as:
- baseline drift
- sudden noise bursts
- amplifier clipping
- channel dropouts
- electrode failure probability

This module is used to illustrate the engineering challenges
in real-world neural interfaces.

Author: Synapse Project
Date: 2025-11-27
"""

import numpy as np
import random


def apply_baseline_drift(signal, drift_rate=0.002):
    """Adds a slow drifting offset to the signal."""
    drift = np.linspace(0, drift_rate * len(signal), len(signal))
    return signal + drift


def apply_noise_bursts(signal, burst_probability=0.01, burst_amplitude=2.0):
    """Random high-amplitude noise events."""
    for i in range(len(signal)):
        if random.random() < burst_probability:
            signal[i] += random.uniform(-burst_amplitude, burst_amplitude)
    return signal


def apply_amplitude_clipping(signal, clip_threshold=1.0):
    """Simulates an amplifier clipping the signal."""
    return np.clip(signal, -clip_threshold, clip_threshold)


def apply_channel_dropouts(signal, dropout_probability=0.005):
    """Simulates moments where the channel stops transmitting."""
    mask = np.random.rand(len(signal)) > dropout_probability
    return signal * mask


def simulate_full_failure_mode(signal):
    """
    Apply all failure effects sequentially.
    This represents a worst-case real-world BCI behavior.
    """

    signal = apply_baseline_drift(signal)
    signal = apply_noise_bursts(signal)
    signal = apply_amplitude_clipping(signal)
    signal = apply_channel_dropouts(signal)

    return signal


if __name__ == "__main__":
    # Test run
    test_signal = np.random.normal(0, 0.1, 1000)
    failed = simulate_full_failure_mode(test_signal)

    print("Failure simulation complete.")
    print("Example output sample:", failed[:10])
