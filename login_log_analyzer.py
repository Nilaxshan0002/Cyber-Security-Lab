
from collections import Counter

failed_ips = []

with open("login.log", "r") as file:
    for line in file:
        if "FAILED" in line:
            ip = line.split()[-1]
            failed_ips.append(ip)

counts = Counter(failed_ips)

for ip, attempts in counts.items():
    if attempts >= 3:
        print("[WARNING]", ip, attempts,
              "failed login attempts")
