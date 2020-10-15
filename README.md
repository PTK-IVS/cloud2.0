[![We recommend IntelliJ IDEA](https://www.elegantobjects.org/intellij-idea.svg)](https://www.jetbrains.com/idea/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
# Инструкция
Просмотр логов: `docker-compose logs -f`
Запуск  тестового приложения: `docker-compose up -d --build`
Ручной запуск миграций: `docker-compose exec cloud python manage.py migrate --noinput`
Проверить volume: `docker volume inspect cloud20_postgres_data`
Запуск рабочего приложения:
`docker-compose -f docker-compose.prod.yml down -v
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec cloud python manage.py migrate --noinput`