import subprocess
import requests

servers = ["google.com", "github.com", "fakeserver123.com"]

for server in servers:
    result = subprocess.run(
        ["ping", "-c", "1", server],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"{server} is UP")
    else:
        print(f"{server} is DOWN!")


sites = [
    {"name": "web-01", "url": "https://google.com"},
    {"name": "web-02", "url": "https://github.com"},
    {"name": "web-03", "url": "https://thisfakedoesnotexist123.com"},
]

for site in sites:
    try:
        response = requests.get(site["url"], timeout=5)
        print(f"{site['name']}: status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print(f"{site['name']}: UNREACHABLE")