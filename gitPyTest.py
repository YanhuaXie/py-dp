
import numpy as np
from osgeo import gdal as gdal
print('gdal test under Git')
print('github test')
print('python-github test')

x = np.linspace(0, 10, 50)
# print(x)


class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        # return self.name
        print(self.name)

    def __repr__(self):
        return f"the name is {self.name}"


person1 = Person("Yanhua")
print(person1)
person1.print_name()

