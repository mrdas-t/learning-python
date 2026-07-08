import re

logs = [
    "2026-06-18 14:23:01 ERROR web-01 CPU threshold exceeded",
    "2026-06-18 14:23:45 INFO web-02 running normally",
    "2026-06-18 14:24:12 ERROR db-01 connection timeout",
    "2026-06-18 14:25:00 WARNING web-03 high memory usage",
    "2026-06-18 14:25:33 ERROR web-04 disk full",
    "2026-06-18 14:26:01 INFO web-01 backup completed",
    "2026-06-18 14:26:45 ERROR web-02 service crashed",
]

# store all parsed logs
parsed = []

for log in logs:
    match = re.search(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARNING|INFO) (\w+-\d+) (.+)", log)
    if match:
        parsed.append({
            "timestamp": match.group(1),
            "level": match.group(2),
            "server": match.group(3),
            "message": match.group(4)
        })
        if match.group(2) == "ERROR" or match.group(2) == "WARNING":
            print(f"[{match.group(2)}] {match.group(3)} at {match.group(1)}: {match.group(4)}")

# now list comprehensions work on the full dataset
errors = [p for p in parsed if p["level"] == "ERROR"]
warnings = [p for p in parsed if p["level"] == "WARNING"]

print(f"\nTotal lines parsed: {len(logs)}")
print(f"Errors found: {len(errors)}")
print(f"Warnings found: {len(warnings)}")