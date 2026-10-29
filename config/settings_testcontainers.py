import atexit

from .settings import *

from testcontainers.postgres import PostgresContainer


# Cria a configuração do PostgreSQL de testes.
postgres = PostgresContainer(
    image="postgres:16-alpine",
    username="django_test",
    password="django_test_password",
    dbname="django_test",
)

# Inicia o container Docker.
postgres.start()

# Registra a função que encerrará o container
# quando o processo Python terminar normalmente.
atexit.register(postgres.stop)


# Informa ao Django como se conectar ao PostgreSQL.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_test",
        "USER": "django_test",
        "PASSWORD": "django_test_password",
        "HOST": postgres.get_container_host_ip(),
        "PORT": postgres.get_exposed_port(5432),
    }
}