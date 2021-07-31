#https://leetcode.com/problems/reverse-string-ii/submissions/

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)

        for i in range(0, len(a), 2 * k):
            a[i:i + k] = a[i:i + k][::-1]

        return ''.join(a)