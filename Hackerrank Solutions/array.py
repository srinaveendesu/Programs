#QQ# #https://www.hackerrank.com/challenges/array-left-rotation/problem

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    l = (a[::][d:]+ a[:d])

    print (' '.join(map(str,l)))


#QQ# https://www.hackerrank.com/challenges/sparse-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    d = {}
    for val in strings:
        if val not in d.keys():
            d[val] = 1
        else:
            d[val] = d[val] +1
    print (d)
    lst = []

    for val in queries:
        if val in d.keys():
            lst.append(d[val])
        else:
            lst.append(0)
    return lst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

