class Country:
    def __init__(self):
        self._code = ""
        self._name = ""
        self._population = 0
        self._surface_area = 0
        self._continent = ""

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        self._population = int(population)

    @property
    def continent(self):
        return self._continent

    @continent.setter
    def continent(self, continent):
        self._continent = continent

    @property
    def surfaceArea(self):
        return self._surface_area

    @surfaceArea.setter
    def surfaceArea(self, surface_area):
        self._surface_area = float(surface_area)

    def __str__(self):
        return f"Country [code: {self.code}, name: {self.name}, continent: {self.continent}, population: {self.population}, surfaceArea: {self.surfaceArea}]"
