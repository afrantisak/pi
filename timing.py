#!/usr/bin/env python
import sys
import timeit

def compute_pi_digits(digits):
    from sympy.mpmath import mp
    mp.dps = digits
    return str(mp.pi)

def main():
    reps = 1
    for digits in xrange(1000, 50000, 1000):
        stmt = "compute_pi_digits({digits})".format(digits=digits)
        setup = "from __main__ import compute_pi_digits"
        time = timeit.timeit(stmt, setup=setup, number=reps)
        print digits, reps, time * 1000000 / (digits * reps)
    return 0

if __name__ == '__main__':
    sys.exit(main())

