#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt
from itertools import permutations
from itertools import combinations_with_replacement

LIMIT = 1000000


def from_list_to_int(digits):
    return int(''.join([str(d) for d in digits]))


def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(sqrt(num)+1), 2):
        if num % i == 0:
            return False
    return True


def get_cycles(num):
    digits = [int(s) for s in str(num)]
    length = len(digits)
    return [from_list_to_int(perm) for perm in \
        [[digits[i - j] for i in range(length)] for j in range(length)]]


def main():
    digits = (1, 3, 7, 9)
    primes = set((2, 3, 5, 7))
    
    for length in range(len(str(LIMIT-1)), 1, -1):
        for c in combinations_with_replacement(digits, length):
            if sum(c) % 3 != 0:
                numbers = set()
                for p in set(permutations(c)):
                    number = from_list_to_int(p)
                    if not number in numbers:
                        cycles = get_cycles(number)
                        map(numbers.add, cycles)
                        for num in cycles:
                            if not is_prime(num):
                                break
                        else:
                            map(primes.add, cycles)
    print len(primes)
                    

if __name__ == "__main__":
    main()
