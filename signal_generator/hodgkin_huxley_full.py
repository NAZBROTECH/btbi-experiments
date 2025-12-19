import numpy as np
import matplotlib.pyplot as plt

class HodgkinHuxleyNeuron:
    def __init__(self, Cm=1.0, gNa=120, gK=36, gL=0.3, ENa=50, EK=-77, EL=-54.4):
        self.Cm = Cm; self.gNa = gNa; self.gK = gK; self.gL = gL
        self.ENa = ENa; self.EK = EK; self.EL = EL
        self.V = -65; self.m = 0.05; self.h = 0.6; self.n = 0.32

    def alpha_m(self, V): return 0.1*(V+40)/(1 - np.exp(-(V+40)/10))
    def beta_m(self, V): return 4*np.exp(-(V+65)/18)
    def alpha_h(self, V): return 0.07*np.exp(-(V+65)/20)
    def beta_h(self, V): return 1/(1 + np.exp(-(V+35)/10))
    def alpha_n(self, V): return 0.01*(V+55)/(1 - np.exp(-(V+55)/10))
    def beta_n(self, V): return 0.125*np.exp(-(V+65)/80)

    def step(self, I_ext, dt=0.01):
        V, m, h, n = self.V, self.m, self.h, self.n
        INa = self.gNa * m**3 * h * (V - self.ENa)
        IK = self.gK * n**4 * (V - self.EK)
        IL = self.gL * (V - self.EL)
        dV = (I_ext - INa - IK - IL) / self.Cm * dt
        dm = (self.alpha_m(V)*(1-m) - self.beta_m(V)*m) * dt
        dh = (self.alpha_h(V)*(1-h) - self.beta_h(V)*h) * dt
        dn = (self.alpha_n(V)*(1-n) - self.beta_n(V)*n) * dt
        self.V += dV; self.m += dm; self.h += dh; self.n += dn
        return self.V

# Demo: spiking with current injection
neuron = HodgkinHuxleyNeuron()
t = np.arange(0, 50, 0.01)
V_trace = []
for i, time in enumerate(t):
    I = 10 if 5 < time < 30 else 0  # stimulus
    V = neuron.step(I)
    V_trace.append(V)

plt.figure(figsize=(10,4))
plt.plot(t, V_trace)
plt.title("Full Hodgkin-Huxley Action Potential (Synapse Physics Model)")
plt.xlabel("Time (ms)")
plt.ylabel("Voltage (mV)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/hh_full_demo.png", dpi=300)
plt.close()
print("Full Hodgkin-Huxley model ready!")
