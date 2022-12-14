countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 90000000}
]
for country in countries:
    print(f"{country['name']}: {country['population']}")
countries.sort(key=lambda ctry: ctry["population"], reverse=True)
for country in countries:
    print(f"{country['name']}: {country['population']}")
