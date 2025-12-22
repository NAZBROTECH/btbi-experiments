from pydantic import BaseModel
from typing import Literal

class TherapeuticPacket(BaseModel):
    receptor_subtype: Literal["AMPA", "NMDA", "GABA_A", "GABA_B"] = "AMPA"
    vesicle_release_prob: float = 0.5
    plasticity_modulator: float = 1.0            # second messenger level
    astrocytic_influence: float = 0.3            # gliotransmission
    therapeutic_target_flag: bool = False        # mark for simulated intervention
    imbalance_type: Literal["exc_over", "inh_over", "none"] = "none"
    source_user_id: str
    timestamp_ms: float
