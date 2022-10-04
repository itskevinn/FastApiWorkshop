from datetime import datetime
from typing import Iterable

from core.prime_numbers.entities.prime_number import PrimeNumber
from core.prime_numbers.entities.dtos.prime_number_dto import PrimeNumberDto

registered_prime_numbers = set()
test_prime_number = PrimeNumber.parse_obj(
    {"number": 3, "is_prime_number": True, "id": 1, "creation_date": datetime.now()})


def fetch_all() -> Iterable[PrimeNumber]:
    """
    Fetch all prime numbers registered previously
    :return: The list of prime numbers
    """
    if registered_prime_numbers:
        registered_prime_numbers.add()
        return registered_prime_numbers


def persist(prime_number: PrimeNumberDto) -> PrimeNumber:
    """
    Saves the given PrimeNumberDto in the database.
    in this case, the value is stored in the registered_prime_numbers set
    :param prime_number: PrimeNumberDto
    :return: The new PrimeNumber
    """
    value_to_register = PrimeNumber.parse_obj(prime_number)
    registered_prime_numbers.add(value_to_register)
    return value_to_register
