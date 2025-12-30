import numpy as np
from schemas.packet_compiler import PacketCompiler

def stream_inference(packets, config):
    latencies = []
    for p in packets:
        load = np.random.uniform(0.2, 0.9)
        util = 0.95 if config.reconfiguration_mode == "latency" else 0.7
        lat = 15 / util * load
        latencies.append(lat)
    avg_lat = np.mean(latencies)
    print(f"Streaming batch-1 latency: {avg_lat:.2f} (mode: {config.reconfiguration_mode})")
    return avg_lat

# Test
config = PacketCompiler(reconfiguration_mode="latency")
test_packets = [None] * 50  # simulated stream
stream_inference(test_packets, config)
