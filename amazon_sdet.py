## AMAZON SDET INTERVIEW ROUND 1

##    //Given an analouge clock time, Can you find the bigger angle?
##    //Example time : 03:00, Bigger angle is 270 Deg
##    
##min hand = 360 - (6 * min)
##hrs hand = 360 - (30 * hrs)
##
##
##H = 360 - (3 * 30) = 270
##M = 360 - (6 * 0) = 36360
##
##H - M = (360 - 36270)
##
##res = 360 - 90 = 270
##----
##11 : 57
##
##H = 360 - (11 * 30) = 30
##M = 360 - (57 * 30) = 18
##
##12
##348
##
##variance = 
##
##
##// Write Code


def cal_angle(h,m):
   h_val = 360 - (h * 30)
   m_val = 360 - (m * 6)
   
   res = abs(h_val- m_val)
   variance = m/2
   res = res - variance
   if res < 180:
      res = 360 - res
   
   
   return (res )

print (cal_angle(3,45))
   
##=====
##Product of 2 Array's : 
##A {5,1,3,2,1}
##B {5,4,3}
##(5 * 5) + (1 * 4) + (3 * 3) + (2 * 5) + (1 * 4) = 52
##

def calc_arr(a,b):
    a_len = len(a)
    b_len = len(b)
    j= 0
    flag = min (a_len, b_len)
    if b_len >a_len:
        temp = a
        a = b
        b = temp
        
    total = 0
    for i in range(0,len(a)):
        if j == flag:
            j = 0
        total = total + ( a[i] * b[j])
        j +=1
     
    return (total)
            
##====
##file is not uploading to web page.how will you debug the scenario
##
##1. Check the name of the file is going to variable or not?
##2. Check the particular file is uploaded or not
##3. Check if it is added in another user's bucket
##4. Check the network filure not happend while uploading
##5. Check if someother process/person hasn't deleted the file 
##6. Check for the recent cde push is breaking any regression
##7. Check with another browser flavor & OS flavour
##8. Check if javascript event is triggered correctly
##9. Check if another user of same bucket is uploaing file
##10 Check his session is active/not

######################################################

""" Round 2
Given an array find all triplets summing to a given value.
Optimize problem.
time complexity.

Asumming that the given triplet function is written already. You as an automation engineer need to wite test automation suite for testing te function
"""

""" Round 3
Given an array with an intial value, each next element is either +1 or -1 of previous element . Task is to find the first occurrance of the given value
optimize optimize optimize.. find best possible solution

Given a linked list find if its a palindrome.
optimize optimize optimize ....find better solution

Have you done anything for any other teams other than your own project. If so why? 
"""

