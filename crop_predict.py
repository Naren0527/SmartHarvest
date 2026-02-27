import joblib
import numpy as np

model = joblib.load("models/crop_model.pkl")

def recommend_crop(N, P, K, temp, humidity, ph, rainfall):
    features = [[N, P, K, temp, humidity, ph, rainfall]]

    probabilities = model.predict_proba(features)[0]
    top_indices = probabilities.argsort()[-3:][::-1]

    top_crops = model.classes_[top_indices]

    return top_crops
