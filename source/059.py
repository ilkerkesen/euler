#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

f = open("p059_cipher.txt", "r")
values = map(int, f.read().split(","))
f.close()


def most_occur(values):
    return Counter(map(lambda x: x ^ ord(' '), values)).most_common()[0][0]


key = [most_occur(values[i::3]) for i in range(3)] * (len(values) / 3 + 1)
result = sum(map(lambda x: x[0] ^ x[1], zip(values, key)))

print result
