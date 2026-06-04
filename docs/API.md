# API Documentation

## Base URL
http://127.0.0.1:8000/api/

---

## AUTH (JWT)

POST /api/token/

{
  "username": "admin",
  "password": "Dimamiller2005"
}

Response:
{
  "access": "token",
  "refresh": "token"
}

---

## NEWS API

GET /api/news/        - список новостей
POST /api/news/       - создать новость
GET /api/news/<id>/   - одна новость
PATCH /api/news/<id>/ - обновить
DELETE /api/news/<id>/ - удалить

---

## FILTER

GET /api/news/?author=1

---

## PAGINATION

10 news per page