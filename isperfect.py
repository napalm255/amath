#!/usr/bin/env python
from sys import argv
import amath

if len(argv) > 1:
    if argv[1].isdigit():
        num = int(argv[1])
        print(amath.is_perfect(num))
    else:
        print('must enter a digit')
else:
    print('must enter a digit')
