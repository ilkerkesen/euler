#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    num = 1
    while True:
        digits = set([int(d) for d in str(num)])
        for i in range(2, 7):
            multiple = num * i
            if digits != set([int(d) for d in str(multiple)]):
                break
        else:
            break
        num += 1

    print num


if __name__ == "__main__":
    main()
