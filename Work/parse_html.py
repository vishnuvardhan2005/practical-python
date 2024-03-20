#!/usr/bin/python
import urllib.request
from xml.etree.ElementTree import parse

u = urllib.request.urlopen('https://dabeaz-course.github.io/practical-python/Notes/01_Introduction/01_Python.html')
doc = parse(u)

for pt in doc.findall('.//pt'):
    print(pt.text)
