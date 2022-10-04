from core.base.auditable_model import AuditableBaseModel


class PrimeNumber(AuditableBaseModel):
    number: int | None = 0
    is_prime_number: bool | None = False

    def calculate_is_prime_number(self):
        for x in range(2, int(self.number / 2)):
            return self.number % x == 0
