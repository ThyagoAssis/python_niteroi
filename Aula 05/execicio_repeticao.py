'''1 – Construa um algoritmo em Python que leia 20 valores
inteiros e calcule seu somatório.
'''
soma = 0
for contar in range(21):
    soma = soma + contar
    print(soma)
'''
 * 2 – Construa um programa em python que solicite ao usuário um 
 valor entre 10 e 100, 
 caso o usuário digite  um valor menor que 10 ou maior que 100, 
 envie uma mensagem informando que os valores são inválidos 
 caso contrário conte de zero até o numero digitado pelo usuário. */

'''
print("Atividade 02")
valor = int(input("Informe um valor entre 10 e 100: "))

#Verifica valores entre 10 e 100
if valor < 10 or valor > 100:
    print("Informe um valor entre 10 e 100")
else:
    for contar in range(valor+1):
        print(contar)


'''
/* 4 - Criar um algoritmo em Python para ler 2 
números  e mostrar todos os números pares entre eles (inclusive) *
'''

num_um = int(input("Informe o valor um: "))
num_dois = int(input("Informe o valor dois: "))

if num_dois < num_um:
    temp = num_um
    num_um = num_dois
    num_dois = temp

while num_um < num_dois:
    if(num_um % 2) == 0:
        print(num_um)
    #num_um = num_um + 1
    num_um += 1