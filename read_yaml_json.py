import yaml
import json

with open("test.yml", "r") as f:
   l = yaml.load(f)

print l

with open("test.json", "r") as a:
   l2 = json.load(a)

print l2
