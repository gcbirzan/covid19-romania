import datetime
import json
from collections import defaultdict

from app_setup import create_app
from model import Data

l = [1,1,3,3,3,3,4,6,7,9,13,15,17,29,47,59,95,123,139,168,217,260,277,308,367,433,576, 762,906, 1029, 1292, 1452,1760, 1952, 2245]

date = datetime.date(2020, 2, 26)
raw_data = []
delta = []
ratio = []
prev_value = 0
for value in l:
    raw_data.append((date.isoformat(), value))
    delta.append((date.isoformat(), value - prev_value))
    if value > 5 and value != prev_value:
        ratio.append((date.isoformat(), (value - prev_value) / prev_value))
    #     else:
    #         ratio.append((date.isoformat(), None))
    # else:
    #     delta.append((date.isoformat(), None))
    #     ratio.append((date.isoformat(), None))

    prev_value = value
    date += datetime.timedelta(days=1)

l = [3, 7, 11, 17, 23, 26, 34, 43, 65, 68]

date = datetime.date(2020, 3, 22)
raw_data_dead = []
delta_dead = []
prev_value = 0
for value in l:
    raw_data_dead.append((date.isoformat(), value))
    delta_dead.append((date.isoformat(), value - prev_value))
    #     else:
    #         ratio.append((date.isoformat(), None))
    # else:
    #     delta.append((date.isoformat(), None))
    #     ratio.append((date.isoformat(), None))

    prev_value = value
    date += datetime.timedelta(days=1)




tested_people = [(19, 4973), (18, 4670), (17, 4150), (16, 3708), (15, 3205), (14, 2929), (10, 1179), (8, 948), (7, 809), (6, 734), (5, 657), (2, 475)]
date = datetime.date(2020, 3, 1)
tested_people = [(date.replace(day=day).isoformat(), number) for day, number in tested_people]

tests = [(18, 7534), (20, 8284), (21, 8915), (22, 9967), (23, 11223), (24, 12624), (25,14466), (26, 15998), (27, 17453), (28, 19663 ), (29, 21460 ), (30, 23103 ), (31, 24654 )]
date = datetime.date(2020, 3, 1)
tests = [(date.replace(day=day).isoformat(), number) for day, number in tests]
delta_tests = []
prev_tests = [0, 0]
iso_format = '%Y-%m-%d'
for test in tests:
    if not prev_tests[1]:
        prev_tests = test
        continue
    cur_date = datetime.datetime.strptime(test[0], iso_format)
    prev_date = datetime.datetime.strptime(prev_tests[0], iso_format)
    if (cur_date - prev_date) <= datetime.timedelta(days=1):
        delta_tests.append((test[0], test[1] - prev_tests[1]))
    prev_tests = test


delta_tests_obj = {t[0]: t[1] for t in delta_tests}
delta_confirmed_obj = {t[0]: t[1] for t in delta}

days = set(delta_confirmed_obj) & set(delta_tests_obj)
ratio_tests_confirmed = [(day, delta_confirmed_obj[day] / delta_tests_obj[day]) for day in sorted(days)]

# print(json.dumps({
#     "confirmed": raw_data,
#     "delta_confirmed": delta,
#     "ratio_confirmed": ratio,
#     "tested_people": tested_people,
#     "tests": tests,
#     "delta_tests": delta_tests,
#     "dead": raw_data_dead,
#     "delta_dead": delta_dead,
#     "ratio_tests_confirmed": ratio_tests_confirmed,
# }))
data_dict = defaultdict(dict)

for k, v in raw_data:
    data_dict[k]['cases'] = v

for k, v in tested_people:
    data_dict[k]['tested_people'] = v

for k, v in tests:
    data_dict[k]['tests'] = v

for k, v in raw_data_dead:
    data_dict[k]['dead'] = v

print(data_dict)
app, db = create_app()

with app.app_context():
    for date, values in data_dict.items():
        data_obj = Data(date=datetime.datetime.strptime(date, iso_format).date(), **values)
        db.session.add(data_obj)

    db.session.add(Data(date=datetime.date(2020,4,1), cases=2460, tests=26609, dead=85,icu=57,critical=34,recovered=252))
    db.session.commit()
