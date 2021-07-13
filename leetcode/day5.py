# https://leetcode.com/problems/search-insert-position/submissions/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i = 0
        j = 0

        while True:
            # print('adf', nums[-1], nums[i], target)
            try:
                if target == nums[i]:
                    return i
                elif nums[i - 1] < target < nums[i]:
                    return i
                elif nums[i] == nums[-1] and target < nums[i]:
                    j = 0
                    i += 1
                elif nums[i] == nums[-1] and target > nums[i]:
                    return i + 1
                else:
                    # print('sadfafff')
                    i += 1
                    j += 1
            except:

                break

        return j


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        i = 0
        j = 0
        n = len(nums)
        if n == 1:
            if target > nums[0]:
                return i + 1
            else:
                return i
        while i < n:
            if nums[i] == target:
                return i
            elif target > nums[i]:
                j += 1
            i += 1
        # print(i,j,k)

        return j


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if (nums[i] == target):
                return i
            elif (nums[i] > target):
                return i
        return len(nums)


# https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split(' ')
        # print(s)

        return len(s[-1])


#https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def climbStairs(self, n: int) -> int:

        a = 1
        b = 2

        if n == 1:
            return a
        elif n == 2:
            return b
        else:
            for i in range(2, n):
                a, b = b, a + b

        return b