import datetime
import json
from collections import defaultdict
from glob import glob

from pytz import UTC

files = sorted(glob('/home/gcbirzan/covid19/v2/1*'))

current_data = {}
log = []
for f in files:
    with open(f, "r") as f:
        raw_data = json.load(f)

        new_data = {county['attributes']['Judete']: (county['attributes']['Cazuri_confirmate'], county['attributes']['EditDate']) for county in raw_data['features']}
    for judet, (cazuri, ts) in new_data.items():
        if judet not in current_data:
            current_data[judet] = cazuri
            continue
        if current_data[judet] != cazuri:
            ts = datetime.datetime(1970, 1, 1, tzinfo=UTC) + datetime.timedelta(seconds=ts / 1000)
            # print(current_data[judet], cazuri, judet)
            log.append({
                           'judet': judet,
                           'cazuri_initiale': current_data[judet],
                           'cazuri_finale': cazuri,
                           'cazuri_delta': cazuri - current_data[judet],
                           'timestamp': ts.isoformat()
                       })
            current_data[judet] = cazuri

with open("latest_log.json", "w") as f:
    json.dump(log, f)

