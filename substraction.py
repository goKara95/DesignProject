import os
import numpy as np
from PIL import Image
import cv2
import sys

## DİFF ARRAYLARİNİ RESME ÇEVİRİP BELLİ BİR THRESHOLD ÜZERİNİ BOYAMAK İÇİN KULLANILIR
for filename in os.listdir("diff_numpy"):
    img_array = np.load(os.path.join("diff_numpy", filename))
    if img_array is not None:
        if img_array.ndim == 2:  # Grayscale image
            above_threshold = img_array > 38
            img_array[above_threshold] = 255  # White color for pixels above the threshold
        new_img = Image.fromarray(img_array.astype('uint8'))
        # Save the modified image
        new_img.save(filename + ".jpg")


##DIFF KLASÖRÜNDEKİ RESIMLERI RESIZE EDIP TXT DOSYASI OLARAK KAYDEDER
'''
pil_images = []
for filename in os.listdir("diff"):
    img = Image.open(os.path.join("diff", filename))
    if img is not None:
        print(filename)
        img = img.resize((256, 240))
        img = img.convert("L")
        pil_images.append(img)
img_array = np.array(pil_images[0])
count = 5
f_name = "result5"
for image in pil_images:
    if count != 5:
        f_name += "-" + str(count)
        img_array = img_array + np.array(image)
    np.savetxt(f_name, img_array, fmt='%d', delimiter=',')
    count += 1
'''