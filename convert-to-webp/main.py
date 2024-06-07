import os
import sys
from PIL import Image

def convert_images_in_folder(input_folder):
    output_folder = './img'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f)) and f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for image_file in image_files:
        try:
            input_path = os.path.join(input_folder, image_file)
            output_path = os.path.join(output_folder, os.path.splitext(image_file)[0] + '.webp')

            with Image.open(input_path) as img:
                img.save(output_path, 'WEBP')
        except Exception as e:
            print(f'Произошла ошибка при конвертации изображения {input_path}: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
        
    input_folder_path = sys.argv[1]
    convert_images_in_folder(input_folder_path)