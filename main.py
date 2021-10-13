import requests
import time
import colorama
from colorama import Fore

print(Fore.RED + 'Github View bot by TusTusDev | https://github.com/TusTusDev ')


username = input("Your github username :   ")

while True:
    time.sleep(4)
    requests.get(f"https://github.com/{username}")
