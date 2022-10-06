import csv

with open("employees.csv", mode="rt") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
