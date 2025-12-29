import numpy as np
import matplotlib.pyplot as plt

class BioInspiredComm:
    def __init__(self, num_agents=4, dim=10000):  # HDC high dimension
        self.num_agents = num_agents
        self.dim = dim
        # Random hypervectors for agents
        self.agent_vectors = np.random.choice([-1, 1], size=(num_agents, dim))
        self.attention = np.ones((num_agents, num_agents)) / num_agents
        self.weights = np.ones((num_agents, num_agents))   # synaptic/homeostatic
        self.phase = np.zeros(num_agents)                  # oscillation phase
        self.history = []

    def oscillate(self):
        self.phase += 0.2  # theta rhythm ~6-8 Hz
        return np.sin(self.phase)

    def communicate(self, sender):
        osc = self.oscillate()
        # Attention-weighted hypervector bundle
        weighted = self.attention[sender] * self.agent_vectors[sender]
        message = np.sum(weighted[:, np.newaxis] * self.agent_vectors, axis=0)
        # Homeostatic normalization
        self.weights[sender] = np.clip(self.weights[sender] + 0.01 * osc[sender], 0.5, 1.5)
        self.weights /= self.weights.mean()
        coord = np.cosine_similarity(message.reshape(1,-1), self.agent_vectors.mean(axis=0).reshape(1,-1))[0][0]
        self.history.append(coord)
        return coord

# Demo: 4-agent rhythmic attention comm
comm = BioInspiredComm()
scores = []
for step in range(120):
    sender = step % 4
    score = comm.communicate(sender)
    scores.append(score)

plt.figure(figsize=(10,6))
plt.plot(scores, color='magenta', lw=3)
plt.title("Bio-Inspired Comm Demo – Oscillation + Homeostasis + HDC Attention")
plt.xlabel("Communication Steps")
plt.ylabel("Coordination Similarity (Higher = Better Sync)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/bio_inspired_comm_demo.png", dpi=300)
plt.close()
print("Oscillation, homeostasis & HDC attention simulation ready!")
