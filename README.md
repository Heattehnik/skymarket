# Skymarket.

Доска объявлений.

## Стэк

![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=green)
![](https://img.shields.io/badge/Framework-DRF-informational?style=flat&logo=Django&logoColor=white&color=green)
![](https://img.shields.io/badge/database-Postgresql-informational?style=flat&logo=postgresql&logoColor=white&color=green)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=green)

## Установка

1. Клонируйте репозиторий на свой компьютер:

   ```bash
   git clone https://github.com/Heattehnik/skymarket.git
   ```

2. Создайте файл `.env` в корне приложения, используя образец из `.env_example`.

3. Запустите приложение из каталога с приложением:

   ```Bash
   python manage.py runserver 0.0.0.0:8000
   ```

5. Приложение будет доступно по адресу `0.0.0.0:8000`.

## Использование

Все доступные эндпоинты находятся по адресу '0.0.0.0:8000/api/redoc-tasks/'

## MISC

Приложение было протестировано со переменными окружения:

- `DB_NAME='postgres'`
- `DB_USER='postgres'`
- `DB_PASSWORD='postgres'`

По умолчанию в приложении отключена авторизация и аутентификация пользователей. Однако при необходимости возможно закрыть неавторизованный доступ к конвертору с помощью JWT.
