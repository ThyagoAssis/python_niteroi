'''
Desafio - Solicitar ao usuario a cor da camisa e guardar
a respota dentro de uma varivel
'''

#Declaro a variavel
nome = input("Informe seu nome: ")
cor_camisa = input("Informe a cor da sua camisa: ")

#print("A cor da camisa é: ", cor_camisa)
print("Modelo 01")
print("A camisa de", nome, " é: ", cor_camisa)

print("Modelo 02")
print(f"A camisa de {nome} é: {cor_camisa}")

print("Modelo 03")
print("A camisa de {} é: {}".format(nome,cor_camisa))