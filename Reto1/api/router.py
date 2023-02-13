# FastAPI
from fastapi import APIRouter, status
from api.schemas import CentralSchema
from api.black_board import board
from api.task import process

router = APIRouter()
response_model = {
    400: {"description": "Bad request, something went wrong"},
    401: {"description": "Unauthorized, missing or invalid token"},
    403: {"description": "Forbidden, missing or invalid token"},
    404: {"description": "Not found, the resource does not exist"},
    500: {"description": "Internal server error, something went wrong"},
}

@router.post("/central", status_code=status.HTTP_200_OK, responses=response_model)
def central(request: CentralSchema) -> dict:
    """
    Central API endpoint
    """
    response = process(board, request)
    return response
