from core.base.auditable_model import AuditableBaseModel


class PrimeNumber(AuditableBaseModel):
    number: int | None = 0
    is_prime_number: bool | None = False

    def calculate_is_prime_number(self):
        number = self.number
        for x in range(2, int(number / 2)):
            return number % x == 0
