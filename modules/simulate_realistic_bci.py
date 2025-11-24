# simulate_realistic_bci.py
# ------------------------------------------------------------
# Demonstrates ideal vs biologically-degraded BCI signals
# using the vision simulation module.

from modules.vision_sim import (
    generate_ssvep_signal,
    generate_degraded_signal,
    plot_ssvep
)

def run_demo():
    clean = generate_ssvep_signal()
    degraded = generate_degraded_signal()

    print("Showing ideal synthetic signal...")
    plot_ssvep(clean)

    print("Showing biologically degraded signal...")
    plot_ssvep(degraded)

if __name__ == "__main__":
    run_demo()



import numpy as np
import random
import time

def generate_signal(length=200):
    """Ideal synthetic signal."""
    t = np.linspace(0, 1, length)
    return np.sin(12 * np.pi * t)  # simple alpha-wave simulation


def apply_failure_modes(signal):
    """Simulates realistic EEG failure conditions."""
    corrupted = signal.copy()

    # 1. Random dropout
    if random.random() < 0.3:
        drop_index = random.randint(10, len(signal)-10)
        corrupted[drop_index:drop_index+10] = 0

    # 2. Amplifier saturation
    if random.random() < 0.3:
        corrupted = np.clip(corrupted, -0.4, 0.4)

    # 3. Latency jitter
    if random.random() < 0.3:
        shift = random.randint(-3, 3)
        corrupted = np.roll(corrupted, shift)

    return corrupted


def run_simulation():
    print("Running ideal vs degraded EEG simulation...")

    ideal = generate_signal()
    degraded = apply_failure_modes(ideal)

    print("Ideal signal sample:", ideal[:10])
    print("Degraded signal sample:", degraded[:10])
    print("Simulation complete.")
