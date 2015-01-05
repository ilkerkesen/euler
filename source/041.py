#!/usr/bin/env python
#-*- coding: utf-8 -*-

from math import sqrt
from itertools import permutations


def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    i = 3
    while i < sqrt(num) + 1:
        if num % i == 0:
            return False
        i += 2

    return True


def main():
    digits = range(10)[:0:-1]
    length = 9

    while length > 0:
        for perm in permutations(digits):
            number = int(''.join(str(i) for i in perm))
            
            if len(str(number)) < length:
                break

            if is_prime(number):
                print number
                exit(0)

        length -= 1
        digits = digits[1:]


if __name__ == "__main__":
    main()
