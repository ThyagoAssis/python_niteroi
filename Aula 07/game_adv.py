#Impotação das bibliotecas
import random

#Minhas funções
def gera_numero(): #Define a função gera_numero()
    return random.randrange(10,100)
def solicita_palpite():#Define a função solicita_palpite()
     return int(input("Insira um valor entre 10 e 100: "))
def verifica_palpite(numero_secreto,papilte):

    if numero_secreto == papilte:
        print("Você acertou. Parabéns")
        return True
    elif papilte < numero_secreto:
        print("O valor informado é menor que o valor oculto")
    elif papilte > numero_secreto:
        print("O valor informado é maior que o valor oculto")
def nivel(nivel):
    if nivel == 1:
        chance = 20
        return chance
    elif nivel == 2:
        chance = 10
        return chance
    elif nivel == 3:
        chance = 5
        return chance
def jogar(): #Define a função jogar()
    #Variáveis Globais
    num_aleatorio = gera_numero()
    tentativas = 1

    #Cabeçalho
    print(18 * "-")
    print("| Descubra o valor |")
    print(18 * "-")

    nivel_jogador = int(input("Escolha um nível:\n 1-Facil\n 2-Médio\n 3-Difícil\n Esolha: "))
    chances = nivel(nivel_jogador)
    while tentativas <= chances:
        #Variavei locais
        palpite_usuario = solicita_palpite()
        print("Tentativa {} de {}".format(tentativas, chances))

        #Força o usuario a inserir valor entre 10 e 100
        if palpite_usuario < 10 or palpite_usuario > 100:
            continue

        if verifica_palpite(num_aleatorio,palpite_usuario):
            break
        tentativas += 1

jogar() #Chamar a função jogar()