#https://leetcode.com/problems/number-of-1-bits/submissions/

#  Brian Kernighan’s Algorithm
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n - 1)
            count += 1

        return count


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1

        return count


class Solution:
    def hammingWeight(self, n: int) -> int:

        a = str(bin(n))
        d = {}
        d['1'] = 1
        for i in range(2, len(a)):
            r = d.get(a[i], None)
            if r:
                d['1'] += 1

        return d['1'] - 1

# https://leetcode.com/problems/remove-linked-list-elements/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        curr = head
        prev = None

        while curr:
            if head.val == val:
                head = head.next
                curr = head
            elif curr.val == val:
                prev.next = curr.next
                # curr = curr.next
                # prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        curr = head
        prev = None

        while head and head.val == val:
            if head.val == val:
                head = head.next
                curr = head

        while curr:

            if curr.val == val:
                prev.next = curr.next
                # curr = curr.next
                # prev = curr
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return head

# https://leetcode.com/problems/reverse-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = None
        nexx = head
        while nexx:
            curr = nexx
            nexx = curr.next
            curr.next = prev
            prev = curr

        head = prev
        return head

# https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        if len(set(nums)) == len(nums):
            return False
        else:
            return True

# https://leetcode.com/problems/power-of-two/submissions/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n and n != 1:
            if n % 2:
                # print(n)
                return False
            n = n // 2

        return True
