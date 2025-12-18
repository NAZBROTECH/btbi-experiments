import numpy as np
from schemas.affective_packet import AffectivePacket

def process_affective_exchange(packets):
    total_valence = np.mean([p.emotional_valence for p in packets])
    avg_dopamine = np.mean([p.dopamine_motivation for p in packets])
    bond_gain = avg_dopamine * (1 + total_valence)   # positive emotions boost bonding faster
    print(f"Session valence: {total_valence:.2f} | Dopamine drive: {avg_dopamine:.2f}")
    print(f"Projected oxytocin bond gain: +{bond_gain:.2f}")
    return bond_gain

# Test
test_packets = [
    AffectivePacket(emotional_valence=0.8, dopamine_motivation=0.7, source_user_id="user1", dest_user_id="user2", timestamp_ms=0),
    AffectivePacket(emotional_valence=0.6, dopamine_motivation=0.6, source_user_id="user2", dest_user_id="user3", timestamp_ms=1000),
    AffectivePacket(emotional_valence=-0.2, dopamine_motivation=0.4, source_user_id="user3", dest_user_id="user1", timestamp_ms=2000)
]
process_affective_exchange(test_packets)
