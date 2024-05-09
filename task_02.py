import re
from collections.abc import Callable


def generator_numbers(text: str):
    pattern = r'-?\d+\.\d+'
    floats = re.finditer(pattern, text)
    for numbers in floats:
        yield float(numbers.group())


def sum_profit(text: str, func: Callable):
    money = 0
    for number in func(text):
        money += number
    return money
