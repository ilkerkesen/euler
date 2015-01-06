#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import count

LIMIT = 1000


def is_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True
    
    if num % 2 == 0:
        return False

    for i in range(3, int(sqrt(num)+1), 2):
        if num % i == 0:
            return False
    return True


def main():
    cs = range(-LIMIT, LIMIT+1)
    max_primes = 0

    for a in cs:
        for b in cs:
            primes = 0
            for n in count(0):
                num = n**2 + a * n + b
                if not is_prime(num):
                    break
                primes += 1
            if primes > max_primes:
                max_primes = primes
                product = a * b
    
    print product

if __name__ == "__main__":
    main()
