# Notes Project - Django REST API

> **Проект системы управления заметками на Django REST Framework**

Полнофункциональное API для создания, чтения, обновления и удаления заметок с архитектурой "клиент-сервер".

**Backend:**
- Django 5.2
- Django REST Framework
- PostgreSQL / SQLite (настраиваемо)
- Python-decouple (управление настройками)
- CORS Headers (для фронтенда)
- Django Filters (фильтрация данных)

**Инструменты разработки:**
- Logging (отладка и мониторинг)
- Django Admin (управление данными)
- Python-decouple (конфигурация)

## Возможности

- RESTful API endpoints
- Поддержка PostgreSQL и SQLite
- CORS-совместимость для фронтенда
- Валидация данных
- Логирование операций
- Админ-панель Django
- Гибкая конфигурация

## API Endpoints

```
GET    /api/v1/notes/          # Список заметок
POST   /api/v1/notes/          # Создание заметки
GET    /api/v1/notes/{id}/     # Детали заметки
PUT    /api/v1/notes/{id}/     # Обновление заметки
DELETE /api/v1/notes/{id}/     # Удаление заметки
```

**Автор:** Бирлик Жумадил  
**Назначение:** Pet-проект для стажировки / портфолио
