# https://leetcode.com/problems/find-the-difference/submissions/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        d = {}

        for val in s:

            r = d.get(val, None)
            if r:
                d[val] += 1
            else:
                d[val] = 1

        for val in t:

            r = d.get(val, None)
            if r:
                d[val] -= 1
                if d[val] == 0:
                    del d[val]
            else:
                return val

        print(d)

import collections
# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/

class Solution:
    def firstUniqChar(self, s: str) -> int:

        l = 0
        d = {}
        d2 = {}
        count = 1
        lowest = 100000
        for val in s:
            # print(d,d2)
            r = d.get(val, None)
            r2 = d2.get(val, None)
            if r:
                d2[val] = d[val]
                del d[val]
            elif r2:
                count += 1
                continue
            else:
                d[val] = count
            # print(d)
            count += 1
        # print(d)

        for k, v in d.items():
            if v < lowest:
                lowest = v

        return (lowest - 1) if lowest != 100000 else -1


class Solution:
    def firstUniqChar(self, s: str) -> int:

        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1