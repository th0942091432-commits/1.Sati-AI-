"""
Environment / User
        │
        ▼
[1. Input Encoding & Context Assembly]
        │
        ▼
[2. Pattern Inference & Initial Evaluation]
        │
        ▼
[3. Risk / Uncertainty / Conflict Scoring]
        │
        ├── Low Risk ──> [Fast Response Path] ──┐
        │                                       │
        └── High Risk ─> [Deliberation Path] ───┤
                                                ▼
                              [4. Verification & Safety Gate]
                                                │
                   ┌────────────────────────────┼─────────────────────┐
                   ▼                            ▼                     ▼
              Respond                      Ask for Info          Human Review
                   │
                   ▼
             [Outcome Monitor]
                   │
                   ▼
       [Filtered Feedback / Memory Update]
"""