#!/usr/bin/env python3
import platform
import psutil
import shutil
import json
import socket
import requests
import argparse
from datetime import datetime

def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
    }

def get_hardware_info():
    info = {}
    try:
        info["CPU Cores"] = psutil.cpu_count(logical=True)
    except Exception:
        info["CPU Cores"] = "Unavailable"

    try:
        info["CPU Usage %"] = psutil.cpu_percent(interval=1)
    except Exception:
        info["CPU Usage %"] = "Unavailable"

    try:
        vm = psutil.virtual_memory()
        info["RAM Total (GB)"] = round(vm.total / (1024**3), 2)
        info["RAM Used (GB)"] = round(vm.used / (1024**3), 2)
    except Exception:
        info["RAM"] = "Unavailable"

    try:
        du = shutil.disk_usage("/")
        info["Disk Total (GB)"] = round(du.total / (1024**3), 2)
        info["Disk Used (GB)"] = round(du.used / (1024**3), 2)
    except Exception:
        info["Disk"] = "Unavailable"

    return info

def get_network_info():
    try:
        ip = requests.get("https://api.ipify.org", timeout=3).text
    except Exception:
        ip = "No internet connection"
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except Exception:
        local_ip = "Unavailable"
    return {
        "Hostname": socket.gethostname(),
        "Local IP": local_ip,
        "Public IP": ip
    }

def run_syscheck(save=None):
    report = {
        "Generated At": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "System": get_system_info(),
        "Hardware": get_hardware_info(),
        "Network": get_network_info()
    }

    # Print to terminal
    print(json.dumps(report, indent=4))

    # Save to file if requested
    if save:
        if save.endswith(".json"):
            with open(save, "w") as f:
                json.dump(report, f, indent=4)
        else:  # save as text
            with open(save, "w") as f:
                f.write(json.dumps(report, indent=4))
        print(f"\n✅ Report saved to {save}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple System Info & Health Checker")
    parser.add_argument("--save", help="Save report to file (example: report.json or report.txt)")
    args = parser.parse_args()
    run_syscheck(save=args.save)
