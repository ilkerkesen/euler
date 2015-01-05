#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

ls = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def is_triangle_word(word):
    value = reduce(lambda x, y: x + y, map(ls.index, word), len(word))
    index = (-1 + sqrt(1 + 8*value)) / 2.0
    return index == int(index)


def main():
    f = open("p042_words.txt", "r")
    words = [word[1:-1] for word in f.read().split(",")]
    f.close()

    print len(filter(is_triangle_word, words))


if __name__ == "__main__":
    main()
