

import os
import psutil
import time
import pandas as pd

def collect(interval=1, duration=20):
    metrics = []


    data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    for i in range(int(duration / interval)):
     
        try:
            load1, load5, load15 = os.getloadavg() 
        except (AttributeError, OSError):
            cpu_percent = psutil.cpu_percent(interval=None)
            load1 = load5 = load15 = cpu_percent

        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent
        net = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        metrics.append({
            'load1': load1,
            'load5': load5,
            'load15': load15,
            'memory': memory,
            'disk': disk,
            'network': net
        })


        print(f"Collected {i+1}/{int(duration/interval)} samples", end='\r')
        time.sleep(interval)

 
    df = pd.DataFrame(metrics)
    csv_path = os.path.join(data_folder, 'system_metrics.csv')
    df.to_csv(csv_path, index=False)
    print(f"\nMetrics collection completed! Saved to {csv_path}")



if __name__ == "__main__":
    collect(interval=1, duration=600)
