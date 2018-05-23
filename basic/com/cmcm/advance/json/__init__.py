import json

# json==>python:json.loads()
# python==>json:json.dumps()

a = {"name": "hong"}
type(a)
b = json.dumps(a)
print(b)
