# dict 

print(dir(dict))

print("-"* 40)

di = {"a": "attila", "b": 3, "c": 2}

#di.clear()

print(di)

c = di.copy()

c["c"] = 12

print(c)

print(di.fromkeys("g", 12))
print(di.fromkeys(("a", "b", "z")))

print(di.get("a"))

print(di.items())
print(di.keys())
print(di.values())



print(di)

