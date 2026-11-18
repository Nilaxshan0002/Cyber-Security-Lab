import time
from collections import deque
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "monitored_folder"
TIME_WINDOW = 10
CHANGE_LIMIT = 15

recent_changes = deque()

class RansomwareMonitor(FileSystemEventHandler):

    def on_modified(self, event):
        if event.is_directory:
            return

        self.check_activity(event.src_path)

    def on_created(self, event):
        if event.is_directory:
            return

        self.check_activity(event.src_path)

    def on_moved(self, event):
        if event.is_directory:
            return

        self.check_activity(event.dest_path)

    def check_activity(self, file_path):
        current_time = time.time()
        recent_changes.append(current_time)

        while (recent_changes and
               current_time - recent_changes[0] > TIME_WINDOW):
            recent_changes.popleft()

        print("[FILE CHANGE]", file_path)

        if len(recent_changes) >= CHANGE_LIMIT:
            print("\n[CRITICAL WARNING]")
            print("Unusually high file activity detected!")
            print("Possible ransomware-like behaviour.")
            print("Investigate the affected system immediately.")

def main():
    observer = Observer()
    handler = RansomwareMonitor()

    observer.schedule(
        handler,
        WATCH_FOLDER,
        recursive=True
    )

    observer.start()

    print("Monitoring folder:", WATCH_FOLDER)
    print("Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    import os

    os.makedirs(WATCH_FOLDER, exist_ok=True)
    main()