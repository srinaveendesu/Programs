
# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = []
        d = {}
        for i, val in enumerate(nums):
            r1 = d.get(val, None)
            r2 = d.get(target - val, None)
            if r1 is not None and r2 is not None:
                return [i, r1]
            if r1 is None and r2 is not None:
                return [i, r2]
            if r1 is None:
                d[val] = i
        return lst


# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        min_v = -pow(2, 31)
        max_v = pow(2, 31) - 1
        if x < 0:
            x = -1 * x
            val = -1 * int(str(x)[::-1])
        else:
            val = int(str(x)[::-1])
        if min_v < val < max_v:
            return val
        else:
            return 0


