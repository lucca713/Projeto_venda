# Sistema de Gestão de Vendas com Django, PostgreSQL e MongoDB

Este projeto foi desenvolvido como um desafio técnico para demonstrar habilidades em desenvolvimento web full-stack com Python e Django. A aplicação consiste em um sistema de vendas simples, mas robusto, que permite o registro de transações, consulta de produtos e visualização de histórico de compras dos clientes.

Um dos principais diferenciais técnicos do projeto é a utilização de uma arquitetura de 2 bancos de dados:
- **PostgreSQL** é utilizado como o banco de dados primário e transacional (a "fonte da verdade"), garantindo a integridade e a segurança dos dados das vendas.
- **MongoDB** é utilizado como um banco de dados secundário, otimizado para leitura, onde uma cópia de cada venda é armazenada em formato de documento. Isso torna a consulta de históricos muito mais rápida e escalável.

## 🚀 Funcionalidades Principais

* **Página de Entrada**: Uma landing page moderna que direciona o usuário para a "Área da Loja" ou "Área do Cliente".
* **Registro de Vendas**: Um formulário completo para registrar novas vendas, associando um comprador e múltiplos produtos.
* **Consulta de CEP via API**: Integração com a API **ViaCEP** para preenchimento automático do endereço de entrega.
* **Tabela de Itens Dinâmica**: Adicione produtos à venda em tempo real. A tabela exibe nome, fornecedores, quantidade e valores, com o subtotal da venda sendo atualizado instantaneamente via JavaScript.
* **Consulta de Produtos**: Uma página dedicada para buscar produtos cadastrados pelo nome.
* **Histórico de Compras**: Uma interface amigável que primeiro lista todos os clientes e, ao selecionar um, exibe seu histórico de compras completo, lendo os dados diretamente do MongoDB.
* **Painel Administrativo Customizado**: O admin do Django foi configurado para facilitar o cadastro inicial de Produtos, Fornecedores e Compradores.

## 🛠️ Tecnologias Utilizadas

| Categoria       | Tecnologia                                                              |
| --------------- | ----------------------------------------------------------------------- |
| **Backend** | Python 3.8+, Django                                                    |
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5, Tailwind CSS (Landing)  |
| **Bancos de Dados** | **PostgreSQL** (Transacional), **MongoDB** (Leitura de Histórico)         |
| **APIs Externas** | ViaCEP                                                                  |

---

## ⚙️ Instalação e Execução do Projeto

Siga este guia passo a passo para configurar e rodar o projeto em seu ambiente local.

### 1. Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados em sua máquina:
* [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
* [Git](https://git-scm.com/)
* Um servidor **PostgreSQL** rodando localmente ou em um container.
* Acesso a um cluster **MongoDB** (a forma mais fácil é criar uma conta gratuita no [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)).

### 2. Configuração do Ambiente Local

**a. Clone o repositório:**
```bash
git clone [https://github.com/lucca713/Projeto_venda.git](https://github.com/lucca713/Projeto_venda.git)
cd Projeto_venda


b. Crie e ative um ambiente virtual:
Um ambiente virtual isola as dependências do projeto.
No Windows:
python -m venv venv
.\venv\Scripts\activate


No macOS / Linux:
python3 -m venv venv
source venv/bin/activate


c. Instale as dependências do projeto:
O arquivo requirements.txt contém todas as bibliotecas Python necessárias.
pip install -r requirements.txt


3. Configuração dos Bancos de Dados
a. PostgreSQL:
Crie um novo banco de dados no seu servidor PostgreSQL. Exemplo: sistema_vendas_db.
Abra o arquivo sistema_vendas/settings.py.
Localize a seção DATABASES e preencha com as suas credenciais:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sistema_vendas_db', # Nome do seu banco
        'USER': 'postgres',          # Seu usuário do Postgres
        'PASSWORD': 'sua_senha_aqui',# Sua senha
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


b. MongoDB:
No site do MongoDB Atlas, crie um usuário/senha para o banco e libere o acesso da sua rede.
Obtenha a String de Conexão (Connection String).
No mesmo arquivo sistema_vendas/settings.py, encontre as configurações do MongoDB e preencha com suas informações:
MONGO_CONNECTION_STRING = "mongodb+srv://seu_usuario:sua_senha@seu_cluster.mongodb.net/?retryWrites=true&w=majority"
MONGO_DATABASE_NAME = "historico_vendas_db"
MONGO_COLLECTION_NAME = "vendas"


4. Preparando a Aplicação Django
a. Aplique as migrações:
Este comando criará todas as tabelas necessárias no seu banco de dados PostgreSQL.
python manage.py migrate


b. Crie um superusuário:
Este usuário terá acesso ao painel administrativo do Django.
python manage.py createsuperuser


Siga as instruções no terminal para definir um nome de usuário, email e senha.
5. Executando o Projeto
Finalmente, inicie o servidor de desenvolvimento do Django:
python manage.py runserver


A aplicação estará rodando em http://127.0.0.1:8000/.
📖 Como Utilizar o Sistema
Para uma experiência completa, siga este fluxo de trabalho:
1. Cadastre os Dados Iniciais (Passo Obrigatório):
Acesse o painel administrativo: http://127.0.0.1:8000/admin/
Faça login com o superusuário que você criou.
Cadastre alguns Fornecedores.
Cadastre alguns Compradores.
Cadastre alguns Produtos, associando-os aos fornecedores.
2. Navegue pela Aplicação:
Acesse a página inicial: http://127.0.0.1:8000/
Para registrar uma venda: Clique em "Área da Loja". Preencha o formulário, adicione produtos e finalize a venda.
Para ver o histórico: Clique em "Área do Cliente". Você verá uma lista de
MUITO OBRIGADO PELA OPORTUNIDADE SEMEQ
Meu github com outros projetos: https://github.com/lucca713/
