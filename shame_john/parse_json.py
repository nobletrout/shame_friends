import json


not_json_string = "john is a pretend british person"
json_string = '{"john": { "pretend british" : { "bool" : "true" }}}'

try:
    not_json_parsed = json.loads(not_json_string)

except json.decoder.JSONDecodeError as err:
    print("that wasn't json: %s" % not_json_string)
    not_json_parsed = {}

try:
    json_parsed = json.loads(json_string)
except json.decoder.JSONDecodeError as err:
    print("that also wasn't json")
    json_parsed = {}
print(not_json_parsed)
print(json_parsed)
print("end of program?")
