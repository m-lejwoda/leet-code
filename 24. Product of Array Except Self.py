from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix = []
    #     postfix = []
    #     prefix.append(nums[0])
    #     postfix.append(nums[-1])
    #     for i in range(1,len(nums)):
    #         prefix.append(nums[i] * prefix[i-1])
    #     for j in range(len(nums) -2, -1,-1):
    #         length = len(postfix)
    #         postfix.append(nums[j] * postfix[length-1])
    #     nums = [1] + nums + [1]
    #     prefix = [1] + prefix + [1]
    #     postfix = [1] + postfix[::-1] + [1]
    #     res = []
    #     for k in range(1, len(nums)-1):
    #         res.append(prefix[k-1] * postfix[k+1])
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] *(len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
sol = Solution()
sol.productExceptSelf([1,2,3,4])