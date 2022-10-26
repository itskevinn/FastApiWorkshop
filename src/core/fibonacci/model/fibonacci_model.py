from pydantic.dataclasses import dataclass
import uuid


@dataclass
class FibonacciModel:
    id = uuid.uuid4()
    fibonacci_sequence = []
    number_terms = 0

    def __init__(self, number_terms: int):
        self.number_terms = number_terms

    def generate_fibonacci_sequence(self):
        count = 0
        previous_number, current_number = 0, 1
        if self.number_terms <= 0:
            return self.fibonacci_sequence.append(0)
        elif self.number_terms == 1:
            return self.fibonacci_sequence.append(previous_number)
        else:
            while count < self.number_terms:
                self.fibonacci_sequence.append(previous_number)
                result_sum_numbers = previous_number + current_number
                previous_number = current_number
                current_number = result_sum_numbers
                count += 1

    def get_last_value_to_sequence(self):
        self.generate_fibonacci_sequence()
        return self.fibonacci_sequence[-1]
