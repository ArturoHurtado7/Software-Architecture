# FastAPI
from fastapi import APIRouter, status
from api.schemas import CentralSchema
from api.params import params
from api.task import Task
from time import time

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
    start_time = time()
    task = Task(params, request, start_time)
    task.priority()
    return {"message": "Task in execution"}
