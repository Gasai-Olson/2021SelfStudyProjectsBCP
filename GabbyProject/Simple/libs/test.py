import json

with open('Simple/libs/data.json', 'r') as openfile:
    data = json.load(openfile)
with open("Simple/libs/data.json", "w") as outfile:
    json.dump(data, outfile)