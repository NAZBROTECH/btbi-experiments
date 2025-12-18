from pydantic import BaseModel
from typing import Literal

class AffectivePacket(BaseModel):
    emotional_valence: float = 0.0               # -1 (negative) to +1 (positive)
    valence_label: Literal["joy", "fear", "anger", "sadness", "disgust", "surprise", "neutral"] = "neutral"
    dopamine_motivation: float = 0.5             # 0-1 drive to share
    oxytocin_bond_strength: float = 0.0          # per user-pair
    desire_intensity: float = 0.0                # normalized arousal
    reward_prediction_error: float = 0.0
    ethical_safeguard_flag: bool = True          # consent/privacy check
    source_user_id: str
    dest_user_id: str
    timestamp_ms: float
