# Chapter 2
# Lazy and eager evaluation

from collections.abc import Iterator


def numbers(stop: int) -> Iterator[int]:
    for i in range(stop):
        print(f"{i=}")
        yield i


def sum_to(limit: int) -> int:
    sum: int = 0
    for i in numbers(1024):
        if i == limit:
            break
        sum += i
    return sum
