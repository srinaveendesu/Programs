#https://leetcode.com/problems/customers-who-never-order/

# Write your MySQL query statement below
#
# select Name as customers from customers where ID not in ( select CustomerID from Orders)


# SELECT Name AS 'Customers'
# FROM Customers c
# LEFT JOIN Orders o
# ON c.Id = o.CustomerId
# WHERE o.CustomerId IS NULL

# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        node.val = node.next.val
        node.next = node.next.next

# https://leetcode.com/problems/guess-number-higher-or-lower/submissions/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        if guess(n) == 0:
            return n
        bigger = 0
        lower = 0
        while guess(n) != 0 and n >= 1 and not (bigger and lower):
            # print(guess(n),n, bigger, lower)
            if guess(n) == -1:
                bigger = n
                n = n // 2
            elif guess(n) == 1:
                lower = n
                n = n + (n // 2 or 1)

            elif guess(n) == 0:
                return n

        n = (bigger + lower) // 2
        b = bigger
        l = lower
        # print (n, b, l)
        while guess(n) != 0 and n < b and n > l:

            if guess(n) == 1:
                lower = n
            elif guess(n) == -1:
                bigger = n
            # print(n)
            n = (bigger + lower) // 2
            # print(n, bigger, lower)

        return n if guess(n) == 0 else None


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            r = guess(mid)
            if r == 0:
                return mid
            elif r < 0:
                high = mid - 1
            else:
                low = mid + 1

        return n