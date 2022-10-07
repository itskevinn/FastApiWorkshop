from typing import List

from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.core.hello_world.services import hello_world_service


router = APIRouter()


@router.get("/",
            response_class=JSONResponse,
            status_code=201,
            responses={201: {"description": "Just chilling"}},
            )
def welcome_to_fast_api():
    """Welcome you to our API
    :return: return hello fastAPi
    """
    return hello_world_service.welcome_to_fast_api()
