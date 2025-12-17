from pydantic import BaseModel
from typing import Literal

class SleepCyclePacket(BaseModel):
    sleep_stage: Literal["NREM1", "NREM2", "NREM3", "REM", "wake"] = "wake"
    delta_power: float = 0.0              # deep sleep intensity
    rem_intensity: float = 0.0            # dream/cognitive processing
    circadian_phase_hours: float = 0.0    # 0-24 clock
    restoration_level: float = 0.0        # 0-1 cumulative recovery
    user_efficiency_profile: Literal["normal", "short_sleeper", "super"] = "normal"
    source_user_id: str
    timestamp_ms: float
