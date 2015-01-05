#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import mul

LIMIT = 1000000


def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    numer = reduce(mul, range(n, n-r, -1))
    denom = reduce(mul, range(1, r+1))
    return numer / denom


def main():
    result = 0
    for n in range(1, 101):
        for r in range(n+1):
            if ncr(n, r) > LIMIT:
                result += 1
    print result

if __name__ == "__main__":
    main()
