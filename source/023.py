#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import combinations_with_replacement

LIMIT = 28213


def is_abundant(num):
    divs = set([1])
    for i in range(2, int(sqrt(num)+1)):
        if num % i == 0:
            divs.add(i)
            divs.add(num/i)
    return sum(divs) > num


def main():
    numbers = set(range(1, LIMIT+1))
    abundants = filter(is_abundant, numbers)
    combinations = combinations_with_replacement(abundants, 2)

    for (a, b) in combinations:
        c = a + b
        if c in numbers:
            numbers.remove(c)

    print sum(numbers)


if __name__ == "__main__":
    main()
