import json

str_json = """
    {
    "hello": "dalboebi",
    "4e": "nado"
}
"""
print(type(str_json))

date = json.loads(str_json)
print(type(date))