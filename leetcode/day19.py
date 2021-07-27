#https://leetcode.com/problems/valid-anagram/submissions/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        if len(s) != len(t):
            return False

        for val in s:
            g = d.get(val, None)
            if g:
                d[val] = d[val] + 1
            else:
                d[val] = 1

        for val in t:
            g = d.get(val, None)
            if g and g >= 0:
                d[val] = d[val] - 1
            else:
                return False

        return True


