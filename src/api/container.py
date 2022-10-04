from dataclasses import dataclass
from typing import Callable, cast

from core.prime_numbers.protocols.prime_number_repo import PrimeNumberRepo
from infra.database.repositories import prime_number_repository


@dataclass(frozen=True)
class Dependencies:
    prime_repo: PrimeNumberRepo


def _build_dependencies() -> Callable[[], Dependencies]:
    deps = Dependencies(
        prime_repo=cast(PrimeNumberRepo, prime_number_repository),
    )

    def fn() -> Dependencies:
        return deps

    return fn


get_dependencies = _build_dependencies()
