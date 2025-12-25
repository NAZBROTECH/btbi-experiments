import numpy as np
from schemas.viral_packet import ViralPacket

def viral_propagation(packets):
    beneficial = [p for p in packets if p.domestication_level > 0.6 and p.immune_check_flag]
    harmful = len(packets) - len(beneficial)
    integration_gain = len(beneficial) * 0.15
    if harmful > 0:
        print(f"Immune system blocked {harmful} harmful packets")
    print(f"Beneficial integration gain: +{integration_gain:.2f}")
    return integration_gain

# Test
test_packets = [
    ViralPacket(rna_payload=[0.8]*10, domestication_level=0.8, immune_check_flag=True, source_user_id="user1", timestamp_ms=0),
    ViralPacket(rna_payload=[-0.5]*10, domestication_level=0.3, immune_check_flag=False, source_user_id="user2", timestamp_ms=1000)
]
viral_propagation(test_packets)
