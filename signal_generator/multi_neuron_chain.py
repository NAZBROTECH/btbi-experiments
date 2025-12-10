import numpy as np
from schemas.action_potential_packet import ActionPotentialPacket

def propagate_chain(packets, noise_std=2.0):
    results = []
    for packet in packets:
        degraded = packet.copy()
        degraded.thought_intensity += np.random.normal(0, noise_std)
        degraded.propagation_speed *= np.random.uniform(0.9, 1.1)  # myelin jitter
        results.append(degraded)
    fidelity = sum(p.is_spike() for p in packets) / len(packets)
    received = sum(p.is_spike() for p in results) / len(results)
    print(f"Chain fidelity: {fidelity*100:.1f}% → {received*100:.1f}% after noise")
    return results

# Quick test
test_packets = [ActionPotentialPacket(thought_intensity=70, timestamp_ms=i*10, source_user_id="user1") for i in range(5)]
propagate_chain(test_packets)
