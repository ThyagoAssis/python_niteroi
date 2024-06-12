'''
Estruturas de decisão

Calssificar
    > Simples
    > Composta
    > Encadeada
    > Aninhadas

Operadores:

== (igual a)

!= (diferente de)

< (menor que)

> (maior que)

<= (menor ou igual a)

>= (maior ou igual a).

'''
print("Simples - é dada por uma única decisao")

idade = 18
if idade >= 18:
    print("Você é maior de dezoito")

print("Composta - é dada por uma única decisao e uma resposta padrão")
fruta = "laranja"
if fruta == "banana":
    print("Fica bom mel")
else:
    print("Não gosto")

print("Encadeada - é dada por mais de uma decisao e uma reposta padrão")
fruta_dois = "laranja"
if fruta_dois == "banana":
    print("Fica bom mel")
elif fruta_dois == "laranja":
    print("Fica bom suco de melancia")
elif fruta_dois == "Melão":
    print("Fruta do verão")
else:
    print("Não gosto")

print("Aninhada - Uma estrutura dentro da outra")

# Variável Idade
idade = 30
# Variável Cartão
tem_cartao = False

# Condição Para Verificar a Idade

'''
if idade >= 18:
    # Condição Para Verificar se o Usuário tem Cartão
    if tem_cartao:
        print("Você pode comprar o produto.")
    else:
        print("Você não pode comprar o produto sem um cartão.")
else:
    print("Você é menor de idade e não pode comprar o produto.")
'''
# Resultado

if idade >= 18 and tem_cartao == True:
    print("Você pode comprar o produto. DOIS")
elif idade >= 18 and tem_cartao == False:
    print("Você não pode comprar o produto sem um cartão.")
else:
    print("Você é menor de idade e não pode comprar o produto.")
