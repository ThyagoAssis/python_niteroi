class Calculadora:
    def __init__(self, valor_um, valor_dois):
        self.valor_um = valor_um
        self.valor_dois = valor_dois

    def soma(self):
        return self.valor_um + self.valor_dois

    def subtrair(self):
        return self.valor_um - self.valor_dois

    def multiplicar(self):
        return self.valor_um * self.valor_dois

    def dividsao(self):
        return self.valor_um / self.valor_dois



calacular = Calculadora(30, 2)
print(calacular.dividsao())