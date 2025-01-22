from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1
        while l < r:
            middle = (l + r) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle

        rotation = l

        l, r = 0, len(nums) - 1
        if nums[rotation] <= target <= nums[r]:
            l = rotation
        else:
            r = rotation - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                l = middle + 1
            else:
                r = middle - 1

        return -1

s = Solution()
s.search(nums = [4,5,6,7,0,1,2], target = 0)