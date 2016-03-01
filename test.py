#!/usr/bin/env python
import amath

numbers = [3,6,28,69,88,121,496,137438691328]
line = str('-'*40)

for n in numbers:
    print('is_perfect(%d) = %s'    % (n, amath.is_perfect(n)))
    print('is_palindrome(%d) = %s' % (n, amath.is_palindrome(n)))
    print('is_even(%d) = %s'       % (n, amath.is_even(n)))
    print('is_odd(%d) = %s'        % (n, amath.is_odd(n)))
    print('is_prime(%d) = %s'      % (n, amath.is_prime(n)))
    print(line)

print('get_facts(%s) = %s\n%s'   % (numbers[3], amath.get_facts(numbers[3]), line))
print('facts(%s) = %s\n%s'       % (numbers[3], amath.facts(numbers[3]), line))
print('facts(%s) = %s\n%s'       % (numbers, amath.facts(numbers), line))
print('facts(%s,%s) = %s\n%s'    % (numbers[1], numbers[2], amath.facts(numbers[1], numbers[2]), line))
print('facts(%s,%s,%s) = %s\n%s' % (numbers[1], numbers[2], numbers[3], amath.facts(numbers[1], numbers[2], numbers[3]), line))
