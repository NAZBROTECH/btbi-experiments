from schemas.perception_packet import PerceptionPacket

def calibrate_reality(packets):
    # Simple Filter Core calibration: average priors to converge
    avg_prior = np.mean([p.predictive_prior for p in packets])
    for p in packets:
        p.predictive_prior = (p.predictive_prior + avg_prior) / 2   # gradual alignment
    convergence = 1 - np.std([p.predictive_prior for p in packets])
    print(f"Shared reality convergence: {convergence:.2%}")
    return packets

# Quick test
test = [
    PerceptionPacket(predictive_prior=0.2, source_user_id="user1", timestamp_ms=0),
    PerceptionPacket(predictive_prior=0.8, source_user_id="user2", timestamp_ms=10),
    PerceptionPacket(predictive_prior=0.5, source_user_id="user3", timestamp_ms=20)
]
calibrate_reality(test)
