#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product


def digit_sum(number):
    return reduce(lambda x, y: x+y, map(int, str(number)))


def main():
    ps = product(range(1, 100), repeat=2)
    max_sum = 0

    for a, b in ps:
        c = digit_sum(a**b)
        if c > max_sum:
            max_sum = c

    print max_sum


if __name__ == "__main__":
    main()
