# yield_model.py
# Smart Harvesting - Yield & Revenue Prediction Module


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
    """
    Convert number to Indian currency format.
    Example: 231000 -> ₹ 2,31,000
    """
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
    "rice": {"base_yield": 2.5, "optimal_rain": 1200, "temp_min": 20, "temp_max": 35},
    "maize": {"base_yield": 3.0, "optimal_rain": 900, "temp_min": 18, "temp_max": 30},
    "wheat": {"base_yield": 2.0, "optimal_rain": 800, "temp_min": 15, "temp_max": 25},
    "banana": {"base_yield": 18, "optimal_rain": 1500, "temp_min": 20, "temp_max": 35},
    "apple": {"base_yield": 10, "optimal_rain": 1000, "temp_min": 10, "temp_max": 25},
    "mango": {"base_yield": 10, "optimal_rain": 1000, "temp_min": 24, "temp_max": 35},
    "cotton": {"base_yield": 1.5, "optimal_rain": 700, "temp_min": 20, "temp_max": 32},
    "orange": {"base_yield": 9, "optimal_rain": 1000, "temp_min": 15, "temp_max": 30},
    "papaya": {"base_yield": 15, "optimal_rain": 1200, "temp_min": 22, "temp_max": 35},
    "watermelon": {"base_yield": 10, "optimal_rain": 600, "temp_min": 22, "temp_max": 32}
}

soil_factor = {
    crop: {"clay": 0.9, "loam": 1.0, "sandy": 0.8}
    for crop in crops
}

irrigation_factor = {
    "drip": 1.1,
    "sprinkler": 1.0,
    "canal": 0.9,
    "none": 0.5
}


# ---------------- Main Prediction Function ---------------- #

def predict_yield_and_revenue(data):
    """
    Expected input (dictionary):
    {
        "crop": "rice",
        "land": 5,
        "rainfall": 1000,
        "temperature": 28,
        "humidity": 70,
        "soil": "clay",
        "irrigation": "drip",
        "market_price": 20000
    }

    Returns dictionary:
    {
        "estimated_yield_tons": value,
        "estimated_revenue": value,
        "estimated_revenue_inr": "₹ formatted value"
    }
    """

    try:
        crop = data["crop"].lower()

        if crop not in crops:
            return {"error": "Invalid crop selected"}

        land = float(data["land"])
        rain = float(data["rainfall"])
        temp = float(data["temperature"])
        humidity = float(data["humidity"])
        soil = data["soil"].lower()
        irrigation = data["irrigation"].lower()
        market_price = float(data["market_price"])

        base = crops[crop]["base_yield"]
        optimal_rain = crops[crop]["optimal_rain"]
        temp_min = crops[crop]["temp_min"]
        temp_max = crops[crop]["temp_max"]

        F_rain = rainfall_factor(rain, optimal_rain)
        F_temp = temperature_factor(temp, temp_min, temp_max)
        F_humidity = humidity_factor(humidity)
        F_soil = soil_factor[crop].get(soil, 0.8)
        F_irrigation = irrigation_factor.get(irrigation, 0.8)

        estimated_yield = (
            base * land *
            F_rain *
            F_temp *
            F_humidity *
            F_soil *
            F_irrigation
        )

        estimated_revenue = estimated_yield * market_price

        return {
            "estimated_yield_tons": round(estimated_yield, 2),
            "estimated_revenue": round(estimated_revenue, 2),
            "estimated_revenue_inr": format_inr(estimated_revenue)
        }

    except Exception as e:
        return {"error": str(e)}