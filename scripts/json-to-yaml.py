import yaml
import json

# read JSON
with open("config/servers.json", "r") as file:
    data = json.load(file)

# write YAML
with open("config/servers.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)

print("Converted servers.json to servers.yaml")