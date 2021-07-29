# https://leetcode.com/problems/reverse-words-in-a-string-iii/submissions/

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        count =0
        for val in s:
            #print(val, count)
            s[count] =val[::-1]
            count +=1
        #print(s)
        s = ' '.join(s)
        return s

#https://leetcode.com/problems/student-attendance-record-i/submissions/

class Solution:
    def checkRecord(self, s: str) -> bool:
        d = {}
        count = 0
        prev = ''
        i = 0
        while i < len(s):
            r = d.get(s[i], None)
            if s[i] == 'L':
                if (i + 2) < len(s) and s[i + 1] == 'L' and s[i + 2] == 'L':
                    return False
            if r:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
            i += 1

        if d.get('A', None) and d['A'] >= 2:
            return False

        return True
