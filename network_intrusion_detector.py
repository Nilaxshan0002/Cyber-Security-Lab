import psutil
import time

def monitor_network():
    print("=== Network Activity Monitor ===")
    print("Monitoring local connections. Press Ctrl+C to stop.")

    previous = set()

    try:
        while True:
            connections = psutil.net_connections(kind="inet")

            for connection in connections:
                if connection.status != "ESTABLISHED":
                    continue

                remote = connection.raddr

                if not remote:
                    continue

                connection_info = (
                    connection.pid,
                    remote.ip,
                    remote.port
                )

                if connection_info not in previous:
                    try:
                        process = psutil.Process(
                            connection.pid
                        )
                        name = process.name()
                    except (psutil.NoSuchProcess,
                            psutil.AccessDenied,
                            TypeError):
                        name = "Unknown"

                    print("\n[NEW CONNECTION]")
                    print("Process:", name)
                    print("PID:", connection.pid)
                    print("Remote IP:", remote.ip)
                    print("Remote Port:", remote.port)

                    previous.add(connection_info)

            time.sleep(3)

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    monitor_network()