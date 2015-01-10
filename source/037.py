#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import permutations, product, count, chain


def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


def is_truncatable_prime(n):
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:i])):
            return False

        if not is_prime(int(str(n)[-i:])):
            return False
    return is_prime(n)


def main():
    digits = (1, 3, 7, 9)
    result = 23 + 37 + 53 + 73
    fls = ((2, 3), (2, 7), (3, 3), (3, 7), (7, 3), (7, 7))
    total = 4

    for i in count(1):
        for p in product(digits, repeat=i):
            for (f, l) in fls:
                num = int(''.join(str(d) for d in (f,) + p + (l,)))
                if is_truncatable_prime(num):
                    total += 1
                    result += num
                    if total == 11:
                        print result
                        exit(0)


if __name__ == "__main__":
    main()

