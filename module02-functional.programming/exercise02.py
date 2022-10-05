names = ["jack", "James", "ben", "Sun", "kate", "jin"]
print(names)
# names.sort(key=lambda s: len(s), reverse=True)  # higher-order function
names.sort(key=lambda name: name.lower())
print(names)
