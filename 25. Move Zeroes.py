from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):

            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 0
        while r < len(nums):
            if nums[r] != 0:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
            r += 1
