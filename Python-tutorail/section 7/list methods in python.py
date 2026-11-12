# list
print(dir(list))

li = [1, 2, 3, 4, 1, 2, 1]

# append methods

li.append(12)

li[len(li):] = [21]

print(li)

# clear methods

l = [1 ,2 ,3, 4]

l.clear()

print(l)

# copy

li2 = []

li2 = li.copy()

li2[0] = 0

print(li2)

# count

print(li.count(1))

# extend

li.extend([32, 2345, 12, 100])

li[len(li):] = [4, 7, 876]

print(li)

# index

print(li.index(1, 2))

# insert

li.insert(0, 100)
print(li)

# pop 

li.pop(1)

print(li)

# remove

li.remove(100)
li.remove(100)
print(li)

# reverse

li.reverse()
print(li)

# sort

li.sort(reverse=True)
print(li)

