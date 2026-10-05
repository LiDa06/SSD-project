from fastapi import FastAPI, HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

from app.config import get_settings
from app.db import check_database

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Минимальная запускаемая основа сервиса заказов «Утиные истории».",
)


@app.get("/", tags=["service"])
def root() -> dict[str, str]:
    return {
        "service": settings.app_name,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["service"])
def health() -> dict[str, str]:
    """Confirm that both the API process and PostgreSQL are reachable."""

    try:
        check_database()
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="database unavailable",
        ) from exc

    return {"status": "ok", "database": "ok"}
