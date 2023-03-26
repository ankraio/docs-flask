import os
import time
from flask import jsonify
import psutil

def status() -> dict:
    """
    Gets the status of the system.

    Args:
        None

    Returns:
        dict: health of this app.
            
    """
    # FastAPI metrics
    cpu_usage_percent = psutil.cpu_percent()
    mem_usage_percent = psutil.virtual_memory().percent
    disk_usage_percent = psutil.disk_usage('/').percent
    network_io_counters = psutil.net_io_counters()
    network_data_sent = network_io_counters.bytes_sent
    network_data_received = network_io_counters.bytes_recv
    load_average = os.getloadavg()[0]
    process_count = len(psutil.process_iter())
    swap_memory = psutil.swap_memory().percent
    disk_io_counters = psutil.disk_io_counters()
    read_ops_per_sec = disk_io_counters.read_count
    write_ops_per_sec = disk_io_counters.write_count
    uptime_seconds = int(time.time() - psutil.boot_time())

    # Measure API response time
    start_time = time.time()
    response = jsonify({'status': 'ok'})
    response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

    # Count HTTP status codes
    status_codes = {
        '200': 0,
        '400': 0,
        '404': 0,
        '500': 0,
    }
    # Assume the Flask app uses Werkzeug as the underlying WSGI server
    for status, count in app.config['request_stats']['werkzeug']['total'].items():
        if status in status_codes:
            status_codes[status] = count

    return jsonify({
        'cpu_usage_percent': cpu_usage_percent,
        'mem_usage_percent': mem_usage_percent,
        'disk_usage_percent': disk_usage_percent,
        'network_data_sent': network_data_sent,
        'network_data_received': network_data_received,
        'load_average': load_average,
        'process_count': process_count,
        'swap_memory': swap_memory,
        'read_ops_per_sec': read_ops_per_sec,
        'write_ops_per_sec': write_ops_per_sec,
        'uptime_seconds': uptime_seconds,
        'http_status_codes': status_codes,
        'average_response_time_ms': response_time,
        'status': 'ok'
    })
    
