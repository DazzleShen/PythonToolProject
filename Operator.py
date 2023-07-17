import os
import shutil
import sys
import ReadFile

def find_and_copy_images(folder_path, image_names, destination_folder):
    found_images = []
    for filename in os.listdir(folder_path):
        if filename in image_names:
            source_path = os.path.join(folder_path, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.copy(source_path, destination_path)
            found_images.append(destination_path)
    return found_images

if __name__ == "__main__":
    file_path = sys.argv[1]
    image_names = ReadFile.read_file_to_list(file_path)
    print(image_names)
    source_path = os.getcwd()
    print("source path:" + source_path)
    target_path = source_path + "/ResultFile"
    print("target paht:" + target_path)
    os.makedirs(target_path)
    result = find_and_copy_images(source_path, image_names, target_path)
    print(result)