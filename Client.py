import time
from datetime import datetime

import psutil
import requests

while True:
    cpu_num = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()

    memory_total = psutil.virtual_memory().total
    memory_ava = psutil.virtual_memory().available
    memory_per = psutil.virtual_memory().percent

    disk_total = psutil.disk_usage('/').total
    disk_free = psutil.disk_usage('/').free

    net_sent = psutil.net_io_counters().bytes_sent
    net_rec = psutil.net_io_counters().bytes_recv

    now = datetime.now()

    data = {'cpu_num': cpu_num, 'cpu_percent': cpu_percent, 'memory_total': memory_total, 'memory_ava': memory_ava,
            'memory_per': memory_per, 'disk_total': disk_total, 'disk_free': disk_free, 'net_sent': net_sent,
            'net_rec': net_rec, 'time': now}

    headers = {'Content-Type': 'application/json'}
    try:
        requests.post('http://192.168.12.1:8000/api', data, headers)
    except:
        print("error")
    time.sleep(1)
