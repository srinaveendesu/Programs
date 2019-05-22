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

#QQ# https://www.hackerrank.com/challenges/missing-numbers/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()

    d1 = {}
    for val in arr:
        if val not in d1.keys():
            d1[val] = 1
        else:
            d1[val] = d1[val] + 1
    d2 = {}
    for val in brr:
        if val not in d1.keys():
            d1[val] = -1
        else:
            d1[val] = d1[val] - 1

    lst = []

    for val in d1.keys():
        if d1[val] < 0:
            lst.append(val)
    print(d1)
    lst.sort()
    return lst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


#QQ# https://www.hackerrank.com/challenges/sherlock-and-array/problem


# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the balancedSums function below.
def balancedSums(arr):
    flag = False
    s = sum(arr)
    half = 0
    index = 0
    n = len(arr)

    for i in range(0, n):
        temp_s = (s - arr[i]) / 2
        if temp_s == half:
            index = i
            i = n
            flag = True
        else:
            half = half + arr[i]

    if not flag:
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

#QQ# https://www.hackerrank.com/challenges/beautiful-triplets/problem

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    lst = []

    for val in arr:
        a = val
        b = val + d
        c = val + (2 * d)
        if b in arr and c in arr:
            lst.append(str(a) + str(b) + str(c))
    print(lst)
    return len(lst)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
