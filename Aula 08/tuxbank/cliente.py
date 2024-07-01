#Classe cliente

class Cliente:
    def __init__(self, nome):
        self.nome = nome

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

'''
cliente_um = Cliente("Carlos")
cliente_um.cpf = 977736513
print(f"Cliente: {cliente_um.nome}, CPF: {cliente_um.cpf} ")
'''

