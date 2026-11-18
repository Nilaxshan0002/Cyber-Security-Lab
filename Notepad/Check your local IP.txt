import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("Computer:", hostname)
print("Local IP:", ip)