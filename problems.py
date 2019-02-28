#! /usr/bin/python3

import json
from itertools import product

expressions = []

for (a, b) in product(range(2, 10), range(2, 10)):
    expressions.append({
        "expression": f"{a} + {b}",
        "simple": True
    })

for (a, b) in product(range(50, 60), range(50, 60)):
    expressions.append({
        "expression": f"{a} + {b}",
        "simple": False
    })

print(json.dumps(expressions))
