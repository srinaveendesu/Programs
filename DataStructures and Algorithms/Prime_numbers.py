# Different methods to find prime numbers

import math

for n in range(2,10):
    #abs(math.sqrt(n))
    for x in range(2,int(n)):
        if n%x ==0:
            print ('{} divides {}'.format(x,n))
            break
    else:
        print ('{} is a prime number'.format(n))