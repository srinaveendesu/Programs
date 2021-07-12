#https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        r = len(set(nums))
        if r == 1:
            nums = [nums[0]]
        n = len(nums)
        lst = []
        if n > 1:
            i = 0
            while i < n:
                try:
                    if nums[i] == nums[i + 1]:
                        val = nums.pop(i + 1)
                        lst.append(val)
                    else:
                        i += 1
                except:
                    break
                # print(nums,i)
        nums = nums + lst
        return r


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(set(nums))
        i = 0
        j = 1
        while i < n:
            try:
                if nums[i] == nums[j]:
                    j += 1
                else:
                    # temp = nums[i+1:j]
                    val = nums.pop(j)
                    nums.insert(i + 1, val)

                    i = i + 1
                    j = j + 1
            except:
                break

        return n

#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        n = len(nums)
        while i < n:
            try:
                if nums[i] == val:
                    nums[i] = nums[n - 1]
                    n -= 1
                else:
                    i += 1
            except:
                break
        return n