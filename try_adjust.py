#!/usr/bin/env python3

from numpy import array, arange, sin, cos, pi, sqrt


def period_adjust(x, period):
    int_shift = round(x / period)
    return x - int_shift * period

def print_result(x):
    print("The result is:", x)

def main():
    period = 2 * pi
    x = period * (-13) + 0.1453
    print_result(period_adjust(x, period))
    print("Now finished")
    
if __name__ == '__main__': 
    main()

