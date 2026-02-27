import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os

# ==============================
# CONFIG
# ==============================
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10

TRAIN_PATH = "dataset/plant_disease_split/train"
VAL_PATH = "dataset/plant_disease_split/val"

MODEL_SAVE_PATH = "models/disease_model.keras"

os.makedirs("models", exist_ok=True)

# ==============================
# LOAD DATASET
# ==============================
train_ds = tf.keras.utils.image_dataset_from_directory(
    TRAIN_PATH,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    VAL_PATH,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
print("Classes:", class_names)
print("Number of classes:", len(class_names))

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)

# ==============================
# LOAD MOBILENETV2 BASE
# ==============================
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

base_model.trainable = False  # Freeze base model

# ==============================
# BUILD MODEL
# ==============================
model = keras.Sequential([
    layers.Rescaling(1./127.5, offset=-1, input_shape=(224, 224, 3)),
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(len(class_names), activation="softmax")
])

# ==============================
# COMPILE
# ==============================
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ==============================
# TRAIN
# ==============================
history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS
)

# ==============================
# SAVE MODEL
# ==============================
model.save(MODEL_SAVE_PATH)

print("MobileNetV2 model saved successfully!")