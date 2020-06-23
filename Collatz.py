#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert 0 < i < 1000000
    assert 0 < j < 1000000
    cycleList =[]
    if i > j:
        start = j
        fin = i
    else:
        start = i
        fin = j
    for x in range(start,fin+1):
        cycleLen = cycle(x)
        cycleList.append(cycleLen)
    maxCycle = max(cycleList)
    assert maxCycle > 0
    return maxCycle

def cycle(y):
    assert 0 < y < 1000000
    counter = 1
    while y > 1:
        if y%2 == 0:
            y = y//2
        else:
            y = 3*y + 1
        counter += 1
    assert counter > 0
    return counter
# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
