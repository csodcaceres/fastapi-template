from app.database.base import Base
from app.database.session import engine

from app.database import models


def init_db() -> None:
    """
    Initialize database tables.
    """

    Base.metadata.create_all(
        bind=engine
    )