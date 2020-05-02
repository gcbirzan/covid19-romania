import json
from collections import defaultdict

import requests

data = requests.get("https://corona.lmao.ninja/v2/historical", {"lastdays": "all"}).json()

to_sum = set(x['country'] for x in data) - set(x['country'] for x in data if not x['province'])

for x in to_sum:
    timeline = defaultdict(lambda : defaultdict(int))
    for y in data:
        if y['country'] == x:
            for k, values in y['timeline'].items():
                for day, value in values.items():
                    timeline[k][day] += value

    new_data = {'country': x, 'province': None, 'timeline': {k: dict(v) for k, v in timeline.items()}}
    data.append(new_data)

with open("../frontend/src/assets/fixed_total.json", "w") as f:
    json.dump(data, f)

