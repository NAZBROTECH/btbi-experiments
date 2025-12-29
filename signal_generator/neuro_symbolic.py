import numpy as np
from schemas.agent_comm_packet import AgentCommPacket

def neuro_symbolic_process(packets):
    # Symbolic rule example: boost positive valence
    for p in packets:
        if "positive" in p.symbolic_rule:
            p.attention_weights = {k: v*1.2 for k,v in p.attention_weights.items()}
    avg_coord = np.mean([p.coordination_score for p in packets])
    print(f"Neuro-symbolic rule applied – avg coordination: {avg_coord:.2f}")
    return avg_coord

# Test
test_packets = [
    AgentCommPacket(hypervector=[1]*100, symbolic_rule="positive valence boost", coordination_score=0.82, source_user_id="user1", timestamp_ms=0)
]
neuro_symbolic_process(test_packets)
