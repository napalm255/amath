#!/usr/bin/env python
from sys import argv
import amath

if argv[1].isdigit():
    num = int(argv[1])
    n = "is not"
    perf = amath.is_perfect(num)
    if perf:
        n = "is"
    print(perf)
    print('the number %s, %s a perfect number' % (num, n))
else:
    print('must be a digit')
