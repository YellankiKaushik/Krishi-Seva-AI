---
name: risk_predictor
description: "Predicts agricultural risks based on weather conditions"
allowed-tools: Read
---

# Risk Predictor

## Instructions

- Analyze the weather insights carefully.

- Identify risks using patterns:

  - High humidity + rain → High fungal disease risk
  - High temperature (>30°C) → Heat stress risk
  - No rain + high temperature → Irrigation needed
  - Strong wind or rain → Avoid spraying

- If key data is missing, respond:
  "Insufficient data to assess full risk."

- Assign risk level:
  - Low
  - Medium
  - High

- Clearly explain the reason for each risk.

## Output Format

Identified Risks:
Risk Level:
Reason: