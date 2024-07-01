from cliente import Cliente
from conta_corrente import Conta

cliente_um = Cliente("Marcos")
cliente_um.cpf = 2222222
conta_um = Conta(1212,23,cliente_um.nome)
#conta_um.saldo = 1000
conta_um.depositar(200)
conta_um.sacar(100)

print(f"Cliente: {conta_um.cliente}\n Agencia: {conta_um.agencia}\n Conta Corrente: {conta_um.conta}\n Saldo: {conta_um.saldo}")

print(50*"-")

cliente_dois = Cliente("Maria")
cliente_dois.cpf = 111111
print(f"Cliente: {cliente_dois.nome}, CPF: {cliente_dois.cpf} ")
conta_um = Conta(1212,23,cliente_um.nome)
#conta_um.saldo = 1000
conta_um.depositar(500)
conta_um.sacar(100)

print(f"Cliente: {conta_um.cliente}\n Agencia: {conta_um.agencia}\n Conta Corrente: {conta_um.conta}\n Saldo: {conta_um.saldo}")