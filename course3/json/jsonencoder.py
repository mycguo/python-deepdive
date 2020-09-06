import json
from datetime import datetime

default_encoder = json.JSONEncoder()
print(default_encoder.encode((1, 2, 3)))


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, arg):
        if isinstance(arg, datetime):
            return arg.isoformat()
        else:
            super().default(arg)


customer_encoder = CustomJSONEncoder()
print(customer_encoder.encode(datetime.utcnow()))

print(json.dumps(dict(name='test', time=datetime.utcnow()),
                 cls=CustomJSONEncoder))
