from pydantic import BaseModel


class PrimeNumberDto(BaseModel):
    number: int = 0
    is_prime_number: bool = False
