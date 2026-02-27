import streamlit as st

# =========================================================
# -------------------- YIELD MODEL ------------------------
# =========================================================

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
    return f"₹ {amount:,.0f}"

crops = {
    "Rice": {"base_yield": 2.5, "optimal_rain": 1200, "temp_min": 20, "temp_max": 35},
    "Maize": {"base_yield": 3.0, "optimal_rain": 900, "temp_min": 18, "temp_max": 30},
    "Wheat": {"base_yield": 2.0, "optimal_rain": 800, "temp_min": 15, "temp_max": 25},
    "Banana": {"base_yield": 18, "optimal_rain": 1500, "temp_min": 20, "temp_max": 35},
    "Cotton": {"base_yield": 1.5, "optimal_rain": 700, "temp_min": 20, "temp_max": 32}
}

soil_options = ["clay", "loam", "sandy"]
irrigation_options = ["drip", "sprinkler", "canal", "none"]

# =========================================================
# -------------------- DISEASE DATA -----------------------
# =========================================================

disease_data = {
    "Early Blight": {
        "description": "Fungal disease causing dark concentric spots on older leaves.",
        "measures": [
            "Use certified disease-free seeds.",
            "Practice crop rotation (2-3 years).",
            "Remove infected leaves immediately.",
            "Avoid overhead irrigation.",
            "Maintain proper plant spacing.",
            "Apply preventive fungicides like Mancozeb."
        ]
    },
    "Late Blight": {
        "description": "Serious disease causing water-soaked lesions that turn brown rapidly.",
        "measures": [
            "Use certified disease-free seeds or tubers.",
            "Ensure proper field drainage.",
            "Avoid water stagnation.",
            "Remove infected plants immediately.",
            "Spray fungicides like Metalaxyl or Mancozeb.",
            "Avoid late evening irrigation."
        ]
    },
    "Healthy": {
        "description": "No disease detected. Plant is healthy.",
        "measures": [
            "Maintain proper irrigation schedule.",
            "Use balanced fertilizers.",
            "Monitor plants regularly."
        ]
    }
}

# =========================================================
# -------------------- FINANCIAL AID ----------------------
# =========================================================

farmer_schemes = [
    {"state": "All India", "name": "PM-KISAN", "description": "₹6000 per year income support.", "link": "https://pmkisan.gov.in/"},
    {"state": "Telangana", "name": "Rythu Bandhu", "description": "Financial assistance per acre.", "link": "https://rythubandhu.telangana.gov.in/"},
    {"state": "Karnataka", "name": "Raitha Siri Scheme", "description": "Millet cultivation support.", "link": "https://raitamitra.karnataka.gov.in/"}
]

# =========================================================
# -------------------- MARKETPLACE DATA -------------------
# =========================================================

equipment_data = {
    "Tractor": {
        "rent_per_day": 2000,
        "owners": [
            {"name": "Ramesh Gowda", "phone": "9876543210"},
            {"name": "Suresh Kumar", "phone": "9123456789"},
            {"name": "Mahesh Reddy", "phone": "9988776655"}
        ]
    },
    "Harvester": {
        "rent_per_day": 5000,
        "owners": [
            {"name": "Praveen Shetty", "phone": "9090909090"},
            {"name": "Karthik Rao", "phone": "9845012345"}
        ]
    },
    "Rotavator": {
        "rent_per_day": 1500,
        "owners": [
            {"name": "Venkatesh Naik", "phone": "9900112233"},
            {"name": "Anil Patil", "phone": "9887766554"}
        ]
    }
}

# =========================================================
# -------------------- STREAMLIT UI -----------------------
# =========================================================

st.set_page_config(page_title="Smart Farming Assistant", layout="wide")
st.title("🌾 Smart Farming Assistant")

menu = st.sidebar.radio(
    "Select Feature",
    ["Yield & Revenue Prediction", "Disease Prevention", "Financial Aid Schemes", "Farm Equipment Marketplace"]
)

# ================= YIELD ================= #
if menu == "Yield & Revenue Prediction":

    st.header("📈 Yield & Revenue Predictor")

    crop = st.selectbox("Select Crop", list(crops.keys()))
    land = st.number_input("Land Size (acres)", min_value=0.0)
    rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0)
    temperature = st.number_input("Average Temperature (°C)")
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)
    soil = st.selectbox("Soil Type", soil_options)
    irrigation = st.selectbox("Irrigation Type", irrigation_options)
    market_price = st.number_input("Market Price (₹ per ton)", min_value=0.0)

    if st.button("Predict Yield"):

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
            base * land * F_rain * F_temp * F_humidity *
            soil_factor[soil] * irrigation_factor[irrigation]
        )

        estimated_revenue = estimated_yield * market_price

        st.success(f"Estimated Yield: {round(estimated_yield, 2)} tons")
        st.success(f"Estimated Revenue: {format_inr(estimated_revenue)}")

