from django.shortcuts import render

# Create your views here.
def lista(request):
    nome_lista = "Lista de Compras"
    return render(request, "lista/lista.html", {"nome_lista": nome_lista})