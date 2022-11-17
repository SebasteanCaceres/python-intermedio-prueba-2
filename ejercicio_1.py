
from functools import reduce


def promedio():
    Pedro = [4, 5, 6, 7, 4, 3]
    Juan = [5, 6, 4, 3, 3, 3]
    María = [6, 6, 5, 4, 3, 3]

    prom_1 = reduce(lambda a, b: (a + b) / 6 , Pedro, Juan, María)

promedio()