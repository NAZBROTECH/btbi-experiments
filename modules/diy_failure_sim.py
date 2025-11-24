@"
# diy_failure_sim.py
# Shows how signals fail under real-world EEG limitations.

from modules.simulate_realistic_bci import generate_signal, apply_failure_modes

def run_demo():
    print("\n=== DIY EEG Failure Simulation Demo ===\n")

    ideal = generate_signal()
    degraded = apply_failure_modes(ideal)

    print("Ideal sample:", ideal[:15])
    print("Degraded sample:", degraded[:15])

    print("\nThis demonstrates how DIY EEG projects often fail:")
    print("- Dropouts   (bad electrodes)")
    print("- Jitter     (timing instability)")
    print("- Saturation (electrical limits)\n")

if __name__ == "__main__":
    run_demo()
"@ | Out-File -Encoding UTF8 modules/diy_failure_sim.py
