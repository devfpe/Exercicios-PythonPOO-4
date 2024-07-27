from .Forma import Forma

class Retangulo(Forma):
    def __init__(self, base: float, altura: float):
        self._base: float = base
        self._altura: float = altura

    def calcular_area(self):
        area = self._base * self._altura
        print(f'A área do retangulo é: >> {round(area, 2)} <<\n')