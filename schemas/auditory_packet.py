from pydantic import BaseModel
from typing import List

class AuditoryPacket(BaseModel):
    frequency_spectrum: List[float] = []       # tonotopic band powers
    amplitude_envelope: float = 1.0
    interaural_time_diff_ms: float = 0.0       # for localization
    interaural_level_diff_db: float = 0.0
    perceived_pitch_hz: float = 440.0
    localization_azimuth_deg: float = 0.0      # perceived direction
    emotional_valence: str = "neutral"         # e.g., "urgent", "calm"
    source_user_id: str
    timestamp_ms: float
