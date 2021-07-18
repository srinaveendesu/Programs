# https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = 1
        l2 = 1
        p1 = headA
        p2 = headB
        while p1.next is not None:
            l1 += 1
            p1 = p1.next
        while p2.next is not None:
            l2 += 1
            p2 = p2.next
        # print(l1, l2)
        if p1 is not p2:
            return None
        p1 = headA
        p2 = headB

        if l1 > l2:
            rem = l1 - l2
            for i in range(rem):
                p1 = p1.next
        elif l2 > l1:
            rem = l2 - l1
            for i in range(rem):
                p2 = p2.next

        # print(p1, p2)
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next

        return p1