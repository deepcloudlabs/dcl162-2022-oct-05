from utility.xml import find_countries

for country in find_countries(lambda c: c.population == 0):
    print(country)
