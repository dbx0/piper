from colorama import Fore, Style
import colorama, random

colorama.init()

banners = []

banners.append(Style.BRIGHT + Fore.GREEN + r"""
    ██▓███   ██▓ ██▓███  ▓█████  ██▀███  
    ▓██░  ██▒▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒
    ▓██░ ██▓▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒
    ▒██▄█▓▒ ▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  
    ▒██▒ ░  ░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒
    ▒▓▒░ ░  ░░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░▒ ░      ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░
    ░░        ▒ ░░░          ░     ░░   ░ 
            ░              ░  ░   ░     
""" + Style.RESET_ALL)

def banner():
    return random.choice(banners)
