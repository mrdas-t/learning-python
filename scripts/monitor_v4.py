import os
import requests
import subprocess
from datetime import datetime
import json
import sys
import yaml
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
webhook=os.environ.get("SLACK_WEBHOOK")

def send_slack(message):
    payload = {"text": message}
    response = requests.post(webhook, json=payload)
    if response.status_code != 200:
        print(f"Failed to send alert: {response.status_code}")

class Server:
    def __init__(self, name, cpu, memory, disk, status, region, host, url):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.disk = disk
        self.status = status
        self.region = region
        self.host = host
        self.url = url

    def check_cpu(self):
        if self.cpu > 90:
            message = f":red_circle: CRITICAL: {self.name} CPU is above 90%"
            print(message)
            send_slack(message)
            return True
        else:
            print(f"{self.name} CPU is OK")
            return False
    
    def check_disk(self):
        if self.disk > 90:
            message = f":red_circle: CRITICAL: {self.name} Disk Usage is above 90%"
            print(message)
            send_slack(message)
        else:
            print(f"{self.name} disk is OK")
            return False

    def check_memory(self):
        if self.memory > 90:
            message = f":red_circle: CRITICAL: {self.name} Memory is above 90%"
            print(message)
            send_slack(message)
            return True
        else:
            print(f"{self.name} memory is OK")
            return False

    def check_status(self):
        if self.status != "running":
            message = f":red_circle: CRITICAL: {self.name} is DOWN"
            print(message)
            send_slack(message)
        else:
            print(f"{self.name} is UP.")
            return False

    def check_ping(self):
        result = subprocess.run(
            ["ping", "-c", "1", self.host],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"[{now}] {self.name} is reachable")
            return False
        else:
            message = f":red_circle: CRITICAL: {self.name} is UNREACHABLE"
            print(message)
            send_slack(message)
            return True

    def check_web(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                print(f"[{now}] {self.name} HTTP OK - {response.status_code}")
                return False
            else:
                print(f"[{now}] {self.name} HTTP Warning - {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"[{now}] {self.name} is UNREACABLE!")
            return True
        except requests.exceptions.Timeout:
            print (f"[{now}] {self.name} has TIMED OUT")
            return True

    def run_all_checks(self):
        critical = 0
        if self.check_cpu():
            critical += 1
        if self.check_disk():
            critical += 1
        if self.check_memory():
            critical += 1
        if self.check_status():
            critical += 1
        if self.check_ping():
            critical += 1
        if self.check_web():
            critical += 1
        return critical

filename = "config/servers.yaml"

if not os.path.exists(filename):
    print("Error: servers.json file not found.")
    sys.exit(1)

with open(filename, "r") as file:
    data = yaml.safe_load(file)

#start with an empty list
servers = []

#loop through JSON data to create a Server object for each one
for item in data:
    server = Server(
        item["name"], item["cpu"], item["memory"], item["disk"],
        item["status"], item["region"], item["host"], item["url"]
    )
    servers.append(server)

total_critical = 0
for server in servers:
    print(f"---{server.name}---")
    total_critical += server.run_all_checks()

critical_servers = [s.name for s in servers if s.cpu > 90]
stopped_servers = [s.name for s in servers if s.status != "running"]
high_memory = [s.name for s in servers if s.memory > 85]
urls = [s.url for s in servers if s.url != ""]

print(f"\nCritical CPU servers: {critical_servers}")
print(f"Stopped servers: {stopped_servers}")
print(f"High memory servers: {high_memory}")
print(f"\nTotal servers checked: {len(servers)}")
print(f"CRITICAL issues: {total_critical}")