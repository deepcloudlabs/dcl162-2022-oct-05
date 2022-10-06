with open("employees.txt", mode="rt") as employees:
    for employee in employees:
        identity, fullname, salary, iban = employee.split(",")
        print(f"{identity}\t{fullname}\t{salary}\t{iban}")
