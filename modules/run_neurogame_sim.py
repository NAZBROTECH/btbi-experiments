"""
run_neurogame_sim.py
-----------------------------------
Demo script: Uses NeurogameSimulator to control a simple game variable.
Object moves left with attention, right with relaxation.
"""

import time
from modules.neurogame_sim import NeurogameSimulator

def run_demo():
    sim = NeurogameSimulator()
    object_x = 50  # starting position

    print("Starting Neurogame Simulation Demo...")
    print("Ctrl + C to exit.\n")

    while True:
        data = sim.get_signals()

        if data["status"] == "dropout":
            print("Signal dropout! Object paused.")
        else:
            attention = data["attention"]
            relaxation = data["relaxation"]

            object_x -= attention * 2
            object_x += relaxation * 2

            print(f"ATT={attention}  REL={relaxation}  | object_x = {round(object_x, 2)}")

        time.sleep(0.4)


if __name__ == "__main__":
    run_demo()
