import kagglehub

# Download latest version
path = kagglehub.dataset_download("forekid/dfc25-track1-trainval")

print("Path to dataset files:", path)