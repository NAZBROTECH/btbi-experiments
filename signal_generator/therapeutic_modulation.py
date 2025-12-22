import numpy as np
from schemas.therapeutic_packet import TherapeuticPacket

def therapeutic_intervention(packets, target="GABA_boost"):
    net_exc = np.mean([1 if p.receptor_subtype in ["AMPA","NMDA"] else 0 for p in packets])
    if net_exc > 0.7:  # simulated epilepsy-like overexcitation
        for p in packets:
            if target == "GABA_boost" and p.receptor_subtype.startswith("GABA"):
                p.astrocytic_influence += 0.4
                p.therapeutic_target_flag = True
    restored_balance = 1 - abs(net_exc - 0.5)
    print(f"Pre-intervention imbalance: {net_exc:.2f} | Post: {restored_balance:.2f}")
    return packets

# Test
test_packets = [TherapeuticPacket(receptor_subtype="AMPA" if i%2==0 else "GABA_A") for i in range(20)]
therapeutic_intervention(test_packets)
