#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import count


def triangle(n):
    return n * (n + 1) / 2


def get_root(a, b, c):
    return (-b + sqrt(b**2 - 4*a*c)) / (2*a)


def is_pentagonal(n):
    root = get_root(3, -1, -2*n)
    return root == int(root)


def is_hexagonal(n):
    root = get_root(2, -1, -n)
    return root == int(root)


def main():
    for i in count(286):
        num = triangle(i)
        if is_pentagonal(num) and is_hexagonal(num):
            break
    print num

if __name__ == "__main__":
    main()
