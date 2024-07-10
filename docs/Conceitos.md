### Framework Django
## O que é um projeto no django?

No Django, um projeto é uma coleção de configurações e aplicativos que formam uma aplicação web completa. Ele fornece a estrutura para a construção de um site ou sistema web, incluindo configurações, URLs, aplicativos, modelos de dados, vistas e templates.

Aqui estão os principais componentes de um projeto Django:

1. ***Configurações  (Settings):*** Contêm todas as configurações do projeto, como configurações de banco de dados, configurações de middleware, locais de templates, entre outras.

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

## Como o Contexto Funciona?
1. Definindo o Contexto na View: Em sua função de view, você cria um dicionário de contexto com as variáveis e valores que deseja passar para o template.

2. Passando o Contexto para o Template: Ao renderizar o template com a função render, você passa o contexto junto com o nome do template.

3. Acessando o Contexto no Template: Dentro do template, você usa a sintaxe {{ variavel }} para acessar e exibir os valores do contexto.

## Exemplo Prático
Arquivo views.py
```bash
from django.shortcuts import render

def minha_view(request):
    contexto = {
        'nome': 'Maria',
        'idade': 30,
        'cidade': 'São Paulo'
    }
    return render(request, 'meu_template.html', contexto)


```