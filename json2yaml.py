import ruamel.yaml
import json

with open("input.json") as fp:
    data = json.load(fp)

yaml = ruamel.yaml.YAML()

with open("output.yaml", "w") as fp:
    yaml.dump(data, fp)
