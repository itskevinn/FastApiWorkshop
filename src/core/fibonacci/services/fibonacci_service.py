from src.core.fibonacci.model.fibonacci_model import FibonacciModel


def get_value_due_to_position(number: int) -> FibonacciModel:

    fibonacci_model = FibonacciModel(number)

    return fibonacci_model.get_last_value_to_sequence()

