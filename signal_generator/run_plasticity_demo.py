import numpy as np
import matplotlib.pyplot as plt

class SimpleSynapse:
    def __init__(self, weight=0.5, plasticity_rate=0.02):
        self.weight = weight                    # synaptic strength (0–1)
        self.plasticity_rate = plasticity_rate  # LTP/LTD speed
        self.history = []

    def transmit(self, presynaptic_spike, postsynaptic_spike=None):
        if presynaptic_spike = 1 if presynaptic_spike else 0
        output = presynaptic_spike * self.weight
        
        # Hebbian LTP/LTD
        if presynaptic_spike and postsynaptic_spike:
            self.weight = min(1.0, self.weight + self.plasticity_rate)   # LTP
        elif presynaptic_spike and not postsynaptic_spike:
            self.weight = max(0.1, self.weight - self.plasticity_rate/2) # LTD
        
        self.history.append(self.weight)
        return output

# Demo: 3-user loop (repeated "thought exchanges")
syn12 = SimpleSynapse(0.5)
syn23 = SimpleSynapse(0.5)
syn31 = SimpleSynapse(0.5)

weights = [[], [], []]
for step in range(200):
    pre1 = np.random.rand() > 0.7   # User 1 thinks
    pre2 = np.random.rand() > 0.7
    pre3 = np.random.rand() > 0.7
    
    out12 = syn12.transmit(pre1, pre2)
    out23 = syn23.transmit(pre2, pre3)
    out31 = syn31.transmit(pre3, pre1)
    
    weights[0].append(syn12.weight)
    weights[1].append(syn23.weight)
    weights[2].append(syn31.weight)

plt.figure(figsize=(10,6))
plt.plot(weights[0], label="User1 → User2")
plt.plot(weights[1], label="User2 → User3")
plt.plot(weights[2], label="User3 → User1")
plt.title("Synaptic Plasticity Demo – LTP in 3-User BTBI Loop")
plt.xlabel("Thought Exchanges")
plt.ylabel("Synaptic Weight")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/synaptic_plasticity_demo.png", dpi=300)
plt.close()
print("Synaptic plasticity simulation complete!")
