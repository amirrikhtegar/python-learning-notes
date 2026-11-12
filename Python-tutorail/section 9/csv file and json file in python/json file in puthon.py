# txt 
# json
# csv for Ai

d = {
    "marks": [[12, 20, 18], [15, 14, 10]],
    "name": "attila",
    "laste_name": "amiri",
    "age": 19
}

s = str(d)
# x = dict(s) error

# مشکل انتقال دیتا هست برای همین از json  استفاده کنم 


# JSON -> javascript , object, notation

import json

# with open("user.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
#     print(data)
#     print(data["amir"])
#     print(data["skills"][0])

# print(data)
# print(data["name"])
# print(data["skills"][0])


# python - javascript
# int/float - number
# True/False - true/false
# None - null
# dict - object
# list/tuple - array
# string - string

# method for json

# loads -> string = json string to python type ---> deserialize / pars
# load -> file

jn_str = "4"
py_type = json.loads(jn_str)

print(jn_str, type(jn_str), sep="\n")
print("*"*40)
print(py_type, type(py_type), sep="\n")


jn_str = "true"
py_type = json.loads(jn_str)

print(jn_str, type(jn_str), sep="\n")
print("*"*40)
print(py_type, type(py_type), sep="\n")


jn_str = '"True"'
py_type = json.loads(jn_str)

print(jn_str, type(jn_str), sep="\n")
print("*"*40)
print(py_type, type(py_type), sep="\n")


jn_str = "[1, 2 ,3 ,4, 5]"
py_type = json.loads(jn_str)

print(jn_str, type(jn_str), sep="\n")
print("*"*40)
print(py_type, type(py_type), sep="\n")

# null -> None

jn_str = 'null'
py_type = json.loads(jn_str)

print(jn_str, type(jn_str), sep="\n")
print("*"*40)
print(py_type, type(py_type), sep="\n")

print(py_type, type(py_type), sep="\n")

# method load

print("*"*40)


with open("user.json", "r", encoding="utf-8") as file:
    s = json.load(file)

print(s)
print(type(s))

# dumps -> python string to json string ---> serialize
# dump -> python file to json file

print("*"*40)
# 1 - dumps

d = {
    "a": 5,
    "b": 6,
    "c": True,
    "d": None
}

j = json.dumps(d)

print(j)
print(type(j))


# 2 - dump

ds = {
    "a": 5,
    "b": 33,
    "c": "True",
    "d": "None",
    "marks": {"math": [12, 2, 3]},
    "am": [1, 2, 4 ,5, ["a", "b"]]
}

with open("us.json", "w", encoding="utf-8") as file:
    json.dump(ds, file, indent=4, sort_keys=True, separators=(",", ":"))

# مثال 
print("*"*40)
print("*"*40)

a = 5
b = 33
c = "True"
d = "None"
marks = {"math": [12, 2, 3]}
am = [1, 2, 4 ,5, ["a", "b"]]


p = {"a": a, "b": b, "c": c, "d": d, "marks": marks, "am": am}

with open("myfile.json", "w") as j:
    json.dump(p, j, indent=4)

with open("myfile.json", "r") as f:
    p = json.load(f)

a = p["a"]
b = p["b"]
c = p["c"]
d = p["d"]
marks = p["marks"]
am = p["am"]

print(p)