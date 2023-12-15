print("----------------")
print("Descubra o valor")
print("----------------")

#Declaração das variáveis
valor_oculto = 35
chance = 5
tentativa = 1

while tentativa <= chance:
    print("Tentativa {} de {}".format(tentativa,chance))
    valor_usuario = int(input("Informe um valor: "))
    #Verifica se o usuario acertou ou errou:
    if valor_usuario == valor_oculto:
        print("Você acertou. Parabéns")
        #Parei
        break
    elif valor_usuario < valor_oculto:
        print("O valor informado é menor que o valor oculto")
    elif valor_usuario > valor_oculto:
        print("O valor inforamdo é maior que o valor oculto")
    tentativa += 1

print("Fim do jogo!")