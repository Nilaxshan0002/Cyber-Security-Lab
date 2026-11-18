import re

SUSPICIOUS_WORDS = [
    "urgent",
    "verify your account",
    "password expired",
    "account suspended",
    "claim your prize",
    "click here",
    "update payment",
    "confirm your identity"
]

URL_PATTERN = r"https?://[^\s<>\"']+"

def analyze_email(email_text):
    score = 0

    print("=== Phishing Email Detector ===")

    text = email_text.lower()

    for word in SUSPICIOUS_WORDS:
        if word in text:
            print("[WARNING] Suspicious phrase:", word)
            score += 1

    urls = re.findall(URL_PATTERN, email_text)

    for url in urls:
        print("[INFO] Link found:", url)

        if "@" in url:
            print("[WARNING] URL contains an @ symbol.")
            score += 1

    print("\nRisk assessment:")

    if score >= 3:
        print("HIGH RISK: Multiple suspicious indicators.")
    elif score >= 1:
        print("POTENTIAL RISK: Review the email carefully.")
    else:
        print("LOW INDICATOR COUNT: No configured indicators found.")

if __name__ == "__main__":
    email = input("Paste email content:\n")
    analyze_email(email)