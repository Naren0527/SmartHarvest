# disease_module.py

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

    "Leaf Spot": {
        "description": "Brown or black spots on leaves caused mainly by fungi.",
        "measures": [
            "Remove infected leaves.",
            "Avoid wetting leaves during watering.",
            "Improve air circulation.",
            "Practice crop rotation.",
            "Apply copper-based fungicide.",
            "Avoid excessive nitrogen fertilizer."
        ]
    },

    "Bacterial Spot": {
        "description": "Small dark lesions on leaves and fruits caused by bacteria.",
        "measures": [
            "Use certified disease-free seeds.",
            "Avoid working in wet fields.",
            "Remove infected plants.",
            "Avoid overhead irrigation.",
            "Spray copper-based bactericides.",
            "Disinfect tools regularly."
        ]
    },

    "Healthy": {
        "description": "No disease detected. Plant is healthy.",
        "measures": [
            "Maintain proper irrigation schedule.",
            "Use balanced fertilizers.",
            "Monitor plants regularly.",
            "Ensure good soil drainage.",
            "Maintain proper plant spacing.",
            "Practice regular field hygiene."
        ]
    }
}

def get_disease_info(disease_name):
    return disease_data.get(disease_name, None)
