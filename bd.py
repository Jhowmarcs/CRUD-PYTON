# app/Util/bd.py

import psycopg2
import yaml

# Função para carregar as configurações do banco de dados
def load_db_params():
    with open("app/Util/paramsBD.yml", "r") as file:
        params = yaml.safe_load(file)
    return params

# Função para conectar ao banco de dados PostgreSQL
def connect_to_db():
    params = load_db_params()
    conn = psycopg2.connect(
        dbname=params["db_name"],
        user=params["db_user"],
        password=params["db_password"],
        host=params["db_host"],
        port=params["db_port"]
    )
    return conn
