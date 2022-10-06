import csv

employees = [
    ["1", "jack bauer", "10000", "tr1"],
    ["2", "kate austen", "20000", "tr2"],
    ["3", "james sawyer", "30000", "tr3"],
    ["4", "jin kwon", "40000", "tr4"],
    ["5", "sun kwon", "50000", "tr5"]
]

with open("employees.csv", mode="wt", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(employees)
#    for employee in employees:
#        writer.writerow(employee)

