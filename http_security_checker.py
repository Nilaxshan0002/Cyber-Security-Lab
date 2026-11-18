
import requests

url = input("Enter your test website URL: ")

try:
    response = requests.get(url, timeout=10)
    headers = response.headers

    security_headers = [
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Referrer-Policy"
    ]

    for header in security_headers:
        if header in headers:
            print("[FOUND]", header, ":", headers[header])
        else:
            print("[MISSING]", header)

except requests.RequestException as error:
    print("Connection error:", error)
