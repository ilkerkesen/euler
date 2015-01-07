#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations


def is_substring_divisible(n):
    divisors = (2, 3, 5, 7, 11, 13, 17)
    for i, div in zip(range(1, 8), divisors):
        if int(str(n)[i:i+3]) % div != 0:
            return False
    return True


def list_to_int(ds):
    return int(''.join([str(d) for d in ds]))


def main():
    result = 0
    for p in permutations(range(9, -1, -1)):
        num = list_to_int(p)
        if len(str(num)) != 10:
            break
        
        if is_substring_divisible(num):
            result += num

    print result


if __name__ == "__main__":
    main()
