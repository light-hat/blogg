# Area 51

> Un artista copia, un gran artista roba (Pablo Picasso).

Мой блог про инфобез. Зачем, а главное зачем этот сайт создан?

- в образовательных целях, чтобы фиксировать результаты самообразования;

- как приложение к портфолио;

- ~~ну и просто чтобы выпендриться.~~

## Что осталось в проекте реализовать?

0. Дорабоать страницы с ошибками 400* и 500*.

1. Fail2ban для админки. Ну или что-то другое, но чтобы контролировать попытки входа в неё.

2. Блокировку IP-адресов.

3. Вытекает из 2. Сделать систему, которая отслеживала бы попытки фаззинга, ddos, сканирование портов и прочие непотребства со стороны пользователя и в автоматическом режиме блокировала бы их ip-шники.

4. Довести до ума админку.

5. Добавить возможность комментирования статей.

6. Добавить dockerfile для проекта.

7. Можно ещё поставить пару honeypot'ов.

## Деплой проекта

Что использовал я:

- Debian 10

- Python <VERSION>

- Pip <VERSION>

- Nginx <VERSION>

### Установка зависимостей

Устанавливаем необходимые пакеты в apt.

```
sudo apt-get update
...
```

Устанавливаем пакеты в pip.

```
pip install ...
```

ДОПИСАТЬ

### Настройки проекта

Будем считать, что уже склонирован репозиторий, создано виртуальное окружение командой `python3 -m venv venv` и активировано командой `source venv/bin/activate`.

Первым делом стоит подключить настройки в `settings.py`. Тут два варианта развития событий.

#### Локальные настройки

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

#### Настройки для деплоя

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
        'PORT': '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

Данные, разумеется, указываем свои. Генерируем `SECRET_KEY` (чем длиннее, тем лучше). Там где `ALLOWED_HOSTS` выставляем либо имя своего домена, либо IP-шник. В `DATABASES` указываем учётные данные для своей базы. СУБД используется PostgreSQL.

### Миграции БД

Выполним миграцию БД следующим образом:

```
python3 manage.py makemigrations
```

```
python3 manage.py migrate
```

Допишу потом...

## Действия после деплоя

После выполненных действий мы получим пустой сайт. Нужно его заполнить данными в админке. Вот краткое пояснение, что там вообще к чему.

Допишу потом...

## Что использовано при разработке

- для frontend использовался фреймворк `Neumorphism`;

- прикольная хрень на главной странице: `vanta.js`;

- анимация: `animate.css` + `wow.js`;

- не обошлось дело без `jquery.js`;

- highlight для картинок: `lightbox`;

- иконки взял отсюда: `flaticon.com`;

- для backend использовался python-фреймворк `Django`;

- В качестве WYSIWYG-редактора в админку django был интегрирован `CKEditor`.