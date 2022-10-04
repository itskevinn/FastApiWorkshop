from typing import Iterable, Protocol

from core.prime_numbers.entities.prime_number import PrimeNumber
from core.prime_numbers.entities.dtos.prime_number_dto import PrimeNumberDto


class PrimeNumberRepo(Protocol):
    def fetch_all(self) -> Iterable[PrimeNumber]:
        ...

    def persist(self, dto: PrimeNumberDto) -> PrimeNumber:
        ...
