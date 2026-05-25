import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error on port {port}:{e}")
                

target = input("Enter IP address to scan: ")
print(f"Scanning {target}...")
print("Please wait this may take a minute.....")

for port in range(1, 1025):
    scan_port(target, port)

print("Scan complete!")
