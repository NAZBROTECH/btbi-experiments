from pydantic import BaseModel
from typing import Dict, List

class PhysicsPacket(BaseModel):
    membrane_voltage: List[float] = []          # time series
    ion_conductance: Dict[str, float] = {"Na": 120.0, "K": 36.0, "Ca": 0.0, "leak": 0.3}
    propagation_velocity_m_s: float = 100.0
    cable_length_constant_um: float = 200.0     # spatial decay
    network_integration_sum: float = 0.0        # summed synaptic inputs
    myelination_factor: float = 1.0             # 1 = unmyelinated, >10 = saltatory boost
    source_neuron_id: str
    timestamp_ms: float
