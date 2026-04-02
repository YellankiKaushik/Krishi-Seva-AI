# 🌾 Krishi Seva Agent

## 🚀 Overview

Krishi Seva is a GitAgent-based AI system that transforms real-time weather data into actionable farming advice.

It helps farmers make better decisions by predicting risks such as crop disease, irrigation needs, and spraying conditions.

---

## ❗ Problem

Farmers receive weather data but struggle to translate it into actionable decisions.

This leads to:
- Crop damage
- Incorrect spraying
- Water mismanagement
- Financial losses

---

## 💡 Solution

Krishi Seva acts as an intelligent agricultural assistant that:

1. Fetches real-time weather data  
2. Analyzes environmental risks  
3. Generates simple, actionable advice  

---

## 🧠 How It Works

```
Weather API → Risk Analysis → Advice Generation
```

### Steps:
- Collects temperature, humidity, and conditions
- Detects risks like fungal disease or heat stress
- Provides clear farmer-friendly recommendations

---

## ⚙️ Agent Architecture (GitAgent)

- agent.yaml → Agent configuration  
- SOUL.md → Agent identity  
- RULES.md → Constraints  
- skills/:
  - weather_analyzer
  - risk_predictor
  - advisory_generator  

---

## 🧪 Demo

### Real-Time Execution

```bash
python live_weather.py
```

### Example Output:

```
Temperature: 34°C
Humidity: 31%
Condition: few clouds

No major risks detected
```

---

### High-Risk Scenario (Simulated)

```
Temperature: 30°C
Humidity: 85%
Condition: rain

Risk:
- High fungal disease
- Spray risk

Advice:
- Apply fungicide
- Avoid spraying
```

---

## 🌍 Impact

- Helps farmers take correct actions  
- Reduces crop loss  
- Works even with simple phone-based delivery (future scope)  

---

## 🔮 Future Scope

- Voice call alerts (local language)  
- Crop-specific recommendations  
- Market price insights  
- Government scheme alerts  

---

## 🏁 Conclusion

Krishi Seva bridges the gap between weather data and real-world farming decisions using AI agent intelligence.