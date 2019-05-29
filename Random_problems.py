#QQ#
"""
Given an array
N = [1,1,1,2,2,3,3,3,3,4,4,4]
return an array counting the consecutive digits in the format of [digit1,count,digit2,count ...]
 [1,3,2,2,3,4,4,3]
"""

N = [1,1,1,2,2,3,3,3,3,4,4,4]

def func(N):
    lst = []
    lst.append(N[0])
    count = 1
    for i in range (1,len(N)):
        if lst[-1] ==N[i]:
            count = count + 1
        else:
            lst.append(count)
            lst.append(N[i])
            count = 1
    lst.append(count)
    return lst



print (func(N))