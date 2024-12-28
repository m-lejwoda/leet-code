class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for i in range(max(len(word1), len(word2))):
            try:
                res += word1[i]
            except IndexError:
                pass
            try:
                res += word2[i]
            except IndexError:
                pass
        return res
s = Solution()
print(s.mergeAlternately(word1="apple", word2="banana"))
print(s.mergeAlternately(word1 = "abc", word2 = "pqr"))
print(s.mergeAlternately(word1 = "ab", word2 = "pqrs"))