import numpy as np
import matplotlib.pyplot as plt

class AdvancedSynapse:
    def __init__(self, receptor_type="AMPA", astro_influence=0.3):
        self.receptor = receptor_type          # "AMPA", "NMDA", "GABA"
        self.release_prob = 0.5                # SNARE/vesicle fusion probability
        self.astro_mod = astro_influence       # gliotransmission boost
        self.plasticity = 1.0                  # LTP/LTD weight
        self.history = []

    def transmit(self, presynaptic_ca):
        # Ca2+ triggers release with probability
        if np.random.rand() < self.release_prob * presynaptic_ca:
            if self.receptor == "AMPA":
                epsp = 5.0 + self.astro_mod * 2      # fast excitation
            elif self.receptor == "NMDA":
                epsp = 8.0 if presynaptic_ca > 1.2 else 0  # voltage-dependent
            elif self.receptor == "GABA":
                epsp = -4.0                          # inhibition
            # Simple LTP if repeated
            self.plasticity = min(2.0, self.plasticity + 0.05)
            output = epsp * self.plasticity
        else:
            output = 0
        self.history.append(output)
        return output

# Demo: excitation vs inhibition balance + astro boost
syn_exc = AdvancedSynapse("AMPA", astro_influence=0.5)
syn_inh = AdvancedSynapse("GABA")
outputs = []
for ca in np.linspace(0.5, 2.0, 100):
    exc = syn_exc.transmit(ca)
    inh = syn_inh.transmit(ca)
    net = exc + inh
    outputs.append(net)

plt.figure(figsize=(10,5))
plt.plot(outputs, label="Net Postsynaptic Current")
plt.axhline(0, color='gray', ls='--')
plt.title("Advanced Synapse Demo – Excitation/Inhibition Balance with Astrocytic Modulation")
plt.xlabel("Presynaptic Ca2+ Steps")
plt.ylabel("EPSP/IPSP (arbitrary units)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/advanced_synapse_demo.png", dpi=300)
plt.close()
print("Advanced synaptic model with therapeutic targets ready!")
