from pydantic import BaseModel
from typing import Literal

class ActionPotentialPacket(BaseModel):
    voltage_threshold: float = -55.0      # mV
    spike_amplitude: int = 100            # arbitrary units
    refractory_duration_ms: float = 2.0
    propagation_speed_m_s: float = 100.0
    thought_intensity: float             # drives firing rate
    neuron_type: Literal["excitatory", "inhibitory"] = "excitatory"
    timestamp_ms: float
    source_user_id: str
    noise_level: float = 0.0

    def is_spike(self) -> bool:
        return self.thought_intensity > self.voltage_threshold + self.noise_level
