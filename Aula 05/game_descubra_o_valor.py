import random
print(18*"-")
print("| Descubra o valor |")
print(18*"-")

#Declaração das variáveis
valor_oculto = random.randrange(10,100)
chance = 0
pontos = 100

##Definido níveis
nivel = int(input("Escolha um nível:\n 1-Facil\n 2-Médio\n 3-Difícil\n Esolha: "))
if nivel == 1:
    chance = 20
elif nivel == 2:
    chance = 10
elif nivel == 3:
    chance = 5
else:
    print("Valor desconhecido!")


print(f"Você possui {pontos} pontos.\nCada erro custa 5 pontos")
#tentativa = 1
#while tentativa <= chance:
for tentativa in range(1,chance+1):

    print("Tentativa {} de {}".format(tentativa,chance))
    valor_usuario = int(input("Informe um valor entre 10 e 100: "))

    #Verifica valor entre 10 e 100
    if valor_usuario < 10 or valor_usuario > 100:
        print("Informe um valor entre 10 ou 100!!!")
        continue #Vai forçar meu usuario a digitar um valor correto


    #Verifica se o usuario acertou ou errou:
    if pontos < 0:
        pontos = 0
    else:
        if valor_usuario == valor_oculto:
            print("Você acertou. Parabéns")
            # Parei
            break
        elif valor_usuario < valor_oculto:
            print("O valor informado é menor que o valor oculto")
            pontos = pontos - 5

        elif valor_usuario > valor_oculto:
            print("O valor informado é maior que o valor oculto")
            pontos = pontos - 5

    #tentativa += 1

print(f"Sua pontuação foi: {pontos} ")
print(f"O valor oculto era: {valor_oculto}")
print("Fim do jogo!")