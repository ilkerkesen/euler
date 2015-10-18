#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations

def sieve(limit):
    numbers = [-1, -1] + range(2, limit+1)

    i = 2
    while i < limit/2:
        if numbers[i] != -1:
            j = 2 * i
            while j <= limit:
                numbers[j] = -1
                j += i
        i += 1

    return filter(lambda x: x != -1, numbers) 


ps = filter(lambda x: x > 999 and not x in [1487, 4817, 8147], sieve(10000))
ps = filter(lambda x: len(set(str(x)[:3])) == 3, ps)

for comb in combinations(ps, 3):
    if comb[2] - comb[1] == comb[1] - comb[0]:
        sets = map(lambda x: set(str(x)), comb)
        if sets[0] == sets[1] == sets[2]:
            print "".join(map(str, comb))
            exit(0)

