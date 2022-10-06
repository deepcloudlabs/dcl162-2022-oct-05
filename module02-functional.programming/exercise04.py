countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80000000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67000000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 90000000}
]
european_countries = filter(lambda ctry: ctry["continent"] == "europe", countries)
european_countries = sorted(european_countries, key=lambda ctry: ctry["population"], reverse=True)
for country in european_countries:
    print(f"{country['name']}: {country['population']}")
