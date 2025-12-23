from pydantic import BaseModel
from typing import Literal

class NeuralinkPacket(BaseModel):
    electrode_count: int = 1024
    channel_bandwidth_bps: float = 0.0
    implant_depth_um: float = 5000.0            # thread penetration
    stimulation_mode: Literal["read", "write", "bidirectional"] = "read"
    patient_consent_flag: bool = True
    decoded_intent: str = ""                    # e.g., "move cursor left"
    source_user_id: str
    timestamp_ms: float
