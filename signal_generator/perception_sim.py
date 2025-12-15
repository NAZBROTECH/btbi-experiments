import numpy as np
import matplotlib.pyplot as plt

class PerceptualBrain:
    def __init__(self, prior_belief=0.5):
        self.prior = prior_belief               # top-down expectation (0-1)
        self.history = []

    def perceive(self, raw_signal):
        # Predictive coding: perceived = raw + weighted prior
        perceived = (raw_signal * 0.7) + (self.prior * 0.3)
        # Illusion example: strong prior overrides weak signal
        if raw_signal < 0.4 and self.prior > 0.7:
            perceived = self.prior               # "see what you expect"
        self.history.append(perceived)
        return perceived

# Demo: 3 users get same raw signal but different priors → different realities
raw_signals = np.random.uniform(0.3, 0.7, 100)   # ambiguous input
user1 = PerceptualBrain(prior_belief=0.2)      # pessimistic bias
user2 = PerceptualBrain(prior_belief=0.5)      # neutral
user3 = PerceptualBrain(prior_belief=0.8)      # optimistic bias

perc1 = [user1.perceive(s) for s in raw_signals]
perc2 = [user2.perceive(s) for s in raw_signals]
perc3 = [user3.perceive(s) for s in raw_signals]

plt.figure(figsize=(10,6))
plt.plot(raw_signals, label="Raw Sensory Input", alpha=0.5, ls="--")
plt.plot(perc1, label="User 1 (Low Prior – Sees Negatively)")
plt.plot(perc2, label="User 2 (Neutral Prior)")
plt.plot(perc3, label="User 3 (High Prior – Sees Positively)")
plt.title("Perception Demo – Same World, Different Realities")
plt.ylabel("Perceived Intensity")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/perception_demo.png", dpi=300)
plt.close()
print("Perceptual simulation with predictive biases ready!")
