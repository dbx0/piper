from datetime import datetime
import time

def print_now():
    print(datetime.now())
    time.sleep(10)
    print(datetime.now())

def get_time_now():
    return datetime.now()