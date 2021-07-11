# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1,
             'IV': 4,
             'V': 5,
             'IX': 9,
             'X': 10,
             'XL': 40,
             'L': 50,
             'XC': 90,
             'C': 100,
             'CD': 400,
             'D': 500,
             'CM': 900,
             'M': 1000}

        i = 0
        # tot = []
        tots = 0
        while i < len(s):
            if s[i] in ['I', 'X', 'C']:
                if s[i:i + 2] in d:
                    # tot.append(d[s[i:i+2]])
                    tots += d[s[i:i + 2]]
                    i += 2
                else:
                    # tot.append(d[s[i]])
                    tots += d[s[i]]
                    i += 1
            else:
                # tot.append(d[s[i]])
                tots += d[s[i]]
                i += 1
        # print(tot)
        return tots


# https://leetcode.com/problems/longest-common-prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        common = strs[0]
        l = len(common)
        for i in range(1, len(strs)):
            if len(strs[i]) == 0:
                return ""
            if len(strs[i]) < l:
                common = common[:len(strs[i])]
                if common == strs[i]:
                    continue
            for j in range(0, len(common)):
                # print(j, common)
                if common[j] == strs[i][j]:
                    continue
                else:
                    if j == 0:
                        common = ""
                    else:
                        common = common[:j]
                    break
        return common

