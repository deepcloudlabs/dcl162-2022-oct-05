from xml.dom import minidom

document = minidom.parse("resources/countries.xml")

countries = document.documentElement