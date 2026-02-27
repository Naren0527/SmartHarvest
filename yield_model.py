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
    "apple": {"base_yield": 10, "optimal_rain": 1000, "temp_min": 10, "temp_max": 25},
    "banana": {"base_yield": 18, "optimal_rain": 1500, "temp_min": 20, "temp_max": 35},
    "blackgram": {"base_yield": 1.2, "optimal_rain": 700, "temp_min": 25, "temp_max": 35},
    "chickpea": {"base_yield": 1.5, "optimal_rain": 600, "temp_min": 20, "temp_max": 30},
    "coconut": {"base_yield": 8, "optimal_rain": 2000, "temp_min": 25, "temp_max": 35},
    "coffee": {"base_yield": 1.8, "optimal_rain": 1500, "temp_min": 18, "temp_max": 28},
    "cotton": {"base_yield": 1.5, "optimal_rain": 700, "temp_min": 20, "temp_max": 32},
    "grapes": {"base_yield": 12, "optimal_rain": 800, "temp_min": 15, "temp_max": 30},
    "jute": {"base_yield": 2.5, "optimal_rain": 1500, "temp_min": 24, "temp_max": 35},
    "kidneybeans": {"base_yield": 1.4, "optimal_rain": 800, "temp_min": 18, "temp_max": 28},
    "lentil": {"base_yield": 1.3, "optimal_rain": 600, "temp_min": 18, "temp_max": 30},
    "maize": {"base_yield": 3.0, "optimal_rain": 900, "temp_min": 18, "temp_max": 30},
    "mango": {"base_yield": 10, "optimal_rain": 1000, "temp_min": 24, "temp_max": 35},
    "mothbeans": {"base_yield": 1.0, "optimal_rain": 500, "temp_min": 25, "temp_max": 35},
    "mungbean": {"base_yield": 1.1, "optimal_rain": 700, "temp_min": 25, "temp_max": 35},
    "muskmelon": {"base_yield": 8, "optimal_rain": 600, "temp_min": 20, "temp_max": 30},
    "orange": {"base_yield": 9, "optimal_rain": 1000, "temp_min": 15, "temp_max": 30},
    "papaya": {"base_yield": 15, "optimal_rain": 1200, "temp_min": 22, "temp_max": 35},
    "pigeonpeas": {"base_yield": 1.6, "optimal_rain": 800, "temp_min": 20, "temp_max": 30},
    "pomegranate": {"base_yield": 7, "optimal_rain": 700, "temp_min": 20, "temp_max": 35},
    "rice": {"base_yield": 2.5, "optimal_rain": 1200, "temp_min": 20, "temp_max": 35},
    "watermelon": {"base_yield": 10, "optimal_rain": 600, "temp_min": 22, "temp_max": 32}
}

# Reasonable Market Prices per KG (₹)
market_price_per_kg = {
    "apple": 120,
    "banana": 20,
    "blackgram": 80,
    "chickpea": 60,
    "coconut": 35,
    "coffee": 250,
    "cotton": 70,
    "grapes": 40,
    "jute": 45,
    "kidneybeans": 90,
    "lentil": 75,
    "maize": 18,
    "mango": 50,
    "mothbeans": 70,
    "mungbean": 85,
    "muskmelon": 25,
    "orange": 30,
    "papaya": 22,
    "pigeonpeas": 95,
    "pomegranate": 110,
    "rice": 22,
    "watermelon": 15
}

soil_factor = {"clay": 0.9, "loam": 1.0, "sandy": 0.8}
irrigation_factor = {"drip": 1.1, "sprinkler": 1.0, "canal": 0.9, "none": 0.5}


# ---------------- Streamlit UI ---------------- #

st.title("🌾 Smart Harvesting Yield & Revenue Predictor")

crop = st.selectbox("Select Crop", list(crops.keys()))
land = st.number_input("Land Size (acres)", min_value=0.0)
rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0)
temperature = st.number_input("Average Temperature (°C)")
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
soil = st.selectbox("Soil Type", list(soil_factor.keys()))
irrigation = st.selectbox("Irrigation Type", list(irrigation_factor.keys()))

if st.button("Predict Yield & Revenue"):

    base = crops[crop]["base_yield"]
    optimal_rain = crops[crop]["optimal_rain"]
    temp_min = crops[crop]["temp_min"]
    temp_max = crops[crop]["temp_max"]

    F_rain = rainfall_factor(rainfall, optimal_rain)
    F_temp = temperature_factor(temperature, temp_min, temp_max)
    F_humidity = humidity_factor(humidity)

    estimated_yield_tons = (
        base * land *
        F_rain *
        F_temp *
        F_humidity *
        soil_factor[soil] *
        irrigation_factor[irrigation]
    )

    estimated_yield_kg = estimated_yield_tons * 1000
    price_per_kg = market_price_per_kg[crop]
    estimated_revenue = estimated_yield_kg * price_per_kg

    st.subheader("📊 Results")
    st.success(f"Estimated Yield: {round(estimated_yield_tons, 2)} tons")
    st.success(f"Estimated Yield: {round(estimated_yield_kg, 0)} kg")
    st.info(f"Market Price: ₹ {price_per_kg} per kg")
    st.success(f"Estimated Total Revenue: {format_inr(estimated_revenue)}")
