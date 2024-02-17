# MDBLOC

Для запуска, заклоньте этот репозиторий

```
git clone 
```

Затем, создайте в корне проекта .env файл со следующим содержимым:

```
MONGO_URL="mongo"
MONGO_PORT="27017"
MONGO_INITDB_ROOT_USERNAME="root"
MONGO_INITDB_ROOT_PASSWORD="root123"
MONGO_INITDB_DATABASE="bloc"
```

Запустите контейнеры:

```
docker-compose build
```

```
docker-compose up
```

После успешного запуска откройте браузер и перейдите на адрес документации http://localhost:8080/docs