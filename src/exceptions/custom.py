from fastapi import HTTPException

class BadRequestException(HTTPException):
    def __init__(self, route: str):
        super().__init__(status_code=400, detail=f"invalid {route}")
class AlreadyExistsException(HTTPException):
    def __init__(self, route: str):
        super().__init__(status_code=400, detail=f"this {route} already exists")
class NotFoundException(HTTPException):
    def __init__(self, route: str):
        super().__init__(status_code=404, detail=f"{route} not found")