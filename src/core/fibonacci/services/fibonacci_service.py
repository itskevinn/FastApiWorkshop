def get_value_due_to_position(number: int) -> int:
    number_init, end_number, sucesion = 1, 1, []
    for x in range(number):
        sucesion.append(number_init)
        sucesion.append(end_number)
        number_init = number_init + end_number
        end_number = number_init + end_number
    return sucesion[number]