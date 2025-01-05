from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest


s = Solution()
# print(s.longestConsecutive([1,2,3,4,5]))
# print(s.longestConsecutive(nums = [100,4,200,1,3,2]))
print(s.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
# print(s.longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))