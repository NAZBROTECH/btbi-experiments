import numpy as np
import matplotlib.pyplot as plt

# Simplified Hodgkin-Huxley model (FitzHugh-Nagumo approximation for speed)
def fh_nagumo(V, w, t, I_ext=0):
    a, b, c = 0.7, 0.8, 3.0
    dVdt = V - (V**3)/3 - w + I_ext
    dwdt = (V + a - b*w) / c
    return dVdt, dwdt

# Generate realistic spike train
dt = 0.01
t = np.arange(0, 100, dt)
V, w = 0, 0
spikes = []
for i in range(len(t)):
    if i % 1000 == 0:  # periodic stimulus
        I_ext = 1.0
    else:
        I_ext = 0.3
    dV, dw = fh_nagumo(V, w, t[i], I_ext)
    V += dV * dt
    w += dw * dt
    spikes.append(V)

plt.figure(figsize=(12,4))
plt.plot(t, spikes)
plt.title("Simplified Hodgkin-Huxley Spike Train (Synapse Signal Generator v0.1)")
plt.xlabel("Time (ms)")
plt.ylabel("Membrane Potential")
plt.tight_layout()
plt.savefig("signal_generator/hh_spikes_demo.png")
plt.close()
print("Hodgkin-Huxley demo saved!")
