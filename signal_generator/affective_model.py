import numpy as np
import matplotlib.pyplot as plt

class AffectiveBrain:
    def __init__(self, num_users=3):
        self.dopamine = np.ones(num_users) * 0.5    # motivation level per user
        self.oxytocin = np.zeros((num_users, num_users))  # bonding matrix
        self.history = {"dopamine": [], "bond": []}

    def exchange(self, sender, receiver, emotion_valence):
        # Dopamine boost for anticipation/reward
        self.dopamine[sender] += 0.1 * abs(emotion_valence)
        self.dopamine[receiver] += 0.08 * abs(emotion_valence)
        # Oxytocin bonding (stronger for positive valence)
        bond_boost = 0.15 if emotion_valence > 0 else 0.05
        self.oxytocin[sender, receiver] += bond_boost
        self.oxytocin[receiver, sender] += bond_boost  # symmetric
        # Cap values
        self.dopamine = np.clip(self.dopamine, 0, 1)
        self.oxytocin = np.clip(self.oxytocin, 0, 1)

    def run_session(self, steps=100):
        for step in range(steps):
            sender = np.random.randint(0, 3)
            receiver = (sender + 1) % 3
            valence = np.random.uniform(-0.5, 1.0)   # -negative to +positive emotion
            self.exchange(sender, receiver, valence)
            self.history["dopamine"].append(self.dopamine.copy())
            self.history["bond"].append(self.oxytocin.copy().mean())

# Demo: 3-user emotional sharing
brain = AffectiveBrain()
brain.run_session(150)

plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
for i in range(3):
    dop = [h[i] for h in brain.history["dopamine"]]
    plt.plot(dop, label=f"User {i+1} Dopamine")
plt.title("Dopamine Motivation Growth During Exchanges")
plt.legend()
plt.subplot(2,1,2)
plt.plot(brain.history["bond"], color='purple')
plt.title("Average Oxytocin Bonding Strength Over Time")
plt.tight_layout()
plt.savefig("signal_generator/affective_bonding_demo.png", dpi=300)
plt.close()
print("Affective reward & bonding simulation ready!")
