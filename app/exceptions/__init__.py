
from fastapi import HTTPException


class BadRequestException(HTTPException):

    def __init__(self, message: str = "Bad Request Exception"):
        code = 400
        super().__init__(code, message)


class UnauthorizedException(HTTPException):

    def __init__(self, message: str = "Unauthorized Exception"):
        code = 401
        super().__init__(code, message)


class NotFoundException(HTTPException):

    def __init__(self, message: str = "NotFound Exception"):
        code = 404
        super().__init__(code, message)


class InternalServerErrorException(HTTPException):

    def __init__(self, message: str = "Internal Server Error Exception"):
        code = 500
        super().__init__(code, message)
