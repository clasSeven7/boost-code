#!/bin/bash

# Verifique se o Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo "O Docker não está em execução. Por favor, inicie o Docker e tente novamente."
    exit 1
fi

# Rodar o container da aplicação
WEB_CONTAINER_NAME="web"
echo "Subindo o Docker Compose para a aplicação..."
docker compose up -d $WEB_CONTAINER_NAME

# Função para verificar se o container está em execução
wait_for_container() {
    local container_name=$1
    while ! docker ps -q -f name=$container_name > /dev/null; do
        echo "O container $container_name ainda não está em execução. Aguardando 5 segundos..."
        sleep 5
    done
}

# Aguardar o container da aplicação
echo "Aguardando o container $WEB_CONTAINER_NAME subir..."
wait_for_container $WEB_CONTAINER_NAME

# Executar as migrações
echo "Executando migrações..."
docker compose exec $WEB_CONTAINER_NAME python3 manage.py migrate

# Criar superusuário
echo "Criando superusuário..."
docker compose exec $WEB_CONTAINER_NAME python3 manage.py shell -c "
from django.contrib.auth.models import User;
username = 'admin'
email = 'code@code.com'
password = 'admin'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created.')
else:
    print('Superuser already exists.')
"

echo "O container $WEB_CONTAINER_NAME está pronto!"
