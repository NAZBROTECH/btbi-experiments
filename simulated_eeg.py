import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch, butter, filtfilt

# -------------------------------
# Simulated EEG Signal Generator
# -------------------------------

# Sampling details
fs = 250  # Hz (sampling rate)
t = np.arange(0, 10, 1/fs)  # 10 seconds of data

# Generate simulated EEG with different rhythms
alpha = np.sin(2 * np.pi * 10 * t) * 50      # 10 Hz alpha rhythm
beta = np.sin(2 * np.pi * 20 * t) * 20       # 20 Hz beta rhythm
noise = np.random.normal(0, 10, len(t))      # random noise

# Combine signals
eeg = alpha + beta + noise

# --- Plot raw EEG signal ---
plt.figure(figsize=(10, 4))
plt.plot(t[:1000], eeg[:1000])  # first 4 seconds
plt.title("Simulated EEG Signal (time series)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.tight_layout()
plt.savefig("eeg_timeseries.png")
plt.close()

# --- Power Spectral Density (PSD) ---
f, psd = welch(eeg, fs, nperseg=1024)
plt.figure(figsize=(8, 4))
plt.semilogy(f, psd)
plt.title("Power Spectral Density of EEG")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power")
plt.tight_layout()
plt.savefig("eeg_psd.png")
plt.close()

# --- Filtered Alpha Band (8–12 Hz) ---
b, a = butter(4, [8/(fs/2), 12/(fs/2)], btype="band")
alpha_band = filtfilt(b, a, eeg)

plt.figure(figsize=(10, 4))
plt.plot(t[:1000], alpha_band[:1000])
plt.title("Filtered Alpha Band (8–12 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (µV)")
plt.tight_layout()
plt.savefig("eeg_alpha.png")
plt.close()

print("✅ EEG simulation complete! Images saved as:")
print("- eeg_timeseries.png")
print("- eeg_psd.png")
print("- eeg_alpha.png")
