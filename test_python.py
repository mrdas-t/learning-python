import subprocess

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