# https://leetcode.com/problems/add-binary/submissions/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

#https://leetcode.com/problems/merge-sorted-array/submissions/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:]
        del nums2[n:]

        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
                m += 1

        if i == m and j < n:
            while j < n:
                if bool(nums1) and nums1[i - 1] <= nums2[j]:
                    nums1[i + 1:] = nums2[j:]
                    break
                else:
                    nums1.insert(i, nums2[j])
                    i += 1
                j += 1
