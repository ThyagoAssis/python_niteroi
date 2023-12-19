'''
1 - O que é função?
As funções são blocos de código reutilizáveis que realizam uma
tarefa específica.
las ajudam a organizar o código e facilitam a manutenção.

'''
#2 - Sintaxe basica da função
def nome_da_funcao():
    #Corpo da função
    #Comandos da função
    resultado = 0
    return resultado
#def - Palava-chave par definir a função
#nome_da_funcao - Nome que identifica a função
#return - Epecifica o que a função retorna

print("Função simples")
print(20*"-")
#Cria a função
def saudacao():
    print("Ola. Boa noite. Ass: Bonner")

#Chama a função
saudacao()

print(20*"-")
print("Função com parametros")
print(20*"-")

def saudacao_turma(nome_aluno):
    print("Boa noite {}".format(nome_aluno))

saudacao_turma("Jose")

def turma_aluno(turma,aluno):
    print(f"O aluno {aluno} pertence turma {turma}")

turma_aluno(2023.2,"Jorge")

print(20*"-")
print("Função com retorno")
print(20*"-")

def soma(valor_um,valor_dois):
    return valor_um + valor_dois

resultado = soma(5,6)
print(f"5 + 6 = {resultado}")

resultado_dois = soma(8,6)
print(f"8 + 6 = {resultado_dois}")

def multiplicar(valor_um,valor_dois):
    resultado = valor_um * valor_dois
    return resultado

print("Multiplicação")
numero_um = 65
numero_dois = 152
multi = multiplicar(numero_um,numero_dois)
print(f"{numero_um} x {numero_dois} = {multi}")

'''
multi_dois = multiplicar(8,6)
print(f"8 x 6 = {multi_dois}")
'''