# Projeto de Microserviço com Python

Este repositório foi criado para ensinar os alunos da UniFAAT a trabalhar com microserviços utilizando Python e PostgreSQL. Ele inclui um microserviço que oferece um CRUD para a tabela `categories` de um banco de dados PostgreSQL.

## Estrutura do Projeto

- **InfraBD/**: Contém os arquivos de infraestrutura para configurar o banco de dados PostgreSQL.
  - `northwind.sql`: Script SQL para criar o banco e as tabelas.
  - `dockerFile`: Dockerfile para rodar o PostgreSQL com a configuração do banco.
  - `Readme.md`: Instruções sobre como inicializar o banco no Docker.
  
- **app/**: Contém a aplicação Python com o microserviço CRUD.
  - `Util/`: Contém arquivos utilitários para a aplicação.
    - `bd.py`: Função para conexão com o banco de dados.
    - `paramsBD.yml`: Arquivo de configuração do banco de dados.
  - `crudCateg.py`: Microserviço para manipulação da tabela `categories` (CRUD).
  - `Readme.md`: Instruções de como rodar o microserviço Python.

## Como Rodar o Projeto

### Passo 1: Configurar o Banco de Dados PostgreSQL

1. **Subir o Banco de Dados com Docker**

   - Navegue até a pasta `InfraBD` e construa a imagem Docker do PostgreSQL:
     ```bash
     docker build -t my-postgres-image .
     ```

   - Depois, execute o contêiner:
     ```bash
     docker run -d --name my-postgres-container -p 2000:5432 my-postgres-image
     ```

   - O banco de dados estará disponível em `localhost:2000`.

2. **Configurar o Banco de Dados**

   - O script SQL `northwind.sql` será executado automaticamente para criar as tabelas necessárias.
   - Conecte-se ao banco de dados usando um cliente PostgreSQL como DBeaver ou psql com as credenciais definidas no `paramsBD.yml`.

---

### Passo 2: Configurar a Aplicação Python

1. **Instalar Dependências**

   Instale as dependências necessárias para o projeto Python:
   ```bash
   pip install -r requirements.txt
