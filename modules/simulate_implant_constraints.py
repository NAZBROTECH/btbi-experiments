"""
simulate_implant_constraints.py
--------------------------------
Simulates implant-like limitations:
- reduced electrode count
- noise increase
- signal drift
- dropout failures

This helps users understand why real invasive BCIs
(ECoG, Utah arrays, Neuralink-style threads) still face signal instability.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_clean_signal(duration=2.0, fs=250):
    """Generate a clean synthetic neural signal."""
    t = np.linspace(0, duration, int(duration * fs))
    signal = np.sin(2 * np.pi * 10 * t)  # 10 Hz alpha-like oscillation
    return t, signal


def apply_constraints(signal, noise_level=0.2, dropout_prob=0.05, drift=0.1):
    """Apply implant-like constraints to a clean signal."""
    noisy = signal + np.random.normal(0, noise_level, size=len(signal))

    # Random dropouts (mimicking failed electrodes)
    drop_mask = np.random.rand(len(signal)) > dropout_prob
    noisy = noisy * drop_mask

    # Drift (gradual shift as tissue response changes)
    drift_curve = np.linspace(0, drift, len(signal))
    noisy = noisy + drift_curve

    return noisy


def run_simulation():
    t, clean = generate_clean_signal()

    constrained = apply_constraints(
        clean,
        noise_level=0.3,
        dropout_prob=0.10,
        drift=0.3,
    )

    plt.figure()
    plt.plot(t, clean, label="Clean Signal")
    plt.plot(t, constrained, label="Implant-Constrained Signal")
    plt.legend()
    plt.title("Neural Signal: Clean vs Implant-Constrained")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.show()


if __name__ == "__main__":
    run_simulation()
