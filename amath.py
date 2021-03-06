"""
amath is an advanced math module
"""

from __future__ import absolute_import
import math

def is_even(num):
    """returns true if given number is even"""
    # if num is evenly divisible by 2
    return num % 2 == 0

def is_odd(num):
    """returns true if given number is odd"""
    # if num is not evenly divisible by 2
    return num % 2 != 0

def is_palindrome(num):
    """return true if given number is a palindrome"""
    # if num equals the reversal of num
    return str(num) == str(num)[::-1]

def is_perfect(num):
    """returns true if given number is perfect"""
    # skip 1
    if num == 1:
        return False
    # initialize the sum; include 1 by starting at 1
    s = 1
    # loop through all possible numbers
    for i in xrange(2, (num / 2) + 1):
        # if (i) is a proper positive divisor to num
        if num % i == 0:
            a = num / i
            # crossed median, ran out of possible divisors
            if i >= a:
                break
            # add both divisors to sum
            s += a + i
            # if the sum is greater than num it is not a perfect number
            if s > num:
                break
    # if the sum matches num then it is a perfect number
    if s == num:
        return True
    return False

def is_perfect_slow(num):
    """returns true if given number is perfect"""
    # skip 1
    if num == 1:
        return False
    # initialize the sum
    s = 1
    # loop through all possible numbers
    for i in xrange(2, (num / 2) + 1):
        # if (i) is a proper positive divisor to num
        if num % i == 0:
            s += i
    # if the sum matches num then it is a perfect number
    if s == num:
        return True
    return False

def is_perfect_list(num):
    """returns true if given number is perfect"""
    # skip 1
    if num == 1:
        return False
    # initialize the sum; include 1 by starting at 1
    div = [1]
    for i in xrange(2, (num / 2) + 1):
        # if (i) is a proper positive divisor to num
        if num % i == 0:
            a = num / i
            # crossed median, ran out of possible divisors
            if i >= a:
                break
            # add both divisors to sum
            div.append(i)
            div.append(a)
            # if the sum is greater than num it is not a perfect number
            if sum(div) > num:
                break
    # if the sum matches num then it is a perfect number
    if sum(div) == num:
        return True
    return False

def is_prime(num):
    """return true if given number is prime"""
    # no number less than 2 is prime
    if num < 2:
        return False
    # check if num is divisible by any number up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        # if num is evenly divisible by number (i) then num is not prime
        if num % i == 0:
            return False
    return True

def get_divisors(num):
    """return list of all divisors of given number"""
    div = [1]
    # loop through all possible numbers
    for i in xrange(2, (num / 2) + 1):
        if num % i == 0:
            a = num / i
            # crossed median, ran out of possible divisors
            if i > a:
                break
            div.append(i)
            div.append(a)
    return sorted(div)

def get_facts(num):
    """return dict with facts of given number"""
    return {
        'palindrome': is_palindrome(num),
        'divisors'  : get_divisors(num),
        'perfect'   : is_perfect(num),
        'prime'     : is_prime(num),
        'even'      : is_even(num),
        'odd'       : is_odd(num)
    }

def facts(*args):
    """return dict with facts for given number(s)
       int = single integer to gather facts = facts(6)
       list = list of numbers to gather facts = facts([6,28])
       int,int = two integers defining start an and end range to gather facts = facts(1,33)
    """
    f = {}
    if len(args) > 2:
        return f
    if len(args) == 1:
        if isinstance(args[0], int):
            f = get_facts(args[0])
        elif isinstance(args[0], list):
            for i in args[0]:
                f[i] = get_facts(i)
    elif len(args) == 2:
        if isinstance(args[0], int) and isinstance(args[1], int):
            for i in range(args[0], args[1] + 1):
                f[i] = get_facts(i)
    return f
