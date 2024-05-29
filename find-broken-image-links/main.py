import os
import re
import sys

def print_image_names(directory):
    image_names = set()
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_names.add(filename)
    return image_names

def find_links(directory, image_names):
    link_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith('.md'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                links = link_pattern.findall(content)
                modified = False
                for alt_text, link in links:
                    image_file_name = link.split('/')[-1].split(' "')[0]
                    if image_file_name not in image_names:
                        content = content.replace(f'![{alt_text}]({link})', '')
                        modified = True
                if modified:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(content)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
        
    image_directory_path = sys.argv[1]
    md_directory_path = sys.argv[2]
    image_names = print_image_names(image_directory_path)
    find_links(md_directory_path, image_names)
