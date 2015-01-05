#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIMIT = 1000000


def main():
    frac = ""
    i = 1
    
    while len(frac) <= LIMIT:
        frac += str(i)
        i += 1

    result, i = 1, 1
    while i <= LIMIT:
        result *= int(frac[i-1])
        i *= 10

    print result
    

if __name__ == "__main__":
    main()
