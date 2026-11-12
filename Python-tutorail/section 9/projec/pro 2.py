import json
def func_json(x:str):
    s = json.dumps(x)
    print(s)

func_json('{"a": 5,"b": 6,"c": true,"d": null}')

