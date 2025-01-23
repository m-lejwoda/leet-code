class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_res = float('-inf')
        temp_value = 0
        for i in range(k):
            temp_value += nums[i]
        max_res = max(max_res, temp_value / k)
        r = k
        l = 0
        while r < len(nums):
            temp_value += nums[r]
            temp_value -= nums[l]
            max_res = max(max_res, temp_value / k)
            r += 1
            l += 1
        return max_res