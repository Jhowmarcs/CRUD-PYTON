## Propósito

Este Repositorio foi criado para ensinar os alunos da UniFAAT a trabalharem com microserviço em Python.

## Estrutura do Projeto

├── InfraBD/
│   ├── northwind.sql            # Script SQL para criar o banco de dados e tabelas
│   ├── dockerFile               # Dockerfile para configurar o banco de dados PostgreSQL
│   └── Readme.md                # Instruções para configurar o banco de dados no Docker
├── app/
│   ├── Util/
│   │   ├── bd.py                # Funções para conexão com o banco de dados
│   │   └── paramsBD.yml         # Configurações de conexão com o banco de dados
│   ├── crudCateg.py             # Microserviço CRUD de categorias
│   └── Readme.md                # Instruções de como rodar a aplicação Python
└── Readme.md                    # Instruções gerais para o projeto
