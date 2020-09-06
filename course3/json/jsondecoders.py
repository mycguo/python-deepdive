from decimal import Decimal
import json
from pprint import pprint
from datetime import datetime

j = '''
{
    "name": "python",
    "age": 27,
    "versions": ["2.x", "3.x"]
}
'''


def make_decimal(arg):
    return Decimal(arg)


print(json.loads(j))

p = '''
{
    "time": {
        "objectType": "datetime",
        "value": "2018-10-21T09:14:00"
    },
    "message": "created this json string"
}
'''

d = json.loads(p)

for key, value in d.items():
    if (isinstance(value, dict) and 'objectType' in value
            and value['objectType'] == 'datetime'):
        d[key] = datetime.strptime(value['value'], '%Y-%m-%dT%H:%M:%S')

print(d)