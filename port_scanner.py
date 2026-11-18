
import socket
from datetime import datetime

target = "127.0.0.1"

start_port = 1
end_port = 1024

print("=" * 45)
print("       PYTHON PORT SCANNER")
print("=" * 45)

print("Target:", target)
print("Scan started:", datetime.now())
print("-" * 45)

open_ports = []

for port in range(start_port, end_port + 1):

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.settimeout(0.2)

    result = client.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        open_ports.append(port)

    client.close()

print("-" * 45)
print("Scan completed!")

print("Total open ports:", len(open_ports))
print("Open ports:", open_ports)
print("=" * 45)
