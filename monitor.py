def check_cpu(server, cpu_usage):
    if cpu_usage > 90:
        print(f"CRITICAL: {server} is at a CRITICAL CPU usage")
        return True
    elif cpu_usage > 80:
        print(f"WARNING: {server}'s CPU is getting HIGH")
    else:
        print(f"{server} CPU is OK")
        return False

def check_disk(server, disk_usage):
    if disk_usage > 90:
        print(f"CRITICAL: {server}'s disk is almost FULL")
        return True
    elif disk_usage > 75:
        print(f"WARNING: {server}'s disk may need clearing")
    elif disk_usage > 60:
        print(f"NOTICE: {server}'s disk is getting high")
    else:
        print(f"{server} disk is OK")
        return False

def check_memory(server, memory_usage):
    if memory_usage > 95:
        print(f"CRITICAL: {server}'s memory usage is CRITICAL!")
        return True
    elif memory_usage > 85:
        print(f"WARNING: {server} memory is getting high.")
    else:
        print(f"{server} Memory is OK")
        return False

def check_status(server, status):
    if status == "running":
        print(f"{server} is UP.")
        return False
    else:
        print(f"{server} is DOWN!!!")
        return True

def check_region(server, region):
    print(f"{server} is in {region} region")

servers = [
    {"name": "web-01", "cpu": 55, "memory": 99, "disk": 50, "status": "running", "region": "east"},
    {"name": "web-02", "cpu": 65, "memory": 10, "disk": 99, "status": "running", "region": "north"},
    {"name": "web-03", "cpu": 75, "memory": 20, "disk": 12, "status": "stopped", "region": "south"},
    {"name": "web-04", "cpu": 85, "memory": 30, "disk": 45, "status": "running", "region": "west"},
    {"name": "web-05", "cpu": 95, "memory": 40, "disk": 90, "status": "running", "region": "east"},
]

critical_servers = 0

for server in servers:
    print(f"--- {server['name']} ---")
    if check_cpu(server["name"], server["cpu"]):
        critical_servers += 1
    if check_disk(server["name"], server["disk"]):
        critical_servers += 1
    if check_memory(server["name"], server["memory"]):
        critical_servers += 1
    if check_status(server["name"], server["status"]):
        critical_servers += 1
    check_region(server["name"], server["region"])

print(f"\nTotal servers checked: {len(servers)}")
print(f"CRITICAL servers: {critical_servers}")