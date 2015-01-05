#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIMIT = 1000000


def is_double_base_palindrome(num):
    return str(num) == str(num)[::-1] and bin(num)[2:] == bin(num)[2:][::-1]


def main():
    result = 0
    i = 1

    while i < LIMIT:
        if is_double_base_palindrome(i):
            result += i
        i += 1

    print result


if __name__ == "__main__":
    main()
