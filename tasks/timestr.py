__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    result: str = ""
    d: int = seconds // 86400
    result += f"{d:02}d" * (d > 0)

    seconds -= d * 86400
    h: int = seconds // 3600
    result += f"{h:02}h" * (h > 0 or len(result) > 0)

    seconds -= h * 3600
    m: int = seconds // 60
    result += f"{m:02}m" * (m > 0 or len(result) > 0)

    seconds -= m * 60

    return result + f"{seconds:02}s"
