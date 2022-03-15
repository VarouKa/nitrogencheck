import random
import string
import requests
from threading import Thread
from time import strftime, gmtime, sleep

print("""

███╗░░██╗██╗████████╗██████╗░░█████╗░  ░██████╗░███████╗███╗░░██╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝░██╔════╝████╗░██║
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║  ██║░░██╗░█████╗░░██╔██╗██║
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║  ██║░░╚██╗██╔══╝░░██║╚████║
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝  ╚██████╔╝███████╗██║░╚███║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░╚═════╝░╚══════╝╚═╝░░╚══╝""")
sleep(0.3)
print('RΞO Nitro Gen Créer par ٴٴ ¥ズٴٴ]#0110')
sleep(0.3)
print('Besoin d\'aide : discord.gg/EVDqbEye9C')
sleep(0.3)

count_threads = 8
interval = 5


def generate_url():
    return 'https://discord.gift/' + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))


def checker(nitro):
    url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
    r = requests.get(url)
    if r.status_code == 200:
        with open('Nitro Codes Valid.md', 'a') as f:
            f.write(nitro + '\n')
        print(" Valid | {} ".format(nitro))


def main():
    while True:
        checker(generate_url())


def main_info():
    i = 0
    while True:
        checker(generate_url())
        i += 1
        if i % interval == 0:
            print(f'[{strftime("%H:%M:%S", gmtime())}] Check de {i * count_threads} codes nitros')


for i in range(count_threads-1):
    Thread(target=main).start()
Thread(target=main_info).start()
