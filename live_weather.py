import requests

API_KEY = "af5422ca4c776de67d2fc96043f089e6"
CITY = "Hyderabad"


# 🔹 Step 1: Fetch Live Weather
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        # print("\nDEBUG RESPONSE:", data)

        if data.get("cod") != 200:
            print("\n❌ API Error:", data.get("message"))
            return None, None, None

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        return temp, humidity, condition

    except Exception as e:
        print("\n❌ Error occurred:", e)
        return None, None, None


# 🔹 Step 2: Risk Prediction (Agent Thinking)
def analyze_risk(temp, humidity, condition):
    risks = []

    if humidity >= 75:
        risks.append("High fungal disease risk")

    if temp >= 35:
        risks.append("Heat stress risk")

    if "rain" in condition.lower():
        risks.append("Avoid spraying due to rain")

    return risks


# 🔹 Step 3: Advisory Generation (Agent Output)
def generate_advice(risks):
    advice = []

    if not risks:
        advice.append("Conditions are normal. Continue regular monitoring.")

    for risk in risks:
        if "fungal" in risk.lower():
            advice.append("Apply preventive fungicide after rain.")
        elif "heat" in risk.lower():
            advice.append("Irrigate crops early morning or evening.")
        elif "spraying" in risk.lower():
            advice.append("Avoid pesticide spraying during rain.")

    return advice


# 🔹 Main Execution Flow
def main():
    print("\n🚀 Fetching live weather data...")

    temp, humidity, condition = get_weather()
    
    # DEMO MODE (temporary)
    # temp = 30
    # humidity = 85
    # condition = "rain"
    
    if temp is None:
        print("\n⚠️ Failed to fetch weather data.")
        return

    print("\n✅ LIVE WEATHER DATA")
    print("----------------------")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

    # 🔥 Decision Engine
    risks = analyze_risk(temp, humidity, condition)
    advice = generate_advice(risks)

    print("\n⚠️ IDENTIFIED RISKS")
    print("----------------------")
    if risks:
        for r in risks:
            print(f"- {r}")
    else:
        print("- No major risks detected")

    print("\n🌱 ADVICE FOR FARMER")
    print("----------------------")
    for a in advice:
        print(f"- {a}")


if __name__ == "__main__":
    main()