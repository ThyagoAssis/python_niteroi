## Framework Django
### O que é um projeto no django?

No Django, um projeto é uma coleção de configurações e aplicativos que formam uma aplicação web completa. Ele fornece a estrutura para a construção de um site ou sistema web, incluindo configurações, URLs, aplicativos, modelos de dados, vistas e templates.

Aqui estão os principais componentes de um projeto Django:

1. ***Configurações  (Settings):*** Contêm todas as configurações do projeto, como configurações de banco de dados,  locais de templates, entre outras.

2. ***URLs:*** Um arquivo principal de roteamento (geralmente urls.py) que mapeia URLs para as vistas correspondentes.

3. ***Aplicativos (Apps):*** Um projeto pode ser composto por vários aplicativos. Cada aplicativo é uma funcionalidade ou módulo independente dentro do projeto. Por exemplo, um site de e-commerce pode ter um aplicativo para gestão de produtos, outro para carrinho de compras e outro para processamento de pagamentos.

4. ***Modelos (Models):*** Definem a estrutura dos dados do projeto e são mapeados para o banco de dados. Eles utilizam o ORM (Object-Relational Mapping) do Django para facilitar as operações com o banco de dados.

5. ***Vistas (Views):*** Contêm a lógica para processar as requisições e devolver as respostas apropriadas (como HTML, JSON, etc.).

6. ***Templates:*** Arquivos HTML que definem a apresentação do conteúdo enviado pelas vistas.

Em resumo, um projeto Django é a unidade completa que engloba toda a configuração e estrutura necessárias para rodar uma aplicação web. Ele pode ser subdividido em vários aplicativos menores que juntos formam a funcionalidade completa da aplicação.

###

# o conceito de "context"
No Django, o conceito de "context" refere-se ao conjunto de dados que você passa para um template ao renderizá-lo. Esses dados são passados na forma de um dicionário, onde as chaves são os nomes das variáveis que você deseja acessar no template e os valores são os dados correspondentes.

## Por que o "context" é Importante?
O contexto é essencial porque ele permite que você passe informações dinâmicas do seu backend para os templates, possibilitando a renderização de conteúdo dinâmico nas suas páginas web. Sem o contexto, os templates do Django seriam estáticos e não poderiam exibir dados específicos para cada solicitação.

## Como o "context" Funciona?
1. Definindo o "context" na View: Em sua função de view, você cria um dicionário de contexto com as variáveis e valores que deseja passar para o template.
2. Passando o "context" para o Template: Ao renderizar o template com a função render, você passa o contexto junto com o nome do template.
3. Acessando o Contexto no Template: Dentro do template, você usa a sintaxe {{ variavel }} para acessar e exibir os valores do contexto.



## Exemplo Prático

### Exibindo uma Variável
Vamos aprender como passar uma variável simples para um template e exibi-la.


```bash
# views.py
from django.shortcuts import render

def saudacao_view(request):
    mensagem = 'Olá, bem-vindo ao meu site!'
    contexto = {
        'mensagem': mensagem
    }
    return render(request, 'saudacao/saudacao.html', contexto)
```
### Criando o Template

```bash
<!-- saudacao.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Saudação</title>
</head>
<body>
    <h1>{{ mensagem }}</h1>
</body>
</html>

```
## Exibindo um Dicionário
Agora, vamos passar um dicionário para o template e exibir seus conteúdos.

### Definindo a view
```bash

# views.py
from django.shortcuts import render

def informacoes_view(request):
    info_dict = {
        'site': 'Meu Site',
        'ano': 2024,
        'autor': 'Seu Nome'
    }
    contexto = {
        'info': info_dict
    }
    return render(request, 'info/informacoes.html', contexto)
```
## Criando o template

```bash
<!-- informacoes.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Informações</title>
</head>
<body>
    <h1>Informações do Site</h1>
    <p>Site: {{ info.site }}</p>
    <p>Ano: {{ info.ano }}</p>
    <p>Autor: {{ info.autor }}</p>
</body>
</html>
```

## Usando um Loop for para Iterar uma Lista
Agora, vamos passar uma lista para o template e iterar sobre ela usando um loop for.

## Definindo view
```bash
# views.py
from django.shortcuts import render

def lista_nomes_view(request):
    nomes = ['Maria', 'João', 'Ana', 'Pedro']
    contexto = {
        'nomes': nomes
    }
    return render(request, 'lista_nomes.html', contexto)

```

## Criando o template
```bash

<!-- lista_nomes.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Lista de Nomes</title>
</head>
<body>
    <h1>Lista de Nomes</h1>
    <ul>
        {% for nome in nomes %}
            <li>{{ nome }}</li>
        {% endfor %}
    </ul>
</body>
</html>

```
### Combinando Variável, Dicionário e Loop for
### Definindo a View

```bash

# views.py
from django.shortcuts import render

def exemplo_view(request):
    mensagem = 'Bem-vindo ao meu site!'
    lista_nomes = ['Maria', 'João', 'Ana', 'Pedro']
    info_dict = {
        'site': 'Meu Site',
        'ano': 2024,
        'autor': 'Seu Nome'
    }
    contexto = {
        'mensagem': mensagem,
        'nomes': lista_nomes,
        'info': info_dict
    }
    return render(request, 'exemplo.html', contexto)
```
### Criando o Template
```bash

<!-- exemplo.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Exemplo</title>
</head>
<body>
    <h1>{{ mensagem }}</h1>
    
    <h2>Lista de Nomes:</h2>
    <ul>
        {% for nome in nomes %}
            <li>{{ nome }}</li>
        {% endfor %}
    </ul>

    <h2>Informações:</h2>
    <p>Site: {{ info.site }}</p>
    <p>Ano: {{ info.ano }}</p>
    <p>Autor: {{ info.autor }}</p>
</body>
</html>


```

### Desafio: 

Você foi selecionado pela empresa XPTO Tecnologias para uma entrevista de emprego. A XPTO trabalha com desenvolvimento de aplicações Web e, devido a flexibilidade e escalabilidade o Django é o framework pricipal no dia a dia da empresa.
A sua avaliação de emprego será pautada em desenvovler uma aplicação de cadastro de alunos para um cliente da XPTO do ramo escolar. Requisitos da aplicação:

1. Criar uma nova pasta e chama-la de xpto (area de trabalho)
2. Abrir esta pasta no pycharm
3. Cria um novo ambiente virtual
4. Instalar o django
5. Criar um novo projeto em django chamado tuxschool
2. Criar um app chamado cadastro
3. No template deste app deverá conter uma lista com nome, curso, turma e dois botões: um chamado edição e o outro chamado excluir para cada aluno     


### OBS: Os dados dos alunos deverão vir de uma lista de dicionário contida na view e deverão ser exibidas no template através do conceito de context do django.