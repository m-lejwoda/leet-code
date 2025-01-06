from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums) - 1
        res = []
        while l <= r:
            if nums[l] * nums[l] <= nums[r] * nums[r]:
                res.append(nums[r] * nums[r])
                r -= 1
            elif nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l+=1
        l,r = 0, len(nums) - 1
        while l < r:
            res[l], res[r] = res[r], res[l]
            l+=1
            r-=1
        return res
        # return res[::-1]


s = Solution()
print(s.sortedSquares(nums = [-4,-1,0,3,10]))
print(s.sortedSquares(nums = [-7,-3,2,3,11]))
print(s.sortedSquares(nums = [-7,-3,0,0,0,2,3,11]))