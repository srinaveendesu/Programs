# https://leetcode.com/problems/single-number-ii/submissions/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return ((3 * sum(set(nums))) - sum(nums)) // 2


# https://leetcode.com/problems/pascals-triangle/submissions/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        num = 11

        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        lst = [[1], [1, 1]]

        for i in range(1, numRows - 1):
            # print(len(lst[i]))
            l = [1] + [lst[i][j] + lst[i][j - 1] for j in range(1, len(lst[i]))] + [1]
            lst.append(l)
            # print(l)
        return lst

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lst = [0]

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                s = prices[j] - prices[i]
                lst.append(s)

        if max(lst) <= 0:
            return 0
        return max(lst)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mi = 10000000000
        mx = 0

        for i in range(0, len(prices)):
            if prices[i] < mi:
                mi = prices[i]
            elif (prices[i] - mi) > mx:
                mx = prices[i] - mi
        return mx