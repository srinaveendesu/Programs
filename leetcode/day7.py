# https://leetcode.com/problems/valid-palindrome/submissions/
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]*', '', s)
        s =s.lower()
        if s == s[::-1]:
            return True
        return False

# https://leetcode.com/problems/single-number/submissions/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        i =0
        while True:
            try:
                if d.get(nums[i], None):
                    del d[nums[i]]
                else:
                    d[nums[i]] = 1
                i+=1
            except:
                for k,val in d.items():
                    if val ==1:
                        return k


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (2 * sum(set(nums))) - sum(nums)