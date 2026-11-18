import socket

target = "127.0.0.1"

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    if s.connect_ex((target, port)) == 0:
        print(f"[OPEN] Port {port}")

    s.close()