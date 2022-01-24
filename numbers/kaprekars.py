from functools import reduce
from typing import Sequence

KAPREKAR_NUMBER = 6174


def K(n: int) -> int:
    if n < 1001: raise ValueError("the number cannot be less than 1 001")
    if n > 9999: raise ValueError("the number must be less than 10 000")
    if is_repdigit(n): raise ValueError("the number cannot be repdigit")
    
    n = lst_to_num(list(sorted(decompose(n), reverse=True)))
    m = reverse(n)
    x = n - m
    
    print(f"{n:<6} - {m:<6} = {x:<6}")
    
    return x


def reverse(n: int) -> int:
    if n < 0: raise ValueError("number must be non-negative")
    return lst_to_num(decompose(n))


def lst_to_num(s: Sequence[int]) -> int:
    return sum(e * 10 ** (len(s) - i - 1) for i, e in enumerate(s))


def is_repdigit(n: int) -> bool:
    return bool(reduce(lambda x, y: x * (x == y), decompose(n)))


def decompose(n: int) -> list[int]:
    s = []
    
    while n:
        n, a = divmod(n, 10)
        s.append(a)
    
    return s


def main():
    n = int(input("Number: "))
    
    while n != KAPREKAR_NUMBER:
        n = K(n)


if __name__ == '__main__':
    main()
