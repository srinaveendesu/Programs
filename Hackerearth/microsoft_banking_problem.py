def solution(R, V):
    # write your code in Python 3.8.10
    A = 0
    B = 0
    a = 0
    b= 0
    for bank,money in zip(list(R),V):

        if bank == 'A':
            a = a + money
            b = b - money

        if bank == 'B':
            b = b + money
            a = a - money
        if a <0:
            A = A + (-a)
            a = a + (-a)
        if b <0:
            B = B + (-b)
            b = b + (-b)
        print(a,b)
    #print(a, b)
    print(A,B)


solution('BAABA', [2, 4, 1, 1, 2])
solution('ABAB', [10, 5, 10, 15])
solution('B', [100])
