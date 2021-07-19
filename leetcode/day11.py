#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(0, len(numbers)):

            val = target - numbers[i]
            try:
                s = numbers[i + 1:].index(val)
                if s >= 0:
                    return [i + 1, i + s + 2]
            except:
                pass


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        index = 0
        end = 0
        while numbers[n - 1] > target:
            end = n
            n = n // 2
            print(n)

        for i in range(0, n):

            val = target - numbers[i]
            try:
                s = numbers[i + 1:].index(val)
                if s >= 0:
                    return [i + 1, i + s + 2]
            except:
                pass

        for i in range(n, end):

            val = target - numbers[i]
            try:
                s = numbers[i + 1:].index(val)
                if s >= 0:
                    return [i + 1, i + s + 2]
            except:
                pass

        print(n, index, end, len(numbers))
        print(numbers[13010 - 5: 13010 + 5])


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = {}

        for i in range(len(numbers)):
            r = d.get(numbers[i], None)
            if r is None:
                d[numbers[i]] = i + 1
                val = target - numbers[i]
                try:
                    s = numbers[i + 1:].index(val)
                    if s >= 0:
                        return [i + 1, i + s + 2]
                except:
                    pass


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l + 1, r + 1]
            elif total < target:
                l += 1
            else:
                r -= 1

# https://leetcode.com/problems/majority-element/submissions/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        d = {}

        for val in nums:

            if d.get(val, None) is None:
                d[val] = 1
            else:
                d[val] = d[val] + 1

        d = {i: k for k, i in d.items()}
        val = max(d.keys())
        return d[val]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]