from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        default_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            default_dict[key].append(s)
        return list(default_dict.values())
s = Solution()
print(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))