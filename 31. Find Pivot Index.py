from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arr_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = arr_sum - nums[i] - left_sum
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1