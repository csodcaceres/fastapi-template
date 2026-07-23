from fastapi import status


class AppException(Exception):
    """
    Base exception for the application.
    """

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail: str = "Internal server error"

    def __init__(self, detail: str | None = None):
        if detail is not None:
            self.detail = detail


class NotFoundException(AppException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Resource not found"


class ConflictException(AppException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Resource already exists"


class UnauthorizedException(AppException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Unauthorized"


class ForbiddenException(AppException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Forbidden"
