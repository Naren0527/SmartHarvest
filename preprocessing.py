import numpy as np
from tensorflow.keras.preprocessing import image

IMG_SIZE = 224

def preprocess_image(uploaded_file):
    img = image.load_img(uploaded_file, target_size=(IMG_SIZE, IMG_SIZE))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
