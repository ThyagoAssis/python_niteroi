import random

def gerar_numero():
    """Gera um número aleatório entre 1 e 10."""
    return random.randint(1, 10)

def solicitar_palpite():
    """Solicita um palpite ao jogador."""
    return int(input("Adivinhe o número (entre 1 e 10): "))

def verificar_palpite(numero_secreto, palpite):
    """Verifica se o palpite do jogador está correto."""
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        return True
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")
    return False

def jogar_jogo():
    """Função principal para o jogo de adivinhação."""
    numero_secreto = gerar_numero()
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")

    while tentativas < 3:  # Limite de 3 tentativas
        palpite_do_jogador = solicitar_palpite()
        tentativas += 1

        if verificar_palpite(numero_secreto, palpite_do_jogador):
            break

    if tentativas == 3:
        print(f"Fim de jogo! O número secreto era {numero_secreto}.")

# Iniciar o jogo
jogar_jogo()