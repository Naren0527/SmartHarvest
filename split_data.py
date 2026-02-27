import os
import shutil
import random

source_dir = "data/plant_disease/train"
dest_dir = "data/plant_disease_split"

split_ratio = 0.8

for class_name in os.listdir(source_dir):

    class_path = os.path.join(source_dir, class_name)

    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    random.shuffle(images)

    split_index = int(len(images) * split_ratio)

    train_images = images[:split_index]
    val_images = images[split_index:]

    for img in train_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(dest_dir, "train", class_name, img)

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)

    for img in val_images:
        src = os.path.join(class_path, img)
        dst = os.path.join(dest_dir, "val", class_name, img)

        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)

print("Dataset split complete.")
