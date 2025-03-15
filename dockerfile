# InfraBD/dockerFile

# Usar a imagem oficial do PostgreSQL
FROM postgres:latest

# Definir as variáveis de ambiente
ENV POSTGRES_DB=northwind
ENV POSTGRES_USER=faat
ENV POSTGRES_PASSWORD=faat

# Copiar o script SQL para inicializar o banco
COPY northwind.sql /docker-entrypoint-initdb.d/

# Expor a porta padrão do PostgreSQL
EXPOSE 5432
