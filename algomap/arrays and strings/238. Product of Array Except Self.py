from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums = [1] + nums + [1]
        prefix = []
        postfix = []
        res = []
        total = 1
        for i in range(0, length):
            total *= nums[i]
            prefix.append(total)
        total_2 = 1
        for i in range(len(nums)-1, 1, -1):
            total_2 *= nums[i]
            postfix.append(total_2)
        for i in range(len(prefix)):
            res.append(postfix[-i-1] * prefix[i])
        return res

s = Solution()
s.productExceptSelf(nums=[1, 2, 3, 4])
