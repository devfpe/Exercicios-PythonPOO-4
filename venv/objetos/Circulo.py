from .Forma import Forma
from math import pi

class Circulo(Forma):
    def __init__(self, raio: float):
        self._raio: float = raio

    def calcular_area(self):
        area = pi * (self._raio ** 2)
        print(f'A área do círculo é: >> {round(area, 2)} <<\n')