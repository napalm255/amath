#!/usr/bin/env python
from sys import argv
import amath

if len(argv) > 2:
    v = argv[1]
    n = argv[2]
    ver = ['v1', 'v2', 'v3', 'v4']
    if v not in ver:
        print('must suuply version %s' % (ver))
        exit()
    if not n.isdigit():
        print('must enter digit')
        exit()

    if v == 'v1':
        print(amath.is_perfect_v1(int(n)))
    if v == 'v2':
        print(amath.is_perfect(int(n)))
    if v == 'v3':
        print(amath.is_perfect_v3(int(n)))
    if v == 'v4':
        print(amath.is_perfect_v4(int(n)))
else:
    print('invalid arguments')
