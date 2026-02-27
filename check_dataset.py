import os

dataset_path = "data/plant_disease"

print("Scanning for empty or corrupted files...\n")

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        file_path = os.path.join(root, file)

        try:
            # Check if file is empty
            if os.path.getsize(file_path) == 0:
                print("EMPTY FILE:", file_path)
                os.remove(file_path)
                print("Deleted.\n")

        except Exception as e:
            print("ERROR FILE:", file_path)
            print("Reason:", e)
            os.remove(file_path)
            print("Deleted.\n")

print("Scan complete.")