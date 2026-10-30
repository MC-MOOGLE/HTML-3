# movies_api

Мини backend на FastAPI для хранения фильмов: название, год выхода, рейтинг.

## Возможности

- CRUD для фильмов (создание, просмотр, полное и частичное обновление, удаление)
- Фильтрация списка по году и рейтингу
- Сортировка и пагинация
- Автотесты фильтров на тестовой БД

## Стек

- Python 3.12+
- FastAPI + Uvicorn
- SQLAlchemy 2 (async) + aiosqlite
- SQLite
- Pydantic
- pytest + httpx

## Структура проекта

```
movies_api/
├── src/
│   ├── models/
│   │   └── movie.py          # модель Movie
│   ├── schemas/
│   │   └── movie.py          # схемы
│   ├── repositories/
│   │   └── movies.py         # запросы к БД
│   ├── routers/
│   │   └── movies.py         # эндпоинты /movies
│   ├── database.py           # подключение к БД, сессии
│   ├── seed.py               # тестовые данные
│   └── main.py
├── tests/
│   ├── conftest.py         
│   └── test_movies.py      
├── pytest.ini
├── requirements.txt
└── README.md
```

## Быстрый старт

```
git clone <url-репозитория> movies_api
cd movies_api

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

uvicorn src.main:app --reload
```

Миграции: отдельного инструмента нет, таблицы создаются автоматически при запуске приложения (`Base.metadata.create_all`). Заполнить БД тестовыми фильмами:

```
python -m src.seed
```

- API: http://127.0.0.1:8000
- Swagger: http://127.0.0.1:8000/docs
- Тесты: `pytest`

## Эндпоинты

| Метод  | Путь               | Описание                    |
|--------|--------------------|-----------------------------|
| GET    | `/movies/`         | Список фильмов (с фильтрами) |
| GET    | `/movies/{id}`     | Фильм по id                 |
| POST   | `/movies/`         | Создать фильм               |
| PUT    | `/movies/{id}`     | Полностью обновить фильм    |
| PATCH  | `/movies/{id}`     | Частично обновить фильм     |
| DELETE | `/movies/{id}`     | Удалить фильм               |

Если фильма нет, возвращается `404`.

## Фильтрация и сортировка

Параметры запроса `GET /movies/`:

| Параметр     | Пример          | Значение                          |
|--------------|-----------------|-----------------------------------|
| `year_min`   | `2000`          | год ≥ значения                    |
| `year_max`   | `2015`          | год ≤ значения                    |
| `min_rating` | `8.0`           | рейтинг ≥ значения                |
| `order_by`   | `-rating`       | сортировка (по умолчанию `-rating`) |
| `limit`      | `10`            | 1–100, по умолчанию 50            |
| `offset`     | `0`             | сдвиг, по умолчанию 0             |

`order_by`: `id`, `title`, `year`, `rating`. Минус перед полем - по убыванию (`-year`). Неизвестное значение заменяется на `-rating`.

Пример: `GET /movies/?year_min=2000&min_rating=8&order_by=-year`

## Модель данных

Таблица `movies`:

| Поле     | Тип          | Описание                |
|----------|--------------|-------------------------|
| `id`     | integer      | первичный ключ          |
| `title`  | varchar(200) | название                |
| `year`   | integer      | год выхода              |
| `rating` | float        | рейтинг, по умолчанию 0 |

## Ограничения БД

- `id` - первичный ключ, автоинкремент
- `title`, `year`, `rating` - `NOT NULL`
- `title` - не длиннее 200 символов

Дополнительно на уровне API (Pydantic), при нарушении возвращается `422`:

- `title` - от 1 до 200 символов
- `year` - от 1888 до 2100
- `rating` - от 0 до 10
