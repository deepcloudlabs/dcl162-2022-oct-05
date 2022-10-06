import xml.sax

from world.domain import Country


class CountryHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.countries = []
        self.country = Country()
        self.open_tag = ""
        self.property_tag_names = {
            "Code": "code",
            "Name": "name",
            "Continent": "continent",
            "Population": "population",
            "SurfaceArea": "surfaceArea"
        }

    def startElement(self, tag, attributes):
        self.open_tag = tag

    def characters(self, content):
        if self.open_tag in self.property_tag_names.keys():
            property_name = self.property_tag_names[self.open_tag]
            setattr(self.country, property_name, content)

    def endElement(self, tag):
        self.open_tag = ""
        if tag == "country":
            self.countries.append(self.country)
            self.country = Country()


parser = xml.sax.make_parser()
handler = CountryHandler()
parser.setContentHandler(handler)
parser.parse("resources/countries.xml")
for country in handler.countries:
    print(country)
