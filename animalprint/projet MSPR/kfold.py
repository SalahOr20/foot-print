import os
import shutil
import random
import math


def k_fold_cross_validation(image_folder, output_folder, k=5):
    os.makedirs(output_folder, exist_ok=True)

    image_files = [f for f in os.listdir(image_folder)]
    random.shuffle(image_files)

    num_images = len(image_files)
    fold_size = math.ceil(num_images / k)
    start_index = 0
    for i in range(k):
        fold_output_folder = os.path.join(output_folder, f'fold_{i+1}')
        os.makedirs(fold_output_folder, exist_ok=True)

        end_index = min(start_index + fold_size, num_images)
        fold_files = image_files[start_index:end_index]

        start_index = end_index

        for filename in fold_files:
            src = os.path.join(image_folder, filename)
            dst = os.path.join(fold_output_folder, filename)
            shutil.copyfile(src, dst)



image_folder = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/Mammiferes/Ecureuil'
output_folder = 'C:/Users/Thuy-trang/Desktop/mspr-ia/projet MSPR/split_data/Ecureuil'
k_fold_cross_validation(image_folder, output_folder, k=5)
