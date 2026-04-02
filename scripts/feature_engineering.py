import psutil
import time
import csv
import os
from datetime import datetime

OUTPUT_FILE = "data/raw/system_metrics.csv"


def ensure_dir(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def collect(interval=1, duration=300):
    ensure_dir("data/raw")

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "timestamp",
            "cpu_percent",
            "mem_percent",
            "disk_read_bytes",
            "disk_write_bytes",
            "net_sent_bytes",
            "net_recv_bytes",
            "load_avg_1",
            "load_avg_5",
            "load_avg_15"
        ])

        start_time = time.time()

        prev_disk = psutil.disk_io_counters()
        prev_net = psutil.net_io_counters()

        while time.time() - start_time < duration:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            cpu = psutil.cpu_percent(interval=None)
            mem = psutil.virtual_memory().percent

            disk = psutil.disk_io_counters()
            net = psutil.net_io_counters()

            disk_read = disk.read_bytes - prev_disk.read_bytes
            disk_write = disk.write_bytes - prev_disk.write_bytes

            net_sent = net.bytes_sent - prev_net.bytes_sent
            net_recv = net.bytes_recv - prev_net.bytes_recv

            prev_disk = disk
            prev_net = net

            load1, load5, load15 = os.getloadavg()

            writer.writerow([
                now,
                cpu,
                mem,
                disk_read,
                disk_write,
                net_sent,
                net_recv,
                load1,
                load5,
                load15
            ])

            print(f"[LOG] {now} | CPU={cpu}% MEM={mem}% LOAD1={load1:.2f}")
            time.sleep(interval)

    print(f"[DONE] Metrics saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    collect(interval=1, duration=600)
