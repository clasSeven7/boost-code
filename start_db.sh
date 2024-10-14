#!/bin/bash

# Verifique se o Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo "O Docker não está em execução. Por favor, inicie o Docker e tente novamente."
    exit 1
fi

# Rodar o container do banco de dados
DB_CONTAINER_NAME="db"
echo "Subindo o Docker Compose para o banco de dados..."
docker compose up -d $DB_CONTAINER_NAME

# Função para verificar se o container está em execução
wait_for_container() {
    local container_name=$1
    while ! docker ps -q -f name=$container_name > /dev/null; do
        echo "O container $container_name ainda não está em execução. Aguardando 5 segundos..."
        sleep 5
    done
}

# Aguardar o container do banco de dados
echo "Aguardando o container $DB_CONTAINER_NAME subir..."
wait_for_container $DB_CONTAINER_NAME

# Verificar se o serviço de banco de dados está pronto para conexões
echo "Aguardando o banco de dados $DB_CONTAINER_NAME ficar pronto para conexões..."
while ! docker compose exec -T $DB_CONTAINER_NAME pg_isready -U postgres > /dev/null; do
    echo "O banco de dados ainda não está pronto. Aguardando 5 segundos..."
    sleep 5
done

echo "O banco de dados $DB_CONTAINER_NAME está pronto!"
