from utility import countries
from world.domain import Country


def find_countries(predicate):
    result = []
    for country in countries.getElementsByTagName("country"):
        continent = country.getElementsByTagName("Continent")[0].childNodes[0].data
        a_country = Country()
        a_country.code = country.getElementsByTagName("Code")[0].childNodes[0].data
        a_country.name = country.getElementsByTagName("Name")[0].childNodes[0].data
        a_country.population = int(country.getElementsByTagName("Population")[0].childNodes[0].data)
        a_country.surfaceArea = float(country.getElementsByTagName("SurfaceArea")[0].childNodes[0].data)
        a_country.continent = continent
        if predicate(a_country):
            result.append(a_country)
    return result
