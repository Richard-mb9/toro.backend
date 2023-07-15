from http import HTTPStatus
from fastapi import HTTPException


class APIError(Exception):
    """Api Error"""

    def __init__(self, status_code, message) -> None:
        super().__init__()
        raise HTTPException(detail={"error": message}, status_code=status_code)


class BadRequestError(APIError):
    """Class Bad Request Error"""

    def __init__(self, message):
        super().__init__(HTTPStatus.BAD_REQUEST, message)


class ConflictError(APIError):
    """Class Conflict Error"""

    def __init__(self, message):
        super().__init__(HTTPStatus.CONFLICT, message)


class NotFoundError(APIError):
    """Class Not Found Error"""

    def __init__(self, message):
        super().__init__(HTTPStatus.NOT_FOUND, message)


class AccessDeniedError(APIError):
    """Access denied error"""

    def __init__(self, message="Access denied"):
        super().__init__(HTTPStatus.FORBIDDEN, message)


class UnauthorizedError(APIError):
    """Unauthorized error"""

    def __init__(self, message):
        super().__init__(HTTPStatus.UNAUTHORIZED, message)


class UnprocessableEntity(APIError):
    """Unauthorized error"""

    def __init__(self, message):
        super().__init__(HTTPStatus.UNPROCESSABLE_ENTITY, message)
