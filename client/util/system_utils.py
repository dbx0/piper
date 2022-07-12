import platform
import requests

def get_external_ip():
    response = requests.get("https://ipinfo.io")

    return response.json()

def get_system_data():
    system_data = {
        "platform": {
            "machine": platform.machine(),
            "version": platform.version(),
            "platform": platform.platform(),
            "uname": platform.uname(),
            "system": platform.system(),
            "processor": platform.processor(),
            "architecture": platform.architecture()
        }
    }
    
    return system_data