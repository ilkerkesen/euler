#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product


def list_to_dict(totals):
    result = dict()
    for t in totals:
        if result.has_key(t):
            result[t] += 1
        else:
            result[t] = 1
    return result


def get_won_count(n, d):
    return sum(map(lambda x: x[1], filter(lambda x: x[0] < n, d.items())))


def get_total_won_count(p1, p2):
    return sum(map(lambda x: get_won_count(x[0], p2) * x[1], p1.items()))


def main():
    peter_totals = map(sum, product(range(1, 5), repeat=9))
    colin_totals = map(sum, product(range(1, 7), repeat=6))

    peter = list_to_dict(peter_totals)
    colin = list_to_dict(colin_totals)
    
    print get_total_won_count(peter, colin) / \
        float(len(peter_totals) * len(colin_totals))

if __name__ == "__main__":
    main()
