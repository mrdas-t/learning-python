import os
import sys
import json
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def check_cpu(server,cpu_usage):
    if cpu_usage > 90:
        print(f"[{now}] CRITICAL: {server} CPU is above 90%!")
        with open("alerts.log","a") as log:
            log.write(f"[{now}] CRITICAL: {server} CPU is above 90%!\n")
        return True
    elif cpu_usage > 80:
        print(f"[{now}] WARNING: {server} CPU is rising.")
    else:
        print(f"[{now}] {server} CPU is ok")
        return False

def check_disk (server,disk_usage):
    if disk_usage > 90:
        print(f"[{now}] CRITICAL: {server} disk usage is above 90%!")
        with open("alerts.log","a") as log:
            log.write(f"[{now}] CRITICAL: {server} DISK is above 90%!\n")
        return True
    elif disk_usage > 80:
        print(f"[{now}] WARNING: {server}'s disk is filling up.")
    else:
        print(f"[{now}] {server} disk usage is OK.")
        return False

def check_memory(server,memory_usage):
    if memory_usage > 90:
        print(f"[{now}] CRITICAL: {server} memory is above 90%!")
        with open("alerts.log","a") as log:
            log.write(f"[{now}] CRITICAL: {server} MEMORY is above 90%!\n")
        return True
    elif memory_usage > 85:
        print(f"[{now}] WARNING: {server} memory is above 85%.")
    else:
        print(f"[{now}] {server} memory is OK.")
        return False

def check_status(server,status):
    if status != "running":
        print(f"[{now}] {server} is DOWN!")
        with open("alerts.log","a") as log:
            log.write(f"[{now}] CRITICAL: {server} DOWN!\n")
        return True
    else:
        print(f"[{now}] {server} is UP")

def print_region(server,region):
    print(f"[{now}] {server} is in {region} region.")

critical_servers = 0
total_servers = 0
filename = "servers.json"

if os.path.exists(filename):
    print(f"Found {filename}")
else:
    sys.exit(1)

try:
    with open("servers.json","r") as file:
        servers = json.load(file)

    for server in servers:
        total_servers += 1
        print(f"---{server['name']}---")
        if check_cpu(server["name"],server["cpu"]):
           critical_servers += 1
        if check_disk(server["name"], server["disk"]):
            critical_servers += 1
        if check_memory(server["name"], server["memory"]):
            critical_servers += 1
        if check_status(server["name"], server["status"]):
            critical_servers += 1
        print_region(server["name"], server["region"])

    print(f"Total servers checked: {total_servers}")
    print(f"CRITICAL servers: {critical_servers}")

except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: incorrect value in dictionary")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Monitoring Complete")