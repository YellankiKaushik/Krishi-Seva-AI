import requests

API_KEY = "af5422ca4c776de67d2fc96043f089e6"
CITY = input("Enter city (default: Hyderabad): ") or "Hyderabad"


# 🔹 Step 1: Fetch Live Weather
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

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


# 🔹 Step 2: Risk Prediction
def analyze_risk(temp, humidity, condition):
    # print("\n[DEBUG] Risk Analysis Started")
    # print(f"[DEBUG] Input → Temp: {temp}, Humidity: {humidity}, Condition: {condition}")
    risks = []

    if humidity >= 75:
        # print("[DEBUG] Rule Triggered: High Humidity → Fungal Risk")
        risks.append("High fungal disease risk")

    if temp >= 35:
        # print("[DEBUG] Rule Triggered: High Temperature → Heat Stress")
        risks.append("Heat stress risk")

    if any(word in condition.lower() for word in ["rain", "drizzle", "storm", "shower", "thunder"]):
        # print("[DEBUG] Rule Triggered: Rain-like Condition → Avoid Spraying")
        risks.append("Avoid spraying due to rain")

    if any(word in condition.lower() for word in ["smoke", "haze"]):
        risks.append("Air quality may affect crop health")

    return risks




# 🔹 Step 3: Advisory Generation
def generate_advice(risks):
    # print("\n[DEBUG] Generating Advice Based on Risks:", risks)
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


# 🔹 Main Execution (REAL SYSTEM)
def main():
    print("\n🚀 Fetching live weather data...")

    temp, humidity, condition = get_weather()

    if temp is None:
        print("\n⚠️ Failed to fetch weather data.")
        return

    print("\n✅ LIVE WEATHER DATA")
    print("----------------------")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition}")

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


# 🔹 TEST MODE (ALL SCENARIOS)
def run_all_tests():
    print("\n==============================")
    print("🚀 RUNNING ALL TEST SCENARIOS")
    print("==============================")

    test_cases = [
        {"name": "NORMAL CASE", "temp": 30, "humidity": 40, "condition": "clear sky"},
        {"name": "HIGH HUMIDITY", "temp": 30, "humidity": 85, "condition": "cloudy"},
        {"name": "RAIN CONDITION", "temp": 28, "humidity": 60, "condition": "rain"},
        {"name": "EXTREME HEAT", "temp": 38, "humidity": 30, "condition": "clear sky"},
    ]

    for test in test_cases:
        print("\n------------------------------")
        print(f"🧪 TEST: {test['name']}")
        print("------------------------------")

        temp = test["temp"]
        humidity = test["humidity"]
        condition = test["condition"]

        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition}")

        risks = analyze_risk(temp, humidity, condition)
        advice = generate_advice(risks)

        print("\n⚠️ IDENTIFIED RISKS")
        if risks:
            for r in risks:
                print(f"- {r}")
        else:
            print("- No major risks detected")

        print("\n🌱 ADVICE")
        for a in advice:
            print(f"- {a}")


# 🔹 SWITCH MODE HERE
if __name__ == "__main__":
    main()
# for testing all the cases 
# if __name__ == "__main__":
#run_all_tests()