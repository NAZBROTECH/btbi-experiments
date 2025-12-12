import numpy as np
import matplotlib.pyplot as plt

class NervousSystemNode:
    def __init__(self, role="CNS"):
        self.role = role                     # "PNS", "CNS", "ANS"
        self.threshold = 0.6
        self.stress_level = 0.0              # 0.0 = calm, 1.0 = max sympathetic

    def process(self, sensory_inputs):
        total = np.sum(sensory_inputs)
        # ANS modulates threshold (fight-or-flight = easier firing)
        effective_thresh = self.threshold * (1 - 0.4*self.stress_level)
        output = 1 if total > effective_thresh else 0
        return output

# Demo: 3-user mini nervous system
pns = NervousSystemNode("PNS")   # senses "thought"
cns = NervousSystemNode("CNS")   # integrates
ans = NervousSystemNode("ANS")   # adds stress modulation

history = []
for step in range(150):
    # User1 sends a "thought" (random intensity)
    thought = np.random.rand()
    cns_out = cns.process([thought])
    ans.stress_level = 0.8 if step > 100 else 0.2   # sudden "stress" at step 100
    final = ans.process([cns_out])
    history.append(final)

plt.figure(figsize=(10,4))
plt.plot(history, label="BTBI Output Signal", lw=2)
plt.axvline(100, color='red', ls='--', label="Stress event (sympathetic activation)")
plt.title("Nervous System Hierarchy Demo – Stress Modulates Transmission")
plt.legend()
plt.tight_layout()
plt.savefig("signal_generator/nervous_system_demo.png", dpi=300)
plt.close()
print("Nervous system hierarchy simulation ready!")
