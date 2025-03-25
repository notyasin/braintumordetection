import os
import shutil

img_path = "C:/Users/racco/Documents/python_project/braintumordetection/archive/"

for kelas in os.listdir(img_path):
    if not kelas.startswith("."):
        img_num = len(os.listdir(img_path + kelas))
        print(img_num)
        print(os.listdir(img_path + kelas))
        # img_num -> number of images are there 
        for (n, file_name) in enumerate(os.listdir(img_path + kelas)):
            img = img_path + kelas + "/" + file_name
            if n < 5:
                shutil.copy(img, "TEST/" + kelas.upper() + "/" + file_name)
            elif n < 0.8 * img_num:
                shutil.copy(img, "TRAIN/" + kelas.upper() + "/" + file_name)
            else:
                shutil.copy(img, "VAL/" + kelas.upper() + "/" + file_name)