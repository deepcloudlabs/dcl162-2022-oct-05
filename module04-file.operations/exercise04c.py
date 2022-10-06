import csv

with open("employees_header.csv", mode="rt") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))
