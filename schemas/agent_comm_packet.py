from pydantic import BaseModel
from typing import List, Dict

class AgentCommPacket(BaseModel):
    message_vector: List[float] = []             # embedded thought
    attention_weights: Dict[str, float] = {}     # user: weight
    backprop_feedback: float = 0.0               # credit for learning
    emergent_protocol_id: str = "v0.1"
    coordination_score: float = 0.0
    source_user_id: str
    timestamp_ms: float
