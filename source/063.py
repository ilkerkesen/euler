#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil, floor

n = 1
result = 0
l = 0

while l < 10:
    l = int(ceil((10**(n-1))**(1/float(n))))

    result += 10 - l
    n += 1

print result
