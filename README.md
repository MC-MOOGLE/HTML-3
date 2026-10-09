# movies_api

Мини backend для хранения фильмов (FastAPI + SQLAlchemy + SQLite).

## Запуск

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

Документация: http://127.0.0.1:8000/docs

## Тесты

```
pytest
```
