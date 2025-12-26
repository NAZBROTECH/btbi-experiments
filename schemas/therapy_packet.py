from pydantic import BaseModel
from typing import Dict

class TherapyPacket(BaseModel):
    brainwave_state: Dict[str, float] = {}       # delta/theta/alpha/beta powers
    feedback_stimulation: Dict[str, float] = {}  # auditory parameters
    progress_score: float = 0.0
    parent_monitor_flag: bool = False
    doctor_override: Dict[str, float] = {}       # remote adjustments
    session_id: str
    user_role: str = "child"                     # child/parent/doctor
    timestamp_ms: float
