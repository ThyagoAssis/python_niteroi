class Conta:
    def __init__(self, agencia, conta, cliente):
        self.agencia = agencia
        self.conta = conta
        self.cliente = cliente
        self.__saldo = 0

#Definir saldo da conta corrente
#Encapsular
    @property
    def saldo(self):
        return self.__saldo

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return valor

    def depositar(self, valor):
        if valor <= 0:
            return
        else:
            self.__saldo += valor
