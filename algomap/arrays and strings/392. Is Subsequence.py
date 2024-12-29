class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = 0
        counted = 0
        for i in s:
            while counted < len(t):
                if i == t[counted]:
                    res += 1
                    counted += 1
                    break
                counted += 1
        return True if res == len(s) else False
s = Solution()
print(s.isSubsequence(s = "abc", t = "ahbgdc"))
print(s.isSubsequence(s = "axc", t = "ahbgdc"))