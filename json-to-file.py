import json

servers = [
    {"name": "web-01", "cpu": 55, "memory": 99, "disk": 50, "status": "running", "region": "east", "url": "https://google.com", "host": "8.8.8.8"},
    {"name": "web-02", "cpu": 65, "memory": 10, "disk": 99, "status": "running", "region": "north", "url": "https://github.com", "host": "8.8.8.8"},
    {"name": "web-03", "cpu": 75, "memory": 20, "disk": 12, "status": "stopped", "region": "south", "url": "https://hulu.com", "host": "8.8.8.8"},
    {"name": "web-04", "cpu": 85, "memory": 30, "disk": 45, "status": "running", "region": "west", "url": "https://amazon.com", "host": "8.8.8.8"},
    {"name": "web-05", "cpu": 95, "memory": 40, "disk": 90, "status": "running", "region": "east", "url": "https://example123.com", "host": "8.8.8.8"}
]

with open("servers.json","w") as file:
    json.dump(servers, file, indent=4)