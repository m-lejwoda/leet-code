from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            goal = target - nums[num]
            if goal in nums[num+1:]:
                return [num, nums.index(goal,num+1)]

s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))
print(s.twoSum(nums = [3,2,4], target = 6))