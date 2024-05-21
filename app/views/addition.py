from fastapi import APIRouter
from app.models.request import AdditionRequest
from app.models.response import AdditionResponse
from app.controllers.addition_controller import process_addition

router = APIRouter()

@router.post("/addition", response_model=AdditionResponse)
async def addition_endpoint(request: AdditionRequest):
    return process_addition(request)
