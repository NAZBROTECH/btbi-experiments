from pydantic import BaseModel
from typing import Literal

class PacketCompiler(BaseModel):
    model_framework: Literal["PyTorch", "TensorFlow", "ONNX", "HuggingFace"] = "ONNX"
    reconfiguration_mode: Literal["latency", "power", "balanced"] = "balanced"
    utilization_target: float = 0.9               # >90% goal
    memory_bandwidth_reduction: float = 0.0
    deployment_bitstream: str = ""                # analog for compiled output
    batch_size: int = 1                           # BTBI real-time focus
    target_hardware: str = "edge"                 # FPGA/ASIC simulation
