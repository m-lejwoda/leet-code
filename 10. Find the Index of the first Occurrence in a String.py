class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        for i in range(len(haystack)):
            if i + needle_length > len(haystack):
                return -1
            if haystack[i:i+needle_length] == needle:
                return i
        return -1

sol = Solution()
print(sol.strStr("hello", "ll"))
print(sol.strStr("sadbutsad", "sad"))
print(sol.strStr("leetcode", "leeto"))
print(sol.strStr("mississippi", "a"))