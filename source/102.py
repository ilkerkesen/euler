#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calculate_area(ax, ay, bx, by, cx, cy):
    return abs(ax*(by-cy) + bx*(cy-ay) + cx*(ay-by)) / 2.0


def main():
    f = open("p102_triangles.txt", "r")
    lines = f.read().split("\n")
    lines.pop()
    f.close()

    result = 0
    for line in lines:
        (ax, ay, bx, by, cx, cy) = tuple(map(int, line.split(",")))
        total_area = calculate_area(ax, ay, bx, by, cx, cy)
        
        area1 = calculate_area(0, 0, bx, by, cx, cy)
        area2 = calculate_area(ax, ay, 0, 0, cx, cy)
        area3 = calculate_area(ax, ay, bx, by, 0, 0)

        if area1 + area2 + area3 == total_area:
            result +=1
    print result


if __name__ == "__main__":
    main()
