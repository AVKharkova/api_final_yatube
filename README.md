# API для Yatube

![Python](https://img.shields.io/badge/Python-3.9-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-A30000?logo=django&logoColor=white)
![Djoser](https://img.shields.io/badge/Djoser-4B32C3)

API для соцсети Yatube. Классика блогинга — регистрируйся, пиши посты, комментируй других, подписывайся на авторов, ищи единомышленников по группам. Подходит для интеграции с мобильным приложением, чат-ботом или любым фронтендом.

## Быстрый старт

1. Клонируйте проект и перейдите в папку:
    ```bash
    git clone https://github.com/AVKharkova/api_final_yatube
    cd api_final_yatube
    ```
2. Создайте и активируйте виртуальное окружение:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Установите зависимости:
    ```bash
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Примените миграции:
    ```bash
    python3 manage.py migrate
    ```
5. Запустите сервер:
    ```bash
    python3 manage.py runserver
    ```
6. Документация API: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## Аутентификация

Используется JWT (через Djoser):

- Получить токен:  
  **POST** `/api/v1/jwt/create/`  
  ```json
  { "username": "your_login", "password": "your_password" }
  ```

* Обновить токен:
  **POST** `/api/v1/jwt/refresh/`

* Проверить токен:
  **POST** `/api/v1/jwt/verify/`

---
### Основные  запросы к API:

1. [Публикации](#1-публикации)
   - [1.1. Получение списка публикаций](#11-получение-списка-публикаций)
   - [1.2. Создание публикации](#12-создание-публикации)
   - [1.3. Получение публикации по ID](#13-получение-публикации-по-id)
   - [1.4. Обновление публикации](#14-обновление-публикации)
   - [1.5. Удаление публикации](#15-удаление-публикации)

2. [Комментарии](#2-комментарии)
   - [2.1. Получение списка комментариев](#21-получение-списка-комментариев)
   - [2.2. Добавление комментария](#22-добавление-комментария)
   - [2.3. Удаление комментария](#23-удаление-комментария)

3. [Сообщества](#3-сообщества)
   - [3.1. Получение списка сообществ](#31-получение-списка-сообществ)
   - [3.2. Получение информации о сообществе](#32-получение-информации-о-сообществе)

4. [Подписки](#4-подписки)
   - [4.1. Получение списка подписок](#41-получение-списка-подписок)
   - [4.2. Подписка на пользователя](#42-подписка-на-пользователя)

5. [Аутентификация](#5-аутентификация)
   - [5.1. Получение JWT-токена](#51-получение-jwt-токена)
   - [5.2. Обновление JWT-токена](#52-обновление-jwt-токена)
   - [5.3. Проверка JWT-токена](#53-проверка-jwt-токена)

Для работы с API требуется аутентификация через JWT-токен, который можно получить через соответствующий эндпоинт.

#### 1. Публикации

##### 1.1. Получение списка публикаций
**GET** `/api/v1/posts/`

**Описание:**  
Получение списка всех публикаций.  Поддерживает пагинацию через параметры `limit` и `offset`.

**GET** `/api/v1/posts/?limit=10&offset=20`

**Пример ответа:**
```json
{
  "count": 123,
  "next": "http://api.example.org/api/v1/posts/?offset=30&limit=10",
  "previous": "http://api.example.org/api/v1/posts/?offset=10&limit=10",
  "results": [
    {
      "id": 0,
      "author": "username",
      "text": "Текст публикации",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "http://example.com/image.jpg",
      "group": 1
    }
  ]
}
```

---

##### 1.2. Создание публикации
**POST** `/api/v1/posts/`

**Описание:**  
Добавление новой публикации. Анонимные запросы запрещены.

**Тело запроса:**
```json
{
  "text": "Текст новой публикации",
  "image": "http://example.com/image.jpg",
  "group": 1
}
```

**Пример ответа:**
```json
{
  "id": 1,
  "author": "username",
  "text": "Текст новой публикации",
  "pub_date": "2021-10-14T20:41:29.648Z",
  "image": "http://example.com/image.jpg",
  "group": 1
}
```

---

##### 1.3. Получение публикации по ID
**GET** `/api/v1/posts/{id}/`

**Описание:**  
Получение публикации по её идентификатору.

**Пример ответа:**
```json
{
  "id": 1,
  "author": "username",
  "text": "Текст публикации",
  "pub_date": "2021-10-14T20:41:29.648Z",
  "image": "http://example.com/image.jpg",
  "group": 1
}
```

---

##### 1.4. Обновление публикации
**PUT** `/api/v1/posts/{id}/`

**Описание:**  
Обновление публикации по её идентификатору. Только автор публикации может её обновить.

**Тело запроса:**
```json
{
  "text": "Обновлённый текст публикации",
  "image": "http://example.com/new_image.jpg",
  "group": 2
}
```

**Пример ответа:**
```json
{
  "id": 1,
  "author": "username",
  "text": "Обновлённый текст публикации",
  "pub_date": "2021-10-14T20:41:29.648Z",
  "image": "http://example.com/new_image.jpg",
  "group": 2
}
```

---

##### 1.5. Удаление публикации
**DELETE** `/api/v1/posts/{id}/`

**Описание:**  
Удаление публикации по её идентификатору. Только автор публикации может её удалить.

**Ответ:**  
Статус `204 No Content`.

---

#### 2. Комментарии

##### 2.1. Получение списка комментариев
**GET** `/api/v1/posts/{post_id}/comments/`

**Описание:**  
Получение всех комментариев к публикации.

**Пример ответа:**
```json
[
  {
    "id": 1,
    "author": "username",
    "text": "Текст комментария",
    "created": "2021-10-14T20:41:29.648Z",
    "post": 1
  }
]
```

---

##### 2.2. Добавление комментария
**POST** `/api/v1/posts/{post_id}/comments/`

**Описание:**  
Добавление нового комментария к публикации. Анонимные запросы запрещены.

**Тело запроса:**
```json
{
  "text": "Текст нового комментария"
}
```

**Пример ответа:**
```json
{
  "id": 2,
  "author": "username",
  "text": "Текст нового комментария",
  "created": "2021-10-14T20:41:29.648Z",
  "post": 1
}
```

---

##### 2.3. Удаление комментария
**DELETE** `/api/v1/posts/{post_id}/comments/{id}/`

**Описание:**  
Удаление комментария по его идентификатору. Только автор комментария может его удалить.

**Ответ:**  
Статус `204 No Content`.

---

#### 3. Сообщества

##### 3.1. Получение списка сообществ
**GET** `/api/v1/groups/`

**Описание:**  
Получение списка всех доступных сообществ.

**Пример ответа:**
```json
[
  {
    "id": 1,
    "title": "Название сообщества",
    "slug": "community-slug",
    "description": "Описание сообщества"
  }
]
```

---

##### 3.2. Получение информации о сообществе
**GET** `/api/v1/groups/{id}/`

**Описание:**  
Получение информации о сообществе по его идентификатору.

**Пример ответа:**
```json
{
  "id": 1,
  "title": "Название сообщества",
  "slug": "community-slug",
  "description": "Описание сообщества"
}
```

---

#### 4. Подписки

##### 4.1. Получение списка подписок
**GET** `/api/v1/follow/`

**Описание:**  
Получение списка подписок пользователя. Анонимные запросы запрещены.

**Пример ответа:**
```json
[
  {
    "user": "username",
    "following": "following_username"
  }
]
```

---

##### 4.2. Подписка на пользователя
**POST** `/api/v1/follow/`

**Описание:**  
Подписка на пользователя. Анонимные запросы запрещены.

**Тело запроса:**
```json
{
  "following": "username_to_follow"
}
```

**Пример ответа:**
```json
{
  "user": "username",
  "following": "username_to_follow"
}
```

---

#### 5. Аутентификация

##### 5.1. Получение JWT-токена
**POST** `/api/v1/jwt/create/`

**Описание:**  
Получение JWT-токена для аутентификации.

**Тело запроса:**
```json
{
  "username": "username",
  "password": "password"
}
```

**Пример ответа:**
```json
{
  "refresh": "refresh_token",
  "access": "access_token"
}
```

---

##### 5.2. Обновление JWT-токена
**POST** `/api/v1/jwt/refresh/`

**Описание:**  
Обновление JWT-токена.

**Тело запроса:**
```json
{
  "refresh": "refresh_token"
}
```

**Пример ответа:**
```json
{
  "access": "new_access_token"
}
```

---

##### 5.3. Проверка JWT-токена
**POST** `/api/v1/jwt/verify/`

**Описание:**  
Проверка валидности JWT-токена.

**Тело запроса:**
```json
{
  "token": "access_token"
}
```

**Ответ:**  
Статус `200 OK`, если токен валиден.

---

### Технологический стек

- Python
- Django
- Django REST Framework
- Djoser

---

### Автор

[Anastasiya Kharkova](https://github.com/AVKharkova)
