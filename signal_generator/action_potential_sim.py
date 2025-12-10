import numpy as np
import matplotlib.pyplot as plt

# Simplified Hodgkin-Huxley style model (Izhikevich neuron – fast & realistic)
class IzhikevichNeuron:
    def __init__(self, a=0.02, b=0.2, c=-65, d=8):
        self.a, self.b, self.c, self.d = a, b, c, d
        self.v = -65  # membrane potential
        self.u = self.b * self.v  # recovery variable
        self.history = []

    def step(self, I, dt=0.5):
        for _ in range(int(1/dt)):
            dv = (0.04*self.v**2 + 5*self.v + 140 - self.u + I)
            du = self.a*(self.b*self.v - self.u)
            self.v += dv * dt
            self.u += du * dt
            if self.v >= 30:               # spike!
                self.history.append(30)
                self.v = self.c
                self.u += self.d
                break
            self.history.append(self.v)
        return self.history[-1] >= 30

# Simulate variable "thought intensity" → current injection
def generate_spike_train(thought_intensity=8.0, duration_ms=200):
    neuron = IzhikevichNeuron()
    t = np.arange(0, duration_ms, 0.5)
    spikes = []
    fired = []
    for i in t:
        I = thought_intensity + np.random.normal(0, 1)  # base + noise
        spike = neuron.step(I)
        spikes.append(neuron.v)
        fired.append(1 if spike else 0)
    return t, spikes, fired

# Demo: low vs high intensity thoughts
t_low, v_low, f_low = generate_spike_train(6.0)
t_high, v_high, f_high = generate_spike_train(12.0)

plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.plot(t_low, v_low, label="Low intensity thought")
plt.title("Action Potential Simulation – Synapse Signal Generator v0.2")
plt.ylabel("mV")
plt.legend()
plt.subplot(2,1,2)
plt.plot(t_high, v_high, 'orange', label="High intensity thought")
plt.xlabel("Time (ms)")
plt.ylabel("mV")
plt.legend()
plt.tight_layout()
plt.savefig("signal_generator/action_potential_demo.png", dpi=300)
plt.close()
print("Enhanced action potential generator ready + demo saved!")
