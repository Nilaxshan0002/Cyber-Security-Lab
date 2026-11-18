
from urllib.parse import urlparse

url = input("Enter URL: ")

parsed = urlparse(url)
suspicious = []

if parsed.scheme != "https":
    suspicious.append("Not using HTTPS")

if "@" in url:
    suspicious.append("Contains @ symbol")

if len(url) > 100:
    suspicious.append("Unusually long URL")

if parsed.hostname and parsed.hostname.replace(".", "").isdigit():
    suspicious.append("Uses an IP address instead of a domain")

if suspicious:
    print("Potential warning signs:")
    for item in suspicious:
        print("-", item)
else:
    print("No basic warning signs detected")
