import numpy as np
from schemas.agent_comm_packet import AgentCommPacket

def learn_protocol(packets):
    # Simple attention update from feedback
    for p in packets:
        if p.backprop_feedback > 0.5:
            p.attention_weights[p.source_user_id] = min(1.0, p.attention_weights.get(p.source_user_id, 0.5) + 0.1)
    total_score = np.mean([p.coordination_score for p in packets])
    print(f"Protocol learning step – avg coordination: {total_score:.2f}")
    return total_score

# Test
test_packets = [
    AgentCommPacket(message_vector=[0.8]*10, backprop_feedback=0.7, coordination_score=0.85, source_user_id="user1", timestamp_ms=0),
    AgentCommPacket(message_vector=[0.3]*10, backprop_feedback=0.2, coordination_score=0.4, source_user_id="user2", timestamp_ms=1000)
]
learn_protocol(test_packets)
