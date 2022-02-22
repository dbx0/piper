import os
from util.banners import banners
import random
import colorama
from colorama import Fore, Style
from plyer import notification

def clear_screen():
    if(os.name.lower() == "nt"):
        os.system("cls")
    else:
        os.system("clear")

def get_banner():
    colorama.init()

    style = Style.BRIGHT
    color = random.choice([Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.YELLOW])
    banner = random.choice(banners)

    return style + color + banner + Style.RESET_ALL

def show_pop_up(title, message):
    notification.notify(title, message, timeout=2)
