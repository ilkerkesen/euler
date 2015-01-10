#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations, count
from operator import add


def main():
    for p in permutations(range(9, 0, -1)):
        for i in range(1, 5):
            num = int(reduce(add, map(str, p[:i])))
            l = len(str(num))

            for j in count(2):
                n = num * j

                if len(str(n)) + l > 9:
                    break

                if n != int(reduce(add, map(str, p[l:l+len(str(n))]))):
                    break
                
                l += len(str(n))
                if l == 9:
                    print reduce(add, map(str, p))
                    exit(0)


if __name__ == "__main__":
    main()
