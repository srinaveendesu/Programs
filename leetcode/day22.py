#https://leetcode.com/problems/fibonacci-number/submissions/

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        a, b = 1, 1

        for i in range(0, n - 2):
            a, b = b, a + b

        return b