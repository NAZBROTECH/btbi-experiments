import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq

class CochlearModel:
    def __init__(self, sample_rate=44100, num_bands=32):
        self.sample_rate = sample_rate
        self.num_bands = num_bands

    def tonotopic_spikes(self, thought_signal, duration=0.5):
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        # Simulate "thought oscillation" as sum of frequencies
        signal = np.sum([np.sin(2 * np.pi * f * t) for f in thought_signal], axis=0)
        # FFT for frequency decomposition (cochlea-like)
        freqs = rfftfreq(len(signal), 1/self.sample_rate)
        spectrum = np.abs(rfft(signal))
        # Map to tonotopic bands (log scale like basilar membrane)
        band_edges = np.logspace(np.log10(20), np.log10(20000), self.num_bands+1)
        spikes = []
        for i in range(self.num_bands):
            band_mask = (freqs >= band_edges[i]) & (freqs < band_edges[i+1])
            band_power = np.sum(spectrum[band_mask])
            spike_rate = band_power / np.max(spectrum) if np.max(spectrum) > 0 else 0
            spikes.append(spike_rate)
        return np.array(spikes), freqs, spectrum

# Demo
model = CochlearModel()
high_thought = [200, 1000, 5000]    # "sharp/alert" thought
low_thought = [50, 200, 800]       # "calm/deep" thought
spikes_high, _, _ = model.tonotopic_spikes(high_thought)
spikes_low, _, _ = model.tonotopic_spikes(low_thought)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.bar(range(len(spikes_high)), spikes_high)
plt.title("Tonotopic Spike Pattern – High-Frequency 'Alert' Thought")
plt.subplot(2,1,2)
plt.bar(range(len(spikes_low)), spikes_low, color='orange')
plt.title("Tonotopic Spike Pattern – Low-Frequency 'Calm' Thought")
plt.tight_layout()
plt.savefig("signal_generator/cochlear_tonotopic_demo.png", dpi=300)
plt.close()
print("Cochlear model with tonotopic mapping ready!")
