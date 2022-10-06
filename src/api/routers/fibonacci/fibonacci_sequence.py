from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from core.fibonacci.services import fibonacci_service

router = APIRouter()


@router.get(
    "/{number}",
    response_class=JSONResponse,
    status_code=201,
    responses={201: {"description": "Calculated"}},
)
def create(
        number: int
):
    """Return the number due to position
    :param number: Position number
    :return: the number due to position
    """
    return fibonacci_service.get_value_due_to_position(number)
