import ruamel.yaml
import json

yaml = ruamel.yaml.YAML()

with open("input.yaml") as fp:
    data = yaml.load(fp)

with open("output.json", "w") as fp:
    json.dump(data, fp, ensure_ascii=False, indent=4)
