import os
from PIL import Image

dataset_path = "dataset/plant_disease_split"

print("Scanning dataset for corrupted images...\n")

bad_files = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            file_path = os.path.join(root, file)
            try:
                img = Image.open(file_path)
                img.verify()  # Verify image integrity
            except Exception:
                print("Corrupted:", file_path)
                bad_files.append(file_path)

# Delete corrupted files
for file_path in bad_files:
    try:
        os.remove(file_path)
        print("Deleted:", file_path)
    except:
        print("Could not delete:", file_path)

print("\nScan complete.")
print("Total corrupted images removed:", len(bad_files))