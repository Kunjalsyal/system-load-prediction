# scripts/collect_metrics.py

import os
import psutil
import time

def collect(interval=1, duration=600):
    metrics = []
    for _ in range(int(duration / interval)):
        # Handle OS-specific system load
        try:
            load1, load5, load15 = os.getloadavg()  # Linux
        except AttributeError:
            # Windows fallback: use CPU %
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
        time.sleep(interval)
    
    # Save metrics to file
    import pandas as pd
    df = pd.DataFrame(metrics)
    df.to_csv('data/system_metrics.csv', index=False)
    print("Metrics collection completed!")

# Run
if __name__ == "__main__":
    collect(interval=1, duration=600)
