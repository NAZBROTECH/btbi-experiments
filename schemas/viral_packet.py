from pydantic import BaseModel
from typing import List

class ViralPacket(BaseModel):
    gag_capsid_protein: float = 0.0              # packaging efficiency
    integration_site: str = "memory_locus"       # analogy for long-term storage
    rna_payload: List[float] = []                # thought content vector
    domestication_level: float = 0.0             # 0-1 co-opted utility
    immune_check_flag: bool = True               # block harmful spread
    propagation_risk: float = 0.0
    source_user_id: str
    timestamp_ms: float
