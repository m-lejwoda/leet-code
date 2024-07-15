from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""
        first_element = strs[0]
        for i in range(len(first_element)):
            for j in strs[1:]:
                try:
                    if j[i] == first_element[i]:
                        pass
                    else:
                        return result
                except IndexError:
                    return result
            result += first_element[i]
        return result

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["ab", "a"]))