import numpy as np
import matplotlib.pyplot as plt

class SleepCycleSimulator:
    def __init__(self, cycle_duration_min=90):
        self.cycle_min = cycle_duration_min
        self.stages = ["NREM1", "NREM2", "NREM3", "REM"]
        self.history = {"delta": [], "rem": [], "restoration": []}

    def run_nightly_cycle(self, num_cycles=5):
        restoration = 0.0
        for cycle in range(num_cycles):
            # More deep sleep early, more REM later
            deep_weight = max(0.1, 1 - cycle/num_cycles)
            rem_weight = 1 - deep_weight
            delta_power = np.random.uniform(0.6, 1.0) * deep_weight
            rem_intensity = np.random.uniform(0.4, 0.9) * rem_weight
            restoration += delta_power * 0.6 + rem_intensity * 0.4
            self.history["delta"].append(delta_power)
            self.history["rem"].append(rem_intensity)
            self.history["restoration"].append(restoration)
        return restoration / num_cycles

# Demo: "Super sleeper" vs normal user
normal = SleepCycleSimulator()
super_sleeper = SleepCycleSimulator()  # same model, but imagine genetic efficiency boost

normal_rest = normal.run_nightly_cycle(5)
super_rest = super_sleeper.run_nightly_cycle(3) * 1.3  # simulated efficiency

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(normal.history["delta"], label="Normal - Deep Sleep (Delta)")
plt.plot(normal.history["rem"], label="Normal - REM")
plt.legend()
plt.title("Sleep Cycles Demo – Normal User")
plt.subplot(2,1,2)
plt.plot(super_sleeper.history["delta"][:3], label="Super Sleeper - Deep Sleep", color='green')
plt.plot(super_sleeper.history["rem"][:3], label="Super Sleeper - REM", color='orange')
plt.title("Super Sleeper – Higher Restoration in Fewer Cycles")
plt.legend()
plt.tight_layout()
plt.savefig("signal_generator/sleep_cycle_demo.png", dpi=300)
plt.close()
print(f"Normal restoration: {normal_rest:.2f} | Super sleeper: {super_rest:.2f}")
print("Sleep cycle simulation ready!")
