#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import hypot
from itertools import count

LIMIT = 1000


def is_pythagorean(a, b, c):
    return hypot(a, b) == c


def triangles(p):
    res = 0
    for a in range(1, p/3):
        b = (p**2 - 2*p*a) / (2*p - 2*a)
        c = p - a - b
        if is_pythagorean(a, b, c):
            res += 1
    return res


def find_max_solution(limit):
    return reduce(
        lambda x, y: x if x[1] > y[1] else y,
        zip(range(1, limit+1), map(triangles, range(1, limit+1))), (0, 0))[0]


def main():
    print find_max_solution(LIMIT)


if __name__ == "__main__":
    main()
