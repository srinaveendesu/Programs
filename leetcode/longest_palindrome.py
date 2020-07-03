# Brute force approach
def palin( s):
    n = len(s) - 1
    i = 0
    while i < n:
        if s[i] == s[n]:
            i += 1
            n -= 1
        else:
            return False
    return True


def longestPalindrome( s: str) -> str:
    d = {}
    max1 = 0
    for i in range(0, len(s)):
        for j in range(len(s), 0, -1):
            l = len(s[i:j])
            #print(l)
            if j > i and l >= max1:
                flag = palin(s[i:j])
                if flag:
                    max1 = max(l, max1)
                    if l in d.keys():
                        d[l] = d[l] + [s[i:j]]
                    else:
                        d[l] = [s[i:j]]
            else:
                break
        if len(s) == max1:
            break

    print(d)
    print(max1)
    if max1 in d.keys():
        return d[max1][0]
    elif len(s) == 0:
        return s
    else:
        return s[0]


ss = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
import datetime
start = datetime.datetime.now()
longestPalindrome(ss)
print(datetime.datetime.now() - start)

# manacher's algorithm implementation

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        print(T)
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]


# Solving using DP

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome.
        dp = [[False] * n for _ in range(n)]

        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]

        maxLen = 1
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                # palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end + 1]

        return ans