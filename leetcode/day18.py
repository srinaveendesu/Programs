#https://leetcode.com/problems/missing-number/submissions/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        n = ((n) * (n + 1)) // 2

        print(n)

        return n - sum(nums)

#https://leetcode.com/problems/first-bad-version/submissions/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low < high:
            mid = low + (high - low) // 2
            r = isBadVersion(mid)
            if r:
                high = mid
            else:
                low = mid + 1

        return low

