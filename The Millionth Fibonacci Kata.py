from math import fabs

from decimal import Decimal

import numpy
from numpy import matrix


def fib(n):
    return (matrix('1,1;1,0', dtype=object) ** n).item(1) if n<0 else (matrix('1,1;1,0', dtype=object) ** abs(n)).item(1)*pow(-1,n-1)


if __name__ == '__main__':
    print(fib(96))
