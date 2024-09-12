<h1 align="center">
  🔗Boost Code
</h1>

<div align="center">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/clasSeven7/boost-code.svg" />
  
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/clasSeven7/boost-code.svg" />
  
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/clasSeven7/boost-code.svg" />

  <a href="https://github.com/clasSeven7/boost-code/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/clasSeven7/boost-code.svg" />
  </a>
  
  <a href="https://github.com/clasSeven7/boost-code/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/clasSeven7/boost-code.svg" />
  </a>
</div>

<div align="center">
  <img src=".github/preview.png" width="100%"/>
</div>

### 📖 Sobre

**Boost Code** é uma plataforma inovadora projetada para acelerar seu aprendizado em programação e desenvolvimento de software. Com uma abordagem prática e dinâmica, nosso objetivo é fornecer ferramentas e recursos que ajudem desenvolvedores a aprimorar suas habilidades rapidamente.

### Funcionalidades

- **Gerenciamento de Links:** Criação, atualização, exclusão e recuperação de links.
- **Autenticação de Usuário:** Sistema de autenticação seguro utilizando o sistema de autenticação do Django.
- **API RESTful:** Expõe uma API RESTful para todas as operações de gerenciamento de links.
- **Interface de Administração:** Gerencie usuários e links através da interface de administração do Django.

### Tecnologias Utilizadas

- **Django:** Um framework web de alto nível em Python que encoraja o desenvolvimento rápido e um design limpo e pragmático.
- **Django Rest Framework:** Um conjunto de ferramentas poderoso e flexível para a construção de APIs Web.
- **PostgresSQL:** Um sistema de gerenciamento de banco de dados relacional de código aberto que oferece robustez, suporte a transações ACID, e uma rica funcionalidade, incluindo suporte a tipos de dados avançados e extensões como o PostGIS para dados geoespaciais.
- **Python:** Uma linguagem de programação que permite trabalhar de maneira rápida e integrar sistemas de forma mais eficaz.

### Instalação

Para obter uma cópia local em funcionamento, siga estas etapas:

#### Pré-requisitos

- Python 3.x
- pip (instalador de pacotes Python)
- Virtualenv (opcional, mas recomendado)

#### Passos para instalação

**1. Clone o repositório:**

```bash
git clone https://github.com/clasSeven7/boost-code.git
cd boost-code
```

**2. Crie e ative um ambiente virtual (opcional, mas recomendado):**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Aplique as migrações:**

```bash
python3 manage.py migrate
```

**5. Crie um superusuário (para acessar a interface de administração do Django):**

```bash
python3 manage.py createsuperuser
```

**6. Execute o servidor de desenvolvimento:**

```bash
python3 manage.py runserver
```

**7. Acesse a aplicação:**

- Abra seu navegador e vá para <http://127.0.0.1:8000/> para acessar a aplicação.
- Acesse a interface de administração do Django em <http://127.0.0.1:8000/admin/>.

#### Endpoints da API

A aplicação fornece uma API RESTful para gerenciar links. Abaixo estão alguns dos endpoints disponíveis:

- `GET /api/links/:` Recupera uma lista de todos os links.
- `POST /api/links/:` Cria um novo link.
- `GET /api/links/{id}/:` Recupera um link específico pelo ID.
- `PUT /api/links/{id}/:` Atualiza um link específico pelo ID.
- `DELETE /api/links/{id}/:` Exclui um link específico pelo ID.

#### Exemplo de Requisições

**Criar um Novo Link:**

```bash
curl -X POST http://127.0.0.1:8000/api/links/ -H
```

**Recuperar Todos os Links:**

```bash
curl http://127.0.0.1:8000/api/links/
```

#### Testes da API de Posts

**Dependências:**

Certifique-se de ter as seguintes dependências instaladas:

- Django
- Django REST Framework
- Django REST Framework Simple JWT

#### Descrição dos Testes

A classe PostAPITestCase realiza os seguintes testes:

- **Criação de Post:** Verifica se um post pode ser criado com sucesso por um usuário autenticado e se os dados do post são salvos corretamente.

- **Recuperação de Post:** Testa se um post existente pode ser recuperado e se os dados retornados estão corretos.

- **Atualização de Post:** Valida se um post pode ser atualizado com sucesso e se as alterações são refletidas no banco de dados.

- **Exclusão de Post:** Confirma que um post pode ser excluído e que o banco de dados é atualizado corretamente após a exclusão.

- **Criação de Post sem Autenticação:** Garante que a criação de um post é negada quando a solicitação é feita sem um token de autenticação.

**1. Criação de Post:**

Verifica se um post pode ser criado com sucesso:

```python
def test_create_post(self):
  response = self.client.post('/api/post/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'}, HTTP_AUTHORIZATION=self.authorization_header)
  self.assertEqual(response.status_code, status.HTTP_201_CREATED)
  self.assertEqual(Post.objects.count(), 1)
```

**2. Recuperação de Post:**

Verifica se um post existente pode ser recuperado:

```python
def test_retrieve_post(self):
  post = Post.objects.create(title='Post', content='Conteúdo')
  response = self.client.get(f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
  self.assertEqual(response.status_code, status.HTTP_200_OK)
```

**3. Atualização de Post:**

Verifica se um post pode ser atualizado:

```python
def test_update_post(self):
  post = Post.objects.create(title='Post', content='Conteúdo')
  response = self.client.patch(f'/api/post/{post.id}/', {'title': 'Post Atualizado'}, HTTP_AUTHORIZATION=self.authorization_header)
  self.assertEqual(response.status_code, status.HTTP_200_OK)
```

**4. Exclusão de Post:**

Verifica se um post pode ser excluído:

```python
def test_delete_post(self):
  post = Post.objects.create(title='Post', content='Conteúdo')
  response = self.client.delete(f'/api/post/{post.id}/', HTTP_AUTHORIZATION=self.authorization_header)
  self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
```

**5. Criação de Post sem Autenticação:**

Verifica se a criação de um post é negada sem autenticação:

```python
def test_create_post_unauthenticated(self):
  response = self.client.post('/api/post/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'})
  self.assertEqual(response.status_code, 401)
```

#### Execução dos Testes

Para rodar os testes, utilize o comando:

```bash
python3 manage.py test
```

### Como Executar o Projeto

1. Clone o repositório
2. Instale as dependências com `pip install -r requirements.txt`
3. Execute as migrações com `python manage.py migrate`
4. Inicie o servidor com `python manage.py runserver`

### Contribuição

Contribuições são bem-vindas! Por favor, siga estas etapas para contribuir:

1. Faça um fork do repositório.
2. Crie um novo branch `(git checkout -b feature/SuaFuncionalidade)`.
3. Faça suas alterações.
4. Faça o commit das suas alterações `(git commit -m 'Adicionar SuaFuncionalidade')`.
5. Envie para o branch `(git push origin feature/SuaFuncionalidade)`.
6. Abra um pull request.
