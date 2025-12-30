import numpy as np
import matplotlib.pyplot as plt

class ReconfigurableCore:
    def __init__(self, modes=["latency", "power", "balanced"]):
        self.modes = modes
        self.current_mode = "balanced"
        self.utilization = 0.5
        self.history = []

    def reconfigure(self, load_intensity):
        # High load → latency mode (max parallelism)
        if load_intensity > 0.7:
            self.current_mode = "latency"
            self.utilization = 0.95
        # Low load → power mode
        elif load_intensity < 0.3:
            self.current_mode = "power"
            self.utilization = 0.6
        else:
            self.current_mode = "balanced"
            self.utilization = 0.85
        return self.utilization

    def infer_batch1(self, thoughts):
        latency = 10 / self.utilization  # inverse relation
        self.history.append(latency)
        return latency

# Demo: streaming "thoughts" with dynamic reconfiguration
core = ReconfigurableCore()
latencies = []
for step in range(100):
    intensity = np.sin(step/10)*0.5 + 0.5  # varying load
    util = core.reconfigure(intensity)
    lat = core.infer_batch1(intensity)
    latencies.append(lat)

plt.figure(figsize=(10,6))
plt.plot(latencies, label="Inference Latency", color='orange', lw=3)
plt.title("Reconfigurable Core Demo – DNA/MERA-Inspired Low-Latency Adaptation")
plt.xlabel("Streaming Thought Steps")
plt.ylabel("Latency (arbitrary units)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/reconfigurable_demo.png", dpi=300)
plt.close()
print("Reconfigurable DNA-style core simulation ready!")
