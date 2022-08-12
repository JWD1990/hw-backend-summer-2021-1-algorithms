from asyncio import SendfileNotAvailableError
from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    string: str = ''
    min_len_str: str = ''
    max_len_str: str = ''
    last_idx: int = len(text) - 1

    def replace_strings(s: str) -> None:
        nonlocal min_len_str, max_len_str

        if not len(min_len_str) or len(min_len_str) and len(min_len_str) > len(s):
            min_len_str = s

        if len(max_len_str) < len(s):
            max_len_str = s

    for idx, ch in enumerate(text):
        if ch.isspace():
            replace_strings(string)
            string = ''
        else:
            string += ch

            if idx != last_idx:
                continue

            replace_strings(string)

    return min_len_str if len(min_len_str) else None, max_len_str if len(max_len_str) else None
