from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return res
        l,r = 0, 1
        more_than_two = False
        while r < len(nums):
            if nums[r] == nums[r-1] + 1:
                more_than_two = True
            else:
                if more_than_two:
                    res.append("{}->{}".format(nums[l], nums[r-1]))
                else:
                    res.append(str(nums[l]))
                l = r
                more_than_two = False
            r += 1
        if more_than_two:
            res.append("{}->{}".format(nums[l], nums[r - 1]))
        else:
            res.append(str(nums[l]))
        return res
s = Solution()
print(s.summaryRanges([1,2,3,4,5]))
print(s.summaryRanges([0,1,2,4,5,7]))