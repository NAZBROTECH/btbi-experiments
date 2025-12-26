import numpy as np
from schemas.therapy_packet import TherapyPacket

def remote_therapy_session(packets):
    child_state = [p.brainwave_state for p in packets if p.user_role == "child"]
    if child_state:
        avg_theta = np.mean([s.get("theta", 0.5) for s in child_state])
        if avg_theta > 0.6:  # high activity = needs calm
            for p in packets:
                if p.user_role == "doctor":
                    p.doctor_override = {"binaural_boost": 0.4}
            print("Doctor remotely applied calm boost")
        progress = 1 - avg_theta
        print(f"Session progress (calm): {progress:.2f}")
    return progress

# Test
test_packets = [
    TherapyPacket(brainwave_state={"theta": 0.7}, user_role="child", timestamp_ms=0),
    TherapyPacket(user_role="parent", parent_monitor_flag=True, timestamp_ms=500),
    TherapyPacket(user_role="doctor", timestamp_ms=1000)
]
remote_therapy_session(test_packets)
