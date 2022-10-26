
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from src.core.prime_numbers.services import prime_number_service

router = APIRouter()


@router.get(
    "/{number}",
    response_class=JSONResponse,
    status_code=201,
    responses={201: {"description": "Calculated"}},
)
def calculate(
        number: int
):
    """Calculates if the number is a prime number
    :param number: The number to check
    :return: True if the number is a prime number, False otherwise
    """
    return prime_number_service.calculate(number)

