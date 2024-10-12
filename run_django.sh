# Verifique se o Docker está rodando
if ! docker info > /dev/null 2>&1; then
    echo "O Docker não está em execução. Por favor, inicie o Docker e tente novamente."
    exit 1
fi

# Rodar o container
echo "Subindo o Docker Compose..."
docker compose up -d

# Esperar até que o container 'web' e 'db' estejam em execução
CONTAINER_NAME="web"
DB_CONTAINER_NAME="db"
echo "Aguardando os containers $CONTAINER_NAME e $DB_CONTAINER_NAME subirem..."

# Função para verificar se o container está em execução
wait_for_container() {
    local container_name=$1
    while ! docker ps -q -f name=$container_name > /dev/null; do
        echo "O container $container_name ainda não está em execução. Aguardando 5 segundos..."
        sleep 5
    done
}

# Aguardar os containers web e db
wait_for_container $CONTAINER_NAME
wait_for_container $DB_CONTAINER_NAME

# Verificar se o serviço de banco de dados está pronto para conexões
echo "Aguardando o banco de dados $DB_CONTAINER_NAME ficar pronto para conexões..."
while ! docker compose exec -T $DB_CONTAINER_NAME pg_isready -U postgres > /dev/null; do
    echo "O banco de dados ainda não está pronto. Aguardando 5 segundos..."
    sleep 5
done

echo "O container $CONTAINER_NAME e o banco de dados $DB_CONTAINER_NAME estão prontos!"

# Executar as migrações
echo "Executando migrações..."
docker compose exec web python3 manage.py migrate

# Criar superusuário
echo "Criando superusuário..."
docker compose exec web python3 manage.py shell -c "
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

echo "Script finalizado!"
