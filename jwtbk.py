import jwt
import argparse
import warnings
import time
from colorama import Fore


warnings.filterwarnings(
    "ignore",
    message=".*HMAC key is .* below the minimum recommended length.*"
)

def bruteforce(token,wordlist):

    start = time.time()
    try:
        with open(wordlist, 'r') as wfile:
            keys = [line.strip() for line in wfile if line.strip()]
    except FileNotFoundError:
        print(Fore.RED + "[!] Wordlist not found")
        return
    if not keys:
        print(Fore.RED + "Wordlist empty")
        return
    for i in keys:
        try:
            jwt.decode(token, i.strip(), algorithms=["HS256"])
            end = time.time()
            print(Fore.GREEN + "\n=== RESULT ===")
            print(Fore.GREEN + f"[+] Found valid key: {i}")
            print(Fore.BLUE + f"[+] Time elapsed: {end - start:.4f}s\n")
            return
        except jwt.InvalidTokenError:
           pass
    end = time.time()
    print(Fore.RED + "\n=== RESULT ===")
    print(Fore.RED + "[-] No valid key found")
    print(Fore.YELLOW + f"[+] Time elapsed: {end - start:.4f}s\n")

def main():

    parser = argparse.ArgumentParser(description ='Bruteforce JWT secret keys', usage='jwtbk.py -t <token> -w <wordlist>')
    parser.add_argument("-t", required=True, help="Token", metavar="TOKEN")
    parser.add_argument("-w", required=True, help="wordlist", metavar="WORDLIST")
    parser.add_argument("-v", help="Version number", action="version", version=" Version 1.0")
    args = parser.parse_args()

    bruteforce(args.t, args.w)

if __name__ == "__main__":
    main()
