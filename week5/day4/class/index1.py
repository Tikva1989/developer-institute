
import json
import random

with open('file.json', 'r') as f:
    family= json.load(f)
#
for child in family['children']:
    print(f'Jane\'s child: {child["firstName"]} is {child["age"]} years old. ')
    child["favorite_color"] = random.choice(["blue", "green", "yellow"])

with open('file.json', 'w') as f:
    json.dump(family, f, indent=2)
#
