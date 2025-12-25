import numpy as np
import matplotlib.pyplot as plt

class ViralIntelligence:
    def __init__(self, num_users=4):
        self.num_users = num_users
        self.capsid_payload = np.zeros(num_users)   # "RNA" thought content
        self.integration_level = np.zeros(num_users)  # domesticated "gene" strength
        self.history = []

    def propagate_viral_thought(self, sender, payload_intensity):
        # Capsid packaging + transfer
        self.capsid_payload += payload_intensity * 0.3
        # Beneficial integration (Arc-like)
        if payload_intensity > 0.6:
            self.integration_level[sender] += 0.1
            # Spread to others
            self.integration_level += 0.05
        self.integration_level = np.clip(self.integration_level, 0, 1)
        coord = np.mean(self.integration_level)
        self.history.append(coord)
        return coord

# Demo: beneficial viral thought spreads intelligence
viral = ViralIntelligence(4)
scores = []
for step in range(100):
    sender = 0 if step % 20 == 0 else np.random.randint(0,4)  # periodic strong sender
    intensity = 0.9 if sender == 0 else np.random.uniform(0.2,0.5)
    score = viral.propagate_viral_thought(sender, intensity)
    scores.append(score)

plt.figure(figsize=(10,6))
plt.plot(scores, color='green', lw=3)
plt.title("Viral-Inspired Emergent Intelligence Demo – Beneficial Thought Integration")
plt.xlabel("Propagation Steps")
plt.ylabel("Network Integration Level (Higher = Smarter Coordination)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/viral_intelligence_demo.png", dpi=300)
plt.close()
print("Viral capsid-inspired intelligence propagation ready!")
