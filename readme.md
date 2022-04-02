<p align="center">
<img src=".github/chip.png" alt="logo">
</p>

<h1 align="center">Area 51</h1>

![header_picture](.github/readme_header.jpg)

## Содержание

- [Деплой проекта](#деплой-проекта)
	- [Установка базы данных](#установка-базы-данных)
	- [Виртуальное окружение Python](#виртуальное-окружение-python)
	- [Локальные настройки](#локальные-настройки)
	- [Настройки для деплоя](#настройки-для-деплоя)
	- [Миграция БД](#миграция-бд)
	- [Запуск сервера gunicorn](#запуск-сервера-gunicorn)
	- [Настройка nginx](#настройка-nginx)
	- [Supervisor](#supervisor)
	- [Подключаем SSL-сертификат](#подключаем-ssl-сертификат)
- [Действия после деплоя](#действия-после-деплоя)
	- [Создаём суперпользователя в админке](#создаём-суперпользователя-в-админке)
- [Что использовано при разработке](#что-использовано-при-разработке)

## Деплой проекта

Устанавливаем необходимые пакеты в apt.

```
sudo apt-get update
```

```
sudo apt-get install nginx git supervisor gunicorn
```

### Установка базы данных

Устанавливаем Postgresql через apt-get

```
sudo apt-get install postgresql
```

Также нам надо установить драйвер для postgres вот этой командой:

```
pip3 install psycopg2-binary
```

Дальше входим в консоль postgres и выполняем следующие команды:

```
sudo -u postgres psql
CREATE DATABASE area51;
CREATE USER db_user_name WITH PASSWORD '12345';
ALTER ROLE db_user_name SET client_encoding TO 'utf-8';
ALTER ROLE db_user_name SET default_transaction_isolation TO 'read committed';
ALTER ROLE db_user_name SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE area51 TO db_user_name;
\q
```

`db_user_name` - имя пользователя в базе данных;
`12345` - его пароль, который лучше выбрать посильнее, чем этот;
`area51` - имя базы данных.

Запускаем postgres:

```
sudo service postgresql start
```

### Виртуальное окружение Python

Будем считать, что уже склонирован репозиторий, создано виртуальное окружение командой `python3 -m venv venv` и активировано командой `source venv/bin/activate`.

Сначала нужно установить python-пакеты. Примерно так:

```
pip3 install -r requirements.txt
```

Далее нам стоит подключить настройки в `settings.py`. Тут два варианта развития событий.

### Локальные настройки

Эти настройки используем, если работаем над проектом на своей машине. На прод это лучше не грузить.

В той же директории с файлом `settings.py` создаём новый файл с именем `local_settings.py`. Содержимое файла примерно следующее:

```
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-...'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
```

`SECRET_KEY` пренебрегать не советую. Хоть и работаем на localhost, правила безопасности никто не отменял.

### Настройки для деплоя

А эти настройки уже грузим на прод. Файл будет называться `prod_settings.py` и иметь такое содержание:

```
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '...'

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'user_name',
        'PASSWORD': 'pass',
        'HOST': 'localhost',
        'PORT': '5434',
    }
}

#STATIC_DIR = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Данные, разумеется, указываем свои. Генерируем `SECRET_KEY` (чем длиннее, тем лучше). Там где `ALLOWED_HOSTS` выставляем либо имя своего домена, либо IP-шник. В `DATABASES` указываем учётные данные для своей базы. СУБД используется PostgreSQL.

### Миграция БД

Выполним миграцию БД следующим образом:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

### Запуск сервера gunicorn

Запускаем из папки с проектом через эту команду:

```
gunicorn --bind 127.0.0.1:8000 area51.wsgi
```

Только ip-шник свой указываем.

Может не запуститься. Решил это, установив django в глобальное окружение.

### Настройка nginx

Конфиг находится здесь: `/etc/nginx/sites-available/default`. Содержимое:

```
server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name 192.168.43.23; # меняем потом на домен

        location /static/ {
                root /home/sickmyduck/blogg;
                expires 30d;
        }

        location /media/ {
                root /home/sickmyduck/blogg;
                expires 30d;
        }

        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                }
}
```

Перезапускаем nginx:

```
sudo systemctl restart nginx
```

### Supervisor

```
cd /etc/supervisor/conf.d/
sudo ln /home/l1ghth4t/blogg/config/area51.conf

sudo update-rc.d supervisor enable
sudo service supervisor start
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status project
sudo supervisorctl restart project
```

### Подключаем SSL-сертификат

Выключаем сервер:

```
sudo systemctl stop nginx
```

Нам надо два файла в директории `/etc/ssl`: `domain.crt` и `domain.key`. Закидываем их туда и прописываем новый конфиг для nginx:

```
server {
        listen 80;
        server_name area51-lab.ru;

        return 301 https://www.area51-lab.ru$request_uri;
}

server {
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;

        # include snippets/snakeoil.conf; # Заглушка

        ssl_certificate /etc/ssl/area51.crt;
        ssl_certificate_key /etc/ssl/area51.key;

        server_name area51-lab.ru www.area51-lab.ru;

        location /static/ {
                root /home/l1ghth4t/blogg;
                expires 30d;
        }

        location /media/ {
                root /home/l1ghth4t/blogg;
                expires 30d;
        }

        location / {
                proxy_pass http://127.0.0.1:8000;
                proxy_set_header Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```

И заново запускаем сервер:

```
sudo systemctl start nginx
```

## Действия после деплоя

После выполненных действий мы получим пустой сайт. Нужно его заполнить данными в админке. Вот краткое пояснение, что там вообще к чему.

### Создаём суперпользователя в админке

```
python3 manage.py createsuperuser
```

Вводим данные, которые у нас запрашивают.

## Что использовано при разработке

- для frontend использовался фреймворк `Neumorphism`;

- прикольная хрень на главной странице: `vanta.js`;

- анимация: `animate.css` + `wow.js`;

- не обошлось дело без `jquery.js`;

- highlight для картинок: `lightbox`;

- иконки взял отсюда: `flaticon.com`;

- для backend использовался python-фреймворк `Django`;

- В качестве WYSIWYG-редактора в админку django был интегрирован `CKEditor`.

> Un artista copia, un gran artista roba (Pablo Picasso).
