l = range(5)
l.append('test')
l.append('stuffs')
l.append({})
l[-1]['abc'] = range(5);
l[-1]['vwr'] = 'xyz';
print "Starting with these: ",l

import yaml

print yaml.dump(l, default_flow_style=False)
with open("test.yml", "w") as f:
    f.write(yaml.dump(l, default_flow_style=False))    

import json

with open("test.json", "w") as f:
    f.write(json.dumps(l))


