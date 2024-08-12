#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum = 0
    for index in range(0, len(ar)):
        sum = sum + ar[index]

    return sum

if __name__ == '__main__':
    result = simpleArraySum([1, 2, 3, 4, 10, 11])
