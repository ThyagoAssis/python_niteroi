'''
O que é uma repetição?
    é algo que acontece rotineiramente, ou seja, algo que se repete

'''

print("Repetição com while")
#O Contador vai controlar o meu loop (Repetição)
contador = 0

while contador <= 12:
    print(f"Volta ao mundo {contador}")
    #contador = contador + 1
    contador += 1

print("Repetição com while com else")
contar = int(input("Informe o inicio da contagem"))

while contar <= 10:
    print(f"Valor {contar}")
    contar += 1
else:
    print("Só sei contar até 10")

'''
Estrutura de repetição FOR
'''

print("For simples")

for contar_for in range(0,10):
    print("Contagem do for {}".format(contar_for))

print("For com array")
caixa_frutas = ["Banana","Maçã","Pera","Tomate"]

for fruta in caixa_frutas:
    print(fruta)

print("For com else")
sequencia = [1,2,3]
for item in sequencia:
    print(item)
else:
    print('Todos os items foram exibidos com sucesso')
