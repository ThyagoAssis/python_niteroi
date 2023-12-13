'''
1 - Elabore um programa em python para ler um valor inteiro e informar,
através de uma mensagem se este valor é um número par ou ímpar.
'''

print("Exercicio 01")
#Declaração de variáveis
valor_inteiro = int(input("Informe um valor: ")) #Guarda o valor do usuario
resto = valor_inteiro % 2

print(resto)
if resto == 0:
    print("O valor {} é par".format(valor_inteiro))
else:
    print("O valor {} é ímpar".format(valor_inteiro))

'''
2 - Implemente um programa que leia dois valores inteiros e verificar se o primeiro  
é múltiplo do segundo,  seu programa deverá exibir a mensagem: 
“São múltiplos” ou “Não são múltiplos” 
'''
#Declarar variaveis
numero_um = int(input("Informe o primeiro valor: "))
numero_dois = int(input("Informe o segundo valor: "))
modulo = numero_um % numero_dois

if modulo == 0:
    print(f"Os valores {numero_um} e  {numero_dois} são multiplos")
else:
    print(f"Os valores {numero_um} e  {numero_dois} não são multiplos")

'''
3 - Desenvolva um programa para ler um valor inteiro e apresentar
     *  a. Exibir a mensagem “número negativo” se n < 0.
     *  b. Exibir a mensagem “zero” se n = 0.
     *  c. Exibir a mensagem “número positivo” se n > 0.

'''
#Declarar as varaiveis
valor = int(input("Informe o valor: "))

if valor < 0:
    print("O numero", valor, "é menor que zero")
elif valor > 0:
    print("O numero", valor, "é maior que zero")
elif valor == 0:
    print("O numero", valor, "é zero")
else:
    print("Valor desconhecido")