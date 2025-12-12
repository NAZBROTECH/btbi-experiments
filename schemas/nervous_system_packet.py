from pydantic import BaseModel
from typing import Literal, List

class NervousSystemPacket(BaseModel):
    system_type: Literal["CNS", "PNS", "ANS"]
    autonomic_state: Literal["sympathetic", "parasympathetic", "neutral"] = "neutral"
    sensory_input: List[float] = []      # raw "thought" intensities
    effector_output: bool = False
    stress_level: float = 0.0            # 0–1
    source_user_id: str
    timestamp_ms: float
