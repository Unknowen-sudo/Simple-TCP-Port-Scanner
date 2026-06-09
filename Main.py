import socket
import sys

target_host = input("Type The Target Ip: ") 

print(f"\n[*] Starting scan on host: {target_host}")
print("-" * 50)

start_port = 1
end_port = 100

try:
    for port in range(start_port, end_port + 1):
        # socket.AF_INET For Selecting IPv4 and SOCK_STREAM For Making The Connection TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        try:
            # Returns 0 if the Port Is Opened
            result = s.connect_ex((target_host, port))
            if result == 0:
                print(f"[+] Port {port}: OPEN")
        finally:
            # Closing The Socket guarantees it runs every time to reduce system usage
            s.close()

except KeyboardInterrupt:
    print("\n[-] Exiting script (Ctrl+C detected).")
    sys.exit()

except socket.gaierror:
    print("\n[-] Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\n[-] Could not connect to server.")
    sys.exit()

print("-" * 50)
print("[*] Scan completed successfully.")
