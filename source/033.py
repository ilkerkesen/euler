#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import combinations
from fractions import Fraction


def main():
    final = Fraction(1, 1)
    for nu, de in combinations(range(10, 100), 2):
        ns, ds = set(map(int, str(nu))), set(map(int, str(de)))
        lns, lds = map(len, (ns, ds))
        ndd, ddn = tuple(ns - ds), tuple(ds - ns)
        nud, nid = tuple(ns.union(ds)), tuple(ns.intersection(ds))
        lndd, lddn, lnud, lnid = map(len, (ndd, ddn, nud, nid))

        if lns == lds and not 0 in nud and lnid == 1 and not 0 in (lndd, lddn) \
           and float(nu) / de == float(ndd[0]) / ddn[0] and lnud == 3:
            final *= Fraction(nu, de)
    print final.denominator


if __name__ == "__main__":
    main()
