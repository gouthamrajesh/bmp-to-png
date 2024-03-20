import os
from PIL import Image

def convert_bmp_to_png(folder_path):
    num_files_changed = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.bmp'):
                bmp_path = os.path.join(root, file)
                png_path = os.path.splitext(bmp_path)[0] + '.png'
                try:
                    with Image.open(bmp_path) as img:
                        img.save(png_path)
                    os.remove(bmp_path)  # Remove the original BMP file
                    num_files_changed += 1
                    print(f"Converted {bmp_path} to {png_path} and removed original BMP file")
                except Exception as e:
                    print(f"Failed to convert {bmp_path}: {e}")
    return num_files_changed

folder_path = "./FINGERPRINT"

# Convert BMP images within the s6 folder
num_s6_files_changed = convert_bmp_to_png(os.path.join(folder_path, "s6"))

# Convert BMP images within the s8 folder
num_s8_files_changed = convert_bmp_to_png(os.path.join(folder_path, "s8"))

total_files_changed = num_s6_files_changed + num_s8_files_changed
print(f"Total number of files converted and replaced: {total_files_changed}")
