import numpy as np
from schemas.sleep_cycle_packet import SleepCyclePacket

def offline_consolidation(packets, sleep_quality=0.8):
    # Simulate pruning noise + strengthening signal during sleep
    consolidated = []
    for p in packets:
        # Higher restoration = better fidelity
        new_signal = p.delta_power * sleep_quality + np.random.normal(0, 1-sleep_quality)
        consolidated.append(new_signal)
    improvement = np.mean(consolidated) - np.mean([p.delta_power for p in packets])
    print(f"Offline consolidation improvement: +{improvement:.2f}")
    return consolidated

# Test with dummy prior data
test_packets = [SleepCyclePacket(delta_power=np.random.uniform(0.3,0.8), source_user_id="user1", timestamp_ms=i*1000) for i in range(10)]
offline_consolidation(test_packets)
