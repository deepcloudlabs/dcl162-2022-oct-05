numbers = [3, 5, 7, 9, 5, 9, 15, 19, 23, 49]

print(all(map(lambda num: num % 2 == 1, numbers)))

all_numbers_odd = True
for n in numbers:
    if n % 2 == 0:
        all_numbers_odd = False
        break
