import os
import requests
from colorama import Fore, init
from wonderwords import RandomWord

init(autoreset=True)

random_word = RandomWord()

def check_username(username):
    url = f"https://github.com/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error checking username '{username}': {e}")
        return False

def main():
    if os.name == 'nt':
        os.system('title github.com/MrShadowDev')

    try:
        available_usernames = []
        for _ in range(5000000):  # Change if you wawnt less
            username = random_word.word()
            if check_username(username):
                available_usernames.append(username)
                print(Fore.GREEN + f"[+] '{username}' is available.")
                with open('available.txt', 'a', encoding='utf-8') as outfile:
                    outfile.write(username + '\n')
            else:
                print(Fore.RED + f"[-] '{username}' not available.")

        print(f"\n{len(available_usernames)} usernames are available.")

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()
