# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        index = 0
        last = None
        for i in range(0, len(digits) - 1):
            if digits[i] != 9:
                last = i
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        if last is None:
            digits.insert(0, 0)
            last = 0
        digits[last] = digits[last] + 1
        index = last + 1
        while index < len(digits):
            digits[index] = 0
            index += 1
        return digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''.join([str(i) for i in digits])
        num = int(num) + 1
        digits = list(str(num))
        return digits
