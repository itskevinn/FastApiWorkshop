def calculate(number: int) -> bool:
    """
    -
    :param number: The number to calculate if is prime number
    :return: The created prime number
    """
    is_prime = calculate_is_prime_number(number)
    return is_prime


def calculate_is_prime_number(n: int) -> bool:
    """
    -
    :param n: The number to calculate if is prime number
    :return: True if the number is a prime number and false otherwise
    """
    for i in range(2, n):
        return (n % i) != 0
