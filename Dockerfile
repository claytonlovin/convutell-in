# Use a imagem oficial do Ubuntu 20.04 como base
FROM ubuntu:20.04

# Instale as dependências do MongoDB
RUN apt-get update && apt-get install -y gnupg curl

# Importe a chave pública GPG do MongoDB
RUN curl -fsSL https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add -

# Adicione o repositório do MongoDB ao sources.list
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list

# Atualize novamente o sistema
RUN apt-get update

# Instale o pacote mongodb-org
RUN apt-get install -y mongodb-org

# Crie o diretório para armazenar os dados do MongoDB
RUN mkdir -p /data/db

# Copie o arquivo de configuração personalizado (se você tiver um)
# COPY mongodb.conf /etc/mongod.conf

# Exponha a porta padrão do MongoDB
EXPOSE 27017

# Inicie o servidor MongoDB
CMD ["mongod"]
