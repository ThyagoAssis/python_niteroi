#Impotação das bibliotecas
import random

#Minhas funções
def gera_numero(): #Define a função gera_numero()
    valor_aleatorio = random.randrange(10,100)
    return valor_aleatorio
def solicita_palpite():#Define a função solicita_palpite()
    valor_usuario = int(input("Insira um valor entre 10 e 100: "))
    return valor_usuario
def jogar(): #Define a função jogar()
    print(18 * "-")
    print("| Descubra o valor |")
    print(18 * "-")
    num_aleatorio = gera_numero()
    palpite_usuario = solicita_palpite()

    if palpite_usuario == num_aleatorio:
        print("Acertou miseravi!!")
    else:
        print("Errou miseravi!!")

#Chamar a função jogar()
jogar()


