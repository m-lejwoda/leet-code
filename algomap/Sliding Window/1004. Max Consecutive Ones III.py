from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        res = 0
        zero_count = 0
        while r < len(nums):
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))