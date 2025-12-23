import numpy as np
import matplotlib.pyplot as plt

class NeuralinkArray:
    def __init__(self, channels=1024, threads=64):
        self.channels = channels
        self.threads = threads
        self.bandwidth = 0.0
        self.history = []

    def record_activity(self, thought_intensity):
        # Simulate high-density recording: more channels = higher bandwidth
        noise = np.random.normal(0, 0.1, self.channels)
        signal = thought_intensity * np.ones(self.channels) + noise
        decoded_bits = np.sum(signal > 0.5) / self.channels * 20  # rough bits/sec
        self.bandwidth = decoded_bits
        self.history.append(decoded_bits)
        return signal

    def stimulate(self, target_pattern):
        # Simple write mode: feedback stimulation
        return np.mean(target_pattern)

# Demo: cursor control speed vs channel count
array_high = NeuralinkArray(1024)
array_low = NeuralinkArray(64)  # older BCI comparison

bits_high = []
bits_low = []
for intensity in np.linspace(0.2, 1.0, 100):
    bits_high.append(array_high.record_activity(intensity))
    bits_low.append(array_low.record_activity(intensity))

plt.figure(figsize=(10,6))
plt.plot(bits_high, label="Neuralink-style (1024 channels)", lw=3)
plt.plot(bits_low, label="Older BCI (64 channels)", lw=2, alpha=0.7)
plt.title("Neuralink-Inspired Bandwidth Demo – Channels vs Thought Control Speed")
plt.xlabel("Thought Intensity Steps")
plt.ylabel("Decoded Bandwidth (bits/sec)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/neuralink_bandwidth_demo.png", dpi=300)
plt.close()
print("High-channel Neuralink simulation ready!")
