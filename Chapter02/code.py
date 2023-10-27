# Chapter 2
# Lazy and eager evaluation

from collections.abc import Iterator
import math


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


def isPrime(n: int) -> bool:
    """
    Check if n is a prime number
    prime(𝑛)=∀𝑥[2≤𝑥<√𝑛+1∧𝑛≢0 mod𝑥]
    """
    return not any(n % p == 0 for p in range(2, int(math.sqrt(n)) + 1))


def isprimer(n: int) -> bool:
    def iscoprime(k: int, a: int, b: int) -> bool:
        """
        Is k coprime with a value in the given range?
        """
        if a == b:
            return True
        return (k % a != 0) and iscoprime(k, a + 1, b)

    return iscoprime(n, 2, int(math.sqrt(n)) + 1)


def isprimer2(n: int) -> bool:
    def iscoprime(k: int, a: int, b: int) -> bool:
        """
        Is k coprime with a value in the given range.
        Counting down.
        """
        if a == b:
            return True
        return (k % a != 0) and iscoprime(k, a, b - 1)

    return iscoprime(n, 3, int(math.sqrt(n)) + 1)
