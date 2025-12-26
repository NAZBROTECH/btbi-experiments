import numpy as np
import matplotlib.pyplot as plt

class NeurofeedbackTherapy:
    def __init__(self, num_users=3):
        self.num_users = num_users
        self.brainwaves = np.random.uniform(0.3, 0.8, num_users)  # theta/alpha power
        self.calm_level = np.zeros(num_users)
        self.history = []

    def apply_feedback(self, doctor_adjust=0.0):
        # Binaural/auditory stimulation to boost calm
        feedback = np.sin(np.linspace(0, 10, 100)) * 0.2 + doctor_adjust
        self.brainwaves += feedback.mean() * 0.1
        self.brainwaves = np.clip(self.brainwaves, 0, 1)
        self.calm_level = 1 - self.brainwaves  # lower activity = calmer
        avg_calm = np.mean(self.calm_level)
        self.history.append(avg_calm)
        return avg_calm

# Demo: parent monitors, doctor remotely tunes
therapy = NeurofeedbackTherapy(3)
calm_scores = []
for session in range(50):
    # Normal session
    calm = therapy.apply_feedback()
    if session > 30:  # doctor intervention
        calm = therapy.apply_feedback(doctor_adjust=0.3)
    calm_scores.append(calm)

plt.figure(figsize=(10,6))
plt.plot(calm_scores, label="Group Calm Level", color='teal', lw=3)
plt.axvline(30, color='purple', ls='--', label="Doctor Remote Adjustment")
plt.title("Neurofeedback Therapy Demo – Remote Connectivity for Calm")
plt.xlabel("Session Steps")
plt.ylabel("Calm Score (Higher = Better)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("signal_generator/neurofeedback_demo.png", dpi=300)
plt.close()
print("Neurofeedback therapeutic loop ready!")
