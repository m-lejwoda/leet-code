from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        l = 0
        num_zeroes = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeroes += 1
            while num_zeroes > k:
                if nums[l] == 0:
                    num_zeroes -= 1
                l +=1
            w = r-l +1
            max_w = max(max_w,w)
        return max_w

sol = Solution()
print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))