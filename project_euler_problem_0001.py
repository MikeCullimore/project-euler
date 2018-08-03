"""
project_euler_problem_0001.py

Worked solution to problem 1 from Project Euler:
https://projecteuler.net/problem=1

Problem title: Multiples of 3 and 5

Problem: if we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Break the problem down further:
1) Find the largest multiple of 3: e.g. for 10, it is 9 = 3 x 3.
2) Likewise for 5: e.g. for 10, it is 5 = 1 x 5.
3) Factorise each sum e.g. 3 + 6 + 9 = 3*(1 + 2 + 3).
4) Use Gauss's trick for the sums 1 + 2 + ... + n = n*(n - 1)/2.
5) Multiply the sums by 3 or 5 as appropriate then add together.

TODO: use example above as test case.
TODO: input validation.
"""


import numpy as np


def sum_gauss_trick(number):
    """Calculate the sum 1 + 2 + 3 + ... + number using Gauss's trick."""
    sum = int(number*(number+1)/2)
    print('The sum of the natural numbers up to {} is {}.'.format(number, sum))
    return sum


def find_largest_multiplier(number, divisor):
    """Find the largest multiple of divisor below the given number.

    I.e. return largest multiplier such that multiplier*divisor < number.
    """
    multiplier = int(np.floor((number - 1)/divisor))
    print('The largest multiple of {} below {} is {} x {} = {}.'.format(
        divisor, number, multiplier, divisor, multiplier*divisor))
    return multiplier


def find_sum_multiples_3_or_5(upper):
    """Find the sum of all multiples of 3 or 5 below the given upper bound.

    E.g. if upper=10: multiples of 3 or 5 are 3, 5, 6 and 9; sum is 23.
    """
    multiplier_3 = find_largest_multiplier(upper, 3)
    multiplier_5 = find_largest_multiplier(upper, 5)
    sum_3 = sum_gauss_trick(multiplier_3)
    sum_5 = sum_gauss_trick(multiplier_5)
    solution = 3*sum_3 + 5*sum_5
    print('The sum of all multiples of 3 or 5 below {} is:'.format(upper))
    print('3*{} + 5*{} = {}.'.format(upper, sum_3, sum_5, solution))
    return solution


def main():
    # find_sum_multiples_3_or_5(10)
    find_sum_multiples_3_or_5(1000)


if __name__ == '__main__':
    main()
