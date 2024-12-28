from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')
        res_diff = float('inf')
        for i in range(len(nums)):
            if abs(nums[i]) < res_diff:
                res = nums[i]
                res_diff = abs(nums[i])
            elif abs(nums[i]) == res_diff:
                if res < nums[i]:
                    res = nums[i]
                    res_diff = abs(nums[i])
        return res


s = Solution()
print(s.findClosestNumber(nums = [-4,-2,1,4,8]))
print(s.findClosestNumber(nums = [2,-1,1]))
