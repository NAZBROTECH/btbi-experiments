from pydantic import BaseModel
from typing import List, Dict

class AgentCommPacket(BaseModel):
    hypervector: List[int] = []                  # -1/1 HDC vector
    attention_weights: Dict[str, float] = {}     # agent: weight
    oscillation_phase: float = 0.0
    homeostatic_weight: float = 1.0
    symbolic_rule: str = ""                      # e.g., "if valence>0 then boost"
    coordination_score: float = 0.0
    source_user_id: str
    timestamp_ms: float
