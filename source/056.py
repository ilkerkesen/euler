#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product


def main():
    ps = product(range(1, 100), repeat=2)
    max_digit_sum = 0

    for a, b in ps:
        digit_sum = reduce(lambda x, y: x+y, map(int, str(a**b)))
        if digit_sum > max_digit_sum:
            max_digit_sum = digit_sum

    print max_digit_sum


if __name__ == "__main__":
    main()
