# Минимальная запускаемая основа

## Запуск

```bash
cp .env.example .env
docker compose up --build
```

## Проверка

```bash
curl http://localhost:8000/health
```

Ожидаемый ответ:

```json
{"status":"ok","database":"ok"}
```

Swagger UI: `http://localhost:8000/docs`.
