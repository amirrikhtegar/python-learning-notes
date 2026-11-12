# CSV
# ! comma separated value
# ? comma separated value
# * comma separated value
# TODO comma separated value

import csv

# ? reader

with open("iris.csv", "r") as cf:
    data = csv.reader(cf)
    for i in data:
        print(i)
    # ! print(next(data))


# ?  dictreader

with open("name.csv", "r") as csf:
    data = csv.DictReader(csf)
    for i in data:
        print(i)

# ? writer
# ? writerow -> [1, 2, 3] -> row
# ? writerows -> [[1,22,3], [1, 3, 4]]

with open("my csv.csv", "a", newline="") as csf:
    writer = csv.writer(csf)
    writer.writerow(["Id", "Name", "age"])
    data = [["1", "amir", "19"], ["2", "ali", "23"], ["3", "nada", "30"]]
    # * writer.writerows(data)
    for i in data:
        writer.writerow(i)

# ? pandas

import pandas 

df = pandas.read_csv("iris.csv")
print(df)
print(df.head(2))

