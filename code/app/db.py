from functools import lru_cache

from sqlalchemy import Engine, create_engine, text

from app.config import get_settings


@lru_cache
def get_engine() -> Engine:
    """Create one SQLAlchemy engine for the process."""

    settings = get_settings()
    return create_engine(settings.database_url, pool_pre_ping=True)


def check_database() -> None:
    """Raise an SQLAlchemy exception when the database is unavailable."""

    with get_engine().connect() as connection:
        connection.execute(text("SELECT 1"))
