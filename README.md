# News Portal — Django + DRF + JWT API

## 📌 Описание проекта

Это веб-приложение новостного портала, разработанное на Django с использованием Django REST Framework.
Проект поддерживает:

* регистрацию и авторизацию пользователей (JWT)
* создание, редактирование и удаление новостей
* персонализацию новостей по автору
* REST API для работы с данными
* клиентский Python-модуль для тестирования API

---

## ⚙️ Используемые технологии

* Python 3.11+
* Django 6
* Django REST Framework
* SimpleJWT (JWT Authentication)
* django-filter
* requests

---

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <your-repo-url>
cd news_portal3
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Выполнить миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Создать суперпользователя

```bash
python manage.py createsuperuser
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

---

## 🌐 Основные страницы

* `/` — главная страница (список новостей)
* `/news/<id>/` — детальная новость
* `/news/add/` — добавление новости
* `/login/` — вход
* `/register/` — регистрация
* `/profile/` — профиль пользователя

---

## 📡 REST API

### 🔹 Новости

* `GET /api/news/` — список новостей
* `POST /api/news/` — создать новость (требуется JWT)
* `GET /api/news/<id>/` — получить новость
* `PATCH /api/news/<id>/` — обновить новость (владелец)
* `DELETE /api/news/<id>/` — удалить новость (владелец)

### 🔹 Фильтрация

```
/api/news/?author=1
```

### 🔹 Пагинация

По умолчанию: 10 записей на страницу

---

## 🔐 Аутентификация (JWT)

### Получение токена:

```
POST /api/token/
```

```json
{
  "username": "admin",
  "password": "123456"
}
```

### Ответ:

```json
{
  "access": "...",
  "refresh": "..."
}
```

### Использование:

```
Authorization: Bearer <access_token>
```

---

## 🤖 API Client (requests)

Файл: `api_client/client.py`

Возможности:

* автоматический login
* получение токена
* создание новостей
* обновление и удаление
* тестирование API

### Запуск:

```bash
python api_client/client.py
```

---

## 📁 Структура проекта

```
news_portal3/
│
├── news_app3/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── viewsets.py
│   ├── urls.py
│   └── api_urls.py
│
├── api_client/
│   └── client.py
│
├── config/
│   └── settings.py
│
└── manage.py
```

---

## 🧠 Авторизация логики

* Гости могут только читать новости
* Авторизованные пользователи могут создавать новости
* Редактировать и удалять можно только свои новости

---

## ✅ Статус проекта

✔ Django backend
✔ REST API
✔ JWT authentication
✔ Client module
✔ Filtering + pagination
✔ CRUD система

---

## 📌 Автор

Учебный проект: News Portal (Django + DRF)
