import yaml
import json

#read the JSON file
with open("config/servers.json", "r") as file:
    data = json.load(file)

#write the YAML file
with open("config/servers.yaml", "w") as file:
    yaml.dump(data, file, default_flow_style=False)

print("Converted JSON to YAML format")


