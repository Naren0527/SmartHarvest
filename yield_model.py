import streamlit as st

# ---------------- Utility Functions ---------------- #

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))


def rainfall_factor(rainfall, optimal):
    factor = 1 - abs(rainfall - optimal) / optimal
    return clamp(factor, 0.3, 1.0)


def temperature_factor(temp, optimal_min, optimal_max):
    if optimal_min <= temp <= optimal_max:
        return 1.0
    elif optimal_min - 5 <= temp <= optimal_max + 5:
        return 0.8
    elif optimal_min - 10 <= temp <= optimal_max + 10:
        return 0.5
    else:
        return 0.3


def humidity_factor(humidity):
    if 60 <= humidity <= 80:
        return 1.0
    elif 40 <= humidity <= 90:
        return 0.8
    else:
        return 0.5


def format_inr(amount):
    amount = int(round(amount))
    s = str(amount)

    last_three = s[-3:]
    remaining = s[:-3]

    if remaining != "":
        remaining = ",".join(
            [remaining[max(i - 2, 0):i] for i in range(len(remaining), 0, -2)][::-1]
        )
        return "₹ " + remaining + "," + last_three
    else:
        return "₹ " + last_three


# ---------------- Crop Database ---------------- #

crops = {
    "Rice": {"base_yield": 2.5, "optimal_rain": 1200, "temp_min": 20, "temp_max": 35},
    "Maize": {"base_yield": 3.0, "optimal_rain": 900, "temp_min": 18, "temp_max": 30},
    "Wheat": {"base_yield": 2.0, "optimal_rain": 800, "temp_min": 15, "temp_max": 25},
    "Banana": {"base_yield": 18, "optimal_rain": 1500, "temp_min": 20, "temp_max": 35},
    "Apple": {"base_yield": 10, "optimal_rain": 1000, "temp_min": 10, "temp_max": 25},
    "Mango": {"base_yield": 10, "optimal_rain": 1000, "temp_min": 24, "temp_max": 35},
    "Cotton": {"base_yield": 1.5, "optimal_rain": 700, "temp_min": 20, "temp_max": 32},
    "Orange": {"base_yield": 9, "optimal_rain": 1000, "temp_min": 15, "temp_max": 30},
    "Papaya": {"base_yield": 15, "optimal_rain": 1200, "temp_min": 22, "temp_max": 35},
    "Watermelon": {"base_yield": 10, "optimal_rain": 600, "temp_min": 22, "temp_max": 32}
}

soil_options = ["clay", "loam", "sandy"]
irrigation_options = ["drip", "sprinkler", "canal", "none"]

# ---------------- Streamlit UI ---------------- #

st.title("🌾 Smart Harvesting Yield & Revenue Predictor")

crop = st.selectbox("Select Crop", list(crops.keys()))
land = st.number_input("Land Size (acres)", min_value=0.0)
rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0)
temperature = st.number_input("Average Temperature (°C)")
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
soil = st.selectbox("Soil Type", soil_options)
irrigation = st.selectbox("Irrigation Type", irrigation_options)
market_price = st.number_input("Market Price (₹ per ton)", min_value=0.0)

if st.button("Predict"):

    base = crops[crop]["base_yield"]
    optimal_rain = crops[crop]["optimal_rain"]
    temp_min = crops[crop]["temp_min"]
    temp_max = crops[crop]["temp_max"]

    F_rain = rainfall_factor(rainfall, optimal_rain)
    F_temp = temperature_factor(temperature, temp_min, temp_max)
    F_humidity = humidity_factor(humidity)

    soil_factor = {"clay": 0.9, "loam": 1.0, "sandy": 0.8}
    irrigation_factor = {"drip": 1.1, "sprinkler": 1.0, "canal": 0.9, "none": 0.5}

    estimated_yield = (
        base * land *
        F_rain *
        F_temp *
        F_humidity *
        soil_factor[soil] *
        irrigation_factor[irrigation]
    )

    estimated_revenue = estimated_yield * market_price

    st.subheader("📊 Results")
    st.success(f"Estimated Yield: {round(estimated_yield, 2)} tons")
    st.success(f"Estimated Revenue: {format_inr(estimated_revenue)}")
