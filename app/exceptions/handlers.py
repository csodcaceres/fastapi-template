from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from app.exceptions.exceptions import AppException

async def http_exception_handler(
        request: Request, 
        exc: HTTPException
    ) -> JSONResponse:
        """
        Handle HTTP exceptions and return a JSON response.
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail
            },
        )

async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        """
        Handles request validation errors from Pydantic.
        """
        return JSONResponse(
            status_code=422,
            content={
                "detail": "Validation error",
                "errors": exc.errors(),
            },
    )

async def app_exception_handler(
        request: Request,
        exc: AppException,
    ) -> JSONResponse:
        """
        Handles application exceptions.
        """
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "detail": exc.detail,
            },
    )