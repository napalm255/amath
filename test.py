#!/usr/bin/env python
import amath

numbers = [69,88,6,496,28,121,888]
line = str('-'*40)

for n in numbers:
    print('is_perfect(%d) = %s'    % (n, amath.is_perfect(n)))
    print('is_palindrome(%d) = %s' % (n, amath.is_palindrome(n)))
    print('is_even(%d) = %s'       % (n, amath.is_even(n)))
    print('is_odd(%d) = %s'        % (n, amath.is_odd(n)))
    print(line)

print('get_facts(%s) = %s\n%s'   % (numbers[3], amath.get_facts(numbers[3]), line))
print('facts(%s) = %s\n%s'       % (numbers[3], amath.facts(numbers[3]), line))
print('facts(%s) = %s\n%s'       % (numbers, amath.facts(numbers), line))
print('facts(%s,%s) = %s\n%s'    % (numbers[2], numbers[4], amath.facts(numbers[2], numbers[4]), line))
print('facts(%s,%s,%s) = %s\n%s' % (numbers[2], numbers[4], numbers[3], amath.facts(numbers[2], numbers[4], numbers[3]), line))
