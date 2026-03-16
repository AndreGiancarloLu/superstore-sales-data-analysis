import kagglehub
import os, shutil

# Download latest version
path = kagglehub.dataset_download("vivek468/superstore-dataset-final")

print("Path to dataset files:", path)

dataset_file_name = "Sample - Superstore.csv"

dataset_file = os.path.join(path, dataset_file_name)
current_path = os.getcwd()
destination_path = os.path.join(current_path, dataset_file_name)
print("Destination path: ", destination_path)

shutil.copy(dataset_file, destination_path)