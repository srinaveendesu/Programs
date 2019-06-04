#QQ#
"""
Given an array
N = [1,1,1,2,2,3,3,3,3,4,4,4]
return an array counting the consecutive digits in the format of [digit1,count,digit2,count ...]
 [1,3,2,2,3,4,4,3]
"""

N = [1,1,1,2,2,3,3,3,3,4,4,4,5]

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

#QQ#
"""
Given an array N and a value v.
find all the possible ways the values of the array could be summed to value 
N = [1,2]
v = 3
Solution:
lst [ [1,1,1]
        [1,2]
        [2,1]
    ]
"""


N = [1,2]
v = 5
# This give the total number of ways we sum can be obtained
def func2(N,v ):
    count =0
    if v >0:
        for val in list(N):
            count = count + func2( N,v - val )
    elif v==0:
        count =1
        return count
    else:
        pass
    return count

print (func2(N,v) )

## this function tries to give the ways it can take
## partially complete
lst = []
def func3(N,v ,kst):
    global lst
    #N = N[::-1]
    if v > 0:
        for val in list(N):
            kst = kst + [val]
            v = v - val
            print (kst, v,v-val)
            func3(N, v, kst)
        #print (v, kst)
    elif v == 0:
        #print(kst)
        #lst = []
        return lst.append(kst)
    else:
        pass
    return lst
kst = []
print (func3(N,v,kst) )