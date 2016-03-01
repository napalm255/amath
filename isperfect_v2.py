#!/usr/bin/env python
from sys import argv
import amath

if len(argv) > 1:
    if argv[1].isdigit():
        num = long(argv[1])
        n = "is not"
        perf = amath.is_perfect_v2(num)
        if perf:
            n = "is"
        print(perf)
        print('the number %s, %s a perfect number' % (num, n))
    else:
        print('must enter a digit')
else:
    print('must enter a digit')
