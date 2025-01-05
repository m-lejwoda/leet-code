from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        default_dict = defaultdict(int)
        goal = len(nums) // 2 + 1
        for num in nums:
            default_dict[num] += 1
            if default_dict[num] >= goal:
                return num


s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))
print(s.majorityElement([3,2,3]))