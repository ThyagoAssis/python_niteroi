'''
Estruturas de decisão

Calssificar
    > Simples
    > Composta
    > Encadeada

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