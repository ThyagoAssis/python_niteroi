class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def falar(self):
        print(f"Meu nome é: {self.nome} {self.sobrenome}")

pessoa_um = Pessoa("Mario", "Salles")
print(pessoa_um.falar())

