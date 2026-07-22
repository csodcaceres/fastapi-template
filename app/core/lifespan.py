from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI

from app.core.logging import configure_logging

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

    # Startup code
    yield
    # Shutdown code

    logger.info("Application stopped")