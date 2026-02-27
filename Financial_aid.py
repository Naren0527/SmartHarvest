# financial_aid.py

farmer_schemes = [
    {
        "state": "All India",
        "name": "PM-KISAN",
        "description": "₹6000 per year income support for farmers.",
        "link": "https://pmkisan.gov.in/"
    },
    {
        "state": "All India",
        "name": "PM Fasal Bima Yojana",
        "description": "Crop insurance scheme protecting farmers from natural risks.",
        "link": "https://pmfby.gov.in/"
    },
    {
        "state": "Telangana",
        "name": "Rythu Bandhu",
        "description": "Financial assistance per acre per season.",
        "link": "https://rythubandhu.telangana.gov.in/"
    },
    {
        "state": "Tamil Nadu",
        "name": "Tamil Nadu Agricultural Schemes",
        "description": "Seed subsidy and productivity improvement schemes.",
        "link": "https://www.tnagrisnet.tn.gov.in/"
    },
    {
        "state": "Karnataka",
        "name": "Raitha Siri Scheme",
        "description": "Encourages millet cultivation with financial support.",
        "link": "https://raitamitra.karnataka.gov.in/"
    },
    {
        "state": "Kerala",
        "name": "Kerala Agricultural Development Schemes",
        "description": "State-supported schemes for irrigation and farmer welfare.",
        "link": "https://keralaagriculture.gov.in/"
    },
    {
        "state": "Andhra Pradesh",
        "name": "YSR Rythu Bharosa",
        "description": "Annual financial assistance to farmers.",
        "link": "https://ysrrythubharosa.ap.gov.in/"
    }
]


def get_schemes_by_state(state):
    """
    Returns list of schemes filtered by state.
    Includes central (All India) schemes automatically.
    """
    return [
        scheme for scheme in farmer_schemes
        if scheme["state"] == "All India" or scheme["state"] == state
    ]


# Optional test block (only runs if file is executed directly)
if __name__ == "__main__":
    test_state = "Telangana"
    schemes = get_schemes_by_state(test_state)

    for scheme in schemes:
        print(f"{scheme['name']}")
        print(f"{scheme['description']}")
        print(f"{scheme['link']}")
        print("-" * 40)
