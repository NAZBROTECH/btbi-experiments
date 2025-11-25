"""
neurogame_sim.py
-----------------------------------
Simulated EEG signal generator for Synapse.
Creates two channels: attention and relaxation.
Includes optional noise, drift, and dropout to mimic real hardware.
"""

import random
import math
import time


class NeurogameSimulator:
    def __init__(self, noise_level=0.1, drift_rate=0.01, dropout_chance=0.02):
        self.attention = 0.5
        self.relaxation = 0.5
        self.noise_level = noise_level
        self.drift_rate = drift_rate
        self.dropout_chance = dropout_chance
        self.t = 0

    def _apply_noise(self, value):
        return value + random.uniform(-self.noise_level, self.noise_level)

    def _apply_drift(self, value):
        drift = math.sin(self.t * self.drift_rate) * 0.05
        return value + drift

    def _dropout(self):
        return random.random() < self.dropout_chance

    def get_signals(self):
        self.t += 1

        if self._dropout():
            return {"attention": None, "relaxation": None, "status": "dropout"}

        att = self._apply_noise(self._apply_drift(self.attention))
        rel = self._apply_noise(self._apply_drift(self.relaxation))

        att = max(0, min(1, att))
        rel = max(0, min(1, rel))

        return {
            "attention": round(att, 3),
            "relaxation": round(rel, 3),
            "status": "ok"
        }


if __name__ == "__main__":
    sim = NeurogameSimulator()
    while True:
        print(sim.get_signals())
        time.sleep(0.5)
