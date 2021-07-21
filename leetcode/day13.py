# https://leetcode.com/problems/pascals-triangle-ii/submissions/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        lst = [[1], [1, 1]]

        for i in range(1, rowIndex):
            # print(len(lst[i]))
            l = [1] + [lst[i][j] + lst[i][j - 1] for j in range(1, len(lst[i]))] + [1]
            lst.append(l)
            # print(l)
        return lst[rowIndex]

# https://leetcode.com/problems/reverse-bits/submissions/

class Solution:
    def reverseBits(self, n: int) -> int:
        a = str(bin(n))
        r = len(a)
        # print(a,r)
        a = a[::-1][:r - 2] + ('0' * (32 - r + 2))
        # print(a)
        return int(a, 2)

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


