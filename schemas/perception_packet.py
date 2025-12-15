from pydantic import BaseModel
from typing import Dict

class PerceptionPacket(BaseModel):
    raw_sensory_data: Dict[str, float] = {}     # e.g., {"visual": 0.4, "auditory": 0.6}
    perceived_interpretation: str = ""          # e.g., "threat" or "opportunity"
    predictive_prior: float = 0.5               # 0.0–1.0 top-down belief strength
    illusion_risk: bool = False
    user_bias_profile: Dict[str, float] = {}    # personalized priors per category
    source_user_id: str
    timestamp_ms: float