# ================= DISEASE ================= #
elif menu == "Disease Prevention":

    st.header("🦠 Crop Disease Information")

    disease = st.selectbox("Select Disease", list(disease_data.keys()))
    info = disease_data[disease]

    st.subheader("Description")
    st.write(info["description"])

    st.subheader("Prevention Measures")
    for measure in info["measures"]:
        st.write("•", measure)


# ================= FINANCIAL ================= #
elif menu == "Financial Aid Schemes":

    st.header("💰 Government Schemes")

    farmer_schemes = {

        "All India": [
            {"name": "PM-KISAN",
             "description": "₹6000 per year income support for farmers.",
             "link": "https://pmkisan.gov.in/"},

            {"name": "PM Fasal Bima Yojana",
             "description": "Crop insurance against natural calamities.",
             "link": "https://pmfby.gov.in/"},

            {"name": "Soil Health Card Scheme",
             "description": "Soil testing & fertilizer recommendation support.",
             "link": "https://soilhealth.dac.gov.in/"},

            {"name": "Kisan Credit Card (KCC)",
             "description": "Low-interest agricultural credit facility.",
             "link": "https://kisancreditcard.com/"}
        ],

        "Telangana": [
            {"name": "Rythu Bandhu",
             "description": "Investment support per acre per season.",
             "link": "https://rythubandhu.telangana.gov.in/"},

            {"name": "Rythu Bima",
             "description": "Farmer life insurance scheme.",
             "link": "https://rythubima.telangana.gov.in/"},

            {"name": "Free Power Supply Scheme",
             "description": "Free electricity for agricultural pumps.",
             "link": "https://www.telangana.gov.in/"}
        ],

        "Tamil Nadu": [
            {"name": "TN Seed Subsidy Scheme",
             "description": "Subsidy for certified seeds.",
             "link": "https://www.tnagrisnet.tn.gov.in/"},

            {"name": "Micro Irrigation Scheme",
             "description": "Subsidy for drip and sprinkler irrigation.",
             "link": "https://www.tn.gov.in/"},

            {"name": "Uzhavar Pathukappu Scheme",
             "description": "Farmer welfare and pension scheme.",
             "link": "https://www.tn.gov.in/"}
        ],

        "Karnataka": [
            {"name": "Raitha Siri Scheme",
             "description": "Millet cultivation financial support.",
             "link": "https://raitamitra.karnataka.gov.in/"},

            {"name": "Krishi Bhagya Scheme",
             "description": "Water conservation & farm pond scheme.",
             "link": "https://raitamitra.karnataka.gov.in/"},

            {"name": "Karnataka Crop Loan Waiver",
             "description": "Loan waiver support for farmers.",
             "link": "https://www.karnataka.gov.in/"}
        ],

        "Kerala": [
            {"name": "Kerala Agricultural Subsidy",
             "description": "Subsidy for crop and irrigation support.",
             "link": "https://keralaagriculture.gov.in/"},

            {"name": "Karshaka Kshemanidhi",
             "description": "Farmer welfare pension scheme.",
             "link": "https://keralaagriculture.gov.in/"}
        ],

        "Andhra Pradesh": [
            {"name": "YSR Rythu Bharosa",
             "description": "Annual financial assistance.",
             "link": "https://ysrrythubharosa.ap.gov.in/"},

            {"name": "Zero Interest Crop Loan Scheme",
             "description": "Interest-free crop loans.",
             "link": "https://apagrisnet.gov.in/"}
        ]
    }

    state = st.selectbox(
        "Select State",
        list(farmer_schemes.keys())
    )

    # ✅ Correct way to get schemes
    schemes = farmer_schemes[state]

    for scheme in schemes:
        st.subheader(scheme["name"])
        st.write(scheme["description"])
        st.markdown(f"[Apply Here]({scheme['link']})")
        st.write("---")

# ================= MARKETPLACE ================= #
elif menu == "Farm Equipment Marketplace":

    st.header("🚜 Farm Equipment Rental Marketplace")

    equipment = st.selectbox("Select Equipment", list(equipment_data.keys()))
    days = st.number_input("Number of Rental Days", min_value=1)

    if st.button("Calculate Rental Cost"):

        rent = equipment_data[equipment]["rent_per_day"]
        total_cost = rent * days

        st.success(f"Rent per Day: {format_inr(rent)}")
        st.success(f"Total Rental Cost: {format_inr(total_cost)}")

        st.subheader("📞 Contact Equipment Owners")

        for owner in equipment_data[equipment]["owners"]:
            st.write(f"👨 {owner['name']} — 📱 {owner['phone']}")