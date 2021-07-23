# https://leetcode.com/problems/reverse-string/submissions/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        i = 0
        j = len(s) - 1

        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        print(s)

# https://leetcode.com/problems/power-of-three/submissions/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1:
            return False
        while n and n != 1:
            if n % 3:
                # print(n)
                return False
            n = n // 3

        return True

# https://leetcode.com/problems/add-digits/submissions/

class Solution:
    def addDigits(self, num: int) -> int:

        s = 0

        while num > 0:
            s = s + (num % 10)
            num = num // 10
            if num == 0 and s > 9:
                num = s
                s = 0

        return s


class Solution:
    def addDigits(self, num: int) -> int:

        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9