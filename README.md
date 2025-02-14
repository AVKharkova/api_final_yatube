## Проект API для Yatube

Проект API для Yatube в рамках обучения в Яндекс Практикуме - это реализация REST API для социальной сети Yatube, позволяющее работать с постами, комментариями, подписками и группами.

### Информация о стеке технологий, которые использовались для реализации проекта

- Python 3.9
- Django
- Django REST Framework
- djoser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AVKharkova/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Спецификация API

После запуска проекта спецификация API доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

### Автор

[Anastasiya Kharkova](https://github.com/AVKharkova)
