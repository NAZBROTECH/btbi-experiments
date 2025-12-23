import numpy as np
from schemas.neuralink_packet import NeuralinkPacket

def control_cursor(packets, target="cursor"):
    intents = [p.decoded_intent for p in packets if p.patient_consent_flag]
    if "left" in intents:
        position = -10
    elif "right" in intents:
        position = 10
    else:
        position = 0
    accuracy = len([i for i in intents if "move" in i]) / len(packets)
    print(f"Cursor position: {position} | Control accuracy: {accuracy:.1%}")
    return position

# Test: shared thought control
test_packets = [
    NeuralinkPacket(decoded_intent="move cursor right", channel_bandwidth_bps=9.2, source_user_id="helper1", timestamp_ms=0),
    NeuralinkPacket(decoded_intent="move cursor right", channel_bandwidth_bps=8.7, source_user_id="helper2", timestamp_ms=100),
    NeuralinkPacket(decoded_intent="idle", channel_bandwidth_bps=2.1, source_user_id="patient", timestamp_ms=200)
]
control_cursor(test_packets)
