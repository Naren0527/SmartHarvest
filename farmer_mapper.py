def map_farmer_input(state, season, soil):

    # -------------------------
    # STATE BASE CLIMATE
    # -------------------------
    if state == "Kerala":
        temp = 27
        humidity = 85
        rainfall = 300

    elif state == "Tamil Nadu":
        temp = 32
        humidity = 65
        rainfall = 120

    elif state == "Karnataka":
        temp = 28
        humidity = 70
        rainfall = 150

    elif state == "Andhra Pradesh":
        temp = 33
        humidity = 60
        rainfall = 140

    elif state == "Telangana":
        temp = 34
        humidity = 55
        rainfall = 100

    # -------------------------
    # SEASON ADJUSTMENT
    # -------------------------
    if season == "Kharif":
        rainfall += 100
        humidity += 5

    elif season == "Rabi":
        rainfall -= 40
        temp -= 2

    elif season == "Summer":
        temp += 4
        rainfall -= 60

    # -------------------------
    # SOIL NPK + PH
    # -------------------------
    if soil == "Red Soil":
        N, P, K = 40, 40, 40
        ph = 6.0

    elif soil == "Black Soil":
        N, P, K = 60, 50, 50
        ph = 7.5

    elif soil == "Alluvial Soil":
        N, P, K = 70, 60, 60
        ph = 6.8

    elif soil == "Sandy Soil":
        N, P, K = 30, 30, 30
        ph = 5.8

    elif soil == "Laterite Soil":
        N, P, K = 35, 35, 35
        ph = 5.5

    return N, P, K, temp, humidity, ph, rainfall
