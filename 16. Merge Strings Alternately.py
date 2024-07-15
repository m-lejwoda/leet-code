class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_value = max(len(word1), len(word2))
        res = ""
        for i in range(max_value):
            try:
                res += word1[i]
            except IndexError:
                pass
            try:
                res += word2[i]
            except IndexError:
                pass
        return res

sol = Solution()
print(sol.mergeAlternately("apple", "plea"))
print(sol.mergeAlternately("abc", "pqr"))
print(sol.mergeAlternately("ab", "pqrs"))



# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         output = ""
#
#
#         while word1 and word2:
#             output += f"{word1[0]}{word2[0]}"
#             word1 = word1[1:]
#             word2 = word2[1:]
#
#         if word1:
#             output += word1
#         elif word2:
#             output += word2