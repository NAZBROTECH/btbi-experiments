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
