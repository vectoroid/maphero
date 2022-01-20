"""
@SpotsAPI

API Exceptions
"""
import fastapi
import typing


class BadRequestHTTPException(fastapi.exceptions.HTTPException):
    def __init__(self, msg: str="Bad Request") -> None:
        super().__init__(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            detail=msg 
        )

# API bespoke exceptions
class UnprocessableEntityException(fastapi.HTTPException):
    """
    UnprocessableEntityException
    """
    def __init__(
            self, 
            msg: typing.Optional[str]="The entity could not be processed.",
            status: int = fastapi.status.HTTP_422_UNPROCESSABLE_ENTITY
        ) -> None:
        super().__init__(status_code=status, detail=msg)
        

class ForbiddenHTTPException(fastapi.HTTPException):
    def __init__(self, msg: typing.Optional[str]="You are not authorized to access your requested resource."):
        super().__init__(
            status_code=fastapi.status.HTTP_403_FORBIDDEN,
            detail=msg 
        )
        

class NotFoundHTTPException(fastapi.HTTPException):
    def __init__(self, msg: typing.Optional[str]="The resource you requested could not be located.")
        super().__init__(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=msg
            )
    