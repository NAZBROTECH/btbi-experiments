from pydantic import BaseModel, Field
from typing import List, Optional

class SynapseMessage(BaseModel):
    """
    Structured neural-signal communication packet.
    Ensures Synapse only transmits validated message intent—not thoughts or identity.
    """

    sender_id: str = Field(..., description="Unique ID of the sender")
    target_id: str = Field(..., description="ID of receiving user/device")
    intent_label: str = Field(..., description="Linguistic-like intent category")
    signal_pattern: List[float] = Field(..., description="Neural-encoded message pattern")
    timestamp_ms: int = Field(..., description="Message creation time (ms)")

    # Optional metadata for safe routing
    metadata: Optional[dict] = Field(
        default=None,
        description="Optional structured metadata for routing/consent validation."
    )
