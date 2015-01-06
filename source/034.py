#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import factorial as f

LIMIT = f(9) * 8 + 1

def is_curious_number(num):
    return num == sum(map(f, map(int, str(num))))

def main():
    result = 0
    for i in range(10, LIMIT+1):
        if is_curious_number(i):
            result += i
    print result


if __name__ == "__main__":
    main()
