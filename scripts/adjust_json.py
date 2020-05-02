import json
import sys

with open(sys.argv[1], "r") as f:
    raw_data = json.load(f)

new_data = [county['attributes'] for county in raw_data['features']]
with open("new_fixed.json", "w") as f:
    json.dump(new_data, f)
