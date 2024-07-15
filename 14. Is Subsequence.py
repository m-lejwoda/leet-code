class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        start = 0
        for i in range(len(s)):
            if start == len(t):
                return False
            for j in range(start, len(t)):
                if s[i] == t[j]:
                    start = j + 1
                    break
                if j == len(t) - 1:
                    return False
        return True

sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))
print(sol.isSubsequence("axc", "ahbgdc"))
print(sol.isSubsequence("aaaaaa", "bbaaaa"))