# Synapse Inference Privacy & Safety Requirements

## Core Safety Principles
Any real-time inference backend handling neural-signal messages must enforce:

### 1. Explicit Consent
All users must knowingly opt-in for connection, encoding, and decoding.
No silent data processing is allowed.

### 2. No Thought Extraction
Decoding models must only process *structured communication signals*,
not private thoughts, memories, or identity-related patterns.

### 3. Secure Transmission
All neural-signal messages must be encrypted during:
- transmission
- storage
- inference

### 4. Model Transparency
All models must be documented:
- what they decode
- what they DO NOT decode
- limitations and boundaries

### 5. User Control
Users can disconnect, disable encoding, or wipe data at any time.

These rules scale with the technology to keep Synapse ethical and safe.
