#!/usr/bin/env python

import math

def is_even(num):
    # if num is evenly divisible by 2 then it's even
    return num % 2 == 0

def is_odd(num):
    # if num is not evenly divisible by 2 then it's odd
    return num % 2 != 0

def is_perfect(num):
    # initialize the sum
    s = 0
    # loop through all numbers from 1 to num
    for i in range(1, num):
        # if number (i) is a proper positive divisor to num then
        # add the number (i) to the sum
        if(num % i == 0):
            s += i
    # if the sum matches num then it is a perfect number
    if (s == num):
        return True
    return False

def is_prime(num):
    # no number less than 2 is prime
    if num < 2: return False
    # check if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        # if num is evenly divisible by number (i) then
        # num is not prime
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    # check if num equals the reversal of num
    if str(num) == str(num)[::-1]:
        return True
    return False

def facts(*args):
    # int = single integer to gather facts = facts(6)
    # list = list of numbers to gather facts = facts([6,28])
    # int,int = two integers defining start an and end range to gather facts = facts(1,33)
    if len(args) > 2: return False
    elif len(args) == 1:
        if isinstance(args[0], int):
            return facts_get(args[0])
        elif isinstance(args[0], list):
            f = {}
            for i in args[0]:
                f[i] = facts_get(i)
            return f
    elif len(args) == 2:
        if isinstance(args[0], int) and isinstance(args[1], int):
            f = {} 
            for i in range(args[0],args[1] + 1):
                f[i] = facts_get(i)
            return f
    return

def facts_get(num):
    f = {
        'palindrome': is_palindrome(num),
        'perfect'   : is_perfect(num),
        'prime'     : is_prime(num),
        'even'      : is_even(num),
        'odd'       : is_odd(num)
    }
    return f
