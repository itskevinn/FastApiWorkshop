from typing import Iterable

from core.prime_numbers.entities.prime_number import PrimeNumber
from core.prime_numbers.entities.dtos.prime_number_dto import PrimeNumberDto
from core.prime_numbers.protocols.prime_number_repo import PrimeNumberRepo


def create(repo: PrimeNumberRepo, number: int) -> bool:
    """
    -
    :param repo: The prime number repository
    :param number: The number to calculate if is prime number
    :return: The created prime number
    """
    prime_number = PrimeNumberDto
    prime_number.number = number
    is_prime = prime_number.is_prime_number

    if is_prime:
        repo.persist(PrimeNumberDto.parse_obj(prime_number))
    return is_prime


def get_all(repo: PrimeNumberRepo) -> Iterable[PrimeNumber]:
    """
    -
    :param repo: The prime number repository
    :return: The list of prime numbers
    """
    return repo.fetch_all()
