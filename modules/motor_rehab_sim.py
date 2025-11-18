# motor_rehab_sim.py
# ---------------------------------------------------
# Synthetic motor-rehabilitation simulator for Synapse.
# Educational only. NO real neural or physiological data.
# All values are randomly generated for safe offline testing.

import numpy as np

class MotorRehabSim:
    """
    Simulates the chain:
    neural intent --> classifier decision --> FES trigger.
    Useful for testing BCIs without real EEG or real stimulation.
    """

    def __init__(self,
                 intent_threshold=0.6,
                 base_latency_ms=120,
                 latency_jitter_ms=40,
                 fatigue_rate=0.005):
        """
        Parameters:
        - intent_threshold: probability needed to count as 'intent'
        - base_latency_ms: average simulated time for stimulation response
        - latency_jitter_ms: random noise added to latency
        - fatigue_rate: how quickly success probability drops over repetitions
        """
        self.intent_threshold = intent_threshold
        self.base_latency = base_latency_ms
        self.latency_jitter = latency_jitter_ms
        self.fatigue_rate = fatigue_rate
        self.fatigue_level = 0.0  # starts fresh
        self.history = []         # store logs

    def generate_intent_signal(self):
        """
        Produce a synthetic probability value representing
        a classifier output estimating user's motor intent.
        """
        return np.clip(np.random.rand(), 0.0, 1.0)

    def check_intent(self, intent_prob):
        """
        Determine if intent probability is strong enough
        to trigger FES activation.
        """
        return intent_prob >= self.intent_threshold

    def simulate_latency(self):
        """
        Create a latency value: base + random jitter.
        """
        jitter = np.random.randn() * self.latency_jitter
        return max(0, self.base_latency + jitter)

    def apply_fatigue(self):
        """
        Simulate fatigue accumulation over time.
        Every activation attempt increases fatigue.
        Fatigue decreases success rate.
        """
        self.fatigue_level += self.fatigue_rate
        self.fatigue_level = min(0.9, self.fatigue_level)  # avoid going too high

    def simulate_activation(self):
        """
        Final stimulation step:
        success is reduced by accumulated fatigue.
        """
        success_prob = np.clip(1.0 - self.fatigue_level, 0.0, 1.0)
        return np.random.rand() < success_prob

    def run_step(self):
        """
        Run a full simulation cycle:
        1. generate classifier intent
        2. determine if activation should occur
        3. simulate latency + fatigue trends
        4. determine success/failure
        5. log results
        """
        intent_prob = self.generate_intent_signal()
        is_intent = self.check_intent(intent_prob)

        if is_intent:
            latency = self.simulate_latency()
            self.apply_fatigue()
            success = self.simulate_activation()
        else:
            latency = None
            success = False

        log = {
            "intent_prob": intent_prob,
            "intent_detected": is_intent,
            "fatigue_level": round(self.fatigue_level, 4),
            "latency_ms": latency,
            "activation_success": success
        }

        self.history.append(log)
        return log


# ----------------- DEMO ----------------------------
if __name__ == "__main__":
    sim = MotorRehabSim()
    for i in range(10):
        print(sim.run_step())
