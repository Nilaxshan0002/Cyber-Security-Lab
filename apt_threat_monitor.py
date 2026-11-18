import os
import time
import psutil
from collections import deque
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "apt_monitored_folder"
LOG_FILE = "security_alerts.txt"

recent_file_changes = deque()

def log_alert(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    alert = f"[{timestamp}] {message}"

    print(alert)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(alert + "\n")

def scan_processes():
    suspicious_names = [
        "keylogger",
        "keycapture",
        "ransomware"
    ]

    for process in psutil.process_iter(["pid", "name"]):
        try:
            name = (process.info["name"] or "").lower()

            if any(item in name for item in suspicious_names):
                log_alert(
                    f"Suspicious process indicator: "
                    f"{name}, PID: {process.info['pid']}"
                )

        except (psutil.NoSuchProcess,
                psutil.AccessDenied):
            continue

def scan_network():
    try:
        connections = psutil.net_connections(kind="inet")

        for connection in connections:
            if connection.status == "ESTABLISHED" and connection.raddr:
                log_alert(
                    f"Established connection: "
                    f"{connection.raddr.ip}:"
                    f"{connection.raddr.port}, "
                    f"PID: {connection.pid}"
                )

    except psutil.AccessDenied:
        print("Network scan requires additional permissions.")

class FileMonitor(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return

        current_time = time.time()
        recent_file_changes.append(current_time)

        while (recent_file_changes and
               current_time - recent_file_changes[0] > 10):
            recent_file_changes.popleft()

        if len(recent_file_changes) >= 15:
            log_alert(
                "Possible ransomware-like activity: "
                "rapid file modifications detected."
            )
            recent_file_changes.clear()

def main():
    os.makedirs(WATCH_FOLDER, exist_ok=True)

    observer = Observer()
    observer.schedule(
        FileMonitor(),
        WATCH_FOLDER,
        recursive=True
    )

    observer.start()

    print("=== APT Threat Monitor ===")
    print("Monitoring local security indicators.")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            scan_processes()
            scan_network()
            time.sleep(15)

    except KeyboardInterrupt:
        print("\nStopping monitor.")

    finally:
        observer.stop()
        observer.join()

if __name__ == "__main__":
    main()