import csv

with open("data2.csv") as f:
    sp = csv.reader(f, delimiter=";")
    for i in sp:
        print(i)
        