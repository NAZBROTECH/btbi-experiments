import numpy as np
from schemas.auditory_packet import AuditoryPacket

def binaural_localize(packets):
    # Simple ITD/ILD → azimuth calculation
    for p in packets:
        itd = p.interaural_time_diff_ms
        ild = p.interaural_level_diff_db
        # Rough mapping: max ITD ~0.6ms for 90°
        azimuth = (itd / 0.6) * 90
        azimuth += ild * 2  # ILD contribution
        p.localization_azimuth_deg = np.clip(azimuth, -90, 90)
    avg_azimuth = np.mean([p.localization_azimuth_deg for p in packets])
    print(f"Shared perceived source direction: {avg_azimuth:.1f}°")
    return packets

# Test: same thought from "left" for 3 users
test_packets = [
    AuditoryPacket(interaural_time_diff_ms=0.4, interaural_level_diff_db=6, source_user_id="user1", timestamp_ms=0),
    AuditoryPacket(interaural_time_diff_ms=0.35, interaural_level_diff_db=5, source_user_id="user2", timestamp_ms=10),
    AuditoryPacket(interaural_time_diff_ms=0.45, interaural_level_diff_db=7, source_user_id="user3", timestamp_ms=20)
]
binaural_localize(test_packets)
