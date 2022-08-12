__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number in [0, 1]:
        return False

    for d in range(2, int(number ** (1/2) + 1)):
        if number % d == 0:
            return False

    return True
