from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        first_element = strs[0]
        for el in range(len(first_element)):
            for word in strs[1:]:
                if el >= len(word):
                    return result
                if word[el] != first_element[el]:
                    return result
            result += first_element[el]
        return result

s = Solution()
print(s.longestCommonPrefix(["a", "b", "c"]))
print(s.longestCommonPrefix(strs = ["flower","flow","flight"]))
print(s.longestCommonPrefix(strs = ["dog","racecar","car"]))