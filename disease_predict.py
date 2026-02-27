import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

model = tf.keras.models.load_model("models/disease_model.h5")

IMG_SIZE = 224

# Automatically get class names from training folder
TRAIN_DIR = "data/plant_disease/train"
class_names = sorted(os.listdir(TRAIN_DIR))

def predict_disease(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = np.max(prediction)

    return class_names[class_index], float(confidence)
