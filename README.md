# api_yamdb

### Описание проекта

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

```
source venv/Scripts/activate
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

### Пример запроса к API

Запрос:

```
GET http://127.0.0.1:8000/api/v1/
```

Ответ:

```
