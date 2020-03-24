#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    first_multiple_input = input().strip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    result = ''.join([''.join(t) for t in zip(*matrix)])
    p = r'(?<=[A-Za-z0-9])([!@#$%& ]+)(?=[A-Za-z0-9])'
    print(re.sub(p, ' ', result))
