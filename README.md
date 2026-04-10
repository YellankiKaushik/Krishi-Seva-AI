# 🌾 Krishi Seva AI Agent

### 🚀 Overview
Krishi Seva is an intelligent, real-time agricultural decision support system built on the **GitAgent standard**. It fetches live environmental data, predicts agricultural risks, and converts complex weather signals into simple, actionable farming advice to prevent crop loss.

---

### ❗ Problem Statement
Farmers today face a massive "insight gap." While they can access basic weather forecasts, they often lack the technical expertise to translate those numbers (e.g., 85% humidity) into specific field actions. This leads to:
*   **Preventable Crop Loss:** Delayed response to disease or heat stress.
*   **Resource Wastage:** Applying pesticides just before unscheduled rain.
*   **Decision Paralysis:** Inability to act decisively due to complex data.

---

### 💡 Solution
Krishi Seva acts as a specialized digital companion that "thinks" like an agronomist. It converts raw environmental data into direct, actionable directives—telling the farmer exactly **what to do** and **what to avoid** in the moment, ensuring optimal crop health and resource management.

---

### 🧠 How It Works (Pipeline)
The system operates as a modular intelligence pipeline:
1.  **Ingestion:** Fetches real-time metrics (Temp, Humidity, Condition) via the OpenWeatherMap API.
2.  **Analysis:** Processes signals through the `weather_analyzer` skill.
3.  **Risk Modeling:** Identifies threats (e.g., fungal risk, heat stress) using the `risk_predictor` skill.
4.  **Advisory:** Generates simple, direct instructions using the `advisory_generator` skill.

---

### 🤖 Agent Architecture (GitAgent)
This project strictly adheres to the GitAgent specifications, separating identity, logic, and operational constraints:
*   **`agent.yaml`**: Configuration hub for agent metadata and preferred models.
*   **`SOUL.md`**: Defines the agent’s core persona (direct, calm, farmer-centric).
*   **`RULES.md`**: Strict operational guardrails (e.g., "Must Never give vague advice").
*   **`skills/`**: Encapsulated logic units that drive the agent's capabilities.

---

### 🔧 Skills Breakdown
*   **`weather_analyzer`**: Interprets raw metrics and highlights potentially risky weather patterns.
*   **`risk_predictor`**: Logic engine that identifies specific agricultural threats (Heat stress, Fungal disease, Spraying risks).
*   **`advisory_generator`**: Translation layer that converts technical data into simple, actionable instructions.

---

### ▶️ How to Run
1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/YellankiKaushik/Krishi-Seva-AI.git
    cd Krishi-Seva-AI
    ```
2.  **Install Dependencies:**
    ```bash
    pip install requests
    ```
3.  **Execute the Agent:**
    ```bash
    python run_agent.py
    ```

---

### 📊 Example Output
```text
✅ LIVE WEATHER DATA
----------------------
Temperature: 33°C
Humidity: 85%
Condition: Overcast

⚠️ IDENTIFIED RISKS
----------------------
- High fungal disease risk
- Heat stress risk

🌱 ADVICE FOR FARMER
----------------------
- Apply preventive fungicide after rain.
- Irrigate crops early morning or evening.
```

---

### 🌍 Real-World Impact
Krishi Seva empowers small-scale farmers to move from reactive to proactive farming. By providing clarity on when to irrigate, when to spray, and how to protect crops from atmospheric stress, the agent significantly reduces financial risk and improves food security at the grassroots level.

---

### 🏆 Why This Project Stands Out
*   **Standard-Compliant:** Fully compatible with the GitAgent framework.
*   **Real-Time Ready:** Uses live API data rather than static samples.
*   **Action-Oriented:** Focuses on *decisions*, not just *displaying data*.
*   **Lightweight & Scalable:** Modular skill design allows for easy expansion into specialized crop-based logic.

---

### 🔮 Future Scope
*   **Voice Interface:** Automated voice alerts for non-literate farmers.
*   **Multi-Crop Logic:** Specialized skills for diverse crops like cotton, paddy, and wheat.
*   **Localized Wisdom:** Integrating local traditional farming practices into the advisory logic.

---

### 🏁 Conclusion
Krishi Seva AI Agent demonstrates the power of agentic workflows in solving fundamental real-world problems. By simplifying complex data into reliable advice, it ensures that technology serves those who feed the world.
