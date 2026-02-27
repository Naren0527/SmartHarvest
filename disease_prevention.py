# ============================================
# Plant Disease Prevention Module
# Backend-friendly version (No input/print)
# ============================================

def get_preventive_measures(disease_name):
    """
    Returns disease details and preventive measures.
    Can be used directly in Flask/Django backend.
    """

    disease_data = {

        "early_blight": {
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

        "late_blight": {
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

        "leaf_spot": {
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

        "bacterial_spot": {
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

        "healthy": {
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

    disease_name = disease_name.lower()

    if disease_name in disease_data:
        return {
            "status": "success",
            "data": disease_data[disease_name]
        }
    else:
        return {
            "status": "error",
            "message": "Disease not found in database."
        }