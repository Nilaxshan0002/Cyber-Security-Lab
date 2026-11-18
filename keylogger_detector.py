import psutil

SUSPICIOUS_NAMES = [
    "keylogger", "logkeys", "pynput",
    "keystroke", "keycapture"
]

def scan_processes():
    print("=== Process Security Scan ===")

    for process in psutil.process_iter(
        ["pid", "name", "exe"]
    ):
        try:
            name = (process.info["name"] or "").lower()
            path = (process.info["exe"] or "").lower()

            if any(word in name or word in path
                   for word in SUSPICIOUS_NAMES):
                print("\n[WARNING] Suspicious process indicator")
                print("Name:", process.info["name"])
                print("PID:", process.info["pid"])
                print("Path:", process.info["exe"])

        except (psutil.NoSuchProcess,
                psutil.AccessDenied):
            continue

    print("\nScan completed.")

if __name__ == "__main__":
    scan_processes()