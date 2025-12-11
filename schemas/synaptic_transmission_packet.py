from pydantic import BaseModel
from typing import Literal

class SynapticTransmissionPacket(BaseModel):
    neurotransmitter_type: Literal["glutamate", "gaba", "dopamine"] = "glutamate"
    plasticity_weight: float = 0.5          # 0.1 – 1.0 (LTP/LTD)
    cleft_delay_ms: float = 1.0
    receptor_binding_strength: float = 1.0
    presynaptic_spike: bool
    postsynaptic_response: float = 0.0
    source_user_id: str
    dest_user_id: str
    timestamp_ms: float
