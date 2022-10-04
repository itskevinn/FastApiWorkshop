from typing import List

from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from api.container import get_dependencies
from core.prime_numbers.entities.prime_number import PrimeNumber
from core.prime_numbers.services import prime_number_service

repo = get_dependencies().prime_repo
router = APIRouter()


@router.post(
    "",
    response_class=JSONResponse,
    response_model=PrimeNumber,
    status_code=201,
    responses={201: {"description": "Calculated"}},
)
def create(
        number: int
):
    """Calculates if the number is a prime number
    :param number: The number to check
    :return: True if the number is a prime number, False otherwise
    """
    return prime_number_service.create(repo, number)


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[PrimeNumber],
    status_code=200,
    responses={
        200: {"description": "Items found"},
    },
)
def get_all():
    """Gets all prime numbers
    :return: List of prime numbers
    """
    return prime_number_service.get_all(repo)
