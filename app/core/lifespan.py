from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.core.logging import configure_logging
from app.database.init_db import init_db


logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown events.

    Startup:
        - Initialize resources.
        - Verify external services.
        - Configure shared objects.

    Shutdown:
        - Close connections.
        - Release resources.
    """

    configure_logging()

    logger.info("Application started")

    init_db()

    yield

    logger.info("Application stopped")