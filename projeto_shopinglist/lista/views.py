from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Alunos

# Create your views here.

class AlunoListViews(ListView):
    title = "Listagem de Alunos"
    model = Alunos

class AlunosCreateViews(CreateView):
    model = Alunos

    #Quais são os campos que o usuario ira preencher
    fields = ["nome", "curso", "turma"]

    #Redireciona caso aja sucesso
    #Precisa deficnir o name  na url
    #fAZEMOS REFERENCIA ATRAVES DONAME
    success_url = reverse_lazy('aluno_list')











def lista(request):
    nome_lista = "Minhas fotos"
    minhas_fotos = [
        "https://cdn.pixabay.com/photo/2024/01/11/12/46/pitbull-8501582_640.jpg",
        "https://cdn.pixabay.com/photo/2024/03/25/20/30/german-shorthaired-pointer-8655457_640.jpg",
        "https://cdn.pixabay.com/photo/2024/01/16/22/29/dog-8513202_640.jpg",
        "https://cdn.pixabay.com/photo/2024/04/13/11/29/muffins-8693748_640.jpg",
    ]
    dados = {
        "title": nome_lista,
        "fotos": minhas_fotos
    }
    return render(request, "lista/lista.html", dados)
'''
def mensagem(request):
    mensagem = "Lista de alunos"
    nome_aluno =  [
        {
            "id": 1,
            "nome": "Jose Carlos",
            "curso":"Python",
            "turma":2024.3,
        },
        {
            "id": 2,
            "nome": "Maria Eduarda",
            "curso": "PHP",
            "turma": 2024.2,
        },
        {
            "id": 3,
            "nome": "Robert Rojas",
            "curso": "JAVA",
            "turma": 2024.5,
        }
    ]
    alunos = {
        "title": mensagem,
        "alunos":nome_aluno

    }
    return render(request, "lista/mensagem.html", alunos)
'''
def testando(resquest):
    teste = "Banana"
    frutas = ["Banana", "Maça"]

    return render(resquest, "lista/testando.html", {"teste":teste, "frutas":frutas})
