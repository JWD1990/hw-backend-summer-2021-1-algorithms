__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    even: int = 0
    odd: int = 0

    for num in arr:
        if num % 2 == 0:
            even += num
        else:
            odd += num

    if odd == 0:
        return 0

    return even / odd
