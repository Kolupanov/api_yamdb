# api_yamdb

### Описание проекта

Проект **YaMDb** собирает отзывы пользователей на различные произведения.

Данный проект основан на методе протокола HTTP (REST API) и предназначен для получения данных с сервера в формате JSON.

### Установка проекта

Клонировать репозиторий:

```
git clone https://github.com/Kolupanov/api_yamdb.git
```

Перейти в репозиторий в командной строке:

```
cd api_yamdb
```

Cоздать виртуальное окружение:

```
python -m venv venv
```

Активировать виртуальное окружение:

Windows
```
venv\Scripts\activate.bat
```

Linux и MacOS
```
source venv/bin/activate
```

Установить и обновить систему управления пакетами pip:

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в репозиторий в командной строке:

```
cd api_yamdb
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Запросы к API

Регистрация пользователей:

```
POST-запрос на добавление нового пользователя с параметрами `email` и `username`
http://127.0.0.1:8000//api/v1/users/
```

```
POST-запрос для получения сообщения с кодом подтверждения (`confirmation_code`) с параметрами `email` и `username`
http://127.0.0.1:8000/api/v1/auth/signup/
```

```
POST-запрос с параметрами `username` и `confirmation_code`, для получения токена
http://127.0.0.1:8000/api/v1/auth/token/
```

Используемые запросы:

```
Работа с категориями. Запросы: Get, Post и Del
http://127.0.0.1:8000/api/v1/categories/
```

```
Работа с жанрами. Запросы: Get, Post и Del
http://127.0.0.1:8000/api/v1/genres/
```

```
Работа с произведениями. Запросы: Get, Post, Patch и Del
http://127.0.0.1:8000/api/v1/titles/
```

```
Работа с отзывами. Запросы: Get, Post, Patch и Del
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
```

```
Работа с комментариями. Запросы: Get, Post, Patch и Del
http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

```
Получение и изменение своих данных. Запросы: Get, Patch
http://127.0.0.1:8000/api/v1/users/me/
```