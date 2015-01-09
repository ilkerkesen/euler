#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_recurring(num):
    numer = 1
    denom = num
    remainders = dict()
    
    i = 0
    while True:
        if denom > numer:
            numer *= 10
            while denom > numer:
                numer *= 10
                i += 1

        numer = numer % denom
        i += 1

        if remainders.has_key(numer):
            return i - remainders.get(numer)
        elif numer == 0:
            return -1

        remainders[numer] = i

    return i - remainders.get(numer)


def main():
    max_recurring = 0
    num = 0

    for i in range(11, 1001, 2):
        recurring = get_recurring(i)
        if recurring > max_recurring:
            num = i
            max_recurring = recurring
    print num


if __name__ == "__main__":
    main()
