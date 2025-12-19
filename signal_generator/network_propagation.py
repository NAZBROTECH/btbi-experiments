import numpy as np
from schemas.physics_packet import PhysicsPacket

def propagate_chain(num_neurons=5, steps=100):
    voltages = np.zeros((num_neurons, steps))
    for step in range(steps):
        for n in range(num_neurons):
            I_syn = 8 if n == 0 and step > 20 else 0  # input at first neuron
            delay = n * 2  # simple cable delay
            voltages[n, step] = np.sin(step/10 + delay) * 30 if I_syn else -65
    avg_fidelity = np.corrcoef(voltages[0], voltages[-1])[0,1]
    print(f"End-to-end fidelity in {num_neurons}-neuron chain: {avg_fidelity:.2f}")
    return voltages

# Run demo
chain_V = propagate_chain()
